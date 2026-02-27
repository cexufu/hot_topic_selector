#!/usr/bin/env python3
"""
选题卡片生成器
将选题建议生成可下载的图片卡片
"""

import os
import sys
import json
import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class CardGenerator:
    """选题卡片生成器"""
    
    def __init__(self):
        # 卡片尺寸
        self.width = 800
        self.height = 1200
        
        # 颜色方案
        self.colors = {
            'background': '#FFFFFF',
            'primary': '#2E86C1',      # 蓝色
            'secondary': '#E74C3C',    # 红色
            'text': '#2C3E50',         # 深灰
            'text_light': '#7F8C8D',   # 浅灰
            'line': '#BDC3C7',         # 分隔线
            'score_high': '#27AE60',   # 高分-绿色
            'score_mid': '#F39C12',    # 中分-黄色
            'score_low': '#E74C3C'     # 低分-红色
        }
        
        # 加载中文字体
        self.fonts = self._load_fonts()
    
    def _load_fonts(self):
        """加载中文字体"""
        fonts = {}
        
        # 字体搜索路径（按优先级）
        font_paths = [
            # Linux
            '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            # Windows
            'C:/Windows/Fonts/simhei.ttf',
            'C:/Windows/Fonts/msyh.ttc',
            # macOS
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/STHeiti Medium.ttc',
        ]
        
        # 尝试加载字体
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    fonts['title'] = ImageFont.truetype(font_path, 36)
                    fonts['subtitle'] = ImageFont.truetype(font_path, 24)
                    fonts['body'] = ImageFont.truetype(font_path, 18)
                    fonts['small'] = ImageFont.truetype(font_path, 14)
                    return fonts
                except Exception as e:
                    continue
        
        # 如果没有找到中文字体，使用默认字体（可能不支持中文）
        print("警告：未找到中文字体，使用默认字体（可能无法正确显示中文）", file=sys.stderr)
        fonts['title'] = ImageFont.load_default()
        fonts['subtitle'] = ImageFont.load_default()
        fonts['body'] = ImageFont.load_default()
        fonts['small'] = ImageFont.load_default()
        
        return fonts
    
    def _hex_to_rgb(self, hex_color):
        """十六进制颜色转RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _draw_text_with_wrap(self, draw, text, font, color, x, y, max_width, line_spacing=5):
        """绘制自动换行的文本"""
        words = text
        lines = []
        current_line = ""
        
        for char in words:
            test_line = current_line + char
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] > max_width:
                lines.append(current_line)
                current_line = char
            else:
                current_line = test_line
        
        if current_line:
            lines.append(current_line)
        
        for i, line in enumerate(lines):
            draw.text((x, y + i * (font.size + line_spacing)), line, fill=color, font=font)
        
        return len(lines) * (font.size + line_spacing)
    
    def _draw_score_bar(self, draw, label, score, x, y, width):
        """绘制评分进度条"""
        # 标签
        draw.text((x, y), label, fill=self.colors['text'], font=self.fonts['small'])
        
        # 进度条背景
        bar_y = y + 20
        bar_height = 12
        draw.rectangle([x, bar_y, x + width, bar_y + bar_height],
                      fill=self._hex_to_rgb('#ECF0F1'), outline=self._hex_to_rgb(self.colors['line']))

        # 进度条填充
        fill_width = int(width * score / 10)
        if score >= 7:
            fill_color = self.colors['score_high']
        elif score >= 5:
            fill_color = self.colors['score_mid']
        else:
            fill_color = self.colors['score_low']

        if fill_width > 0:
            draw.rectangle([x, bar_y, x + fill_width, bar_y + bar_height],
                          fill=self._hex_to_rgb(fill_color), outline=self._hex_to_rgb(fill_color))
        
        # 分数
        draw.text((x + width + 10, y), f"{score}分", fill=self.colors['text'], font=self.fonts['small'])
        
        return bar_y + bar_height + 15
    
    def generate_card(self, data, output_path, index=1):
        """
        生成选题卡片
        
        Args:
            data: 选题数据（包含11个字段）
            output_path: 输出图片路径
            index: 卡片编号
        """
        # 创建画布
        img = Image.new('RGB', (self.width, self.height), self._hex_to_rgb(self.colors['background']))
        draw = ImageDraw.Draw(img)
        
        # 当前Y坐标
        y = 20
        
        # ============ 顶部标题区 ============
        # 标题
        title_text = f"热点选题建议 #{index}"
        draw.text((20, y), title_text, fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['title'])
        
        # 综合得分
        score = data.get('综合得分', {})
        score_value = score.get('value', 0)
        score_level = score.get('level', '未知')
        draw.text((600, y), f"{score_value}分", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['title'])
        y += 40
        draw.text((600, y), score_level, fill=self._hex_to_rgb(self.colors['text_light']), font=self.fonts['subtitle'])
        y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=2)
        y += 30
        
        # ============ 选题方向区 ============
        draw.text((20, y), "【选题方向】", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['subtitle'])
        y += 30
        
        # 标题
        topic = data.get('选题方向', {})
        title = topic.get('标题', '')
        y += self._draw_text_with_wrap(draw, f"标题：{title}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        
        # 核心观点
        core_view = topic.get('核心观点', '')
        y += self._draw_text_with_wrap(draw, f"核心观点：{core_view}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        
        # 内容形式
        content_form = topic.get('内容形式', '')
        y += self._draw_text_with_wrap(draw, f"内容形式：{content_form}", self.fonts['small'], 
                                       self._hex_to_rgb(self.colors['text_light']), 20, y, 760)
        y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 推荐渠道区 ============
        draw.text((20, y), "【推荐渠道】", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['subtitle'])
        y += 30
        
        channel = data.get('推荐渠道', {})
        main_platform = channel.get('主推平台', '')
        aux_platform = channel.get('辅助平台', '')
        reason = channel.get('选择理由', '')
        
        y += self._draw_text_with_wrap(draw, f"主推平台：{main_platform}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"辅助平台：{aux_platform}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"选择理由：{reason}", self.fonts['small'], 
                                       self._hex_to_rgb(self.colors['text_light']), 20, y, 760)
        y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 传播契合点区 ============
        draw.text((20, y), "【传播契合点】", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['subtitle'])
        y += 30
        
        fit_point = data.get('传播契合点', {})
        angle = fit_point.get('关联角度', '')
        value_prop = fit_point.get('价值主张', '')
        emotion = fit_point.get('情感共鸣', '')
        
        y += self._draw_text_with_wrap(draw, f"关联角度：{angle}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"价值主张：{value_prop}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"情感共鸣：{emotion}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 执行建议区 ============
        draw.text((20, y), "【执行建议】", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['subtitle'])
        y += 30
        
        execute = data.get('执行建议', {})
        direction = execute.get('创作方向', '')
        key_elements = execute.get('关键要素', '')
        timing = execute.get('发布时机', '')
        interaction = execute.get('互动策略', '')
        
        y += self._draw_text_with_wrap(draw, f"创作方向：{direction}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"关键要素：{key_elements}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"发布时机：{timing}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 10
        y += self._draw_text_with_wrap(draw, f"互动策略：{interaction}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['text']), 20, y, 760)
        y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 评分明细区 ============
        draw.text((20, y), "【评分明细】", fill=self._hex_to_rgb(self.colors['primary']), font=self.fonts['subtitle'])
        y += 30
        
        scores = data.get('评分明细', {})
        
        # 分两列显示5个评分维度
        col_width = 350
        row_height = 35
        
        # 左列
        y = self._draw_score_bar(draw, "相关性", scores.get('相关性得分', 0), 20, y, col_width)
        y = self._draw_score_bar(draw, "地区相关性", scores.get('地区相关性得分', 0), 20, y, col_width)
        y = self._draw_score_bar(draw, "行业相关性", scores.get('行业相关性得分', 0), 20, y, col_width)
        
        # 右列
        y_right = y - 3 * row_height
        y_right = self._draw_score_bar(draw, "火爆价值", scores.get('火爆价值得分', 0), 410, y_right, col_width)
        y_right = self._draw_score_bar(draw, "长期传播价值", scores.get('长期传播价值得分', 0), 410, y_right, col_width)
        
        y = max(y, y_right) + 10
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 风险提示区 ============
        draw.text((20, y), "【风险提示】", fill=self._hex_to_rgb(self.colors['secondary']), font=self.fonts['subtitle'])
        y += 30
        
        risk = data.get('风险提示', {})
        marketing_risk = risk.get('营销风险', '无')
        sensitive = risk.get('敏感点提示', '')
        compliance = risk.get('合规建议', '')
        
        y += self._draw_text_with_wrap(draw, f"营销风险：{marketing_risk}", self.fonts['body'], 
                                       self._hex_to_rgb(self.colors['secondary']), 20, y, 760)
        y += 10
        if sensitive:
            y += self._draw_text_with_wrap(draw, f"敏感点：{sensitive}", self.fonts['body'], 
                                           self._hex_to_rgb(self.colors['secondary']), 20, y, 760)
            y += 10
        if compliance:
            y += self._draw_text_with_wrap(draw, f"合规建议：{compliance}", self.fonts['body'], 
                                           self._hex_to_rgb(self.colors['secondary']), 20, y, 760)
            y += 20
        
        # 分隔线
        draw.line([(20, y), (780, y)], fill=self._hex_to_rgb(self.colors['line']), width=1)
        y += 20
        
        # ============ 底部信息区 ============
        brand = data.get('品牌信息', {})
        brand_name = brand.get('品牌名', '')
        product_name = brand.get('产品名', '')
        
        footer_text = f"{brand_name} · {product_name} · {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        draw.text((20, self.height - 40), footer_text, fill=self._hex_to_rgb(self.colors['text_light']), font=self.fonts['small'])
        
        # 保存图片
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, 'PNG', quality=95)
        
        print(f"选题卡片已生成：{output_path}", file=sys.stderr)


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='生成选题卡片图片')
    parser.add_argument('--input', type=str, required=True, help='输入JSON文件路径')
    parser.add_argument('--output', type=str, default='./topic-cards', help='输出目录路径')
    parser.add_argument('--index', type=int, default=1, help='卡片编号')
    
    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()
    
    # 加载输入数据
    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 生成卡片
    generator = CardGenerator()
    output_path = os.path.join(args.output, f'topic-card-{args.index}.png')
    generator.generate_card(data, output_path, args.index)


if __name__ == '__main__':
    main()
