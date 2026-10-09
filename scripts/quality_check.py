#!/usr/bin/env python3
"""教程学习笔记终检脚本（确定性检查，不耗 token）。

用法：python quality_check.py <笔记.md 路径>
逐项输出 PASS/FAIL，全部通过后再人工过一遍 SKILL.md Phase 8 的终检清单。
"""
import re
import sys

REQUIRED_SECTIONS = [
    "一段话总结",
    "五视角证据表",
    "矛盾图",
    "调研简报",
    "同行评审",
    "资源清单",
    "负面清单",
    "一周学习路径",
    "五级难度地图",
    "80/20",
    "10 次课",
    "前沿问题",
    "常见错误",
]

LEVELS = ["完全初学者", "基本理解", "实际使用者", "问题解决者", "自信的实践者"]
LEVEL_QUESTIONS = ["级别名称", "阶段理解", "掌握", "重点关注", "进阶里程碑",
                   "动手练习", "常犯的错误", "自测问题"]


def check(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    failures = 0

    for sec in REQUIRED_SECTIONS:
        ok = sec in text
        print(f"{'PASS' if ok else 'FAIL'}  必需小节存在: {sec}")
        failures += not ok

    for lv in LEVELS:
        ok = lv in text
        print(f"{'PASS' if ok else 'FAIL'}  难度级别存在: {lv}")
        failures += not ok

    for q in LEVEL_QUESTIONS:
        n = len(re.findall(re.escape(q), text))
        ok = n >= 5
        print(f"{'PASS' if ok else 'FAIL'}  每级8问之「{q}」出现 {n} 次（需≥5）")
        failures += not ok

    # 「$紧跟数字」会被部分 runtime 的 skill 加载器当参数占位符插值
    hits = re.findall(r"\$\d", text)
    ok = not hits
    print(f"{'PASS' if ok else 'FAIL'}  无「$紧跟数字」写法（发现 {len(hits)} 处）")
    failures += bool(hits)

    # 残留模板占位符
    ph = re.findall(r"\[(?:待填|TODO|xxx|主题占位)[^\]]*\]", text, re.I)
    ok = not ph
    print(f"{'PASS' if ok else 'FAIL'}  无残留占位符（发现 {len(ph)} 处）")
    failures += bool(ph)

    # 「凭记忆未核」标注若出现，必须原样保留（不许洗白）——只报告数量
    mem = len(re.findall(r"凭记忆未核", text))
    print(f"INFO  「凭记忆未核」标注 {mem} 处（人工确认均为未核实内容）")

    print("=" * 40)
    print("ALL PASS" if failures == 0 else f"{failures} 项 FAIL，回 SKILL.md 对应 Phase 修补")
    return failures


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(1 if check(sys.argv[1]) else 0)
