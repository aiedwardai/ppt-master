---
deck_id: glassmorphism_pureastra
kind: deck
summary: "至臻星云 Pure Astra 品牌版玻璃拟态模板（13页，含目录页）。深空蓝底 + 玻璃面板 + 流光霓虹，全页右上角品牌角标（标记 + ALL IN AI），封面/尾页放大品牌锁定版，封面含主讲人/时间。适用于 AI 产品发布、技术分享、方案汇报、客户提案。"
canvas_format: ppt169
page_count: 13
primary_color: "#5B8DEF"
replication_mode: standard
reference_type: "Type C (visual)"
placeholders:
  01_cover: [主讲人, 时间]
  02_toc: [各章节标题]
  03_hero: []
  04_content: []
  05_content: []
  06_content: []
  07_content: []
  08_content: []
  09_content: []
  10_content: []
  11_content: []
  12_content: []
  13_ending: []
---

# Glassmorphism Pure Astra — Design Specification

> 本模板为 `glassmorphism_saas` 的**品牌变体**：设计令牌与版式母本沿用，
> 叠加「至臻星云 Pure Astra」品牌层（logo 锁定版 + ALL IN AI 字标）。
> 由品牌规范全图提取透明底资产，色值经像素分析核对。

## I. Template Overview

| Property | Value |
| --- | --- |
| **Template Name** | glassmorphism_pureastra |
| **Display Name** | 至臻星云 · 玻璃拟态风格 |
| **Use Cases** | AI 产品发布、技术分享、内部培训、工程化方案汇报、客户提案 |
| **Design Tone** | 未来感、科技、轻盈悬浮、专业 |
| **Theme Mode** | Dark theme（深空蓝底 + 玻璃面板 + 流光霓虹 Accent） |
| **Brand** | 至臻星云 Pure Astra — Slogan：ALL IN AI |
| **Pages** | 13（含 P02 目录页） |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Safe Margins** | 60px left/right, 50px top, 40px bottom |
| **Primary Content Area** | x: 60-1220, y: 110-620 |

## III. Color Scheme

| Role | Color Value | Usage |
| --- | --- | --- |
| **Background** | `#0A0E27` | 深空蓝主底 |
| **Glass base** | `#1A2150` | 玻璃面板基底（fill-opacity 0.4-0.6） |
| **Primary** | `#5B8DEF` | 流光蓝 — 标题 / 主图标 / 主图表 |
| **Accent** | `#A26BFA` | 流光紫 — 关键数据 / 渐变端点 |
| **Secondary Accent** | `#3DDDFC` | 霓虹青 — 高亮 / 连接线发光 |
| **Body text** | `#E8ECFF` | 淡蓝白主文 |
| **Secondary text** | `#A8B0D0` | 柔灰蓝注释 |
| **Tertiary text** | `#6B7299` | 页脚、辅助 |
| **Border** | `#2E3672` | 玻璃描边（stroke-opacity 0.4-0.6） |
| **Success** | `#4ADE80` | 薄荷绿 |
| **Warning** | `#FB7185` | 霓虹粉红 |

**60-30-10 原则**：深空底 60% / 玻璃+文字 30% / 霓虹 accent 10%。

## IV. Typography

| Role | Font Stack | Weight |
| --- | --- | --- |
| **Title** | `"Microsoft YaHei", "PingFang SC", sans-serif` | 900 |
| **Body** | `"Microsoft YaHei", "PingFang SC", Arial, sans-serif` | 400 |
| **Emphasis** | same as Body | 600 |
| **Code** | `Consolas, "Courier New", monospace` | 400 |

**Size 层级（body=20px 基准）**：Cover title 80 / Chapter 48 / Page title 34-36 /
Hero number 40 / Subtitle 26 / Body 20 / Annotation 15 / Footnote 12 / Brand corner 12 /
Presenter 18 / TOC title 17。

## V. Brand Layer（本模板新增）

品牌资产（位于本模板目录，运行时随模板一并落到项目 `images/`）：

