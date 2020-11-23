import traceback

import pymysql
from get_data.get_tencent_data import get_tencent_data
import time
from get_data.get_hot_search import get_hot_search
from utils.utils import get_conn, close_conn


# 更新details表
def update_details():
    cursor = None
    conn = None

    try:
        li = get_tencent_data()[1]  # 0是历史数据字典， 1是详细数据字典
        conn, cursor = get_conn()
        sql = "insert into details (update_time, province, city, confirm, confirm_now, confirm_add, heal, dead) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()} 开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()} 更新数据已经完毕")
        else:
            print(f"{time.asctime()} 已经是最新的数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# 插入history表
def insert_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'), v.get('suspect'), v.get('suspect_add'),
                                 v.get('heal'), v.get('heal_add'), v.get('dead'), v.get('dead_add')])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完成")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# 更新history表
def update_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'), v.get('suspect'), v.get('suspect_add'),
                                     v.get('heal'), v.get('heal_add'), v.get('dead'), v.get('dead_add')])
        conn.commit()
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# 将百度热搜的标题存储到数据库中
def update_hotsearch():
    cursor = None
    conn = None

    try:
        content = get_hot_search()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = get_conn()
        sql = "insert into hotsearch (dt, content) values(%s, %s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in content:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f"{time.asctime()} 更新热搜数据结束")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    insert_history()
    # update_details()
    # update_hotsearch()
