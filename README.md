# Apple HIG for agents

An installable agent skill and practical reference for designing, building, and reviewing interfaces across Apple platforms. It translates Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) into decisions an agent can apply while working on a real product: which system component fits a task, how layouts adapt, what accessibility states to check, and where to verify a platform-specific rule.

The repository includes guidance for **iOS, iPadOS, macOS, watchOS, tvOS, visionOS, Mac Catalyst, games, and iPhone Duo**. The [iPhone Duo guide](apple-hig/iphone-duo.md) covers outer and inner displays, partial folds, reserved regions, arrangement views, vertical controls, and a focused QA matrix.

> [!IMPORTANT]
> This is an independent synthesis, not an Apple publication or a substitute for the live HIG. Apple changes its guidance and SDKs. Verify version-sensitive APIs, dimensions, branded assets, and submission requirements against Apple's current documentation before shipping.

## Start here

1. Clone the repository:

   ```sh
   git clone https://github.com/Neel-Sh/Apple-HIG.git
   cd Apple-HIG
   ```

2. Copy the **entire** [`apple-hig/`](apple-hig/) directory into your agent's skill directory. The `SKILL.md` file links to the other files; copying only `SKILL.md` breaks those references.
3. Start a new agent session or reload its skill list. Ask for a concrete Apple UI task, or invoke `apple-hig` explicitly if your agent supports explicit skill invocation.

For example, to make it available to Codex in all your projects:

```sh
mkdir -p "$HOME/.codex/skills/apple-hig"
cp -R apple-hig/. "$HOME/.codex/skills/apple-hig/"
```

Then ask:

```text
Use $apple-hig to review the navigation and accessibility of my iPhone app.
Read the relevant references, cite the Apple HIG pages behind material changes,
and distinguish what you inspected in code from what you tested in the UI.
```

The skill is plain Markdown. It does not need a package manager, API key, plugin, or build step.

## Give it to your agent

Install the `apple-hig` folder under **one** of the following parent directories. The final path should end in `apple-hig/SKILL.md`. These paths are documented by the corresponding agent projects; check their current documentation if your version differs.