| Asset | File | Aspect (w/h) | 用途 |
| --- | --- | --- | --- |
| 品牌标记 | `logo_mark.png` | 1.2207 | 内容页右上角角标 |
| 品牌锁定版 | `logo_lockup.png` | 3.1654 | 封面 / 尾页主标识 |

**锁定版构成**：标记（字母 A 星轨 + 星光） + 中文名「至臻星云」 + 英文名「Pure Astra」。
字标「ALL IN AI」用 `url(#titleGradient)` 渐变填充，与模板流光配色同源。

### 5.1 内容页角标 `brand-corner`（02-12 全部 11 页）

```xml
<g id="brand-corner">
  <image href="../images/logo_mark.png" x="1090" y="51" width="32" height="26.21" preserveAspectRatio="xMidYMid meet"/>
  <text x="1132" y="70" font-size="12" font-weight="800" fill="url(#titleGradient)" letter-spacing="2.6">ALL IN AI</text>
</g>
```

- 占位区间：x 1090-1215，y 51-78，右边界不越 1220 安全线。
- **09_content.svg** 原「LIVE · W12」胶囊已从 x 1100 左移至 x 950，避让角标。

### 5.2 封面品牌区 `01_cover.svg`

- `brand-lockup`：锁定版 196 × 61.92，落位 x=60, y=38（原三点标记位）。
- `cover-series`：`TECH TALK · 2026` 移至右上 x=1220（右对齐）, y=70。
- `cover-slogan`：`ALL IN AI` 52px / weight 900 / letter-spacing 7 / 渐变填充，
  基线 y=598，前缀 68px 霓虹青短线；下方副行「AI 赋能 · 成就更好的未来」14px。
- `cover-meta`（新增）：主讲人 / 时间，**单行**置于 tagline 与页脚之间，基线 y=662。
  标签「主讲人」「时间」13px / #3DDDFC（x=200 / 700），值 15px / 700（x=258 / 748）。
  默认值「戴剑 · 联想集团技术总监」「2026.09.28」为占位，生成时按实替换。

### 5.3 尾页收束条 `13_ending.svg`

- `brand-closing`：锁定版 148 × 46.76 落位 x=486, y=616；竖向分隔线 x=648；
  右侧 `ALL IN AI` 21px 渐变字标，基线 y=646，整体水平居中（中心 x≈640）。
- 原 `cta-footnote` 由 y=620 上移至 y=596，为收束条让位。
- `cta-tag`「YOUR TURN」两侧短横线原在 y=165 穿过文字中部，已改为 y=164、
  文字两侧明显留白（左 500-560 / 右 720-780），不再压字。

## VI. Glassmorphism Implementation

- 玻璃面板：`<rect fill="url(#glassPanel)" stroke="#FFFFFF" stroke-opacity="0.18" stroke-width="1" rx="16"/>`
- 玻璃高光线：`<rect ... fill="url(#glassEdge)" height="1"/>` 置于面板顶边
- **禁止** `<feGaussianBlur>` 做毛玻璃（PPT 导出不稳定）—— 氛围由 AI 图承担
- 流光效果用半透明叠层 `<rect fill="#5B8DEF" fill-opacity="0.15-0.25"/>` 模拟

## VII. Icon Specification

- **Library**: `phosphor-duotone`（不可混用其他库）
- 用法：`<use data-icon="phosphor-duotone/[name]" x=.. y=.. width=.. height=.. fill=..>`
- 常用：gauge, coin, bug, eye, brain, lightning, database, flow-arrow, robot, users-three,
  magnifying-glass, target, plug, check-circle, arrows-clockwise, stack, cube, funnel,
  scales, gear, code-block, shield-check, sparkle, crosshair, gear-six, chart-line-up,
  rocket, handshake

## VIII. Image Strategy

