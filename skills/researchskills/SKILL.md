---
name: researchskills
description: "Research entry point for concept and method explanations, paper reading and retrieval, mechanism and figure analysis, and evidence-grounded writing. Supports depth 1 (quick understanding), 2 (research analysis), or 3 (deep critical analysis). Includes TAS, FSRS, THz, PPP and PL. Use research-guide only for an explicitly requested staged subfield-to-review project."
---

# Research

Use this as the main research entry point, including a short explanation of a concept or method. It works without a manuscript, research-stage record, or existing paper library. Answer a focused explanation directly; resolve an external library only when the work needs saved papers or evidence. Keep reusable methods here and research findings in the user's external project or output location.

## Choose depth 1, 2, or 3

| Level | User-facing choice | Work to provide |
|---|---|---|
| 1 | 快速理解 | Answer the immediate question, explain only the necessary concepts, give a helpful example if needed, and state the main limit or uncertainty. Use verified sources for scientific claims without expanding into a course or full survey. |
| 2 | 研究分析（推荐） | Connect the question to mechanisms, methods and inspected evidence; compare relevant explanations or studies, state important assumptions and limitations, and identify a useful next research action when appropriate. |
| 3 | 深入论证 | Develop the decisive argument, compare the strongest plausible alternatives, inspect controls and contrary evidence, check quantitative reasoning or identifiability where relevant, and explain what evidence could change the conclusion. Keep unresolved premises explicit. |

Honor a level the user already chose. Natural language such as “简单讲一下” or “快速理解” selects 1; “研究角度分析” selects 2; “深入分析”, “批判性分析”, or “推导并比较替代解释” selects 3. Keep that choice for related follow-ups and supporting-skill handoffs, and allow it to change at any time.

When starting a research task without a supplied, clearly implied, or previously chosen level, ask one concise question in the user's language and briefly describe all three choices. For example:

“Which level would you like?
1. Quick understanding: the core idea, a plain explanation, and the main caveat.
2. Research analysis (recommended): mechanisms, methods, evidence, and limits.
3. Deep critical analysis: competing explanations, assumptions, counterevidence, and decisive tests.
Reply 1, 2, or 3.”

Use a supported choice/question interface when available; otherwise ask in chat. Wait for the user's selection before the substantive explanation, analysis, or drafting. Level 2 is a recommendation, not a silent default; no reply is not a choice. If the user asks you to choose, select a suitable level, state it briefly, and proceed. While a choice is pending, you may inspect already authorized context or gather independent inputs. If the topic or local source path is also missing, combine that request with the level question rather than asking in separate rounds. Do not ask again after an explicit or clearly implied choice, on related follow-ups, or in a helper that receives the choice from its parent task.

A bare 1, 2, or 3 changes depth when it clearly answers that choice or refers to the ongoing depth selection. Paper IDs, figure panels, question numbers and “进入第3阶段” retain their ordinary meaning. Ask only if the ambiguity changes the requested action. For a new unrelated task, ask again if no level is specified, unless the user asked to keep a preference across tasks.

Depth controls the explanation and scrutiny of evidence. It does not change the selected model or app settings, create a new chat, trigger an exhaustive literature search, authorize a website or experiment, or bypass the user's research-stage decisions. Provide conclusions, decisive reasoning, assumptions and checks; do not claim access to private internal reasoning. At every level, preserve evidence quality and disclose actual source-access limits. Level 3 still respects “只看这两篇” or “只回答这一点”. A requested full corpus remains complete at level 1; shorten the synthesis rather than silently sample it.

After depth is settled, give the explanation or requested analysis directly. Do not require a knowledge test, self-rating, prerequisite map, learning plan, or completed exercise before helping. Offer exercises or a study plan only when the user requests training, assessment or a learning plan; use [learn-and-audit.md](references/learn-and-audit.md) then. Reuse the user's supplied work and avoid beginner material they already understand.

For bounded independent checks, use available subagents when useful and permitted, applying the current model-choice guard before dispatch. Do not hard-code a consultation model. Creating a separate user-owned chat requires the user's explicit request and a supported tool; deeper analysis alone does not require another chat.

The figure-analysis route covers transient absorption (TAS), femtosecond stimulated Raman spectroscopy (FSRS), terahertz spectroscopy (THz), pump-push-probe (PPP), and steady-state/time-resolved photoluminescence (PL). It can start with supplied figures and develop supported analysis into manuscript sections. It does not imply that a figure alone supplies all experimental methods or guarantees publication.