| Agent | Personal, across projects | Project, checked into a repo | How to call it |
| --- | --- | --- | --- |
| [Codex](https://developers.openai.com/blog/eval-skills) | `~/.codex/skills/` | `.codex/skills/` | Ask naturally or say `Use $apple-hig` |
| [Cursor](https://prod.cursor.com/docs/skills) | `~/.cursor/skills/` | `.cursor/skills/` | Ask the Agent to use `apple-hig` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | Ask naturally or use `/apple-hig` |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | `~/.copilot/skills/` | `.github/skills/` | Ask Copilot to use the skill |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `~/.gemini/skills/` | `.gemini/skills/` | Ask naturally; use `/skills list` to confirm discovery |

For a single project, copy the folder to the project's agent directory. This example targets Cursor; replace `.cursor/skills` with the project path in the table for your agent:

```sh
mkdir -p /path/to/your-app/.cursor/skills/apple-hig
cp -R apple-hig/. /path/to/your-app/.cursor/skills/apple-hig/
```

Some agents also recognize the shared `.agents/skills/` location. Cursor, GitHub Copilot, and Gemini CLI document it; use the agent-specific path above when you want the least ambiguity. For cloud or remote agents, commit the project-local skill folder to the repository they will read. A skill installed only on your laptop may not reach a remote worker.

### An agent without skill support

Provide the generated [`apple-hig.md`](apple-hig.md) as a file attachment or local context file, then ask the agent to use the relevant sections and check the linked Apple pages for current details. It is a large, single-file copy intended for environments that cannot load a `SKILL.md` folder. Prefer the folder when supported because it lets the agent read only the references needed for the task.

### Confirm installation

- Confirm that the destination contains `apple-hig/SKILL.md`, `iphone-duo.md`, and the other sibling references.
- Start a fresh conversation, or use your agent's skill reload command if it has one. Gemini CLI offers `/skills reload` and `/skills list`.
- Ask: `What does the apple-hig skill recommend checking before implementing an iPhone layout?` The answer should mention the relevant reference, available space or size classes, safe areas, accessibility, and current Apple guidance. If the agent cannot read a reference, check the folder path and file permissions.

## How to work with it

The [`SKILL.md`](apple-hig/SKILL.md) entrypoint tells the agent when this guide applies and routes it to focused references. It should read the files relevant to the current UI, inspect the project and deployment target, and use the [catalog](apple-hig/catalog.md) to locate Apple's official page. The catalog is a dated map of **158 HIG articles captured September 27, 2026**; it is not a live copy of the HIG.

Give the agent the product goal and constraints. The guide does not decide your product strategy for you.

### Design a feature

```text
Use the apple-hig skill to design a search and detail flow for my iPhone and iPad app.
The core task is finding a saved recipe and opening it quickly. Support large text,
VoiceOver, keyboard on iPad, and compact and regular widths. Recommend native
navigation and controls, explain key tradeoffs, and link the relevant Apple HIG pages.
```

### Implement in an existing codebase

```text
Use $apple-hig while implementing this SwiftUI screen. First inspect the app's
deployment target, navigation, and existing styles. Keep the product's current
information architecture. Build and inspect the UI if tools are available, and
report which states were verified versus still needing a simulator or device.
```

### Review an interface

```text
Review this macOS settings window using apple-hig. Prioritize issues that affect
task completion, keyboard access, accessibility, resizing, and platform behavior.
For each issue, give the affected control or view, the user impact, a specific
fix, and the relevant official HIG page. Avoid speculative pixel preferences.
```

### Prepare for iPhone Duo

```text
Use the apple-hig iPhone Duo reference to audit this iOS app. Check the outer
compact layout, inner regular layout, partial fold, reserved regions, vertical
bars, Split View, and continuity of selection and edits. Separate HIG guidance
from API implementation advice, and tell me what still needs testing on the
current Duo simulator or hardware.
```

## What is inside

| File | Use it for |
| --- | --- |
| [`SKILL.md`](apple-hig/SKILL.md) | Agent workflow, component choices, platform defaults, and routing to references |
| [`getting-started.md`](apple-hig/getting-started.md) | Design principles and platform-specific starting points |
| [`iphone-duo.md`](apple-hig/iphone-duo.md) | Foldable iPhone layout and verification guidance |
| [`foundations.md`](apple-hig/foundations.md) | Accessibility, layout, color, typography, materials, icons, privacy, writing, and motion |
| [`patterns.md`](apple-hig/patterns.md) | Onboarding, search, feedback, modality, data entry, files, media, settings, and more |
| [`components-content-layout.md`](apple-hig/components-content-layout.md) | Lists, tables, charts, split views, text, images, and organizational components |
| [`components-menus-navigation.md`](apple-hig/components-menus-navigation.md) | Buttons, menus, sidebars, tab bars, toolbars, and search fields |
| [`components-presentation-input.md`](apple-hig/components-presentation-input.md) | Alerts, sheets, popovers, windows, pickers, toggles, and fields |
| [`components-status-system.md`](apple-hig/components-status-system.md) | Widgets, Live Activities, notifications, controls, progress, and complications |
| [`inputs.md`](apple-hig/inputs.md) | Touch, keyboard, pointer, Pencil, Crown, focus, remote, and spatial input |
| [`technologies.md`](apple-hig/technologies.md) | Apple Pay, Sign in with Apple, HealthKit, Siri, Wallet, CarPlay, AI, and other integrations |
| [`catalog.md`](apple-hig/catalog.md) | Official HIG URLs, article headings, platform tags, and cited API symbols |

## Quality bar for agent output

A useful design or implementation answer should:

- Name the target platform, available layout sizes, primary input, and minimum OS or SDK when code depends on it.
- Keep the user's product goal and existing information architecture in view. Use familiar system behavior where it serves the task.
- Cover relevant states: normal, empty, loading, failure, permission denied, offline, and interrupted, without inventing states the feature cannot reach.
- Check Dynamic Type, VoiceOver and focus order, contrast, light and dark appearance, RTL, motion and transparency settings, safe areas, and localization where relevant.
- Check compact and regular layouts, rotation, resizable windows, or iPhone Duo poses when those environments are supported.
- Point to the specific Apple HIG page for a material guideline. Label an implementation recommendation as a recommendation when it is not an Apple rule.
- State what was verified in source, by build, by simulator, and on hardware. These are different levels of evidence.

The skill is guidance, not a lint tool or a guarantee of App Store approval. A checklist cannot replace testing with real content and assistive technology.

## iPhone Duo: the key additions

Apple's [Duo HIG page](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) describes an outer display for closed use, an inner display for open use, and a folding region that matters in partially open poses. Compact outer and regular inner layouts cover the fundamentals; multitasking introduces more available sizes. System navigation, toolbars, tab bars, sheets, alerts, and split views adapt to these changes.

The guide turns that into concrete review points:

1. Preserve selection, drafts, hierarchy, and actions as the app changes displays or sizes.
2. Prefer safe areas and system containers to device-specific pixel values. Use `NavigationSplitView` or `UISplitViewController` for hierarchy, and consider arrangement views for suitable two-part custom layouts.
3. Treat the cameras and fold as conditional reserved regions. Use the appropriate reserved-region APIs for manually positioned controls; do not assume a permanent center gap.
4. Let system bars use a vertical edge where appropriate. Prioritize actions under compression and give toolbar symbols useful titles for accessibility and overflow.
5. Test open, closed, partial fold, orientation, Split View, large type, and assistive technologies on the current simulator or hardware before claiming acceptance.

For deeper examples and source links, read [`iphone-duo.md`](apple-hig/iphone-duo.md). Apple's [adaptive layouts Tech Talk](https://developer.apple.com/videos/play/tech-talks/111463/) and [SwiftUI updates](https://developer.apple.com/documentation/Updates/SwiftUI) are useful when implementing new APIs.

## Maintain and contribute

The files in `apple-hig/` are the editable source. [`apple-hig.md`](apple-hig.md) is generated for single-file use. After editing any source file, rebuild and check it:

```sh
python3 scripts/build_single_file.py
python3 scripts/build_single_file.py --check
```

These commands require only Python 3. The check validates the skill entrypoint, local Markdown links, and generated copy. This is documentation, so review the content and source links as well as the mechanical checks.

The same check runs in [GitHub Actions](.github/workflows/validate.yml) on pushes and pull requests.

For a contribution:

1. Identify the official HIG page and its current change date. Do not turn a personal style preference into an Apple requirement.
2. Make the smallest useful change in the relevant reference. Keep `SKILL.md` focused on routing and decisions; put platform-specific detail in its reference.
3. Paraphrase Apple's guidance and link to the source. Do not paste whole Apple articles, artwork, or restricted design resources into this repository.
4. Regenerate `apple-hig.md`, run the checks above, and mention the platforms and UI states you actually inspected.

To update an installed copy, pull the latest repository and copy `apple-hig/` into the same destination again. If you maintain local edits in the installed folder, review them before copying. To uninstall, remove only your installed `apple-hig` directory from the agent's skill path.

## Sources, ownership, and license

The primary source is the [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines). The [catalog](apple-hig/catalog.md) records the article index captured September 27, 2026. Agent installation paths above are linked to each agent's own documentation. This project is independent of Apple, OpenAI, Anthropic, Cursor, GitHub, and Google. Their names and trademarks belong to their owners.

The original text and packaging in this repository are available under the [MIT License](LICENSE). That license does not grant rights to Apple's documentation, trademarks, SDKs, or design assets.
