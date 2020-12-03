import time
import pymysql


# 获取时间
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


# 创建链接
def get_conn():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='mysql',
                           db='china_cov')
    cursor = conn.cursor()

    return conn, cursor


# 关闭数据库
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


# 封装通用查询
def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


# 获取中上数据的函数
def get_center_top_data():
    sql = "select confirm, " \
          "(select sum(confirm_now) from details), " \
          "confirm_add, " \
          "heal, " \
          "dead from history order by ds desc limit 1;"
    res = query(sql)
    return res[0]


# 获取中下数据的函数
def get_center_down_data():
    sql = "select province,confirm_now " \
          "from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res


# 获取左上数据的函数
def get_left_top_data():
    sql = "select ds, confirm, confirm_add, heal, dead from history;"
    res = query(sql)
    return res


# 获取右上数据的函数
def get_right_top_data():
    sql = "select confirm_now, province " \
          "from details where update_time='2020-08-01 15:17:26' " \
          "order by confirm_add desc limit 5;"
    res = query(sql)
    return res


if __name__ == '__main__':

    res = get_right_top_data()
    data_list = []
    for i in res:
        data_list.append({"value": i[0], "name": i[1]})
    print(data_list)