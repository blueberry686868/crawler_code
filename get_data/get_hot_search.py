from selenium.webdriver import Chrome, ChromeOptions


# 爬取百度热搜数据
def get_hot_search():
    url = 'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1'

    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    brower = Chrome(options=option)
    brower.get(url)
    title = brower.find_elements_by_xpath('//*[@id="main"]/div[2]/div/table/tbody/tr/td[2]/a[1]')

    count = 0
    content = []
    for i in title:
        content.append(i.text)
        count += 1
        if count == 20:
            break

    return content


if __name__ == '__main__':
    get_hot_search()
