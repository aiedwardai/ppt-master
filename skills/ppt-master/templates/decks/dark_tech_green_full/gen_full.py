# -*- coding: utf-8 -*-
"""dark_tech_green_full — 21 页版式母版生成器（纯矢量，通用无行业属性）。"""
import os

W, H = 1280, 720
FONT  = "&quot;Microsoft YaHei&quot;, &quot;PingFang SC&quot;, sans-serif"
FMONO = "Consolas, &quot;Courier New&quot;, monospace"

C = {
    "bg": "#0A1020", "bgdeep": "#070C18",
    "panel": "#12203A", "panel2": "#1A2B45",
    "primary": "#00C060", "bright": "#00E070", "cyan": "#06B6D4",
    "red": "#D03040",
    "body": "#F0F0F0", "sec": "#9DB2B0", "ter": "#5E7078",
    "border": "#1F3A52", "greenborder": "#1E4D3A",
    "light": "#EEF3F2",
}

# ---------- inline icons (24x24 stroke paths) ----------
ICONS = {
    "shield": "M12 2 L20 5 V11 C20 16 16 20 12 22 C8 20 4 16 4 11 V5 Z",
    "lock": "M6 10 V7 a6 6 0 0 1 12 0 V10 M5 10 H19 V21 H5 Z",
    "database": "M4 6 C4 3.8 7.6 2 12 2 S20 3.8 20 6 V18 C20 20.2 16.4 22 12 22 S4 20.2 4 18 Z M4 6 V12 C4 14.2 7.6 16 12 16 S20 14.2 20 12 V6 M4 12 V18 C4 20.2 7.6 22 12 22 S20 20.2 20 18 V12",
    "gauge": "M3 14 a9 9 0 0 1 18 0 M12 14 L17 9",
    "cpu": "M7 7 H17 V17 H7 Z M10 10 H14 V14 H10 Z M3 10 H7 M3 14 H7 M17 10 H21 M17 14 H21 M10 3 V7 M14 3 V7 M10 17 V21 M14 17 V21",
    "network": "M6 6 H10 V10 H6 Z M14 4 H18 V8 H14 Z M14 16 H18 V20 H14 Z M10 8 V12 H16",
    "eye": "M2 12 C5 7 9 5 12 5 S19 7 22 12 C19 17 15 19 12 19 S5 17 2 12 Z M12 9 a3 3 0 1 0 0.01 0 Z",
    "warning": "M12 3 L22 20 H2 Z M12 9 V14",
    "check": "M5 12 L10 17 L19 7",
    "chart": "M4 20 V4 M4 20 H20 M8 16 V12 M12 16 V8 M16 16 V10",
    "flow": "M3 12 H13 M13 12 L9 8 M13 12 L9 16 M13 12 H21",
    "building": "M5 21 V5 H13 V21 M17 21 V9 H19 V21 M8 8 H10 M8 12 H10 M8 16 H10",
    "radar": "M12 12 m-9 0 a9 9 0 1 0 18 0 a9 9 0 1 0 -18 0 M12 12 L19 7 M12 3 L12 12 L7 12",
    "cloud": "M7 18 a4 4 0 0 1 0-8 a5 5 0 0 1 9-1 a4 4 0 0 1 1 9 Z",
    "file": "M6 2 H14 L19 7 V22 H6 Z M14 2 V7 H19",
    "car": "M5 13 L7 7 H17 L19 13 M5 13 H19 V18 H5 Z M8 15 H8.01 M16 15 H16.01",
    "layers": "M12 3 L21 8 L12 13 L3 8 Z M3 13 L12 18 L21 13",
    "target": "M12 12 m-9 0 a9 9 0 1 0 18 0 a9 9 0 1 0 -18 0 M12 12 m-5 0 a5 5 0 1 0 10 0 a5 5 0 1 0 -10 0 M12 11 a1 1 0 1 0 0.01 0 Z",
    "list": "M8 6 H21 M8 12 H21 M8 18 H21 M4 6 H4.01 M4 12 H4.01 M4 18 H4.01",
    "hub": "M12 12 m-3 0 a3 3 0 1 0 6 0 a3 3 0 1 0 -6 0 M12 2 V8 M12 16 V22 M2 12 H8 M16 12 H22",
    "gear": "M12 8 a4 4 0 1 0 0.01 0 Z M12 2 V5 M12 19 V22 M2 12 H5 M19 12 H22 M5 5 L7 7 M17 17 L19 19 M19 5 L17 7 M7 17 L5 19",
}

def icon(name, x, cy, size=28, color=None):
    color = color or C["primary"]
    s = size / 24.0
    y = cy - size / 2.0
    d = ICONS.get(name, ICONS["shield"])
    return (f'<g transform="translate({x:.1f},{y:.1f}) scale({s:.4f})" '
            f'stroke="{color}" stroke-width="2" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="{d}"/></g>')

