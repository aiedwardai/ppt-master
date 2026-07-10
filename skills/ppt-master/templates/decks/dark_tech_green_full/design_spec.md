---
deck_id: dark_tech_green_full
kind: deck
summary: "暗场科技绿风格·完整版（21页）。深蓝墨黑底 + 科技绿发光强调 + 数据仪表盘质感。21 种通用版式母版，覆盖列表/对比/流程/架构/辐射/分区/风险等全谱系。纯模板，无任何行业属性，适用于科技汇报/项目方案/技术评估/管理汇报等通用场景。"
canvas_format: ppt169
page_count: 21
primary_color: "#00C060"
replication_mode: standard
reference_type: "Type C (visual / PDF pages)"
placeholders:
  01_cover: []
  02_toc: []
  03_chapter: []
  04_overview: []
  05_content_3col: []
  06_content_list: []
  07_data: []
  08_compare: []
  09_process_h: []
  10_process_v: []
  11_bignumber: []
  12_table: []
  13_icon_grid: []
  14_timeline: []
  15_hub_spoke: []
  16_layers: []
  17_warning: []
  18_checklist: []
  19_zoning: []
  20_quote: []
  21_ending: []
---

# Dark Tech Green Full - Design Specification (21 pages)

> 参考源：一份暗场科技绿风格的 PDF（21页，Type C 视觉参考）。
> 复制模式 standard。颜色/字体值由像素与元数据分析推断，标注为 [suggested]；画布几何为 [fact]。
> 本模板为 dark_tech_green 的**完整扩展版**：纯 SVG 矢量（无 AI 图依赖），21 种通用版式母版，**已去除全部行业属性，作为纯通用模板使用**。

## I. Template Overview

| Property | Value |
| --- | --- |
| **Template Name** | dark_tech_green_full |
| **Display Name** | 暗场科技绿·完整版（21页） |
| **Use Cases** | 科技汇报 / 项目方案 / 技术评估 / 管理汇报 / 通用演示（无行业属性） |
| **Design Tone** | 严谨、科技、数据感、暗场沉稳、发光绿点睛 |
| **Theme Mode** | Dark theme（深蓝墨黑底 + 科技绿 Accent + 数据网格） |

## II. Canvas Specification  [fact]

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Source ratio** | PDF 960×540 → ratio 1.7778（16:9）|
| **Safe Margins** | 60px 左右, 50px 上, 44px 下 |
| **Primary Content Area** | x: 60-1220, y: 120-628 |

## III. Color Scheme  [suggested]

| Role | Color Value | Usage |
| --- | --- | --- |
| **Background** | `#0A1020` | 深蓝墨黑主底 |
| **BG deep** | `#070C18` | 更深层次 / 渐变端点 |
| **Panel base** | `#12203A` | 深蓝面板基底（fill-opacity 0.55-0.9） |
| **Panel light** | `#1A2B45` | 面板高层 |
| **Primary** | `#00C060` | 科技绿 — 标题强调 / 主图表 / 主图标 |
| **Bright green** | `#00E070` | 高亮发光绿 — 关键数据 / 端点 / 发光线 |
| **Cyan** | `#06B6D4` | 青 — 渐变辅助 / 次高亮 |
| **Warning red** | `#D03040` | 警示红 — 风险 / 对比负向 / 强调点缀 |
| **Body text** | `#F0F0F0` | 主文亮白 |
| **Secondary text** | `#9DB2B0` | 柔灰绿注释 |
| **Tertiary text** | `#5E7078` | 页脚、辅助 |
| **Border** | `#1F3A52` | 面板描边（stroke-opacity 0.5-0.7） |
| **Green border** | `#1E4D3A` | 绿调描边 / 激活态 |
| **Light card** | `#EEF3F2` | 数据页浅色卡（承载图表，文字用 #0A1020） |

**60-30-10 原则**：深蓝墨底 60% / 面板+文字 30% / 科技绿 accent 10%。

## IV. Typography  [suggested]

| Role | Font Stack | Weight |
| --- | --- | --- |
| **Title** | `"Microsoft YaHei", "PingFang SC", sans-serif` | 900 |
| **Body** | `"Microsoft YaHei", "PingFang SC", Arial, sans-serif` | 400 |
| **Emphasis** | same as Body | 700 |
| **Mono/Number** | `Consolas, "Courier New", monospace` | 700 |

**Size 层级（body=20px 基准）**：

| Purpose | Size | Weight |
| --- | --- | --- |
| Cover title | 76px | 900 |
| Chapter title | 62px | 900 |
| Page title | 34px | 900 |
| Hero number (KPI) | 54px | 900 |
| Subtitle | 24px | 700 |
| **Body** | **20px** | 400 |
| Annotation | 15px | 400 |
| Footnote | 12px | 400 |

## V. Visual Motif Implementation

- **数据网格**：背景细网格线 `<line stroke="#1F3A52" stroke-opacity="0.22" stroke-width="1"/>`，营造数据室/仪表盘质感
- **发光绿线**：分隔线/进度条用 `url(#greenGlow)` 渐变，端点加小圆点 `<circle fill="#00E070"/>`
- **面板**：`<rect fill="url(#panelGrad)" stroke="#1F3A52" stroke-opacity="0.6" stroke-width="1" rx="14"/>`
- **左侧强调条**：标题左侧竖条 `<rect width="6" fill="url(#greenGlow)" rx="3"/>`
- **角标节点**：几何小方块/圆点作科技装饰，绿/青间隔
- **禁止** `<feGaussianBlur>` 做模糊（导出不稳），发光用半透明叠层 `fill-opacity` 模拟

