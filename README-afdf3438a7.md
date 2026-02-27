<div align="center">

# 🔥 Hot Topic Selector

> **AI驱动的热点选题助手** - 从全网热点到可执行选题方案，只需5分钟

[![Stars](https://img.shields.io/github/stars/yourusername/hot-topic-selector?style=social)](https://github.com/yourusername/hot-topic-selector/stargazers)
[![Forks](https://img.shields.io/github/forks/yourusername/hot-topic-selector?style=social)](https://github.com/yourusername/hot-topic-selector/network/members)
[![License](https://img.shields.io/github/license/yourusername/hot-topic-selector)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

[English](#english) | [中文](#中文)

</div>

---

## ✨ 为什么选择 Hot Topic Selector？

### 🎯 痛点直击

每天刷微博、看热搜、逛知乎，花费数小时找选题，最后还是不知道写什么？

**你的问题不是"信息太少"，而是"信息太吵"。**

Hot Topic Selector 帮你：
- ✅ **告别手动刷热点**：自动聚合微博、百度、抖音等主流平台热点
- ✅ **智能品牌匹配**：五维度评分模型，只推荐真正适合你的热点
- ✅ **输出可执行方案**：不是热点列表，而是含标题、角度、执行建议的完整选题
- ✅ **规避舆情风险**：选题日历预警，特殊节点自动提醒

---

## 🚀 核心特性

### 📊 五维度智能评分

| 维度 | 权重 | 说明 |
|------|------|------|
| 品牌相关性 | 20% | 与品牌调性、产品的关联程度 |
| 行业相关性 | 15% | 与所在行业的匹配度 |
| 地区相关性 | 15% | 与目标地区的关联度 |
| 火爆价值 | 25% | 热度指数、传播速度、平台覆盖 |
| 长期传播价值 | 25% | 话题持续性、二次创作空间 |

### 📅 选题日历预警

自动检测未来 7 天的特殊节点（如纪念日、节日），提供：
- ⚠️ 高风险节点警告（如 918 事变纪念日）
- 📝 建议主题方向
- 🚫 规避建议

### 🎨 三种聚焦模式

| 模式 | 适用场景 | 权重调整 |
|------|----------|----------|
| 全面模式 | 全国性品牌 | 默认权重 |
| 地区聚焦 | 区域性业务（如北京餐饮） | 地区相关性 30% |
| 行业聚焦 | 垂直行业品牌（如科技、美妆） | 行业相关性 30% |

### 📤 多平台热点聚合

- 🔥 微博热搜
- 🔍 百度热榜
- 🎵 抖音热榜
- （持续扩展中...）

---

## 📸 效果预览

### 输入示例

```
品牌：XX科技
产品：智能手表Pro
行业关键词：智能穿戴、健康监测、运动科技
传播目标：产品曝光和用户教育
平台偏好：微博、小红书
```

### 输出示例：Top5 选题建议

<div align="center">

| 排名 | 选题方向 | 综合得分 | 推荐渠道 |
|------|----------|----------|----------|
| 1 | 当健康监测成为标配，智能手表如何重新定义你的生活 | 7.8⭐ | 微博 + 小红书 |
| 2 | 90%的人不知道的智能手表隐藏功能 | 7.5⭐ | 小红书 |
| 3 | 从"配饰"到"必需品"：智能手表的5年进化史 | 7.2⭐ | 微博 |
| 4 | 用了智能手表30天，我发现这些功能最有用 | 6.9⭐ | 小红书 + 微信 |
| 5 | 智能手表选购指南：这3个参数最重要 | 6.5⭐ | 小红书 |

</div>

每个选题包含：
- 📝 **标题**：3个备选标题
- 🎯 **传播契合点**：如何将热点与品牌关联
- 💡 **执行建议**：创作方向、关键要素、发布时机
- ⚠️ **风险提示**：潜在营销风险

---

## 🛠️ 快速开始

### 方式一：GitHub Actions 零成本部署（推荐）

**30秒完成部署，无需任何服务器**

1. **Fork 本仓库**
   ```bash
   点击右上角 Fork 按钮
   ```

2. **配置 Secret**
   - 进入 Fork 后的仓库 → `Settings` → `Secrets and variables` → `Actions`
   - 点击 `New repository secret`
   - 添加以下 Secret（按需）：
     ```
     OPENAI_API_KEY: 你的 OpenAI API Key
     MODEL_NAME: gpt-4o-mini（或其他模型）
     ```

3. **启用 Actions**
   - 进入 `Actions` 标签页
   - 点击 `I understand my workflows, go ahead and enable them`

4. **手动测试**
   - 进入 `Actions` → `Hot Topic Generator` 工作流
   - 点击 `Run workflow` → `Run workflow`
   - 等待运行完成（约 1-2 分钟）

5. **查看结果**
   - 进入 `Actions` → 点击成功的运行记录
   - 在 `Artifacts` 中下载 `topic-report.zip`

### 方式二：Docker 部署（推荐用于生产环境）

```bash
# 克隆仓库
git clone https://github.com/yourusername/hot-topic-selector.git
cd hot-topic-selector

# 使用 Docker 运行
docker run -d \
  --name hot-topic-selector \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  -e OPENAI_API_KEY=your_api_key \
  yourdockerhub/hot-topic-selector:latest

# 查看日志
docker logs -f hot-topic-selector
```

### 方式三：本地运行

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/hot-topic-selector.git
cd hot-topic-selector

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
export OPENAI_API_KEY="your_api_key_here"
export MODEL_NAME="gpt-4o-mini"

# 4. 运行
python hot-topic-selector/scripts/fetch_hot_topics.py --platforms weibo,baidu --limit 50
```

---

## 📖 详细文档

- [用户使用指南](docs/user-guide.md) - 完整使用教程
- [五维度评分说明](docs/scoring-system.md) - 深入了解评分机制
- [选题日历机制](docs/calendar-warning.md) - 特殊节点预警原理
- [配置文件详解](docs/configuration.md) - 自定义配置指南
- [常见问题](docs/faq.md) - FAQ

---

## 🎯 适用人群

### 👩‍💼 内容创作者
- 痛点：每天刷热点，不知道写什么
- 价值：自动筛选高价值选题，节省 80% 选题时间

### 🏢 市场运营团队
- 痛点：需要快速响应热点，但担心舆情风险
- 价值：五维度评分确保热点与品牌匹配，选题日历规避风险

### 🎨 品牌公关
- 痛点：热点借势策划耗时长，决策缺乏数据支撑
- 价值：结构化选题方案，含风险评估，提升决策效率

### 📊 自媒体矩阵运营
- 痛点：多平台分发，每个平台需要不同的选题角度
- 价值：一个热点生成多个平台的适配方案

---

## 🔧 配置说明

### 1. 关键词配置

编辑 `config/frequency_words.txt`：

```
# 普通关键词
AI
人工智能
机器学习

# 必须词（+前缀）
+大模型
+ChatGPT

# 过滤词（!前缀）
!娱乐八卦
!明星绯闻
```

### 2. 评分权重调整

编辑 `config/config.yaml`：

```yaml
scoring:
  brand_relevance: 0.2      # 品牌相关性
  industry_relevance: 0.15  # 行业相关性
  region_relevance: 0.15    # 地区相关性
  viral_value: 0.25         # 火爆价值
  long_term_value: 0.25     # 长期传播价值
```

### 3. 选题日历配置

编辑 `config/calendar-nodes.yaml`：

```yaml
nodes:
  - name: "九一八事变纪念日"
    date: "2024-09-18"
    risk_level: "HIGH"
    suggested_topics: ["铭记历史", "爱国", "勿忘国耻"]
    avoid_suggestions: ["严禁娱乐化营销", "保持严肃态度"]
```

---

## 📊 与其他工具对比

| 特性 | TrendRadar | Hot Topic Selector |
|------|------------|-------------------|
| **核心价值** | 热点监控+自动推送 | 热点筛选+品牌匹配+选题策划 |
| **目标用户** | 个人信息消费者 | 内容创作者、市场运营、品牌公关 |
| **输出形式** | 热点列表 | Top5 选题建议（含执行方案） |
| **智能程度** | 关键词过滤 | 五维度评分+日历预警 |
| **商业价值** | 提升信息获取效率 | 直接产出可执行内容方案 |
| **适用场景** | 个人日常资讯获取 | 品牌传播策划、内容选题决策 |

**一句话总结**：
- TrendRadar 帮你**看**热点
- Hot Topic Selector 帮你**用**热点

---

## 🌟 Star History

<div align="center">

![Star History Chart](https://api.star-history.com/svg?repos=yourusername/hot-topic-selector&type=Date)

</div>

---

## 🤝 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

### 贡献方式

1. 🐛 报告 Bug
2. 💡 提出新功能建议
3. 📝 改进文档
4. 🔧 提交代码
5. 🌍 帮助翻译

---

## 📜 License

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🙏 致谢

- [TrendRadar](https://github.com/sansan0/TrendRadar) - 热点聚合思路参考
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - 网页解析
- [OpenAI API](https://openai.com/api) - AI 分析能力支持

---

## 📮 联系方式

- 作者：Your Name
- 邮箱：your.email@example.com
- 微博：@yourhandle
- 微信：yourwechatid

---

<div align="center">

**如果这个项目对你有帮助，请给它一个 ⭐️ Star**

**让更多人告别选题焦虑**

</div>

---

<a name="english"></a>
<div align="center">

# 🔥 Hot Topic Selector

> **AI-Powered Hot Topic Assistant** - From trending topics to actionable content strategies in 5 minutes

[![Stars](https://img.shields.io/github/stars/yourusername/hot-topic-selector?style=social)](https://github.com/yourusername/hot-topic-selector/stargazers)
[![Forks](https://img.shields.io/github/forks/yourusername/hot-topic-selector?style=social)](https://github.com/yourusername/hot-topic-selector/network/members)
[![License](https://img.shields.io/github/license/yourusername/hot-topic-selector)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

</div>

---

## ✨ Why Hot Topic Selector?

### 🎯 The Problem

Spend hours scrolling through Weibo, checking trending topics, browsing Zhihu, but still don't know what to write?

**Your problem isn't "too little information" — it's "too much noise."**

Hot Topic Selector helps you:
- ✅ **Stop manual topic hunting**: Automatically aggregate trending topics from Weibo, Baidu, Douyin, and more
- ✅ **Smart brand matching**: Five-dimensional scoring model recommends only topics that fit your brand
- ✅ **Output actionable plans**: Not just a topic list, but complete content strategies with titles, angles, and execution suggestions
- ✅ **Avoid PR risks**: Topic calendar warning system automatically alerts you about special dates

---

## 🚀 Core Features

### 📊 Five-Dimension Smart Scoring

| Dimension | Weight | Description |
|-----------|---------|-------------|
| Brand Relevance | 20% | Alignment with brand positioning and products |
| Industry Relevance | 15% | Match with your industry |
| Region Relevance | 15% | Connection to target region |
| Viral Value | 25% | Heat index, spread speed, platform coverage |
| Long-term Value | 25% | Topic sustainability, secondary creation potential |

### 📅 Topic Calendar Warning

Automatically detect special dates in the next 7 days (e.g., memorial days, holidays) and provide:
- ⚠️ High-risk date warnings (e.g., September 18th Memorial Day)
- 📝 Suggested topic directions
- 🚫 Avoidance recommendations

### 🎨 Three Focus Modes

| Mode | Best For | Weight Adjustment |
|------|----------|------------------|
| Full Mode | National brands | Default weights |
| Region Focus | Regional businesses (e.g., Beijing restaurants) | Region relevance 30% |
| Industry Focus | Vertical industry brands (e.g., tech, beauty) | Industry relevance 30% |

### 📤 Multi-Platform Trending Aggregation

- 🔥 Weibo Hot Search
- 🔍 Baidu Hot List
- 🎵 Douyin Trending
- (More coming soon...)

---

## 📸 Preview

### Input Example

```
Brand: XX Tech
Product: Smart Watch Pro
Industry Keywords: Smart wearables, Health monitoring, Sports technology
Communication Goal: Product exposure and user education
Platform Preference: Weibo, Xiaohongshu
```

### Output: Top5 Topic Recommendations

<div align="center">

| Rank | Topic Direction | Score | Recommended Channels |
|------|----------------|--------|---------------------|
| 1 | When Health Monitoring Becomes Standard: How Smart Watches Redefine Life | 7.8⭐ | Weibo + Xiaohongshu |
| 2 | Hidden Features of Smart Watches That 90% Don't Know | 7.5⭐ | Xiaohongshu |
| 3 | From "Accessory" to "Essential": 5-Year Evolution of Smart Watches | 7.2⭐ | Weibo |
| 4 | Used a Smart Watch for 30 Days: These Features Are Most Useful | 6.9⭐ | Xiaohongshu + WeChat |
| 5 | Smart Watch Buying Guide: These 3 Parameters Matter Most | 6.5⭐ | Xiaohongshu |

</div>

Each topic includes:
- 📝 **Title**: 3 alternative titles
- 🎯 **Brand Connection Point**: How to link trending topic with your brand
- 💡 **Execution Suggestion**: Creative direction, key elements, posting timing
- ⚠️ **Risk Warning**: Potential marketing risks

---

## 🛠️ Quick Start

### Option 1: GitHub Actions Zero-Cost Deployment (Recommended)

**Deploy in 30 seconds, no server needed**

1. **Fork this repository**
   ```bash
   Click the Fork button in the top right
   ```

2. **Configure Secrets**
   - Go to Forked repo → `Settings` → `Secrets and variables` → `Actions`
   - Click `New repository secret`
   - Add these Secrets (as needed):
     ```
     OPENAI_API_KEY: Your OpenAI API Key
     MODEL_NAME: gpt-4o-mini (or other model)
     ```

3. **Enable Actions**
   - Go to `Actions` tab
   - Click `I understand my workflows, go ahead and enable them`

4. **Manual Test**
   - Go to `Actions` → `Hot Topic Generator` workflow
   - Click `Run workflow` → `Run workflow`
   - Wait for completion (about 1-2 minutes)

5. **View Results**
   - Go to `Actions` → Click the successful run
   - Download `topic-report.zip` from `Artifacts`

### Option 2: Docker Deployment (Recommended for Production)

```bash
# Clone repository
git clone https://github.com/yourusername/hot-topic-selector.git
cd hot-topic-selector

# Run with Docker
docker run -d \
  --name hot-topic-selector \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/output:/app/output \
  -e OPENAI_API_KEY=your_api_key \
  yourdockerhub/hot-topic-selector:latest

# View logs
docker logs -f hot-topic-selector
```

### Option 3: Local Run

```bash
# 1. Clone repository
git clone https://github.com/yourusername/hot-topic-selector.git
cd hot-topic-selector

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
export OPENAI_API_KEY="your_api_key_here"
export MODEL_NAME="gpt-4o-mini"

# 4. Run
python hot-topic-selector/scripts/fetch_hot_topics.py --platforms weibo,baidu --limit 50
```

---

## 📖 Documentation

- [User Guide](docs/user-guide.md) - Complete tutorial
- [Scoring System](docs/scoring-system.md) - Understand the scoring mechanism
- [Calendar Warning](docs/calendar-warning.md) - Special date warning principles
- [Configuration](docs/configuration.md) - Custom configuration guide
- [FAQ](docs/faq.md) - Frequently Asked Questions

---

## 🎯 Target Users

### 👩‍💼 Content Creators
- **Pain point**: Spend hours browsing topics, don't know what to write
- **Value**: Automatically filter high-value topics, save 80% topic selection time

### 🏢 Marketing Teams
- **Pain point**: Need to respond to hot topics quickly but worry about PR risks
- **Value**: Five-dimension scoring ensures topic-brand fit, calendar warnings avoid risks

### 🎨 Brand PR
- **Pain point**: Trending topic planning takes time, decisions lack data support
- **Value**: Structured topic proposals with risk assessment, improve decision efficiency

### 📊 Multi-Platform Operations
- **Pain point**: Multi-platform distribution, each platform needs different topic angles
- **Value**: One topic generates adapted solutions for multiple platforms

---

## 🔧 Configuration

### 1. Keyword Configuration

Edit `config/frequency_words.txt`:

```
# Regular keywords
AI
Artificial Intelligence
Machine Learning

# Must-have keywords (+ prefix)
+Large Language Models
+ChatGPT

# Filter keywords (! prefix)
!Entertainment gossip
!Celebrity scandals
```

### 2. Scoring Weights Adjustment

Edit `config/config.yaml`:

```yaml
scoring:
  brand_relevance: 0.2      # Brand relevance
  industry_relevance: 0.15  # Industry relevance
  region_relevance: 0.15    # Region relevance
  viral_value: 0.25         # Viral value
  long_term_value: 0.25     # Long-term value
```

### 3. Calendar Configuration

Edit `config/calendar-nodes.yaml`:

```yaml
nodes:
  - name: "September 18th Memorial Day"
    date: "2024-09-18"
    risk_level: "HIGH"
    suggested_topics: ["Remember history", "Patriotism", "Don't forget national humiliation"]
    avoid_suggestions: ["Strictly prohibit entertainment marketing", "Maintain serious attitude"]
```

---

## 📊 Comparison with Other Tools

| Feature | TrendRadar | Hot Topic Selector |
|---------|------------|-------------------|
| **Core Value** | Trending monitoring + auto push | Trending filtering + brand matching + topic planning |
| **Target Users** | Personal info consumers | Content creators, marketing teams, brand PR |
| **Output Format** | Trending list | Top5 topic recommendations (with execution plans) |
| **Intelligence** | Keyword filtering | Five-dimension scoring + calendar warning |
| **Business Value** | Improve info acquisition efficiency | Directly produce actionable content plans |
| **Use Cases** | Personal daily info access | Brand communication planning, content topic decisions |

**In summary**:
- TrendRadar helps you **see** trending topics
- Hot Topic Selector helps you **use** trending topics

---

## 🌟 Star History

<div align="center">

![Star History Chart](https://api.star-history.com/svg?repos=yourusername/hot-topic-selector&type=Date)

</div>

---

## 🤝 Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md)

### How to Contribute

1. 🐛 Report a bug
2. 💡 Suggest new features
3. 📝 Improve documentation
4. 🔧 Submit code
5. 🌍 Help with translation

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [TrendRadar](https://github.com/sansan0/TrendRadar) - Trending aggregation ideas
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Web parsing
- [OpenAI API](https://openai.com/api) - AI analysis capabilities

---

## 📮 Contact

- Author: Your Name
- Email: your.email@example.com
- Twitter: @yourhandle
- WeChat: yourwechatid

---

<div align="center">

**If this project helps you, please give it a ⭐️ Star**

**Help more people say goodbye to topic anxiety**

</div>