def defs():
    return (
        '<defs>'
        '<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%" stop-color="#00E070"/><stop offset="60%" stop-color="#00C060"/>'
        '<stop offset="100%" stop-color="#06B6D4"/></linearGradient>'
        '<linearGradient id="greenGlow" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%" stop-color="#00E070"/><stop offset="100%" stop-color="#06B6D4"/></linearGradient>'
        '<linearGradient id="bgVert" x1="0%" y1="0%" x2="0%" y2="100%">'
        '<stop offset="0%" stop-color="#0A1020"/><stop offset="100%" stop-color="#070C18"/></linearGradient>'
        '<radialGradient id="bgGlow" cx="82%" cy="18%" r="60%">'
        '<stop offset="0%" stop-color="#00C060" stop-opacity="0.18"/>'
        '<stop offset="100%" stop-color="#00C060" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="bgGlow2" cx="12%" cy="88%" r="55%">'
        '<stop offset="0%" stop-color="#06B6D4" stop-opacity="0.14"/>'
        '<stop offset="100%" stop-color="#06B6D4" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="panelGrad" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%" stop-color="#1A2B45" stop-opacity="0.9"/>'
        '<stop offset="100%" stop-color="#0E1830" stop-opacity="0.85"/></linearGradient>'
        '<linearGradient id="barGrad" x1="0%" y1="100%" x2="0%" y2="0%">'
        '<stop offset="0%" stop-color="#00C060" stop-opacity="0.5"/>'
        '<stop offset="100%" stop-color="#00E070"/></linearGradient>'
        '</defs>')

def bg():
    return ('<g id="bg">'
            '<rect width="1280" height="720" fill="url(#bgVert)"/>'
            '<rect width="1280" height="720" fill="url(#bgGlow)"/>'
            '<rect width="1280" height="720" fill="url(#bgGlow2)"/></g>')

def grid():
    return ('<g id="grid">'
            '<line x1="0" y1="180" x2="1280" y2="180" stroke="#1F3A52" stroke-opacity="0.18" stroke-width="1"/>'
            '<line x1="0" y1="360" x2="1280" y2="360" stroke="#1F3A52" stroke-opacity="0.18" stroke-width="1"/>'
            '<line x1="0" y1="540" x2="1280" y2="540" stroke="#1F3A52" stroke-opacity="0.18" stroke-width="1"/>'
            '<line x1="320" y1="0" x2="320" y2="720" stroke="#1F3A52" stroke-opacity="0.13" stroke-width="1"/>'
            '<line x1="640" y1="0" x2="640" y2="720" stroke="#1F3A52" stroke-opacity="0.13" stroke-width="1"/>'
            '<line x1="960" y1="0" x2="960" y2="720" stroke="#1F3A52" stroke-opacity="0.13" stroke-width="1"/>'
            '</g>')

def top_mark():
    return ('<g id="top-mark">'
            '<circle cx="64" cy="62" r="4" fill="#00E070"/>'
            '<circle cx="76" cy="62" r="4" fill="#00C060" fill-opacity="0.7"/>'
            '<circle cx="88" cy="62" r="4" fill="#06B6D4" fill-opacity="0.55"/>'
            f'<text x="106" y="67" font-family="{FONT}" font-size="13" font-weight="600" fill="{C["sec"]}" letter-spacing="3">GENERIC TEMPLATE · 2026</text>'
            '</g>')

def footer(num):
    return ('<g id="footer">'
            f'<text x="60" y="690" font-family="{FONT}" font-size="13" font-weight="600" fill="{C["sec"]}">汇报单位 · 2026</text>'
            f'<text x="1220" y="690" font-family="{FONT}" font-size="13" font-weight="600" fill="{C["ter"]}" text-anchor="end">{num:02d} / 21</text>'
            '</g>')

def header(title, tag):
    return ('<g id="header">'
            '<rect x="60" y="74" width="6" height="40" rx="3" fill="url(#greenGlow)"/>'
            f'<text x="86" y="104" font-family="{FONT}" font-size="34" font-weight="900" fill="{C["body"]}">{title}</text>'
            f'<text x="1220" y="104" font-family="{FONT}" font-size="15" font-weight="400" fill="{C["ter"]}" text-anchor="end" letter-spacing="2">{tag}</text>'
            f'<line x1="60" y1="132" x2="1220" y2="132" stroke="{C["border"]}" stroke-opacity="0.6" stroke-width="1"/>'
            '</g>')

def panel(x, y, w, h, fill=None, stroke=None, so=0.6):
    fill = fill or "url(#panelGrad)"
    stroke = stroke or C["border"]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" '
            f'fill="{fill}" stroke="{stroke}" stroke-opacity="{so}" stroke-width="1"/>')

def wrap(t, n):
    out = []
    for i in range(0, len(t), n):
        out.append(t[i:i+n])
    return out or [""]

def doc(body, num, with_grid=False, with_topmark=False):
    g = grid() if with_grid else ""
    tm = top_mark() if with_topmark else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
            + defs() + "\n" + bg() + "\n" + g + "\n" + tm + "\n" + body + "\n"             + footer(num) + "\n</svg>\n")

def img_placeholder(x, y, w, h, label="图片 / IMAGE"):
    """图片占位框（纯矢量，自洽可复用；生成正式 PPT 时替换为 <image>）。"""
    cx = x + w / 2.0
    cy = y + h / 2.0 - 16
    return (
        f'<g>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#0E1830" fill-opacity="0.45" stroke="#1F3A52" stroke-opacity="0.85" '
        f'stroke-width="1.5" stroke-dasharray="8 6"/>'
        f'<rect x="{cx-22:.0f}" y="{cy-12:.0f}" width="44" height="28" rx="4" fill="none" '
        f'stroke="#00C060" stroke-opacity="0.6" stroke-width="2"/>'
        f'<rect x="{cx-8:.0f}" y="{cy-20:.0f}" width="16" height="9" rx="2" fill="none" '
        f'stroke="#00C060" stroke-opacity="0.6" stroke-width="2"/>'
        f'<circle cx="{cx:.0f}" cy="{cy+2:.0f}" r="9" fill="none" stroke="#00C060" stroke-opacity="0.6" stroke-width="2"/>'
        f'<text x="{cx:.0f}" y="{y+h/2.0+44:.0f}" font-family="{FONT}" font-size="16" font-weight="700" '
        f'fill="#9DB2B0" text-anchor="middle">{label}</text>'
        f'<text x="{cx:.0f}" y="{y+h/2.0+68:.0f}" font-family="{FONT}" font-size="13" '
        f'fill="#5E7078" text-anchor="middle">替换为实景图 / 图表</text>'
        f'</g>')

