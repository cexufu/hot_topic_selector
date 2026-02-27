#!/usr/bin/env python3
"""
热点数据获取脚本
获取全网热点数据并输出JSON格式的热点池

支持的热点来源：
- 微博热搜榜
- 百度热榜
- 抖音热榜（通过第三方接口）

使用示例：
python fetch_hot_topics.py --platforms weibo,baidu --limit 50
python fetch_hot_topics.py --limit 100 --output hot_topics.json
"""

import argparse
import json
import sys
from datetime import datetime
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from topic_classifier import TopicClassifier


class HotTopicFetcher:
    """热点数据获取器"""
    
    def __init__(self, timeout: int = 10, enable_classification: bool = True):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        # 初始化话题分类器
        self.classifier = TopicClassifier() if enable_classification else None
    
    def fetch_weibo_hot(self, limit: int = 50) -> List[Dict]:
        """
        获取微博热搜榜
        
        Returns:
            List[Dict]: 热点列表，每个元素包含title、hot_score、platform等字段
        """
        url = "https://s.weibo.com/top/summary"
        topics = []
        
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                print(f"警告：微博热搜请求失败，状态码：{response.status_code}", file=sys.stderr)
                return topics
            
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'list'})
            
            if table:
                rows = table.find_all('tr')[1:]  # 跳过表头
                for idx, row in enumerate(rows[:limit]):
                    try:
                        cells = row.find_all('td')
                        if len(cells) >= 2:
                            link = cells[1].find('a')
                            if link:
                                title = link.get_text(strip=True)
                                hot_text = cells[1].find('span')
                                hot_score = hot_text.get_text(strip=True) if hot_text else "未知"
                                
                                topics.append({
                                    'title': title,
                                    'hot_score': hot_score,
                                    'platform': '微博',
                                    'rank': idx + 1,
                                    'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                })
                    except Exception as e:
                        continue
            
        except requests.exceptions.RequestException as e:
            print(f"警告：微博热搜请求异常：{str(e)}", file=sys.stderr)
        except Exception as e:
            print(f"警告：微博热搜解析异常：{str(e)}", file=sys.stderr)
        
        return topics
    
    def fetch_baidu_hot(self, limit: int = 50) -> List[Dict]:
        """
        获取百度热榜
        
        Returns:
            List[Dict]: 热点列表
        """
        url = "https://top.baidu.com/board?tab=realtime"
        topics = []
        
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                print(f"警告：百度热榜请求失败，状态码：{response.status_code}", file=sys.stderr)
                return topics
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', {'class': 'category-wrap_iQLoo horizontal_1eKyQ'})
            
            for idx, item in enumerate(items[:limit]):
                try:
                    title_div = item.find('div', {'class': 'c-single-text-ellipsis'})
                    if title_div:
                        title = title_div.get_text(strip=True)
                        
                        # 尝试获取热度值
                        hot_score_div = item.find('div', {'class': 'hot-index_1Bl1a'})
                        hot_score = hot_score_div.get_text(strip=True) if hot_score_div else "未知"
                        
                        topics.append({
                            'title': title,
                            'hot_score': hot_score,
                            'platform': '百度',
                            'rank': idx + 1,
                            'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                except Exception as e:
                    continue
            
        except requests.exceptions.RequestException as e:
            print(f"警告：百度热榜请求异常：{str(e)}", file=sys.stderr)
        except Exception as e:
            print(f"警告：百度热榜解析异常：{str(e)}", file=sys.stderr)
        
        return topics
    
    def fetch_douyin_hot(self, limit: int = 50) -> List[Dict]:
        """
        获取抖音热榜（通过第三方接口）
        
        Returns:
            List[Dict]: 热点列表
        """
        # 使用公开的热点聚合API
        url = "https://api.vvhan.com/api/hotlist/douyinHot"
        topics = []
        
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            
            if response.status_code != 200:
                print(f"警告：抖音热榜请求失败，状态码：{response.status_code}", file=sys.stderr)
                return topics
            
            data = response.json()
            
            if data.get('success') and 'data' in data:
                for idx, item in enumerate(data['data'][:limit]):
                    topics.append({
                        'title': item.get('title', ''),
                        'hot_score': str(item.get('hot', '未知')),
                        'platform': '抖音',
                        'rank': idx + 1,
                        'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
            
        except requests.exceptions.RequestException as e:
            print(f"警告：抖音热榜请求异常：{str(e)}", file=sys.stderr)
        except Exception as e:
            print(f"警告：抖音热榜解析异常：{str(e)}", file=sys.stderr)
        
        return topics
    
    def fetch_all(self, platforms: List[str], limit: int = 50) -> List[Dict]:
        """
        获取多平台热点数据并合并
        
        Args:
            platforms: 平台列表，如 ['weibo', 'baidu', 'douyin']
            limit: 每个平台获取的热点数量
        
        Returns:
            List[Dict]: 合并后的热点列表
        """
        all_topics = []
        
        platform_fetchers = {
            'weibo': self.fetch_weibo_hot,
            'baidu': self.fetch_baidu_hot,
            'douyin': self.fetch_douyin_hot
        }
        
        for platform in platforms:
            if platform in platform_fetchers:
                fetcher = platform_fetchers[platform]
                topics = fetcher(limit)
                all_topics.extend(topics)
                print(f"已获取{platform}热点 {len(topics)} 条", file=sys.stderr)
        
        # 去重（基于标题）
        seen_titles = set()
        unique_topics = []
        for topic in all_topics:
            title = topic.get('title', '')
            if title and title not in seen_titles:
                seen_titles.add(title)
                # 如果启用分类，对每个话题进行分类
                if self.classifier:
                    classification = self.classifier.classify(title)
                    topic.update({
                        'regions': classification['regions'],
                        'industries': classification['industries'],
                        'has_region_topic': classification['has_region_topic'],
                        'has_industry_topic': classification['has_industry_topic']
                    })
                unique_topics.append(topic)
        
        return unique_topics


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='获取全网热点数据')
    parser.add_argument(
        '--platforms',
        type=str,
        default='weibo,baidu',
        help='指定热点来源平台，用逗号分隔，如：weibo,baidu,douyin'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=50,
        help='每个平台获取的热点数量'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='输出文件路径，不指定则输出到stdout'
    )
    parser.add_argument(
        '--no-classification',
        action='store_true',
        help='禁用话题分类功能'
    )
    
    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()
    
    # 解析平台列表
    platforms = [p.strip().lower() for p in args.platforms.split(',')]
    
    # 获取热点数据（默认启用分类）
    enable_classification = not args.no_classification
    fetcher = HotTopicFetcher(enable_classification=enable_classification)
    topics = fetcher.fetch_all(platforms, args.limit)
    
    # 构建结果
    result = {
        'total': len(topics),
        'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'platforms': platforms,
        'has_classification': enable_classification,
        'topics': topics
    }
    
    # 输出结果
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"热点数据已保存到：{args.output}", file=sys.stderr)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
