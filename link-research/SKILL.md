---
name: link-research
description: Research and explain a user-supplied product site, open-source repository, article, technical page, or paper. Use when the user asks what a link is, who needs it, how it works, how it is implemented, how credible it is, or how it compares. Do not use for simple navigation, copying a known passage, or ordinary coding work that merely contains a URL.
---

# Link Research

Turn a link into an evidence-backed explanation of the thing behind it. Default to a medium-depth, read-only investigation covering product meaning and implementation rather than paraphrasing the landing page or README. Respond in the user's language unless they request otherwise, while preserving source-language terms when translation would reduce precision.

## Acquire the target faithfully

Treat a URL and an already-open browser tab as different inputs.

- If the user supplies an exact tab reference, or says the already-rendered page is important, use the installed browser-control capability and read that tab without reloading or navigating to the same URL.
- For login-dependent, strongly dynamic, visual, or anti-bot-prone pages, ask the user to open the page until its main content is visible and attach the exact tab. Verify its title and URL, then read the current DOM; scroll or use screenshots only as needed.
- For ordinary public GitHub repositories, official documentation, and machine-readable pages, prefer the relevant API, CLI, connector, or direct fetch. Do not add browser handoff friction when current browser state has no material value.
- When the user explicitly requests browser-first research, follow that preference for the supplied target.
- For `mp.weixin.qq.com` articles, use the companion `wechat-article-reader` skill when it is available. It owns the specialized acquisition and fallback rules; otherwise follow the evidence reference and disclose acquisition limits.

Do not refresh a successfully loaded protected page. Never bypass CAPTCHA, login, paywalls, or safety interstitials. A failed acquisition is not permission to install tools, submit data, or use credentials.

## Classify and route

Read only the reference matching the target, plus the evidence reference:

- Product or commercial website: [references/product-research.md](references/product-research.md)
- Open-source repository: [references/repository-research.md](references/repository-research.md)
- Article, report, or commentary: [references/article-research.md](references/article-research.md)
- Technical documentation or paper: [references/technical-research.md](references/technical-research.md)
- Evidence, browser handoff, and source labels: always read [references/source-and-evidence.md](references/source-and-evidence.md)

If a target spans multiple types, choose the primary mode and load a second reference only when it materially changes the analysis. For example, a GitHub project with a commercial hosted product normally starts as repository research and adds product research only if business viability is part of the user's question.

## Build the explanation

Unless the user narrows the scope, answer these core questions:

1. What is it, and what is it not?
2. Who uses, buys, or benefits from it?
3. What event or frustration makes someone look for it?
4. What job does it complete, and what did users do before?
5. What is the core input → processing → output → next-action flow?
6. Why are common alternatives insufficient?
7. How is it implemented, and where is the real technical difficulty?
8. What is differentiated, defensible, or easy to copy?
9. How mature and credible is it?
10. What are its limits, risks, and unresolved uncertainties?
11. Who should use it, who should not, and what should be tested first?

Avoid forcing a fixed report template when a concise answer is enough. For a substantial investigation, lead with the conclusion and normally organize the result as:

- one-sentence conclusion;
- what it is and the user need;
- workflow and important capabilities;
- implementation or architecture;
- alternatives and differentiation;
- maturity, business model, or project health;
- limitations and risks;
- judgment and recommended next validation;
- links to the strongest sources.

Use a comparison table or small flow only when it makes relationships materially clearer.

## Preserve epistemic boundaries

- Distinguish verified facts, project claims, analysis, and unresolved items.
- Prefer primary sources: current page, official documentation, repository code, releases, issues, pricing, security pages, and original research.
- Do not treat homepage copy, README claims, star counts, revenue claims, or benchmark charts as self-validating.
- Cite the page that directly supports each time-sensitive or consequential claim.
- State when the target page could not be read and which fallback supplied the evidence.
- Do not imply that a mirror, search snippet, cached page, or repost is the original article.

## Default authorization boundary

Research is read-only. Inspecting public sources, source code, metadata, and existing browser state is allowed. Installing or running third-party code, signing in, submitting forms, publishing, changing permissions, or sending data requires separate scope or confirmation under the active environment rules.