# ===================== PAGE FUNCTIONS =====================

def p01_cover():
    body = (
        img_placeholder(850, 196, 360, 360)
        + '<g id="title-block">'
        '<rect x="160" y="266" width="6" height="200" rx="3" fill="url(#greenGlow)"/>'
        f'<text x="196" y="300" font-family="{FONT}" font-size="14" font-weight="700" fill="#00E070" letter-spacing="4">PROJECT TEMPLATE · 2026</text>'
        f'<text x="194" y="388" font-family="{FONT}" font-size="76" font-weight="900" fill="url(#titleGradient)" letter-spacing="-1">主标题写这里</text>'
        f'<text x="196" y="452" font-family="{FONT}" font-size="24" font-weight="400" fill="{C["body"]}">副标题 · 一句话说明主题与范围</text>'
        f'<line x1="196" y1="484" x2="316" y2="484" stroke="#00E070" stroke-width="2" stroke-linecap="round"/>'
        f'<text x="196" y="524" font-family="{FONT}" font-size="18" font-weight="700" fill="{C["primary"]}">核心要点 · 关键词 · 一句话概述</text>'
        '</g>'
        '<g id="meta">'
        f'<text x="196" y="600" font-family="{FONT}" font-size="16" font-weight="700" fill="{C["body"]}">汇报单位名称</text>'
        f'<text x="340" y="600" font-family="{FONT}" font-size="16" fill="{C["sec"]}">2026 年 3 月 编制</text>'
        '</g>')
    return doc(body, 1, with_topmark=True)

def p02_toc():
    mods = ["项目背景与概述", "目标与范围界定", "核心方案设计", "实施路径规划",
            "技术架构支撑", "组织与人员保障", "风险与合规管理", "进度与里程碑",
            "成效与评估", "结论与下一步"]
    body = top_mark() + (
        '<g id="toc-head">'
        '<rect x="60" y="84" width="6" height="46" rx="3" fill="url(#greenGlow)"/>'
        f'<text x="86" y="104" font-family="{FONT}" font-size="14" font-weight="700" fill="#00E070" letter-spacing="4">目录 / CONTENTS</text>'
        f'<text x="86" y="138" font-family="{FONT}" font-size="34" font-weight="900" fill="{C["body"]}">内容总览</text>'
        '</g>')
    col_x = [80, 660]
    y0 = 196
    rh = 86
    for i, m in enumerate(mods):
        col = i // 5
        row = i % 5
        x = col_x[col]
        y = y0 + row * rh
        body += panel(x, y, 520, 70)
        body += (f'<circle cx="{x+40}" cy="{y+35}" r="22" fill="none" stroke="#00C060" stroke-opacity="0.6" stroke-width="1.5"/>'
                 f'<text x="{x+40}" y="{y+42}" font-family="{FMONO}" font-size="20" font-weight="700" fill="#00E070" text-anchor="middle">{i+1:02d}</text>'
                 f'<text x="{x+78}" y="{y+42}" font-family="{FONT}" font-size="20" font-weight="700" fill="{C["body"]}">{m}</text>')
    return doc(body, 2)

def p03_chapter(part, ptitle, chapters):
    body = (
        img_placeholder(830, 200, 390, 360)
        + f'<text x="80" y="250" font-family="{FONT}" font-size="26" font-weight="700" fill="#00E070" letter-spacing="6">{part}</text>'
        + f'<text x="80" y="346" font-family="{FONT}" font-size="62" font-weight="900" fill="{C["body"]}">{ptitle}</text>'
        + '<rect x="84" y="374" width="160" height="6" rx="3" fill="url(#greenGlow)"/>'
        + '<g id="ch-list">')
    yy = 430
    for ch in chapters:
        body += (f'<circle cx="92" cy="{yy-6}" r="4" fill="#00E070"/>'
                 f'<text x="112" y="{yy}" font-family="{FONT}" font-size="20" font-weight="400" fill="{C["sec"]}">{ch}</text>')
        yy += 40
    body += '</g>'
    return doc(body, 3, with_topmark=True)

def p04_overview():
    cards = [("shield", "项目背景", "依托相关政策与行业标准，明确建设目标、范围与约束条件，覆盖规划、实施、验收、运营全流程。"),
             ("target", "核心目标", "从战略、组织、技术、数据、保障五大维度，构建可落地、可衡量、可持续的推进体系。"),
             ("database", "关键要素", "涵盖核心业务对象、关键流程节点与重要资产，确保全生命周期可控、可追溯。"),
             ("check", "预期成效", "达成既定质量、进度与要求，规避延期、超支与重大风险，实现预期价值。")]
    body = header("概述与四大要点", "OVERVIEW")
    pos = [(80,160),(650,160),(80,400),(650,400)]
    for (ic, t, d), (x, y) in zip(cards, pos):
        body += panel(x, y, 540, 220)
        body += icon(ic, x+30, y+52, 38, C["primary"]) + "\n"
        body += f'<text x="{x+84}" y="{y+62:.0f}" font-family="{FONT}" font-size="26" font-weight="900" fill="{C["body"]}">{t}</text>\n'
        ty = y + 108
        for ln in wrap(d, 24):
            body += f'<text x="{x+32}" y="{ty}" font-family="{FONT}" font-size="18" fill="{C["sec"]}">{ln}</text>\n'
            ty += 28
    return doc(body, 4, with_grid=True)

