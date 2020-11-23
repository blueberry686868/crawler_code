function gettime() {
    $.ajax({
        url: "/time",
        timeout: 10000, //超时时间设置为10秒
        success: function (data) {
            $("#time").html(data)
        },
        error: function (xhr, type, errorThrown) {

        }
    });
}

function get_center_top_data() {
    $.ajax({
        url: '/get_center_top_data',
        success: function (data) {
            $(".num h1").eq(0).text(data.confirm),
                $(".num h1").eq(1).text(data.confirm_now),
                $(".num h1").eq(2).text(data.confirm_add),
                $(".num h1").eq(3).text(data.heal),
                $(".num h1").eq(4).text(data.dead)
        },
        error: function () {

        }

    })
}

function get_center_down_data() {
    $.ajax({
        url: '/get_center_down_data',
        success: function (data) {
            ec_center_option.series[0].data = data.data
            ec_center.setOption(ec_center_option)
        },
        error: function () {

        }
    })
}

function get_lfet_top_data(){
    $.ajax({
        url:"/get_left_top",
        success: function (data) {
            ec_left_top_option.xAxis.data = data.day
            ec_left_top_option.series[0].data = data.confirm
            ec_left_top_option.series[1].data = data.confirm_add
            ec_left_top_option.series[2].data = data.heal
            ec_left_top_option.series[3].data = data.dead

            ec_left1.setOption(ec_left_top_option)
        }
    })
}

function get_right_top_data(){
    $.ajax({
        url: "/get_right_top",
        success: function (data) {
            ec_right1_option.series[0].data=data.data.sort(function (a, b) { return a.value - b.value; })
            ec_right1.setOption(ec_right1_option)
        }
    })
}

gettime()
get_center_top_data()
get_center_down_data()
get_lfet_top_data()
get_right_top_data()


setInterval(gettime, 1000)
setInterval(get_center_top_data, 10000)
setInterval(get_center_down_data, 10000)
setInterval(get_lfet_top_data, 10000)
setInterval(get_right_top_data, 10000)