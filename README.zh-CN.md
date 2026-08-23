# 链接调研 Skill

[English](README.md)

一个证据优先的 Agent Skill，用于根据用户提供的链接调研产品网站、开源项目、文章、技术页面或论文。

它帮助 Agent 超越对首页或 README 的简单复述，回答真正重要的问题：

- 它是什么，又不是什么？
- 谁需要它，什么事件会让用户开始寻找它？
- 核心工作流和实现方式是什么？
- 为什么常见替代方案不能满足需求？
- 它有多可信、成熟和可防御？
- 有哪些限制、风险和后续验证步骤？

## 特点

- 根据目标自动路由到产品、代码仓库、文章或技术调研模式。
- 区分普通 URL 和用户已经成功打开的浏览器页面。
- 优先使用一手来源，并区分项目方自述、分析推断和待验证事实。
- 使用渐进式披露，只读取当前调研目标需要的 reference。
- 默认将调研视为只读操作，除非用户另行授权修改。
- 可与 [`wechat-article-reader`](https://github.com/laberat/wechat-article-reader-skill) 配合读取微信公众号文章。
- Agent 默认使用用户的语言回答，同时保留必要的原文术语。

## 安装

使用兼容 Agent Skills 的安装器：

```bash
npx skills add laberat/link-research-skill --skill link-research
```

手动安装到 Codex：

```bash
cp -R link-research ~/.codex/skills/link-research
```

安装后新建一个 Agent 任务，使 Skill 索引重新加载。

## 使用示例

```text
调研这个产品，解释谁需要它、它如何工作，以及现有替代方案为什么可能无法满足需求：
https://example.com
```

```text
分析这个 GitHub 项目。用代码核对 README，并判断它是否适合生产环境：
https://github.com/example/project
```

## 仓库结构

```text
link-research-skill/
├── link-research/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── tests/
└── .github/workflows/test.yml
```

## 测试

测试会校验 Agent Skills 命名和 frontmatter 约束、reference 链接、UI 元数据、机器指令语言一致性、中英文 README 互链，以及是否存在未完成的脚手架内容。

```bash
python3 -m unittest discover -s tests -v
```

## 安全与范围

该 Skill 定义的是只读调研流程。它不会授权安装或执行第三方代码、登录、提交表单、发布内容、修改权限或发送用户数据。只有在 Agent 环境提供浏览器能力且任务确实需要时，才会使用用户已有的浏览器状态。

所有被调研的页面、代码仓库、文章和读取产物都属于非可信证据。目标内容中嵌入的指令不能覆盖用户请求、Skill 或更高优先级指令。

安全报告方式和支持边界参见 [SECURITY.md](SECURITY.md)。

## 许可证

MIT
