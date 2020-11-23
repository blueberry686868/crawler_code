import requests
import json
import time


# 获取腾讯疫情数据
def get_tencent_data():
    """

    :return: 返回历史数据和当日详细数据
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    r = requests.get(url, headers)

    # 把json格式转换成字典
    res = json.loads(r.text)

    # 字典中有4个key，分别是lastUpdateTime, chinaTotal, chinaAdd, areaTree
    data_all = json.loads(res['data'])

    # 取出data_all中的areaTree这个key值,areaTree是一个列表，里面只有一个字典，索引0取出字典，得到省份数据
    # 字典里面的key值为name(中国),today(全国今日新增),total(总计,包括现有确诊,已确诊,疑似,死亡...),children(省级数据)
    china_data = data_all['areaTree'][0]

    # china_data中key值为children为省级数据，china_data['children']是一个列表(每一个省份是一个字典)
    province_data = china_data['children']

    # 循环遍历出每个省份的数据
    # for province in province_data:
    #     print(province)

    # 爬取历史数据
    history_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery34107549579501076509_1596161763386&_=1596161763387'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    history_res = requests.get(history_url, headers)

    # 把字符串转换成字典
    history_response_data = json.loads(history_res.text.replace('jQuery34107549579501076509_1596161763386(', '')[:-1])

    # 获取字典中的data
    history_response = history_response_data.get('data')

    # 需要把response转换成字典,chinaDayList全国历史数据，是一个列表，每个元素就是一天的数据
    # chinaDayAddList历史新增数据
    history_data_all = json.loads(history_response)

    history = {}  # 历史数据

    for i in history_data_all['chinaDayList']:
        ds = "2020." + i['date']
        # time.strptime是将字符串格式化成元组
        tup = time.strptime(ds, "%Y.%m.%d")
        # time.strftime改变时间格式
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i['confirm']
        suspect = i['suspect']
        heal = i['heal']
        dead = i['dead']
        history[ds] = {'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead}

    for i in history_data_all['chinaDayAddList']:
        ds = '2020.' + i['date']
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i['confirm']
        suspect = i['suspect']
        heal = i['heal']
        dead = i['dead']
        history[ds].update({'confirm_add': confirm, 'suspect_add': suspect, 'heal_add': heal, 'dead_add': dead})

    detail = []  # 当日详细数据

    update_time = data_all['lastUpdateTime']
    data_province = province_data  # 中国各省

    for pro_infos in data_province:
        province = pro_infos['name']
        for city_infos in pro_infos['children']:
            city = city_infos['name']
            confirm = city_infos['total']['confirm']
            confirm_now = city_infos['total']['nowConfirm']
            confirm_add = city_infos['today']['confirm']
            heal = city_infos['total']['heal']
            dead = city_infos['total']['dead']
            detail.append([update_time, province, city, confirm, confirm_now, confirm_add, heal, dead])
    return history, detail


if __name__ == '__main__':
    history, details = get_tencent_data()

    print(history)
    print(details)