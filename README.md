# research-workflow-skills
通用科研技能：理解评估、本地与网络文献分析分类、问题拆解、研究网站及综述。

Start by describing what you have already done, what you observed, and what you want to achieve. Choose a focused learning task, an independent local/online paper analysis, or the original four-stage research workflow. Users do not need to begin as novices or build a website merely to analyze their papers.

## 三个并列入口

| 你现在想做什么 | 调用的技能 | 工作流程 |
|---|---|---|
| 学习某个领域或方法 | `research-foundations` | 简短基础说明＋可核实参考文献 → 少量应用型理解问题 → 按已有能力安排下一步；可复用已展示的理解或跳过测试 |
| 分析、总结和分类文献 | `research-papers` | 提供本地路径（需要本地文献时）→ 读取本地论文并补充网络文献 → 去重、逐篇分析、跨论文比较 → 提交报告与分类方案 → 用户认可方案后在原路径下建立分类文件夹并核验 |
| 开展完整研究项目 | `research-guide` | 根据已有知识调整深度 → 确定子领域 → 确定重要问题 → 建文献网站 → 写综述；原有阶段确认规则保留 |

直接描述任务即可，由入口选择相应技能。只做文献报告时无需先建网站，也不强制进行知识测试。分类报告应列出分类标准、每类文献、分类理由、交叉归属、争议与证据缺口，并区分本地论文和网上补充。用户仅需要分类报告时，交付报告即可，不必继续整理文件。

文件整理前会展示具体文件到文件夹的对应关系、复制或移动方式及冲突处理。默认复制并保留原件；只有明确选择移动的方案获得认可后才移动。确认分类不代表接受研究项目的其他阶段。知识检查、在线检索和本地盘点可在依赖允许时并行，后续结论仍须等待相应证据。

## Quick start

