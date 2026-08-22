# Technical Documentation and Paper Research

## Core questions

- What technical problem does it solve, and under what assumptions?
- Which abstraction, interface, algorithm, or system boundary does it change relative to existing approaches?
- What are the inputs, outputs, state, dependencies, and failure modes?
- Do the examples match the current version, and do they run in the stated environment?
- How were performance, cost, or quality results measured, and are the baselines fair?
- Do the paper's experimental setup, datasets, ablations, and limitations support its conclusion?
- Which changed conditions would invalidate the conclusion?
- What adaptations, dependencies, and validation are required for the user's environment?

## Source priority

Specification or original paper → official documentation → current source code and tests → releases and issues → author commentary → third-party tutorials.

Distinguish conceptual explanation from the current implementation. Verify versions, deprecations, defaults, and API behavior against current official material or code.

## Explaining the implementation

Prefer a small data-flow, call-flow, or module diagram when explaining three or more dependencies. Do not list every class, parameter, or section merely for completeness; focus on mechanisms that affect correctness, performance, reliability, and adoption decisions.
