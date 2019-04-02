from scrapy import cmdline


if __name__ == '__main__':
    # cmdline.execute("scrapy crawl flag -o result.csv".split())  # 用命令行启动
    cmdline.execute("scrapy crawl flag".split())  # 用命令行启动
