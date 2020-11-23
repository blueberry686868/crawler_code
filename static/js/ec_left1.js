var ec_left1 = echarts.init(document.getElementById('left1'));

ec_left_top_option = {
    title: {
        text: ''
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['累计确诊', '新增确诊', '累计治愈', '累计死亡']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一','周一','周一','周一','周一','周一']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '累计确诊',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '新增确诊',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '累计治愈',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '累计死亡',
            type: 'line',
            stack: '总量',
            data: []
        }
    ]
};


