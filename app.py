from flask import Flask, request
from flask import render_template
from utils.utils import get_time as _get_time
from utils.utils import get_center_top_data as _get_center_top_data
from utils.utils import get_center_down_data as _get_center_down_data
from utils.utils import get_left_top_data as _get_left_top_data
from utils.utils import get_right_top_data as _get_right_top_data
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/ajax", methods=['post', 'get'])
def hello_world2():
    name = request.values.get('name')
    score = request.values.get('score')
    print(f"name:{name}, score:{score}")
    return '1000'


# 时间的接口
@app.route("/time")
def get_time():
    return _get_time()


# 获取中上数据的接口
@app.route("/get_center_top_data")
def get_center_top_data():
    data = _get_center_top_data()
    return jsonify(
        {"confirm": data[0], "confirm_now": str(data[1]), "confirm_add": data[2], "heal": data[3], "dead": data[4]})


# 获取中下数据的接口
@app.route("/get_center_down_data")
def get_center_down_data():
    res = []
    for tup in _get_center_down_data():
        res.append({"name": tup[0], "value": tup[1]})
    return jsonify({"data": res})


# 获取左上数据的接口
@app.route("/get_left_top")
def get_left_top_data():
    data = _get_left_top_data()
    day, confirm, confirm_add, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[-7:-1]:
        day.append(str(a.strftime("%m-%d")))
        confirm.append(b)
        confirm_add.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "confirm_add": confirm_add, "heal": heal, "dead": dead})


# 获取右上数据的接口
@app.route("/get_right_top")
def get_right_top_data():
    res = _get_right_top_data()
    data_list = []
    for i in res:
        data_list.append({"value": i[0], "name": i[1]})
    return jsonify({"data": data_list})


if __name__ == '__main__':
    app.run()
