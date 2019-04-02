from scrapy import cmdline


if __name__ == '__main__':
    keyword_list = ['五星红旗', ]
    # cmdline.execute("scrapy crawl flag -o result.csv".split())    # 用命令行启动
    for keyword in keyword_list:
        cmdline.execute(("scrapy crawl flag -a keyword="+keyword).split())  # 用命令行启动

