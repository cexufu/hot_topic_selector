#!/usr/bin/env python3
"""
话题分类器
对热点进行地区识别和行业分类
"""

class TopicClassifier:
    """话题分类器"""
    
    def __init__(self):
        # 地区关键词映射（支持省、市、区县）
        self.region_keywords = {
            '北京': ['北京', '京城', '京', '朝阳区', '海淀区', '东城区', '西城区'],
            '上海': ['上海', '沪', '魔都', '浦东', '徐汇', '静安', '长宁'],
            '广州': ['广州', '穗', '羊城', '天河', '越秀', '海珠'],
            '深圳': ['深圳', '鹏城', '深', '南山', '福田', '罗湖'],
            '杭州': ['杭州', '杭', '西湖', '滨江', '余杭'],
            '成都': ['成都', '蓉', '锦城', '武侯', '青羊', '锦江'],
            '重庆': ['重庆', '渝', '山城', '江北', '渝中'],
            '武汉': ['武汉', '汉', '江城', '武昌', '汉口', '汉阳'],
            '西安': ['西安', '长安', '镐京', '雁塔', '碑林'],
            '南京': ['南京', '金陵', '宁', '鼓楼', '玄武', '秦淮'],
            '天津': ['天津', '津', '和平', '河西', '南开'],
            '苏州': ['苏州', '姑苏', '工业园区', '高新区'],
            '郑州': ['郑州', '豫', '中原', '金水', '二七'],
            '长沙': ['长沙', '湘', '岳麓', '芙蓉', '天心'],
            '沈阳': ['沈阳', '辽', '和平', '沈河', '皇姑'],
            '青岛': ['青岛', '鲁', '市南', '市北', '崂山'],
            '大连': ['大连', '辽', '中山', '西岗', '沙河口'],
            '厦门': ['厦门', '闽', '思明', '湖里', '集美'],
            '宁波': ['宁波', '浙', '海曙', '江东', '江北'],
            '无锡': ['无锡', '苏', '崇安', '南长', '北塘'],
            # 可继续扩展...
        }
        
        # 行业关键词映射
        self.industry_keywords = {
            '科技': ['AI', '人工智能', '大模型', '芯片', '半导体', '5G', '6G', '云计算',
                     '元宇宙', '区块链', '机器人', '物联网', '软件', 'APP', '智能', '科技'],
            '美妆': ['口红', '面膜', '化妆', '护肤', '美妆', '彩妆', '香水', '护肤品', '化妆品',
                     '粉底', '睫毛', '眼影', '唇膏'],
            '母婴': ['宝妈', '奶粉', '育儿', '母婴', '婴儿', '儿童', '早教', '亲子', '孕妇',
                     '新生儿', '辅食', '玩具'],
            '教育': ['高考', '考研', '留学', '培训', '教育', '大学', '学校', '学习', '考试',
                     '课程', '辅导', '培训机构'],
            '汽车': ['汽车', '车', '新能源车', '电动车', '特斯拉', '比亚迪', '驾驶', '车载',
                     '汽车品牌', '4S店', '试驾'],
            '文旅': ['旅游', '景点', '景区', '文旅', '酒店', '民宿', '出行', '旅行', '度假',
                     '门票', '攻略'],
            '金融': ['股票', '基金', '理财', '银行', '保险', '金融', '贷款', '投资', '证券',
                     '基金公司', '基金'],
            '房产': ['房产', '房地产', '房价', '买房', '卖房', '楼盘', '学区房', '租房',
                     '售楼处', '开发商'],
            '快消': ['饮料', '食品', '零食', '生鲜', '超市', '便利店', '外卖', '餐饮', '快餐',
                     '食材'],
            '时尚': ['穿搭', '时尚', '潮流', '服装', '鞋子', '包包', '奢侈品', '服饰', '时装',
                     '潮流'],
            '健康': ['医疗', '健康', '医院', '药品', '医生', '健身', '运动', '养生', '保健',
                     '疫苗', '体检'],
            '娱乐': ['电影', '电视剧', '综艺', '明星', '演员', '歌手', '音乐', '演唱会',
                     '娱乐', '艺人'],
            '体育': ['足球', '篮球', '奥运会', '世界杯', 'NBA', 'CBA', '运动员', '教练',
                     '比赛', '赛事', '体育'],
            '家电': ['家电', '电器', '空调', '冰箱', '洗衣机', '电视', '微波炉', '热水器',
                     '油烟机', '厨电'],
            '手机': ['手机', 'iPhone', '华为', '小米', 'OPPO', 'vivo', '荣耀', '一加',
                     '三星', '手机品牌'],
            '家居': ['家居', '家具', '装修', '建材', '沙发', '床', '衣柜', '厨房', '卫浴',
                     '家装'],
            # 可继续扩展...
        }
        
        # 构建反向映射：从关键词到地区/行业
        self.keyword_to_region = {}
        for region, keywords in self.region_keywords.items():
            for keyword in keywords:
                self.keyword_to_region[keyword] = region
        
        self.keyword_to_industry = {}
        for industry, keywords in self.industry_keywords.items():
            for keyword in keywords:
                self.keyword_to_industry[keyword] = industry
    
    def classify_region(self, text: str) -> list:
        """
        识别话题涉及的地区
        Returns:
            list: 地区列表，如 ['北京', '全国']
        """
        regions = set()
        for keyword, region in self.keyword_to_region.items():
            if keyword in text:
                regions.add(region)
        
        # 如果没有识别到地区，默认为全国
        if not regions:
            regions.add('全国')
        
        return list(regions)
    
    def classify_industry(self, text: str) -> list:
        """
        识别话题涉及的行业
        Returns:
            list: 行业列表，如 ['科技', '金融']
        """
        industries = set()
        for keyword, industry in self.keyword_to_industry.items():
            if keyword in text:
                industries.add(industry)
        
        return list(industries)
    
    def classify(self, title: str) -> dict:
        """
        对话题进行完整分类
        Args:
            title: 话题标题
        Returns:
            dict: 分类结果
            {
                'regions': ['北京'],
                'industries': ['科技'],
                'has_region_topic': True,
                'has_industry_topic': True
            }
        """
        regions = self.classify_region(title)
        industries = self.classify_industry(title)
        
        return {
            'regions': regions,
            'industries': industries,
            'has_region_topic': len(regions) > 0 and regions != ['全国'],
            'has_industry_topic': len(industries) > 0
        }


# 测试代码
if __name__ == '__main__':
    classifier = TopicClassifier()
    
    # 测试地区分类
    test_topics = [
        "北京冬奥会圆满成功",
        "上海外滩人山人海",
        "AI技术突破性进展",
        "护肤新品上市",
        "全国人民喜迎国庆"
    ]
    
    for topic in test_topics:
        result = classifier.classify(topic)
        print(f"话题: {topic}")
        print(f"  地区: {result['regions']}")
        print(f"  行业: {result['industries']}")
        print()
