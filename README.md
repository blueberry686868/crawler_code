# Cov

#### 介绍
疫情的爬取与展示

#### 软件架构
后端框架基于Flask,前端使用ajax + echarts,使用requests + selenium


#### 使用说明

1.  创建数据库并且创建三个表格（details, history, hotsearch）
2.  get_data文件夹中有三个python文件，并且要去官网下载http://npm.taobao.org/mirrors/chromedriver/下载自己chrome中所对应的版本(
设置-关于chrome)
3.  scripts文件中有创建表格的sql文件

#### 接口文档

1. /time  get请求，获取页面右上角的本地时间
2. /get_center_top_data  get请求，获取页面中间上面的疫情数据
3. /get_center_down_data  get请求，获取页面中间下面的中国疫情地图数据
4. /get_left_top get请求，获取页面左上的线型图
5. /get_right_top get请求，获取页面右上的饼状图

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 码云特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5.  码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