### 渐变定义（复制到每页 `<defs>`）

```xml
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#00E070"/>
  <stop offset="60%" stop-color="#00C060"/>
  <stop offset="100%" stop-color="#06B6D4"/>
</linearGradient>
<linearGradient id="greenGlow" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#00E070"/>
  <stop offset="100%" stop-color="#06B6D4"/>
</linearGradient>
<linearGradient id="bgVert" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#0A1020"/>
  <stop offset="100%" stop-color="#070C18"/>
</linearGradient>
<radialGradient id="bgGlow" cx="82%" cy="18%" r="60%">
  <stop offset="0%" stop-color="#00C060" stop-opacity="0.18"/>
  <stop offset="100%" stop-color="#00C060" stop-opacity="0"/>
</radialGradient>
<radialGradient id="bgGlow2" cx="12%" cy="88%" r="55%">
  <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.14"/>
  <stop offset="100%" stop-color="#06B6D4" stop-opacity="0"/>
</radialGradient>
<linearGradient id="panelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#1A2B45" stop-opacity="0.9"/>
  <stop offset="100%" stop-color="#0E1830" stop-opacity="0.85"/>
</linearGradient>
<linearGradient id="barGrad" x1="0%" y1="100%" x2="0%" y2="0%">
  <stop offset="0%" stop-color="#00C060" stop-opacity="0.5"/>
  <stop offset="100%" stop-color="#00E070"/>
</linearGradient>
```

## VI. Icon Specification

- **Library**: 简化线性图标，统一 **内联 path / 基本图元** 绘制（不使用 `<use>` / `<symbol>` 引用，保证导出安全）
- **描边**：`stroke="#00C060"` 或 `#F0F0F0`，`stroke-width="2"`，`fill="none"`，`stroke-linecap="round" stroke-linejoin="round"`
- 内置图标：shield-check, lock, database, gauge, cpu, network, eye, warning, check, chart, flow, building, radar, cloud, file, car, layers, target, list, hub

## VII. Page Roster (21 母版)

| Page | File | Type | 适用场景 |
| --- | --- | --- | --- |
| P01 | `01_cover.svg` | 封面 | 标题 + 副标题 + 主旨 tag |
| P02 | `02_toc.svg` | 目录 | 编号模块导航（10 项） |
| P03 | `03_chapter.svg` | 章节分隔 | 大号篇章标识 + 含章节 |
| P04 | `04_overview.svg` | 概述四宫格 | 4 大要点 / 2×2 |
| P05 | `05_content_3col.svg` | 三栏卡 | 3 并列主题 |
| P06 | `06_content_list.svg` | 图标要点列表 | 5-6 项要点 |
| P07 | `07_data.svg` | 数据图表 | KPI + 柱状 + 浅色表 |
| P08 | `08_compare.svg` | 双栏对比 | 左 vs 右 |
| P09 | `09_process_h.svg` | 横向流程 | 编号步骤 |
| P10 | `10_process_v.svg` | 纵向时间线 | 时间轴步骤 |
| P11 | `11_bignumber.svg` | 大数字强调 | 核心指标 hero |
| P12 | `12_table.svg` | 标准数据表 | 浅色卡全表（多行） |
| P13 | `13_icon_grid.svg` | 图标矩阵 | 3×3 图标网格 |
| P14 | `14_timeline.svg` | 横向路线图 | 里程碑/阶段 |
| P15 | `15_hub_spoke.svg` | 中心辐射 | 五位一体/中心+辐射 |
| P16 | `16_layers.svg` | 分层架构 | 堆叠防护层 |
| P17 | `17_warning.svg` | 风险警示 | 红 accent 三卡 |
| P18 | `18_checklist.svg` | 清单核查 | 勾选要点 |
| P19 | `19_zoning.svg` | 分区布局 | 五功能区/分区图 |
| P20 | `20_quote.svg` | 核心主旨 | 金句强调 |
| P21 | `21_ending.svg` | 结尾 | 收束页 |

## VIII. Forbidden（导出安全）

- `<clipPath>` / 圆角裁切图（原生导出不支持）—— 面板圆角用 rx，图片走 preserveAspectRatio slice
- `<use>` / `<symbol>` 图标引用 —— 图标一律内联
- `rgba()` —— 用 `fill-opacity` / `stop-opacity`
- `<style>`, `class`, `<foreignObject>`, `textPath`, `<animate*>`, `<script>`, `<iframe>`
- `<g opacity="...">` —— 对每个子元素单独设 opacity
- `<feGaussianBlur>` 毛玻璃 —— 用半透明叠层模拟
- HTML 命名实体 —— 写 raw Unicode；XML 保留字用 `&amp; &lt; &gt; &quot; &apos;`
- 颜色只能取本 spec 表中的值

## IX. Reference

- 源参考渲染：参考 PDF 21 页均暗场（平均亮度 37-82），科技绿贯穿每页 2-5%，P12/P14 偏亮（≈76-82）对应含浅色卡片的数据/表格页。