def p05_content_3col():
    cards = [("building", "模块一", "内容说明一，独立功能定位，配独立流程与资源保障。"),
             ("lock", "模块二", "内容说明二，独立功能定位，配独立流程与资源保障。"),
             ("cpu", "模块三", "内容说明三，独立功能定位，配独立流程与资源保障。")]
    body = header("三栏并列内容", "THREE COLUMNS")
    x0, y, w, h = 60, 170, 380, 430
    for i, (ic, t, d) in enumerate(cards):
        x = x0 + i * 410
        body += panel(x, y, w, h)
        body += icon(ic, x+30, y+62, 44, C["primary"]) + "\n"
        body += f'<text x="{x+92}" y="{y+74:.0f}" font-family="{FONT}" font-size="28" font-weight="900" fill="{C["body"]}">{t}</text>\n'
        ty = y + 140
        for ln in wrap(d, 18):
            body += f'<text x="{x+32}" y="{ty}" font-family="{FONT}" font-size="19" fill="{C["sec"]}">{ln}</text>\n'
            ty += 30
        body += f'<rect x="{x+32}" y="{y+h-58}" width="{w-64}" height="6" rx="3" fill="url(#greenGlow)"/>\n'
    return doc(body, 5, with_grid=True)

def p06_content_list():
    rows = [("file", "背景意义", "项目立项背景、政策与业务驱动因素、建设必要性"),
            ("list", "核心目标", "总体目标、分阶段目标与可量化指标"),
            ("shield", "关键策略", "总体策略、重点工作与推进原则"),
            ("database", "实施路径", "任务分解、责任分工与进度安排"),
            ("lock", "资源保障", "组织、资金、技术与人力的支撑保障"),
            ("eye", "风险管控", "风险识别、评估、预警与应对机制")]
    body = header("核心要点列表", "KEY POINTS")
    y = 168
    for ic, t, d in rows:
        body += panel(60, y, 1160, 70)
        body += icon(ic, 90, y+35, 30, C["cyan"]) + "\n"
        body += f'<text x="140" y="{y+44:.0f}" font-family="{FONT}" font-size="21" font-weight="700" fill="{C["body"]}">{t}</text>\n'
        body += f'<text x="360" y="{y+44:.0f}" font-family="{FONT}" font-size="18" fill="{C["sec"]}">{d}</text>\n'
        y += 80
    return doc(body, 6, with_grid=True)

def p07_data():
    body = header("数据图表页", "DATA &amp; CHARTS")
    # KPI row
    kpis = [("98", "%", "整体完成率"), ("120", "", "关键任务项"), ("12", "月", "建设周期")]
    kx = 60
    for val, unit, lab in kpis:
        body += panel(kx, 160, 360, 120)
        body += f'<text x="{kx+28}" y="{222}" font-family="{FMONO}" font-size="46" font-weight="700" fill="#00E070">{val}</text>'
        if unit:
            body += f'<text x="{kx+28+len(val)*26}" y="{222}" font-family="{FONT}" font-size="18" font-weight="700" fill="#9DB2B0">{unit}</text>'
        body += f'<text x="{kx+28}" y="{258}" font-family="{FONT}" font-size="15" fill="#9DB2B0">{lab}</text>'
        kx += 380
    # bar chart
    body += panel(60, 304, 560, 292)
    body += f'<text x="88" y="340" font-family="{FONT}" font-size="18" font-weight="700" fill="#F0F0F0">各维度完成率</text>'
    vals = [100, 140, 80, 160, 110]
    labels = ["A","B","C","D","E"]
    base = 546
    for i, vv in enumerate(vals):
        bx = 132 + i*92
        bh = vv
        body += f'<rect x="{bx}" y="{base-bh}" width="52" height="{bh}" rx="4" fill="url(#barGrad)"/>'
        body += f'<text x="{bx+26}" y="568" font-family="{FONT}" font-size="13" fill="#9DB2B0" text-anchor="middle">{labels[i]}</text>'
    body += (f'<line x1="92" y1="546" x2="596" y2="546" stroke="#1F3A52" stroke-opacity="0.7" stroke-width="1"/>'
             f'<line x1="92" y1="486" x2="596" y2="486" stroke="#1F3A52" stroke-opacity="0.3" stroke-width="1"/>'
             f'<line x1="92" y1="426" x2="596" y2="426" stroke="#1F3A52" stroke-opacity="0.3" stroke-width="1"/>')
    # light card table
    body += ('<rect x="648" y="160" width="572" height="436" rx="16" fill="#EEF3F2"/>'
             '<rect x="648" y="160" width="572" height="52" rx="16" fill="#0A1020"/>'
             '<rect x="648" y="192" width="572" height="20" fill="#0A1020"/>'
             f'<text x="676" y="193" font-family="{FONT}" font-size="17" font-weight="700" fill="#00E070">数据明细表（浅色卡）</text>')
    rows = [("数据行一","86.2%",True),("数据行二","92.7%",True),("数据行三","63.1%",False),("数据行四","78.4%",True),("数据行五","95.0%",True)]
    ry = 256
    body += f'<text x="676" y="{ry}" font-family="{FONT}" font-size="14" font-weight="700" fill="#5E7078">项目</text>'
    body += f'<text x="960" y="{ry}" font-family="{FONT}" font-size="14" font-weight="700" fill="#5E7078">数值</text>'
    body += f'<text x="1120" y="{ry}" font-family="{FONT}" font-size="14" font-weight="700" fill="#5E7078">状态</text>'
    ry += 16
    for name, val, ok in rows:
        body += f'<line x1="676" y1="{ry}" x2="1192" y2="{ry}" stroke="#0A1020" stroke-opacity="0.12" stroke-width="1"/>'
        ry += 18
        body += f'<text x="676" y="{ry}" font-family="{FONT}" font-size="15" fill="#0A1020">{name}</text>'
        body += f'<text x="960" y="{ry}" font-family="{FMONO}" font-size="15" font-weight="700" fill="#0A1020">{val}</text>'
        body += f'<circle cx="1128" cy="{ry-5}" r="5" fill="{"#00C060" if ok else "#D03040"}"/>'
        ry += 36
    body += ('<rect x="676" y="504" width="516" height="68" rx="10" fill="#0A1020" fill-opacity="0.06"/>'
             f'<text x="696" y="536" font-family="{FONT}" font-size="14" font-weight="700" fill="#5E7078">结论摘要</text>'
             f'<text x="696" y="558" font-family="{FONT}" font-size="14" fill="#0A1020">浅色卡承载表格与结论，与暗场主体形成对比。</text>')
    return doc(body, 7, with_grid=True)

