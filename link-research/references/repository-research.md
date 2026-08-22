# Open-Source Repository Research

## Do not stop at the README

Inspect as needed:

README → license → package manifest → entry points → core modules → configuration and permissions → tests and CI → releases and tags → issues and pull requests → commit activity.

## Core questions

- What problem does the project solve, and does it provide a library, CLI, service, plugin, Skill, or complete application?
- What is the minimum usage flow, with real inputs and outputs?
- Do the README's installation commands, package names, and features match the code and release channels?
- Where are the entry points, and how are the main modules and data flows organized?
- Does it call third-party services, and where is data sent?
- Does it read credentials, browser state, local files, or environment variables?
- Does it cause side effects such as uploading, executing, deleting, publishing, or changing permissions?
- Does the license permit the user's intended use, and are there obvious dependency-license conflicts?
- Do tests cover behavior or only syntax and fixed text? Does CI actually run?
- Is the project actively maintained, and what real limitations do open issues reveal?
- Is it best adopted directly, extended, used as a reference implementation, or treated only as a proof of concept?

## Implementation explanation

Provide a verifiable module-level architecture instead of merely repeating the technology stack. Cite entry points and key code locations when useful. Distinguish:

- ordinary engineering composition;
- non-obvious algorithm or protocol handling;
- fragile dependencies on external platforms;
- documented claims that the code does not yet support.

Stars and forks are only attention signals; they do not prove security, maintenance quality, or production maturity.