## Choose the work from the request

| Request | Read next and proceed |
|---|---|
| Explain a concept, field or method | Answer here at the selected depth; read [learn-and-audit.md](references/learn-and-audit.md) only for a requested learning plan or assessment |
| Read a paper, extract its evidence, or distill papers to Markdown | [read-distill.md](references/read-distill.md) |
| Analyze a paper folder, produce a collection report, or classify/organize papers | Use `research-papers` for the bounded inventory, report and file plan; retain the selected depth and its file-operation approval boundary. One-off questions about a few supplied excerpts stay here and do not start a collection workflow. |
| Pursue the full subfield -> questions -> paper website -> review project | Use `research-guide` for that explicitly requested staged workflow and its existing acceptance decisions |
| Read all publications from a researcher or group | The corpus-coverage section of [read-distill.md](references/read-distill.md), then paper distillation |
| Find papers on a topic and save their PDFs to the computer | Search and verify DOI records here, optionally using `sci-brain:survey` for discovery, then pass the records directly to `literature-batch-download` |
| Batch-download an existing bibliography | Use the installed `literature-batch-download` skill for acquisition; retain the catalog and reading-status rules here |
| Learn through papers or compare mechanisms | Explain and compare at the selected depth using inspected evidence; use [learn-and-audit.md](references/learn-and-audit.md) for requested training or evaluation |
| Analyze TAS, FSRS, THz, PPP, or PL figures | [spectroscopy-methods.md](references/spectroscopy-methods.md) and the evidence-assessment steps of [figure-to-manuscript.md](references/figure-to-manuscript.md) |
| Turn supplied figures or experimental results into a submission-oriented manuscript | [figure-to-manuscript.md](references/figure-to-manuscript.md), relevant method sections, then [write-with-evidence.md](references/write-with-evidence.md) |
| Write or revise a scientific manuscript, or evaluate its claims | [write-with-evidence.md](references/write-with-evidence.md), then the appropriate existing writing or review skill |
| Survey a field or produce a technology assessment | Use the available `sci-brain:survey` skill; apply the evidence and coverage rules here when building its source library |

Read only the references needed for the requested route. A supporting skill receives a bounded task and returns its result here; do not bounce between coordinators merely because a task concerns research. When several purposes coexist, first extract the evidence required for the downstream task. Do not turn a request to read papers into a referee report or require the user to supply a manuscript. Conversely, a request for a few cited claims does not authorize an unrelated exhaustive corpus.

For topic-to-download requests, the research skill supplies the DOI list and Codex transfers it to the downloader. After screening each search batch, write verified `doi` and `title` records to a UTF-8 `download-input.json` in the task output folder, then invoke the installed `literature-batch-download` skill immediately. If a supporting search returns records in conversation or tool output, serialize them yourself; never require the user to collect, copy or format the DOI list. Preserve queries, source URLs and screening reasons in the research catalog. Keep unresolved identities outside the runnable queue; retain verified arXiv IDs or full-text URLs when a DOI is unavailable. Reuse the same download folder and append new verified records across batches, letting the downloader skip successful entries. A standalone search-and-download request does not require research-stage acceptance, a website, or a literature review.

For this retrieval route, read the installed downloader's `references/search-and-handoff.md` and use its lightweight verification procedure. Compare DOI, title, authors and year against publisher/authoritative metadata, and retain the evidence URL; an identifier lookup alone is not identity verification. When search finds actual PDF links, pass them with the DOI as ordered `pdf_candidates` objects (`url`, `source`, `version`, `evidence_url`); legacy `pdf_url`, `pdf_urls` and `arxiv_id` remain supported. Keep the version attached to each candidate, including changed-title preprints linked by the official source. The downloader tries these links before fallback API lookups. After access failure, verify new alternatives, enrich the same record and resume a bounded retry; do not repeatedly submit unchanged failures.

For subscribed articles, the downloader's institutional-access reference describes the user's configured institutional, campus/VPN and browser SSO routes. For a readable HTML full text after PDF failures, use its conditional webpage-export procedure only when the supplied text or explicit permission supports reproduction. Keep webpage-derived PDFs separate from source PDFs. Verify the saved file's identity before calling it the requested original; retain unresolved access and identity gaps in the catalog. Neither institutional authentication nor HTML export is assumed successful merely because the route exists.