def p08_compare():
    body = header("双栏对比", "COMPARE")
    cols = [("方案 / 现状 A", "red", ["指标与能力偏弱","协同机制缺失","资源配置不足","过程留痕不完整","缺乏应急预案"]),
            ("方案 / 目标 B", "primary", ["指标与能力达标","协同机制健全","资源配置充分","过程全程留痕","预案完备可落地"])]
    cxs = [60, 650]
    for (t, col, items), x in zip(cols, cxs):
        body += panel(x, 160, 560, 440)
        c = C[col]
        body += f'<rect x="{x}" y="160" width="560" height="56" rx="14" fill="{c}" fill-opacity="0.12"/>'
        body += f'<text x="{x+28}" y="198" font-family="{FONT}" font-size="24" font-weight="900" fill="{c}">{t}</text>'
        yy = 250
        for it in items:
            body += icon("check" if col=="primary" else "warning", x+30, yy, 24, c) + "\n"
            body += f'<text x="{x+70}" y="{yy+6:.0f}" font-family="{FONT}" font-size="19" fill="{C["body"]}">{it}</text>\n'
            yy += 64
    body += (f'<circle cx="640" cy="380" r="30" fill="#0A1020" stroke="#1F3A52" stroke-opacity="0.7" stroke-width="1"/>'
             f'<text x="640" y="388" font-family="{FONT}" font-size="18" font-weight="700" fill="#F0F0F0" text-anchor="middle">VS</text>')
    return doc(body, 8, with_grid=True)

def p09_process_h():
    body = header("横向流程", "PROCESS")
    steps = [("需求调研","明确目标、范围与现状基线"),("方案设计","制定总体方案与技术路线"),
             ("资源筹备","组织、资金、技术就绪"),("实施落地","按计划推进建设交付"),
             ("验收交付","评估验收与闭环移交")]
    n = len(steps)
    gap = 226
    first_cx = 640 - (n-1)*gap/2.0
    y0 = 300
    # connecting line (centered)
    body += f'<line x1="{first_cx:.0f}" y1="{y0}" x2="{first_cx+(n-1)*gap:.0f}" y2="{y0}" stroke="#1E4D3A" stroke-width="2"/>'
    for i, (t, d) in enumerate(steps):
        cx = first_cx + i*gap
        body += (f'<circle cx="{cx:.0f}" cy="{y0}" r="30" fill="#0A1020" stroke="#00C060" stroke-width="2"/>'
                 f'<text x="{cx:.0f}" y="{y0+8}" font-family="{FMONO}" font-size="22" font-weight="700" fill="#00E070" text-anchor="middle">{i+1}</text>')
        body += panel(cx-90, y0+70, 200, 140)
        body += f'<text x="{cx:.0f}" y="{y0+108}" font-family="{FONT}" font-size="20" font-weight="700" fill="{C["body"]}" text-anchor="middle">{t}</text>'
        ty = y0+138
        for ln in wrap(d, 11):
            body += f'<text x="{cx:.0f}" y="{ty}" font-family="{FONT}" font-size="14" fill="{C["sec"]}" text-anchor="middle">{ln}</text>\n'
            ty += 20
    return doc(body, 9, with_grid=True)

def p10_process_v():
    body = header("纵向时间线", "TIMELINE")
    steps = [("规划阶段","目标与方案设计，明确范围与约束条件"),
             ("建设阶段","任务实施与系统集成落地"),
             ("验收阶段","多维度评估与联合验收"),
             ("运营阶段","常态化运营与迭代优化")]
    y = 180
    line_x = 120
    body += f'<line x1="{line_x}" y1="{y}" x2="{line_x}" y2="{y+(len(steps)-1)*120}" stroke="#1E4D3A" stroke-width="2"/>'
    for i, (t, d) in enumerate(steps):
        cy = y + i*120
        body += (f'<circle cx="{line_x}" cy="{cy}" r="18" fill="#0A1020" stroke="#00C060" stroke-width="2"/>'
                 f'<text x="{line_x}" y="{cy+6}" font-family="{FMONO}" font-size="15" font-weight="700" fill="#00E070" text-anchor="middle">{i+1}</text>')
        body += panel(line_x+50, cy-46, 1040, 92)
        body += f'<text x="{line_x+78}" y="{cy-6:.0f}" font-family="{FONT}" font-size="22" font-weight="700" fill="{C["body"]}">{t}</text>'
        for ln in wrap(d, 50):
            body += f'<text x="{line_x+78}" y="{cy+22:.0f}" font-family="{FONT}" font-size="17" fill="{C["sec"]}">{ln}</text>\n'
            break
    return doc(body, 10, with_grid=True)