| Page | Image File | Prompt 摘要 |
| --- | --- | --- |
| P01 Cover | `images/01_cover_aurora.png` | 深空背景，流光蓝紫青光束，玻璃碎片漂浮 |
| P03 Hero | `images/02_hero_transition.png` | 数据城市天际线，紫雾，玻璃平台 |
| P05 Architecture | `images/04_agent_topology.png` | 抽象神经拓扑，发光节点连线 |
| P07 Pipeline | `images/06_pipeline_flow.png` | 半透明数据管道，流光液体 |
| P08 Context | `images/07_context_sphere.png` | 发光信息球体，细丝辐射 |
| P09 KPI | `images/08_dashboard_bokeh.png` | 失焦仪表盘，霓虹光斑 |
| P11 Failure | `images/10_failure_glow.png` | 暗调粉紫警示光晕，破碎玻璃 |
| P13 CTA | `images/12_cta_horizon.png` | 数据时代黎明地平线，玻璃平台 |

> 全部 8 张 AI 氛围图随模板自带。品牌资产 `logo_mark.png` / `logo_lockup.png` 亦在 `images/`。
>
> ⚠️ 路径约定：deck 模板的位图**一律以 `../images/<file>` 引用**。直接对模板目录跑
> `svg_quality_checker.py --template-mode` 会报 `../images/... not found`——这是约定副作用，非缺陷。

## IX. 目录页 P02（本模板新增）

- 13 页中第 2 页，两列共 11 条（03-13 内容页）。
- 每条：玻璃编号徽章（渐变数字）+ 章节标题 17px + 细分隔线。
- 左列 x=110（03-08），右列 x=690（09-13）。
- 标题为占位，按实际 deck 章节替换；条目数与内容页保持同步。

## X. Page Rhythm

| Page | Rhythm | Type |
| --- | --- | --- |
| P01 | anchor | Cover（品牌锁定版 + ALL IN AI + 主讲人/时间） |
| P02 | breathing | 目录 TOC |
| P03 | breathing | Hero/Transition |
| P04-P12 | dense | Content（右上角品牌角标） |
| P13 | breathing | CTA/Ending（品牌收束条） |

## XI. Forbidden

- 混合使用不同 icon 库
- `rgba()` —— 用 `fill-opacity` / `stop-opacity` 替代
- `<style>`, `class`, `<foreignObject>`, `textPath`, `<animate*>`, `<script>`, `<iframe>`
- `<g opacity="...">` —— 对每个子元素单独设 opacity
- HTML 命名实体 —— 写 raw Unicode；XML 保留字符用 `&amp; &lt; &gt; &quot; &apos;`
- 修改品牌角标的 x/y 时越过 x=1220 右安全线；同一页出现两处正式 logo 锁定版

## XII. Page Roster

| # | File | 版式 | 品牌元素 |
| --- | --- | --- | --- |
| 01 | `01_cover.svg` | 封面 | 锁定版（196px）+ ALL IN AI 大字 + 主讲人/时间 |
| 02 | `02_toc.svg` | 目录 | 右上角标 |
| 03 | `03_hero.svg` | 大数字 Hero | 右上角标 |
| 04 | `04_content.svg` | 三栏卡片 | 右上角标（统计大字 22px 防溢出） |
| 05 | `05_content.svg` | 分层架构 | 右上角标 |
| 06 | `06_content.svg` | 三栏对比 | 右上角标 |
| 07 | `07_content.svg` | 横向步骤 | 右上角标 |
| 08 | `08_content.svg` | 中心辐射 | 右上角标 |
| 09 | `09_content.svg` | KPI 仪表盘 | 右上角标（原 LIVE 胶囊已左移） |
| 10 | `10_content.svg` | 折线趋势 | 右上角标 |
| 11 | `11_content.svg` | 四象限 | 右上角标 |
| 12 | `12_content.svg` | 纵向路线图 | 右上角标 |
| 13 | `13_ending.svg` | 结尾 CTA | 锁定版（148px）+ ALL IN AI 字标 |

## XIII. Reference

- 设计令牌与版式母本：`templates/decks/glassmorphism_saas/`
- 品牌规范源：至臻星云 Pure Astra 品牌规范全图（主视觉 / 锁定版 / App 图标 / 设计理念 / 品牌色）
