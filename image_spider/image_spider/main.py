from scrapy import cmdline


if __name__ == '__main__':
    keyword_list = ['五星红旗', '中国共产党党旗', '八一军旗', '美国国旗', '英国国旗',
                    '法国国旗', '日本国旗', '朝鲜国旗', '韩国国旗', '俄罗斯国旗',
                    '西班牙国旗', '奥运会会旗', '联合国旗帜', '欧盟旗帜', '菲律宾共和国国旗',
                    '印度国旗', '巴西国旗', '越南国旗', '老挝国旗', '柬埔寨国旗',
                    '缅甸国旗', '泰国国旗', '马来西亚国旗', '新加坡国旗', '阿富汗国旗',
                    '伊拉克国旗', '伊朗国旗', '叙利亚国旗', '以色列国旗', '巴勒斯坦国旗']
    # cmdline.execute("scrapy crawl flag -o result.csv".split())    # 用命令行启动
    for keyword in keyword_list:
        print(keyword)
        cmdline.execute(("scrapy crawl flag -a keyword="+keyword).split())  # 用命令行启动

