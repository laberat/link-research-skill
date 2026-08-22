# Link Research Skill

An evidence-first Agent Skill for researching a product website, open-source repository, article, technical page, or paper from a user-supplied link.

It helps an agent move beyond homepage or README paraphrasing and answer the questions that matter:

- What is this, and what is it not?
- Who needs it, and what triggers the search for it?
- What is the core workflow and implementation?
- Why are common alternatives insufficient?
- How credible, mature, and defensible is it?
- What are the limits, risks, and next validation steps?

## Highlights

- Routes among product, repository, article, and technical research modes.
- Distinguishes a URL from an already-rendered browser tab.
- Prefers primary sources and labels project claims, analysis, and unresolved facts.
- Uses progressive disclosure: the agent reads only the reference relevant to the current target.
- Treats research as read-only unless the user separately authorizes mutations.
- Integrates cleanly with the companion `wechat-article-reader` Skill for WeChat Official Account links.

## Install

With a Skills-compatible installer:

```bash
npx skills add <github-owner>/link-research-skill --skill link-research
```

Manual Codex installation:

```bash
cp -R link-research ~/.codex/skills/link-research
```

Start a new Agent task after installation so the Skill index is refreshed.

## Usage

```text
Research this product and explain who needs it, how it works, and why Notion is not enough:
https://example.com
```

```text
Analyze this GitHub project. Verify the README against the implementation and assess whether it is production-ready:
https://github.com/example/project
```

## Repository layout

```text
link-research-skill/
├── link-research/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── tests/
└── .github/workflows/test.yml
```

## Test

The test suite validates the Skill manifest, referenced resources, UI metadata, and absence of unfinished scaffold content.

```bash
python3 -m unittest discover -s tests -v
```

## Security and scope

This Skill defines a read-only research workflow. It does not grant permission to install or run third-party code, sign in, submit forms, publish content, change permissions, or send user data. Existing browser state is used only when the active Agent environment exposes it and the task calls for it.

## License

MIT