In a client where the skills are installed, open your research project and describe your field or current work, observations, and desired outcome. Normal task matching can select the coordinator automatically. To choose it explicitly, select **Research Guide** from the skill picker or mention `$research-guide` in Codex. You do not need to paste the internal consultation brief. See the current [skill invocation and installation guidance](https://learn.chatgpt.com/docs/build-skills).

The coordinator first selects the requested route. In the full research route it starts at the earliest unsettled stage and reuses existing accepted decisions. Review each concrete stage result and accept it or ask for changes before the next stage. Standalone learning and paper-analysis tasks have their own scope; they do not alter those stage decisions.

The package provides instructions and templates. Automatic consultation also needs a supported chat-creation/read/wait interface, an available requested model, and actual user authorization. Installing the files does not add those capabilities or turn Work/Codex into regular ChatGPT Pro.

**For the full research route, settle each stage before starting the next.** The agent prepares a concrete result and marks it ready. The user accepts that version or requests changes. A completed draft, successful test, or published website does not substitute for that decision.

```text
Describe completed work, observations, and desired outcome
   -> reconstruct the brief and resume the current stage
1. Specify a subfield
   -> user accepts the scope
2. Choose important questions
   -> user accepts the prioritized question set
3. Build the paper-library website
   -> user accepts the site and its corpus snapshot
4. Generate the review
   -> user accepts the review or requests revisions
```

## Stages and deliverables

| Stage | Skill | What you receive | What you settle |
|---|---|---|---|
| 1 | [research-field-map](skills/research-field-map/SKILL.md) | Evidence-backed comparison, selected subfield, boundaries, prerequisites, and introductory readings | Which subfield and scope to pursue |
| 2 | [research-question](skills/research-question/SKILL.md) | Important questions with stable IDs, priorities, nearest prior work, evidence gaps, and experimental reading/feasibility sketches | Which questions the project and library should address |
| 3 | [research-paper-library](skills/research-paper-library/SKILL.md) | Working paper website, verified records, question mappings, practical method cards, coverage limits, and a portable corpus export | Whether the website and this corpus version are ready to support a review |
| 4 | [research-review](skills/research-review/SKILL.md) | Question-led synthesis of findings, disagreements, methods, limitations, open problems, and a practical research reading route | Whether the review accurately represents the evidence and chosen scope |

[research-guide](skills/research-guide/SKILL.md) coordinates the sequence and resumes from recorded decisions. [research-foundations](skills/research-foundations/SKILL.md) and [research-test-design](skills/research-test-design/SKILL.md) are supporting skills within the current stage. They do not add stages or unlock later ones.

The distribution has eight skill folders: one coordinator, four stage skills, two helpers, and [research-papers](skills/research-papers/SKILL.md) for independent or supporting paper analysis. Use the coordinator to select a route or guide a project. Directly invoking a later-stage skill still checks its prerequisites. The paper-analysis route can produce a standalone report without invoking the stage-4 review skill.

## Local and online paper analysis

For local papers, provide the folder path and the intended question or analysis scope. The skill inventories only the authorized location, reads accessible papers, records unreadable files and inspection depth, and supplements the report with relevant online publications unless you request local-only work. Local documents are not automatically uploaded to external services. Online search limitations remain visible.

The output includes a paper register, per-paper summaries, proposed categories and assignments, comparisons of claims and evidence, methods and controls, contradictions, coverage gaps, and linked references with inspected source locations. Full-text findings remain distinct from abstract-only leads. Multi-topic papers can have multiple tags while keeping one primary physical category.

If file organization is requested, the report includes a versioned file plan. Accept that plan or request changes before any category folders are created or files copied/moved. The default is copying into new category folders under the supplied source root; explicit moving is a separate operation stated in the accepted plan. Conflicts, changed files, and links escaping the root are resolved before execution. A manifest and post-operation checks show what changed. Newly discovered files or revised classifications do not silently inherit earlier approval.

This route complements the original project. Within an active research stage, use only the paper work needed for that stage; do not use the helper to bypass a pending review checkpoint. A separately requested standalone report preserves the project state. Reconcile its corpus before later use in a project website or review.

## Begin with your current work

You do not need a formal proposal or even a field name. Give a rough account of completed work and the result you want next. The agent separates user-reported observations, inspected evidence, interpretations, planned work, and unknowns, then asks only for information that changes the next decision. If your subfield is already specific, it uses that scope as the starting point.

The [intake guide](skills/research-guide/references/research-intake.md) supports whichever stage is active. Intake does not add another acceptance gate. Existing user decisions remain usable; completed activities alone do not imply that a stage has been accepted.

## Automatic consultation inside the current stage

For a consequential uncertainty, the coordinator identifies the decision, assembles the context, creates a chat in the same verified project, submits the question, waits for the completed answer, checks it against the sources, and adjusts the active work. The user does not need to find or paste a prompt. The [consultation brief](skills/research-guide/assets/deep-research-handoff.md) is an internal payload filled by the coordinator.

Prefer regular **ChatGPT Chat with the requested 6-Pro model**, with **ChatGPT Thinking** when Pro is unavailable. Any requested **Work/Codex** consultation uses **GPT-6.1 Sol**. A Work/Codex model setting does not make it a regular ChatGPT Pro chat, and a preference for Sol there does not itself authorize changing product destinations.

Use the app's supported chat tools and the [routing guide](skills/research-guide/references/model-routing.md). A standing human instruction to create and message consultation chats authorizes the loop within its scope; reuse it without asking for every question. The empty public template grants no permissions. A later automatic instruction supersedes earlier prepare-only preferences; prepare-only remains available when explicitly requested.

Resolve the exact project and current model capability before dispatch. An unavailable regular-Chat creation tool does not prove the user lacks Pro access. Report that capability gap instead of silently changing products, opening a browser workaround, or asking the user to paste the prompt. A browser route needs its own user instruction. Continue independent research work while dependent decisions remain pending.

A dispatch acknowledgment is not an answer. Reuse the same chat for authorized clarification, retrieve the full response, verify decisive claims and source details, and record adopted/rejected recommendations and the resulting artifact revision. Timeouts remain pending. Do not create duplicate or recursive chats. Another model's answer cannot accept a stage or serve as experimental confirmation.

## A paper website organized around questions

The website connects `question -> needed evidence -> method -> paper -> result -> limitation`. Each included paper has a verified identity, access/reading status, question links, source locations, relevant conditions, and a clear distinction between reported findings and interpretations.

The default experience is a searchable, filterable paper list with expandable details, question views, and coverage gaps. Add features because they help research decisions. Avoid a large dashboard whose sections duplicate the same information.

The library distinguishes indexed papers from papers read in full and specific evidence checked. It deduplicates versions and records search scope and cutoff. An exported snapshot lets the review use the same evidence without depending on a running website. A static snapshot is a valid implementation if its limits are explicit; editable shared data need actual persistence and verification.

A local website preview can satisfy stage 3 when that is the agreed delivery. Hosted or public delivery follows the user's actual hosting and audience instructions. Stage acceptance and permission to publish are separate decisions. This package itself does not create or deploy a website.

## Figures connect claims to evidence

The default website includes inspected key article figures with explanations of **what the authors wanted to establish, what they measured, which signal and control support the claim, and what remains unproven**. Selecting a method first explains its capabilities, then shows matching paper figures and panels. A multi-method paper retains its recorded method list while the displayed evidence changes with the selection.

Keep authors' interpretations separate from observations and the website's assessment. Track main-text, supplementary, and figure inspection independently. Unavailable images remain marked missing or link to the original source; unrelated images and generated traces cannot fill the gap. Keep literature figures distinct from researcher data, and retain attribution and reuse status in the export.

The [figure evidence guide](skills/research-paper-library/references/figure-evidence.md) defines the records, interaction, and checks. Reference websites can inform the general design, but their topics, papers, figures, results, and links do not enter this public package.

## Important articles that teach experimental practice

The skills recommend papers for their role in the selected question, rather than prestige alone. The reading route may include:

- A foundational paper to understand the model and its assumptions.
- The closest experimental precedent to learn what is already established.
- A method or protocol paper to understand the measurement and its implementation.
- Calibration, control, or artifact studies to judge whether the signal supports the intended inference.
- Analysis and validation papers to process data, compare models, and assess uncertainty.
- Contrary evidence or failed approaches to understand where the procedure or interpretation breaks down.

Each recommendation explains **why to read it, what to extract, the exact source location, what can transfer, and what must be checked locally**. Detailed recommendations require inspected Methods, supplementary information, protocols, or code. An abstract can identify a promising article but cannot supply an executable procedure.

Each substantive experiment proposal includes two linked records:

- **What prior studies did:** verified references, system/preparation, setup, reported conditions, controls, analysis, observed results, limitations, and exact inspected locations.
- **How the proposed steps are supported:** the source for each step, reported settings versus adaptations, transfer assumptions, missing details, and validation needs.

Attach the reference list with direct source links. Separate direct experimental precedents from related-system analogies and new proposals. Unreported settings remain missing; a collection of citations cannot make an incomplete procedure ready to execute. Keep the researcher's completed work distinct from published work and future plans.

Stage 2 uses these papers to assess whether a question is tractable. Stage 3 makes the evidence and procedural lessons searchable. Stage 4 compares the approaches and proposes a source-backed experimental decision path. Actual experiment execution is a separate task.

See the [experimental reading guide](skills/research-test-design/references/experimental-reading.md) and [experimental precedent guide](skills/research-test-design/references/experiment-precedents.md) for the required records.

## Start and resume

Install all eight complete folders under `skills/`. In Codex, ask `$skill-installer` to install the eight research skill folders from this repository URL. The installer resolves its supported destination and checks existing installations. The repository's `skills/` directory is a distribution layout, not by itself a guaranteed discovery path.

For manual installation, use the locations documented by your current client. Current Codex documentation lists `.agents/skills` for repository skills and `~/.agents/skills` for user skills; some installed clients and the bundled installer use `$CODEX_HOME/skills`, usually `~/.codex/skills`. Preserve a working installation and avoid duplicate copies with the same skill name. Verify the eight names in the skill catalog; if changes do not appear, restart the client. The package needs no API key or Python library merely to load its instructions; actual research and website work depend on available tools. [Installation guidance](https://learn.chatgpt.com/docs/build-skills).

```text
Use $research-papers to analyze papers in [folder path], supplement them
with relevant online studies, and report the proposed categories and
evidence comparisons. Show the file plan before organizing the folder.

Use $research-foundations to explain the concepts relevant to [task]
with references, check what I understand, and adapt the next step.

Use $research-guide. Here is what we have already done: [rough notes].
We observed [observations], think [interpretation], and want [outcome].
Help identify the next decision. Prefer Pro for difficult reasoning; if
I cannot use Pro, use ChatGPT Thinking. Automatically create and message
consultation chats in this project, wait for their answers, verify them,
and adjust our work. For any Work/Codex chat I request, use GPT-6.1 Sol.

Use $research-guide. I want to explore [field]. Start by helping me settle
one subfield. Show the evidence and important introductory articles, and
wait for my acceptance before moving to question selection.

I accept subfield brief revision 2. Now help me select the important
questions and identify the papers that would teach me how to investigate them.

I accept question set revision 1. Use $research-paper-library to build the
paper website around those questions. Include protocol, calibration, control,
and analysis papers, with reading status and source-backed practical notes.

I accept the website and corpus snapshot revision 3. Use $research-review
to synthesize that corpus and explain the experimental approaches it supports.
```

These prompts illustrate decisions on artifacts the user has actually inspected. They are not pre-recorded approvals.

Store the workflow record, evidence, data, and reviews in the research project, outside installed skills. The [stage-gate contract](skills/research-guide/references/stage-gates.md) defines acceptance, conditional decisions, resumption, and revision. An [empty record template](skills/research-guide/assets/workflow-state.example.json) contains no approvals.

The version-4 record separates automatic routing, product/model choices, and authorization. Existing version-2 or version-3 stage decisions need no new acceptance solely because the record format changes. Keep filled briefs and consultation records in private project storage, outside the reusable package.

If scope or the corpus changes materially, preserve the earlier accepted version and reopen the affected checkpoint. Deeper reading within the accepted corpus is part of review writing; adding new papers to that corpus needs a new snapshot decision. Cosmetic corrections do not automatically restart the scientific workflow.

## Scientific standards

A learning gap is not automatically an open research problem. Verify closest prior work before asserting novelty. Preserve the distinction between observation, processing, inferred quantity, mechanism, and functional consequence. An important article helps a decision; its citation count does not prove its claim or practical applicability.

The review is organized by the accepted questions and compares evidence across papers. It states the corpus scope, source-access limits, conditions behind disagreements, and what remains unresolved. A narrative synthesis must not be labeled a systematic review without the corresponding search and selection process.

The [methodological sources](skills/research-guide/references/methodology-sources.md) explain selected influences and limits. This workflow does not guarantee novelty, correctness, or research success. Its structure is most directly suited to empirical, computational, and theoretical scientific work; other disciplines may need different evidence standards.

## Validation and public contributions

Run `python scripts/check_package.py .` for release structure, local links, and configured accidental private-content patterns. It uses Python's standard library. The checker does not prove privacy or scientific validity.

See [behavioral scenarios](evals/scenarios.md) and [validation notes](evals/validation.md). Evaluate what the agent actually does at a gate, whether article guidance is source-backed, and whether a website/review preserves evidence boundaries. Do not grade merely by headings or wording.

Contribute general methods and generic examples. Keep project histories, unpublished results, identifiers, private library indexes, credentials, and local paths outside the release. The [fictional question example](skills/research-question/references/worked-example.md) illustrates decomposition rather than a real research project or novelty claim.

## Upload or maintain this repository

Upload the extracted release contents at the repository root: `README.md`, `LICENSE`, `.gitignore`, `skills/`, `scripts/`, and `evals/`. Keep the eight skill folders intact. The ZIP is a download bundle; GitHub does not unpack an uploaded ZIP into installable skill folders.

On GitHub, choose **Add file > Upload files**, add those extracted files and folders, inspect the proposed changes, then commit. For updates to an established default branch, use a new branch and pull request. If a repository already has its own README or license, reconcile them rather than overwrite them blindly. [GitHub upload instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

Run `python scripts/check_package.py .` from the clean release folder before publishing. The checker rejects private working directories as well as configured private-content patterns. Upload only the release contents, not the surrounding authoring workspace, installed-skill backups, or generated research records. Ignore rules are an aid; inspect the actual file list and changes before every upload.

## License

[MIT](LICENSE). Each skill folder includes the license for individual distribution. Linked publications retain their own terms and are not bundled.
