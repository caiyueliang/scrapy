# -*- coding: utf-8 -*-
import subprocess
from logging import getLogger
from argparse import ArgumentParser


logger = getLogger()


def parse_argvs():
    parser = ArgumentParser(description='image spider')
    parser.add_argument("--total_page", dest="total_page", type=int, help="total_page", default=100)
    args = parser.parse_args()
    logger.warning(args)
    return args


if __name__ == '__main__':
    args = parse_argvs()
    # keyword_list = ['淘宝商品', '书籍封面', '淘宝主图', '广告牌', '品牌海报', '手机截屏', '电脑屏幕', '电视剧对话', '包装']
    # keyword_list = ['厨师帽', '安全帽', '厨师服', '口罩', '电风扇',
    #                 '电视机', '电冰箱', '洗衣机', '空调', '微波炉',
    #                 '炒锅', '砧板', '桌子', '椅子', '沙发']
    # keyword_list = ['倪大红', '陈伟霆', '鹿晗', '刘德华', '姚晨', '刘诗诗', '李念', '张艺兴', '黄子韬', '周笔畅',
    #                 '王艳', '高露', '乔振宇', '郭京飞', '杨祐宁', '郑爽', '赵丽颖', '赵敏芬', '杨幂', '易烊千玺',
    #                 '张嘉倪', '徐悦', '张雨绮', 'Angelababy', '杨超越', '薛佳凝', '关晓彤', '高鑫', '胡歌', '迪丽热巴',
    #                 '张晨光', '袁立', '欧阳娜娜', '王俊凯', '范冰冰', '唐嫣', '霍建华', '黄晓明', '张国荣', '杨洋',
    #                 '凌潇肃', '朱一龙', '王源', '董卿', '吴谨言', '周杰伦', '李易峰', '宋茜', '蔡徐坤', '张馨予',
    #                 '袁姗姗', '王鸥', '吴亦凡', '刘亦菲', '华晨宇', '乔任梁', '梅艳芳', '林心如', '周星驰', '张紫妍',
    #                 '李敏镐', '江疏影', '杨紫', '李小龙', '刘涛', '邓紫棋', '成龙', '柴静', '邱淑贞', '吴京',
    #                 '佟丽娅', '陈思成', '李小璐', '古力娜扎', '高圆圆', '钟汉良', '陈百强', '陈赫', '章子怡', '张杰',
    #                 '李晨', '张翰', '邓伦', '彭于晏', '韩雪', '靳东', '冯绍峰', '邓超', '朱亚文', '王菲',
    #                 '陈乔恩', '柳岩', '刘恺威', '柯震东', '王凯', '林志颖', '景甜', '包贝尔', '倪妮', '孙俪',
    #                 '张一山', '谢霆锋', '向华强', '周冬雨', '贾乃亮', '李连杰', '薛之谦', '林正英', '黄家驹', '白百何',
    #                 '蒋欣', '谢娜', '古天乐', '沈腾', '王子文', '姚明', '刘昊然', '宋慧乔', '赵薇', '王宝强',
    #                 '何炅', '高晓松', '马云', '马化腾', '陈妍希', '林俊杰', '袁咏仪', '郑恺', '周润发', '郭德纲',
    #                 '许嵩', '邓丽君', '阚清子', '黄渤', '许晴', '霍思燕', '郭敬明', '赵又廷', '赵本山', '文章',
    #                 '张歆艺', '林志玲', '撒贝宁', '翟天临', '李健', '张铁林', '陈学冬', '马伊琍', '林峰', '沈梦辰',
    #                 '孙红雷', '朱茵', '林更新', '乐嘉', '林允', '郭碧婷', '贾静雯', '周迅', '陆毅', '毕福剑',
    #                 '贾玲', '张智霖', '吴奇隆', '吴昕', '闫妮', '赵文卓', '赵雅芝', '舒畅', '杜淳', '李若彤',
    #                 '郭采洁', '林书豪', '毛不易', '钟丽缇', '田馥甄', '关之琳', '黄磊', '汤唯', '倪萍', '汪峰',
    #                 '娄艺潇', '陈翔', '雷佳音', '应采儿', '王力宏', '吉克隽逸', '陈小春', '王祖蓝', '罗志祥', '李荣浩',
    #                 '吴彦祖', '井柏然', '马苏', '张晋', '吴尊', '张学友', '张韶涵', '陈奕迅', '蔡少芬', '黄日华']          # 百度明星到33页
    keyword_list = ['五星红旗', '中国共产党党旗', '八一军旗', '美国国旗', '英国国旗',
                    '法国国旗', '日本国旗', '朝鲜国旗', '韩国国旗', '俄罗斯国旗',
                    '西班牙国旗', '奥运会会旗', '联合国旗帜', '欧盟旗帜', '菲律宾共和国国旗',
                    '印度国旗', '巴西国旗', '越南国旗', '老挝国旗', '柬埔寨国旗',
                    '缅甸国旗', '泰国国旗', '马来西亚国旗', '新加坡国旗', '阿富汗国旗',
                    '伊拉克国旗', '伊朗国旗', '叙利亚国旗', '约旦国旗', '黎巴嫩国旗',
                    '以色列国旗', '巴勒斯坦国旗', '沙特阿拉伯国旗', '瑞典国旗', '澳大利亚国旗',
                    '加拿大国旗', '白俄罗斯国旗', '北约旗帜', '东南亚国家联盟旗帜', '世贸组织会旗']

    for keyword in keyword_list:
        logger.warning('[crawl] keyword: %s' % keyword)
        subprocess.call("scrapy crawl image -a keyword="+keyword+" -a total_page="+str(args.total_page), shell=True)

