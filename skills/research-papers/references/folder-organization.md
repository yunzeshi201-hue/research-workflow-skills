# Apply an Accepted Classification Plan

This procedure applies only when the user requested physical organization and accepted the concrete classification and file-operation plan. Report-only work stops before this procedure.

## Prepare an inspectable plan

Record the source root, inventory snapshot, category definitions and folder names, and a versioned mapping with each source file, its content hash, intended destination, and operation. The plan must say whether originals remain in place. Default to copying into category subfolders beneath the original source root. If moving is requested, state that original paths will change and make the move mapping explicit.

Use category names valid on the target filesystem. Avoid path separators, parent-directory components, reserved device names, and ambiguous names that collide under the filesystem's case rules. Include attached supplementary files in the mapping and retain their relationship to the main paper. For overlapping categories, choose one primary placement and preserve other memberships as index tags.

Keep online-only papers in the report/index unless a legitimate download is within scope and its proposed destination is included. A proposed category folder does not imply that every online record has a corresponding local file.

Ask for acceptance only after this plan and the report are reviewable. Acceptance of a known version and its explicit operations is sufficient; do not repeat the question without a material change. If the user approves categories but restricts actions to copies, that restriction governs. If approval refers only to taxonomy and physical organization was not requested, retain a report-only result.

## Recheck immediately before writing

- Resolve the absolute source root and every source and destination. Verify that planned destinations remain beneath the intended original root. Reject traversal, unexpected junctions/symlinks, and external targets; do not rely on string prefix matching alone.
- Recheck that source bytes still match the accepted inventory. Changed, missing, or newly discovered files need a revised entry; do not apply a stale classification silently.
- Inspect existing destination folders and files. Reuse an ordinary folder only if it has the accepted purpose; do not replace or rename it. Never overwrite an existing file. If destination bytes are identical, record it as already present; if they differ, skip it and present a revised unique destination for acceptance.
- Confirm sufficient access and storage without broadening permissions or moving files elsewhere as a workaround. Reference-manager-managed libraries need a supported organization method or an explicit export plan.

Explain any affected entries and continue unaffected, clearly approved actions only when they are separable. A filesystem access boundary still applies even after category approval.

## Execute and verify

Create only the approved category folders. Use literal-path filesystem operations and one filesystem API or shell end-to-end. If a deterministic helper is written for a substantial batch, validate it with isolated synthetic fixtures before applying it to the real library; never test on original papers.

Maintain a manifest outside the public skill package containing the plan version, approval evidence, source and destination paths, operation, pre-operation hash, completion status, verification result, and error when applicable. Update it as each operation completes so interruption does not erase the record.

For copies, compare source and destination hashes and confirm the source remains unchanged. For authorized moves, use a move operation without replacing an existing destination, verify destination bytes, and verify the expected source-path change. Preserve file bytes and file metadata where supported; report meaningful metadata limits. Do not implement a move by an unverified copy followed by deletion.

Do not delete duplicates, empty original directories, unreadable papers, or unrelated files. Do not perform a broad cleanup after filing. Repeated runs should recognize verified completed entries rather than duplicate files or silently move them again.

Deliver counts of copied, moved, already-present, skipped, and failed items; the resulting category tree; updated index/file links; and the operation manifest. If any item failed, say that organization is partial. Explain how approved moves can be reversed using the manifest, but do not automatically reverse or delete files. A rollback must recheck current paths and hashes, since subsequent user edits may have changed them.
