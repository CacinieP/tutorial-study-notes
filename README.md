# tutorial-study-notes · 教程学习笔记术

把一个教程/课程/技术主题，用「Agent 加速学习」工作流写成一份有深度的教程式学习笔记。

> Agent 不能替你想，但能替你把「想的过程」拆成可执行的步骤。

## 安装

克隆本仓库，把 `tutorial-study-notes/` 目录整个拷到你的 agent skills 目录即可自包含使用：

```bash
git clone https://github.com/CacinieP/tutorial-study-notes.git
cp -r tutorial-study-notes ~/.claude/skills/   # 或其他 runtime 的 skills 目录
```

## 工作流（八步）

```
Phase 0  入口与主题定义（主题/我的角色/时间预算/输出载体）
Phase 1  找齐 5 个视角（实践者/学者/怀疑者/经济学家/史学家）
Phase 2  画矛盾图 5 问（冲突/证据强弱/杠杆问题/共识/盲区）
Phase 3  压成调研简报 5 要素（一段话总结/可靠性排序/隐藏关联/行动建议/前沿问题）
Phase 4  同行评审 5 问（逐项打分/最没把握的结论/权重失衡/第6视角/教授评分）
Phase 5  筛 5 个资源 + 排一周路径（每个资源过四问 + 负面清单）
Phase 6  5 级难度 × 每级 8 问（初学者→自信的实践者）
Phase 7  80/20 + 10 次课计划（每次课：目标/关键概念/动手练习/推荐资源）
Phase 8  成文与终检（按模板组装 + quality_check.py）
```

底层学习观：一条路径、一次测试、一次压缩、一个反馈循环，四要素缺一不可。

## 用法

对 agent 说：「用 tutorial-study-notes 写一份【主题】的教程学习笔记」，或直接用触发词：

- 写教程学习笔记 / 学 XX 做笔记 / 把这篇教程整理成笔记
- Agent 加速学习 / AI-Native 学习笔记

各 Phase 可直接复制的 prompt 模板在 `references/prompts.md`，最终笔记结构在 `references/note-template.md`，终检脚本：

```bash
python scripts/quality_check.py <笔记.md>
```

## 示例

`examples/408-27kaoyan-study-note.md` —— 用 2027 考研 408 计算机学科专业基础综合大纲跑完整八步工作流产出的 sample 笔记（含五视角证据表、矛盾图、简报、同行评审、资源一周路径、五级难度地图、80/20+10次课计划），终检脚本 ALL PASS。

## 目录结构

```
tutorial-study-notes/
├── SKILL.md                        # Skill 主文件（工作流 + 反模式 + 诚实边界）
├── references/
│   ├── prompts.md                  # 各 Phase 可直接复制的 prompt 模板
│   └── note-template.md            # 最终笔记输出模板
├── examples/
│   └── 408-27kaoyan-study-note.md  # Sample：27考研408大纲笔记
└── scripts/
    └── quality_check.py            # 笔记终检脚本（确定性检查）
```

## 来源与署名

本 Skill 蒸馏自：

- 语码Cace《AI时代，Agent加速学习实践清单》（微信公众号文章，由微信读书内容整理）：https://mp.weixin.qq.com/s/wP1Pya_0kScqMQzZZnMO3w
  - Notion 整理页面将该文来源记为《AI-Native文科生自学计算机301408day01》（疑为微信读书收藏/系列名）；文章实际标题以公众号原文为准
- Notion 页面《AI-Native 文科生自学计算机：Agent 加速学习实践清单》
- 文中提到的 STORM 学习法，出处未标注；最可能对应 Stanford STORM 论文（Shao et al., NAACL 2024, arXiv:2402.14207，多视角写前调研），此对应为推断，详见 SKILL.md

为方法论蒸馏与工程化改写，非原文复制。原框架为个人实践总结，无实证背书，适用边界见 SKILL.md「适用边界与诚实声明」。

## License

MIT
