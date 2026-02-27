#!/usr/bin/env python3
"""
选题日历管理器
管理特殊节点（节日、节气、特殊日期），提供风险预警和建议主题
"""

import os
import yaml
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class CalendarManager:
    """选题日历管理器"""
    
    def __init__(self, config_path: str = None):
        """
        初始化日历管理器
        Args:
            config_path: 日历配置文件路径
        """
        self.config_path = config_path
        self.nodes = []
        self._load_config()
    
    def _load_config(self):
        """加载日历配置文件"""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                    self.nodes = config.get('nodes', [])
            except Exception as e:
                print(f"警告：加载日历配置文件失败：{str(e)}", file=__import__('sys').stderr)
        else:
            print(f"警告：未找到日历配置文件 {self.config_path}", file=__import__('sys').stderr)
    
    def get_upcoming_nodes(self, days: int = 7) -> List[Dict]:
        """
        获取未来N天的特殊节点
        Args:
            days: 查询未来多少天
        Returns:
            List[Dict]: 特殊节点列表
        """
        today = datetime.now()
        upcoming_nodes = []
        
        for node in self.nodes:
            node_date_str = node.get('date', '')
            if not node_date_str:
                continue
            
            # 解析日期（格式：MM-DD，需要补全年份）
            try:
                month, day = map(int, node_date_str.split('-'))
                node_date = datetime(today.year, month, day)
                
                # 如果今年该日期已过，使用明年的日期
                if node_date < today:
                    node_date = datetime(today.year + 1, month, day)
                
                # 计算距离今天的天数
                days_ahead = (node_date - today).days
                
                if 0 <= days_ahead <= days:
                    upcoming_node = node.copy()
                    upcoming_node['days_ahead'] = days_ahead
                    upcoming_node['target_date'] = node_date.strftime('%Y-%m-%d')
                    upcoming_nodes.append(upcoming_node)
            except Exception as e:
                continue
        
        # 按距离天数排序
        upcoming_nodes.sort(key=lambda x: x['days_ahead'])
        
        return upcoming_nodes
    
    def check_risk(self, node: Dict) -> str:
        """
        检查节点的风险级别
        Args:
            node: 节点信息
        Returns:
            str: 风险级别（high/medium/low）
        """
        return node.get('risk_level', 'low')
    
    def get_themes(self, node: Dict) -> List[str]:
        """
        获取节点的建议主题
        Args:
            node: 节点信息
        Returns:
            List[str]: 建议主题列表
        """
        return node.get('themes', [])
    
    def get_avoid_suggestions(self, node: Dict) -> str:
        """
        获取节点的规避建议
        Args:
            node: 节点信息
        Returns:
            str: 规避建议
        """
        return node.get('avoid_suggestions', '')


# 测试代码
if __name__ == '__main__':
    # 测试日历管理器
    config_path = os.path.join(os.path.dirname(__file__), '../references/calendar-nodes.yaml')
    manager = CalendarManager(config_path)
    
    print("=" * 50)
    print("未来7天的特殊节点")
    print("=" * 50)
    
    upcoming_nodes = manager.get_upcoming_nodes(days=7)
    
    if not upcoming_nodes:
        print("未来7天无特殊节点")
    else:
        for node in upcoming_nodes:
            print(f"\n节点名称: {node['name']}")
            print(f"日期: {node['target_date']}（还有{node['days_ahead']}天）")
            print(f"类型: {node['type']}")
            print(f"风险级别: {node['risk_level']}")
            print(f"建议主题: {', '.join(node['themes'])}")
            if node['avoid_suggestions']:
                print(f"规避建议: {node['avoid_suggestions']}")