def p11_bignumber():
    body = header("核心指标强调", "KEY METRIC")
    body += img_placeholder(720, 180, 460, 300)
    body += ('<g id="hero">'
             f'<text x="80" y="360" font-family="{FMONO}" font-size="180" font-weight="700" fill="url(#titleGradient)">100%</text>'
             f'<text x="84" y="420" font-family="{FONT}" font-size="30" font-weight="700" fill="{C["body"]}">核心目标 · 全面达成</text>'
             f'<text x="84" y="460" font-family="{FONT}" font-size="20" fill="{C["sec"]}">以关键指标为牵引，确保质量、进度与成效全面达标。</text>'
             '</g>')
    stats = [("一级","成熟度基线"),("标准A","关键技术"),("常态化","运营机制")]
    y = 520
    for i, (v, l) in enumerate(stats):
        x = 80 + i*380
        body += panel(x, y, 340, 110)
        body += f'<text x="{x+28}" y="{y+58}" font-family="{FMONO}" font-size="34" font-weight="700" fill="#00E070">{v}</text>'
        body += f'<text x="{x+28}" y="{y+88}" font-family="{FONT}" font-size="16" fill="#9DB2B0">{l}</text>'
    return doc(body, 11, with_grid=True)

def p12_table():
    body = header("标准数据表", "DATA TABLE")
    body += ('<rect x="60" y="160" width="1160" height="468" rx="16" fill="#EEF3F2"/>'
             '<rect x="60" y="160" width="1160" height="52" rx="16" fill="#0A1020"/>'
             '<rect x="60" y="192" width="1160" height="20" fill="#0A1020"/>'
             f'<text x="88" y="193" font-family="{FONT}" font-size="17" font-weight="700" fill="#00E070">关键要素对照表</text>')
    headers = ["编号","要素","责任方","关键要求"]
    hx = [88, 360, 720, 980]
    ry = 248
    for h, x in zip(headers, hx):
        body += f'<text x="{x}" y="{ry}" font-family="{FONT}" font-size="15" font-weight="700" fill="#5E7078">{h}</text>'
    ry += 12
    rows = [("T-01","需求分析","业务组","范围清晰、目标可量化"),
            ("T-02","方案设计","技术组","路线可行、风险可控"),
            ("T-03","资源筹备","保障组","组织资金技术到位"),
            ("T-04","实施交付","执行组","按节点高质量完成"),
            ("T-05","验收评估","质控组","达标评审闭环移交")]
    for r in rows:
        body += f'<line x1="88" y1="{ry}" x2="1192" y2="{ry}" stroke="#0A1020" stroke-opacity="0.10" stroke-width="1"/>'
        ry += 16
        for val, x in zip(r, hx):
            fs = 14 if x!=hx[0] else 14
            body += f'<text x="{x}" y="{ry}" font-family="{FONT}" font-size="14" fill="#0A1020">{val}</text>'
        ry += 50
    return doc(body, 12, with_grid=True)

def p13_icon_grid():
    body = header("图标矩阵", "ICON GRID")
    items = [("shield","战略规划"),("lock","组织保障"),("database","流程规范"),("cpu","技术支撑"),
             ("network","数据管理"),("eye","风险管控"),("radar","监测评估"),("cloud","协同联动"),("gear","持续改进")]
    x0, y0, cw, ch = 60, 168, 373, 140
    for i, (ic, t) in enumerate(items):
        r, c = i//3, i%3
        x = x0 + c*cw
        y = y0 + r*ch
        body += panel(x, y, cw-20, ch-20)
        body += icon(ic, x+44, y+70, 40, C["primary"]) + "\n"
        body += f'<text x="{x+96}" y="{y+78:.0f}" font-family="{FONT}" font-size="22" font-weight="700" fill="{C["body"]}">{t}</text>'
    return doc(body, 13, with_grid=True)

def p14_timeline():
    body = header("横向路线图", "ROADMAP")
    ms = [("Q1","启动","立项与规划"),("Q2","建设","实施与部署"),("Q3","验收","评估与评审"),("Q4","运营","运营与迭代")]
    y = 372
    n = len(ms)
    x0, gap = 160, 320
    body += f'<line x1="{x0}" y1="{y}" x2="{x0+(n-1)*gap}" y2="{y}" stroke="#1E4D3A" stroke-width="2"/>'
    for i, (q, t, d) in enumerate(ms):
        cx = x0 + i*gap
        body += (f'<circle cx="{cx}" cy="{y}" r="26" fill="#0A1020" stroke="#00C060" stroke-width="2"/>'
                 f'<text x="{cx}" y="{y+6}" font-family="{FMONO}" font-size="16" font-weight="700" fill="#00E070" text-anchor="middle">{q}</text>')
        # alt above/below — 与节点圆保持安全间距，避免重叠
        if i % 2 == 0:
            body += f'<text x="{cx}" y="{y-72}" font-family="{FONT}" font-size="20" font-weight="700" fill="{C["body"]}" text-anchor="middle">{t}</text>'
            body += f'<text x="{cx}" y="{y-48}" font-family="{FONT}" font-size="15" fill="{C["sec"]}" text-anchor="middle">{d}</text>'
        else:
            body += f'<text x="{cx}" y="{y+58}" font-family="{FONT}" font-size="20" font-weight="700" fill="{C["body"]}" text-anchor="middle">{t}</text>'
            body += f'<text x="{cx}" y="{y+82}" font-family="{FONT}" font-size="15" fill="{C["sec"]}" text-anchor="middle">{d}</text>'
    return doc(body, 14, with_grid=True)