## Resolve the external evidence library

For a user-specified local collection, use the stated folder. If that folder is missing, ask for it; a thematically similar registered library cannot substitute for the files the user means. For work that calls for an existing evidence library, read [library-registry.json](references/library-registry.json). Entries point to external project libraries; a library is selected by the user's explicit path or ID, then by a matching active project, then by the closest subject scope. Inspect its catalog and index before asking the user for context already present. If several entries are equally plausible, ask only the missing selection question while continuing independent source discovery.

The registry is an index, not a store of research findings. An empty registry is valid. If no entry applies, use the user's requested destination or the workspace's output rules and record the resulting location. Do not copy a corpus into this installed skill, move installed skills, or create a second conflicting bibliography. Resolve a registered relative path against that library's root. Treat missing or inaccessible paths as unavailable, not empty libraries.

For corpus-building or paper-distillation tasks, minimum external artifacts are a publication catalog, one Markdown note per requested paper, and an index linking notes to stable bibliographic identifiers. A short figure interpretation or requested paragraph does not require creating an unrelated corpus. For a numerical or experimental comparison, add or reuse a proportionate structured evidence table using the fields in [evidence-records.md](references/evidence-records.md). Reuse equivalent existing files and schemas rather than reorganizing a working library unnecessarily.

For retrieval-only tasks, the search catalog, generated downloader input and acquisition ledger are sufficient. Create per-paper distillations only when reading or analysis is requested; downloading a paper does not mark it as read.

## Integrate existing skills with explicit task boundaries

Discover the relevant installed skill through the current skill catalog and read its actual `SKILL.md` before use. Do not hard-code an installation path or assume a `skills/` folder exists in the project.

- `sci-brain:survey` handles literature discovery and field-level synthesis.
- `sci-brain:paper-reviewer` handles manuscript critique and location-anchored edits when a manuscript is the object of the task. Evidence-learning requests stay in this skill's reading mode.
- `sci-brain:paper-writer` supplies manuscript planning, figure-led organization, venue guidance, and drafting checks when building a full manuscript. This skill handles figure-level analysis, provisional captions, and evidence-supported draft paragraphs before that handoff. Missing venue or narrative preferences do not block those outputs.
- `sci-brain:download-ref` can retrieve references into a compatible existing knowledge base when available. A metadata record or downloaded file is not proof that the paper was read.
- `literature-batch-download` acquires PDFs from verified search records, DOI/arXiv lists, BibTeX, CSV or JSON and keeps a resumable local ledger. When the user requests search and download together, send each screened batch to acquisition without another download checkpoint. Preserve article version, retrieval failures and separate downloaded, identity-checked and read counts.
- Document/PDF and academic-writing skills may handle extraction, layout, and prose quality when needed.

If a supporting skill is unavailable, continue the parts supported by this skill and available tools; state the specific missing capability. Do not pretend an unavailable tool ran.

Use supporting workflows in light of the user's current intent and already established preferences. A request to write authorizes the supported drafting work; do not ask again for permission already given. Default venue, story-selection, template, or formatting checkpoints are planning aids, not new approval gates. Ask only for missing information that materially changes the work, and continue independent analysis or supported sections while it is unresolved. Factual evidence gaps remain binding: authorization to write never authorizes invented data or methods.

Preserve the supplied figure's signal definition and units, including `a.u.` when that is what the source reports. Record unknown normalization or calibration as an evidence gap. A supporting skill's preference for calibrated or dimensionless axes must not trigger invented units, silent rescaling, relabeling, or refusal to describe the existing figure. Replot only from adequate source data under the requested analysis workflow.

For spectroscopy, this skill reads figures, builds conditional assignments, compares complementary measurements, evaluates mechanisms, and drafts evidence-supported text. Preserve original images and data. Use the applicable domain workflow for preprocessing, quantitative fitting, correction, or native scientific delivery when those actions are requested and the necessary inputs exist. In particular, the existing TAS processing, analysis, QC, and delivery skills retain their scientific-array responsibilities. Do not silently extract screenshot pixels and treat them as raw measurements or bypass an existing accepted-data/QC state. A literature peak match is a hypothesis to test against the sample and controls, not a measured identification.

## Completion language

Report cataloged, retrieved, distilled, and evidence-checked counts separately. State material gaps and the next unresolved evidence question. A corpus is complete only against the recorded scope and reconciled source lists. A useful partial library must not be described as all papers read.
