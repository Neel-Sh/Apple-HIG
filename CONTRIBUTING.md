# Contributing

Thanks for helping keep this agent skill useful and accurate. Contributions that correct outdated guidance, improve a concrete Apple platform workflow, or make the skill easier to install are welcome.

## Before you edit

- Check the [open issues](https://github.com/Neel-Sh/Apple-HIG/issues) for existing work.
- Find the relevant current [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) page. Include its URL in an issue or pull request so reviewers can compare the guidance.
- Distinguish Apple's stated guidance from your implementation recommendation. Avoid presenting a preference, draft API, or untested device behavior as a platform rule.
- Paraphrase Apple's documentation. Do not copy entire articles, artwork, or restricted assets into this repository.

## Make a focused change

The editable source lives in [`apple-hig/`](apple-hig/). Keep `SKILL.md` focused on when to use the skill and which reference to read. Put detailed guidance in the relevant reference file. The root `apple-hig.md` is generated; do not edit it by hand.

After editing, run:

```sh
python3 scripts/build_single_file.py
python3 scripts/build_single_file.py --check
```

The check verifies skill metadata, local links, and the generated single-file copy. Review the wording and cited Apple pages yourself; the script cannot validate design claims.

## Open a pull request

Describe the platform and UI problem, link the official source, and explain what changed. State what you verified in the source, build, simulator, or device. A source review alone does not establish simulator or device behavior.

For a broken link, stale claim, or missing platform case, you can [open an issue](https://github.com/Neel-Sh/Apple-HIG/issues/new/choose) first. Small corrections can go straight to a pull request.