def p15_hub_spoke():
    body = header("中心辐射架构", "HUB &amp; SPOKE")
    cx, cy = 640, 400
    nodes = [("战略引领",-200,-120),("组织保障",200,-120),("流程规范",-200,120),("技术支撑",200,120),("数据驱动",0,-210)]
    # spokes
    for _, dx, dy in nodes:
        body += f'<line x1="{cx}" y1="{cy}" x2="{cx+dx}" y2="{cy+dy}" stroke="#1E4D3A" stroke-width="2"/>'
    # center
    body += (f'<circle cx="{cx}" cy="{cy}" r="64" fill="#0A1020" stroke="#00C060" stroke-width="2"/>'
             f'<text x="{cx}" y="{cy+8}" font-family="{FONT}" font-size="22" font-weight="900" fill="#00E070" text-anchor="middle">核心</text>'
             f'<text x="{cx}" y="{cy+34}" font-family="{FONT}" font-size="18" font-weight="700" fill="#00E070" text-anchor="middle">体系</text>')
    for t, dx, dy in nodes:
        nx, ny = cx+dx, cy+dy
        body += (f'<circle cx="{nx}" cy="{ny}" r="50" fill="url(#panelGrad)" stroke="#1F3A52" stroke-opacity="0.6" stroke-width="1"/>'
                 f'<text x="{nx}" y="{ny+7}" font-family="{FONT}" font-size="18" font-weight="700" fill="{C["body"]}" text-anchor="middle">{t}</text>')
    return doc(body, 15, with_grid=True)

def p16_layers():
    body = header("分层架构", "LAYERED")
    layers = [("战略层 · 目标与决策","#00C060"),("管理层 · 组织与制度","#06B6D4"),
              ("执行层 · 任务与流程","#00C060"),("支撑层 · 技术与平台","#06B6D4"),
              ("保障层 · 资源与风险","#00E060")]
    y = 158
    for i, (t, col) in enumerate(layers):
        h = 78
        body += (f'<rect x="60" y="{y}" width="1160" height="{h}" rx="12" fill="url(#panelGrad)" stroke="#1F3A52" stroke-opacity="0.6" stroke-width="1"/>'
                 f'<rect x="60" y="{y}" width="10" height="{h}" rx="5" fill="{col}"/>'
                 f'<text x="100" y="{y+34:.0f}" font-family="{FONT}" font-size="13" font-weight="700" fill="{col}" letter-spacing="2">L{5-i}</text>'
                 f'<text x="100" y="{y+60:.0f}" font-family="{FONT}" font-size="22" font-weight="700" fill="{C["body"]}">{t}</text>')
        if i < len(layers)-1:
            body += f'<text x="640" y="{y+h+20:.0f}" font-family="{FONT}" font-size="16" fill="#00E070" text-anchor="middle">▲</text>'
        y += h + 22
    return doc(body, 16, with_grid=True)

def p17_warning():
    body = header("风险警示", "RISK ALERT")
    items = [("进度风险","计划排期不合理或依赖未就绪，导致关键节点延期、交付超期。"),
             ("质量风险","过程管控不到位、标准执行偏差，影响交付质量与验收结果。"),
             ("资源风险","人力、资金或技术支撑不足，制约项目推进与成效达成。")]
    x0, y, w, h = 60, 170, 380, 430
    for i, (t, d) in enumerate(items):
        x = x0 + i*410
        body += panel(x, y, w, h, stroke=C["red"], so=0.6)
        body += icon("warning", x+30, y+62, 44, C["red"]) + "\n"
        body += f'<text x="{x+92}" y="{y+74:.0f}" font-family="{FONT}" font-size="26" font-weight="900" fill="#D03040">{t}</text>\n'
        ty = y + 140
        for ln in wrap(d, 18):
            body += f'<text x="{x+32}" y="{ty}" font-family="{FONT}" font-size="19" fill="{C["sec"]}">{ln}</text>\n'
            ty += 30
    return doc(body, 17, with_grid=True)

def p18_checklist():
    body = header("核查清单", "CHECKLIST")
    items = ["目标清晰、范围明确，对齐业务战略","方案可行，关键路径与依赖梳理完整",
             "组织到位，责任分工与协同机制健全","资源就绪，资金技术与平台支撑充分",
             "过程留痕，关键节点评审与文档完整","风险可控，预警与应急预案完备",
             "验收闭环，成效评估与持续改进机制"]
    y = 168
    for it in items:
        body += panel(60, y, 1160, 56)
        body += icon("check", 90, y+28, 26, C["primary"]) + "\n"
        body += f'<text x="132" y="{y+36:.0f}" font-family="{FONT}" font-size="19" fill="{C["body"]}">{it}</text>\n'
        y += 66
    return doc(body, 18, with_grid=True)

