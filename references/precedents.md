# Precedents: people who aimed higher with AI

When proposing a bolder version of a task, cite one precedent from this file so the user sees it has already been done, and how. Never overstate: keep the caveats (self-reported, unconfirmed, a big company's resources) attached when you cite.

## Speed

**Airbnb migrated ~3,500 test files in 6 weeks instead of an estimated 1.5 years.** They broke the job into per-file steps run in parallel, with automatic checks (lint, type check, tests) after each step, retry loops when a check failed, and prompts full of extra context. — Source: [Accelerating Large-Scale Test Migration with LLMs](https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms), 2025 (self-reported).

**Amazon cut Java version upgrades from ~50 developer-days per app to a few hours.** They plugged Amazon Q's code-transformation tool into internal systems and upgraded over half of production Java apps in under six months. 79% of the generated changes shipped unedited; Amazon estimates 4,500 developer-years saved. — Source: [Andy Jassy on LinkedIn](https://www.linkedin.com/posts/andy-jassy-8b1615_one-of-the-most-tedious-but-critical-tasks-activity-7232374162185461760-AdSz), 2024-08-22 (self-reported).

**Three Google developers ran 39 code migrations in 12 months, with the LLM writing ~74% of the changes.** A tool first located every place that needed changing, then had an LLM draft the edits for humans to review. Developers estimated a 50% time saving. — Source: [Migrating Code At Scale With LLMs At Google](https://arxiv.org/abs/2504.09691), 2025-04-13.

**A microbiology lab got its unpublished, decade-long hypothesis back from an AI in 48 hours.** Prof. José Penadés (Imperial College) gave Google's "co-scientist" a short prompt about how superbugs spread between species. It reached his team's unpublished conclusion and suggested four more hypotheses, one of which the lab is now testing. — Source: [BBC: AI cracks superbug problem in two days](https://www.bbc.com/news/articles/clyz6e9edy3o), Feb 2025.

## Depth

**A security researcher found a new remote Linux kernel vulnerability using only the o3 API.** Sean Heelan fed the model the relevant kernel code (the SMB file-sharing server) and asked it to audit for bugs. It found CVE-2025-37899, a "use-after-free" (memory used after being released) that only shows up when connections run concurrently. He benchmarked over 100 runs against a bug he had found by hand; roughly 1 in 50 reports was real, so a human still has to triage the output. — Source: [How I used o3 to find CVE-2025-37899](https://sean.heelan.io/2025/05/22/how-i-used-o3-to-find-cve-2025-37899-a-remote-zeroday-vulnerability-in-the-linux-kernels-smb-implementation/), 2025-05-22 (self-reported).

**A top theorist credited GPT-5 with the key idea in a quantum-complexity proof.** Scott Aaronson was stuck on one step. Within about half an hour GPT-5-Thinking suggested the function that made the proof work. He adds that it "should have" been obvious to experts, and that a blog commenter later found a better one. — Source: [The QMA Singularity](https://scottaaronson.blog/?p=9183), 2025-09-27 (self-reported).

**One prompt caught a 10x math error in a viral health paper, and that started a volunteer error-hunting project.** Ethan Mollick asked o1 to "carefully check the math" in the black-plastic-utensils paper. It found that 7,000×60 had been written as 42,000. Steve Newman then organised the Black Spatula Project to run such checks at scale. — Source: [The Black Spatula Project](https://open.substack.com/pub/amistrongeryet/p/the-black-spatula-project), 2024-12-18.

**An amateur solved a 60-year-old Erdős problem with a single prompt.** Liam Price, 23, with no advanced maths training, asked GPT-5.4 Pro about Erdős's conjecture on "primitive sets" (sets where no number divides another) and posted the proof. Terence Tao said the AI took a route humans had missed. — Source: [Scientific American](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/), 2026-04-24.

**The first Erdős problem counted as solved autonomously by AI came with a machine-checked proof.** Kevin Barreto paired GPT-5.2 Pro with Harmonic's Aristotle, which writes proofs in Lean, a language where a computer verifies every step: an outside judge rather than the model grading itself. — Source: [Resolution of Erdős Problem #728](https://arxiv.org/abs/2601.07421), 2026-01-12.

**16 parallel Claude agents wrote a 100,000-line C compiler that builds the Linux kernel.** The work took about 2,000 sessions over two weeks for roughly $20k. A key step was using GCC, an existing trusted compiler, as a "known-good oracle" so agents could check their output against it automatically. — Source: [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler), 2026-02-05 (self-reported, Anthropic).

## Range

**A product manager with no astronomy training found a possible new exoplanet in NASA data.** Pavel Rabtsevich had Claude Code, Codex and another model scan public TESS satellite data on 126,000 stars for regular dips in brightness. He then ran 74 tests trying to disprove his best candidate and got MIT to schedule follow-up telescope time. It is still a *candidate*, with a public, pre-registered prediction. — Source: [Gizmodo](https://gizmodo.com/did-claude-help-an-amateur-astronomer-discover-a-new-planet-2000824393), 2026-10-09.

**A mother got her son's diagnosis after 17 doctors in 3 years had missed it.** She gave ChatGPT his full symptom history and MRI notes. It suggested tethered cord syndrome; a neurosurgeon confirmed it from his MRIs, and he had surgery. — Source: [NBC/TODAY](https://nbcwashington.com/news/national-international/a-boy-saw-17-doctors-over-3-years-for-chronic-pain-chatgpt-found-the-right-diagnosis/3421991), 2023-09-12 (self-reported by the family).

**Andrej Karpathy, with little web-development experience, shipped a paid app end to end.** MenuGen turns a photo of a menu into pictures of each dish. He vibe-coded it ("vibe coding" means building by prompting AI rather than writing code yourself) from a hackathon demo through to deployment, login and payments. — Source: [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/), 2025-04-27 (self-reported).

**A solo-founded, bootstrapped startup sold for $80M cash six months after launch.** Maor Shlomo built Base44, an AI app builder for non-programmers, reaching 250k users and profitability. He was not fully solo: he had 8 employees at the sale. — Source: [TechCrunch](https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash/), 2025-06-18.

**One person connected Claude to Blender, a professional 3D tool, and it went viral.** Siddharth Ahuja's open-source BlenderMCP bridge (MCP is a standard way to plug tools into an AI) lets a model build and edit 3D scenes; the repo has ~31k GitHub stars. — Source: [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender), created 2025-03-07.

**Terence Tao and colleagues took an evolutionary coding agent across 67 open maths problems.** AlphaEvolve uses a search method borrowed from evolution: an LLM proposes candidate programs, an automatic scorer judges them, and the best are refined. It matched most of the best known results and improved on several. — Source: [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864), 2025-11-03.

## Altitude

**Felix Rieseberg stopped asking Claude to fix crashes and asked it to keep the apps crash-free.** First he gave it the access it needed: fetching crash reports, mapping each app version to its git commit, and Windows, macOS and Linux machines to reproduce and verify fixes itself. — Source: [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), 2026-10-13 (self-reported).

**A solo developer built a CI pipeline that fixes itself.** CI ("continuous integration") is the system that runs tests on every change. When tests fail, or Sentry (an error tracker) reports a runtime error, the failure output goes to Claude Code, which commits a fix only if the tests then pass. There is one attempt per cycle; after that a human looks. — Source: [The CI That Fixes Itself](https://ericbrookfield.com/2026/02/24/the-ci-that-fixes-itself/), 2026-02-24 (self-reported).

**Kong pointed an agent loop at its 15 flakiest tests and it fixed 12 in a week and a half.** Flaky tests fail at random. An Opus orchestrator spawned fixer agents, and cheaper Haiku agents re-ran CI repeatedly to confirm each fix held, using Datadog flakiness data as the benchmark. It also found two real bugs. — Source: [How We Used Agentic AI to Fix Kong Gateway's Flakiest Tests](https://konghq.com/blog/engineering/how-we-used-agentic-ai-to-fix-kong-gateways-flakiest-tests), 2026-06-10 (self-reported).

**Anthropic let Claude run a real office shop, and documented where it failed.** "Claudius" handled stock, pricing and customers. Phase 1 (June 2025) lost money; Anthropic said it "would not hire Claudius". Phase 2 added newer models, a CRM (customer tracking system) and better inventory tools, and expanded to three cities. Anthropic says the gap between "capable" and "completely robust" is still wide. Cite it for the limits of "just go run the business". — Source: [Project Vend: Phase two](https://www.anthropic.com/news/project-vend-2), 2025 (self-reported).
