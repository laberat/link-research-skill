# Content Acquisition and Evidence Rules

## Acquisition order

Choose the method that stays closest to the original content while adding the least user friction:

1. An exact, successfully rendered browser tab explicitly handed off by the user.
2. The service's official API, CLI, connector, or semantic reader.
3. Direct retrieval of the original URL.
4. Cross-checking with official documentation, code repositories, and other primary sources.
5. Search indexes, caches, reposts, or mirrors.
6. User-provided HTML, PDF, screenshots, or copied text.

This is not a mechanical sequence. GitHub repositories normally start with GitHub and the code; authenticated or strongly anti-bot-protected pages normally start with the existing browser tab.

MCP is a tool interface, not an evidence tier. First identify an MCP's underlying source and additional capability. Do not retry through it when it merely wraps the same ordinary HTTP request that already failed.

## Browser handoff

When the user's existing page state matters, ask clearly:

> Open the page in Chrome or the Codex in-app browser, wait until the main content is visible, and attach that exact tab. After you confirm, I will read the existing page without refreshing or navigating again.

After handoff:

1. Verify the current title and URL.
2. Read the current DOM directly.
3. Locate the main content or primary data area.
4. Scroll when needed to load lazy content.
5. Use screenshots when the DOM is incomplete or visual information matters.
6. Stop when the page itself is a verification screen; do not attempt to bypass it.

## Evidence labels

Distinguish these categories in reasoning and, when useful, in the answer:

- **Verified fact**: directly supported by the original page, code, official documentation, or original data.
- **Project claim**: stated by the website, README, founder, or marketing material but not independently verified.
- **Analytical inference**: an interpretation derived from multiple facts and explicitly framed as an inference.
- **Unresolved**: evidence is insufficient or conflicting, or the page is inaccessible.

## Time and source handling

- For changing facts such as pricing, team, versions, activity, user counts, revenue, features, and policies, record the current date and use the latest primary source.
- For news and events, check both the publication date and the date the event occurred.
- For technical questions, prefer official documentation, specifications, source code, and papers.
- When an article cites another data source, return to the original source when possible.

## Stopping conditions

- After one request method fails, do not enumerate User-Agents, rotate proxies, or repeat requests in an attempt to bypass the block.
- Stop the relevant path when CAPTCHA, login, payment, or a safety interstitial appears.
- If the original text is unavailable, a repost or search snippet may be used with lower confidence and explicit disclosure of its source type.