def p19_zoning():
    body = header("分区布局示意", "ZONING")
    # outer boundary
    body += '<rect x="80" y="160" width="1120" height="450" rx="16" fill="none" stroke="#1F3A52" stroke-opacity="0.6" stroke-width="2"/>'
    body += f'<text x="104" y="190" font-family="{FONT}" font-size="15" font-weight="700" fill="#9DB2B0">总体布局 · 分区协同</text>'
    zones = [("功能区一","database"),("功能区二","lock"),("功能区三","cpu"),("功能区四","flow"),("功能区五","list")]
    zx, zy, zw, zh = 110, 220, 205, 150
    for i, (t, ic) in enumerate(zones):
        col = i % 3
        row = i // 3
        x = zx + col*(zw+25)
        y = zy + row*(zh+30)
        body += panel(x, y, zw, zh)
        body += icon(ic, x+24, y+40, 30, C["cyan"]) + "\n"
        body += f'<text x="{x+66}" y="{y+48:.0f}" font-family="{FONT}" font-size="20" font-weight="700" fill="{C["body"]}">{t}</text>\n'
        body += f'<text x="{x+24}" y="{y+92:.0f}" font-family="{FONT}" font-size="14" fill="{C["sec"]}">独立隔断 · 专属职能</text>'
    #通道
    body += (f'<rect x="980" y="220" width="190" height="150" rx="12" fill="#0A1020" stroke="#00C060" stroke-opacity="0.5" stroke-width="1.5"/>'
             f'<text x="1075" y="300" font-family="{FONT}" font-size="18" font-weight="700" fill="#00E070" text-anchor="middle">协同通道</text>'
             f'<text x="1075" y="326" font-family="{FONT}" font-size="14" fill="#9DB2B0" text-anchor="middle">互联贯通</text>')
    return doc(body, 19, with_grid=True)

def p20_quote():
    body = (
        '<g id="deco">'
        '<circle cx="120" cy="180" r="40" fill="none" stroke="#00C060" stroke-opacity="0.3" stroke-width="1.5"/>'
        '<circle cx="1160" cy="540" r="60" fill="none" stroke="#06B6D4" stroke-opacity="0.2" stroke-width="1"/>'
        '</g>'
        f'<text x="640" y="250" font-family="{FONT}" font-size="120" font-weight="900" fill="#00E070" text-anchor="middle" fill-opacity="0.25">“</text>'
        f'<text x="640" y="350" font-family="{FONT}" font-size="40" font-weight="900" fill="{C["body"]}" text-anchor="middle">专业 · 安全 · 可靠 · 可追溯</text>'
        f'<text x="640" y="410" font-family="{FONT}" font-size="22" font-weight="400" fill="{C["sec"]}" text-anchor="middle">构建完整闭环管理体系，保障核心业务对象、关键流程与重要资产安全可控，</text>'
        f'<text x="640" y="446" font-family="{FONT}" font-size="22" font-weight="400" fill="{C["sec"]}" text-anchor="middle">支撑业务高质量、可持续发展。</text>'
        '<rect x="560" y="486" width="160" height="5" rx="2.5" fill="url(#greenGlow)"/>')
    return doc(body, 20, with_topmark=True)

def p21_ending():
    body = (
        '<g id="deco-nodes">'
        '<circle cx="1080" cy="360" r="100" fill="none" stroke="#00C060" stroke-opacity="0.22" stroke-width="1.5"/>'
        '<circle cx="1080" cy="360" r="150" fill="none" stroke="#06B6D4" stroke-opacity="0.12" stroke-width="1"/>'
        '<circle cx="1080" cy="360" r="6" fill="#00E070"/>'
        '</g>'
        f'<text x="640" y="320" font-family="{FONT}" font-size="16" font-weight="700" fill="#00E070" letter-spacing="6" text-anchor="middle">专业驱动 · 价值运营</text>'
        f'<text x="640" y="400" font-family="{FONT}" font-size="64" font-weight="900" fill="url(#titleGradient)" text-anchor="middle">谢谢观看</text>'
        f'<text x="640" y="452" font-family="{FONT}" font-size="22" font-weight="400" fill="{C["body"]}" text-anchor="middle">欢迎就本项目进一步交流</text>'
        '<rect x="560" y="486" width="160" height="5" rx="2.5" fill="url(#greenGlow)"/>')
    return doc(body, 21, with_topmark=True)

# ===================== DISPATCH =====================
PAGES = [
    ("01_cover", p01_cover),
    ("02_toc", p02_toc),
    ("03_chapter", lambda: p03_chapter("第一篇", "章节主题", ["一、小节标题一", "二、小节标题二"])),
    ("04_overview", p04_overview),
    ("05_content_3col", p05_content_3col),
    ("06_content_list", p06_content_list),
    ("07_data", p07_data),
    ("08_compare", p08_compare),
    ("09_process_h", p09_process_h),
    ("10_process_v", p10_process_v),
    ("11_bignumber", p11_bignumber),
    ("12_table", p12_table),
    ("13_icon_grid", p13_icon_grid),
    ("14_timeline", p14_timeline),
    ("15_hub_spoke", p15_hub_spoke),
    ("16_layers", p16_layers),
    ("17_warning", p17_warning),
    ("18_checklist", p18_checklist),
    ("19_zoning", p19_zoning),
    ("20_quote", p20_quote),
    ("21_ending", p21_ending),
]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg_output")
    os.makedirs(out, exist_ok=True)
    for fname, fn in PAGES:
        svg = fn()
        with open(os.path.join(out, fname + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg)
        print("written", fname)
    print("TOTAL", len(PAGES))
