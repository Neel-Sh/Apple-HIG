# Apple Human Interface Guidelines skill

Generated from `apple-hig/` by `scripts/build_single_file.py`. Install the directory for skill-aware agents; this file is for agents that need one document. Relative reference links resolve in `apple-hig/`.

Official source: https://developer.apple.com/design/human-interface-guidelines


<!-- source: SKILL.md -->

---
name: apple-hig
description: >-
  Design, implement, or review native interfaces for Apple platforms using the
  Human Interface Guidelines. Use for SwiftUI, UIKit, AppKit, iPhone Duo,
  iPadOS, macOS, watchOS, tvOS, visionOS, and Mac Catalyst UI decisions,
  including layout, navigation, controls, accessibility, Liquid Glass, and
  system experiences. Load the relevant reference before making design claims.
---

# Apple Human Interface Guidelines

Practical synthesis of Apple's Human Interface Guidelines for design, implementation, and review. The [official HIG](https://developer.apple.com/design/human-interface-guidelines) is the source of truth.

Index captured 2026-09-27: 158 articles. Full URL map, section names, and cited APIs: [catalog.md](catalog.md).

This skill is original implementation guidance, not an Apple publication. The catalog is a dated index, so check the live Apple page for version-sensitive APIs, device specifications, measurements, platform availability, branded assets, and App Review requirements. Distinguish Apple's guidance from this skill's implementation suggestions.

## How to use this skill

1. Identify the target platform, minimum OS and SDK, UI framework, task, and input methods from the project. If unspecified, state a reasonable assumption. An iPhone layout is not a Mac layout with touch removed.
2. Read only the matching reference files below, plus [foundations.md](foundations.md) when layout or accessibility is material. Follow the user's product brief and existing architecture.
3. Choose familiar system components and semantic styles when they fit. A custom control is valid when the task needs one; preserve expected interaction and accessibility behavior.
4. Design for actual available space, content, and state: compact and regular widths, Dynamic Type, localization, safe areas, keyboard or pointer where supported, light and dark appearance, and relevant accessibility settings. For iPhone Duo, read [iphone-duo.md](iphone-duo.md).
5. If implementing, inspect the project's deployment target and verify APIs against that SDK before writing code. Build and inspect the resulting UI when tools are available. Do not claim simulator or device acceptance from a source review alone.
6. Explain decisions with the relevant official HIG links when a guideline materially determines the result. Treat the catalog as a locator, not as proof that a current rule or API is unchanged.

## Reference map

| When the work is about | Read |
| --- | --- |
| Principles, iOS, iPadOS, macOS, tvOS, visionOS, watchOS, games | [getting-started.md](getting-started.md) |
| iPhone Duo, fold, dual displays, reserved regions, vertical controls | [iphone-duo.md](iphone-duo.md) |
| Accessibility, icons, color, type, layout, materials, motion, privacy, SF Symbols, writing | [foundations.md](foundations.md) |
| Onboarding, search, settings, files, modality, loading, media, accounts, workouts | [patterns.md](patterns.md) |
| Charts, images, text, lists, split views, tabs, sidebars, outlines | [components-content-layout.md](components-content-layout.md) |
| Buttons, menus, toolbars, search fields, tab bars, menu bar | [components-menus-navigation.md](components-menus-navigation.md) |
| Alerts, sheets, popovers, scroll views, pickers, toggles, text fields | [components-presentation-input.md](components-presentation-input.md) |
| Progress, widgets, Live Activities, notifications, complications, controls | [components-status-system.md](components-status-system.md) |
| Touch, Pencil, keyboard, focus, game controls, Crown, eyes, remote | [inputs.md](inputs.md) |
| Apple Pay, Sign in with Apple, Health, maps, Siri, Wallet, CarPlay, AI | [technologies.md](technologies.md) |
| Exact URL, platforms, headings, cited symbols | [catalog.md](catalog.md) |

## Design principles as code checks

Weigh these when two options both "work":

- **Purpose.** The screen exists to do one job. Cut features that do not serve it.
- **Agency.** People can leave, skip, undo, and explore. Do not trap them in a mode.
- **Responsibility.** Say what you collect and why, at the moment you ask. Collect less.
- **Familiarity.** Use system controls, SF Symbols, and standard gestures before custom ones.
- **Flexibility.** Same task works with touch, keyboard, pointer, VoiceOver, and larger type.
- **Simplicity.** Hierarchy is obvious. One primary action per view.
- **Craft.** System materials, semantic colors, and standard motion. No one-off chrome.
- **Delight.** Character supports the task. It never blocks it.

## Liquid Glass

Liquid Glass is the functional layer for controls and navigation (tab bars, toolbars, sidebars, ornaments). It floats above content. Content uses standard materials, not glass.

- Prefer system components. They adopt glass, scroll edge effects, and the user's glass look automatically.
- Do not paint glass on content-layer cards, list rows, or full-screen backgrounds.
- Custom glass: use `glassEffect(_:in:)` with `Glass.regular` when text must stay legible. Use `Glass.clear` only over rich media, and sparingly.
- Inside content, use `Material` (`ultraThin`, `thin`, `regular`, `thick`) or `UIVisualEffectView` / `NSVisualEffectView`.
- Group nearby glass with one container so shapes morph instead of stacking unrelated blurs.
- Never stack glass on glass. One functional layer over one content layer.

## Choose a component

| Job | Use | Avoid |
| --- | --- | --- |
| Instant action | Button | Toggles, links styled as buttons |
| On/off or yes/no | Toggle / switch / checkbox | A button labeled On |
| One of a small set, mutually exclusive | Picker, segmented control, or radio buttons | Many unrelated buttons |
| Choose from a long list | Menu, pop-up button, or picker | A huge segmented control |
| Several peer sections of the app | Tab bar (iOS) or sidebar (iPad, Mac) | A home screen of buttons |
| Drill into hierarchy | Navigation stack, split view | Modal for every push |
| Confirm a destructive or irreversible step | Alert or confirmation dialog | A sheet full of marketing |
| Related short task, then return | Sheet | A new window or full-screen takeover |
| Secondary choices from an object | Context menu | A persistent toolbar of rare actions |
| Progress with known duration | Determinate progress | An endless spinner |
| Indeterminate wait under a few seconds | Activity indicator, and keep the UI up | A blocking modal spinner |
| Glanceable home/lock data | Widget, Live Activity, complication | A notification used as a dashboard |

## Platform defaults

| Platform | Navigation | Primary input | Layout habit |
| --- | --- | --- | --- |
| iOS | Tab bar + navigation stack | Touch, 44×44 pt targets | Compact width; one column |
| iPhone Duo | System navigation and bars adapt by pose | Touch; size classes | Outer compact, inner regular; preserve state and actions |
| iPadOS | Sidebar or tab bar; split view; windows | Touch, pointer, Pencil, keyboard | Regular width; resizable scenes |
| macOS | Sidebar, menu bar, toolbar, windows | Pointer and keyboard | Dense, persistent controls, full keyboard |
| tvOS | Focus engine, top-to-bottom | Remote click and swipe | 10-foot type, no small text, no touch-only targets |
| visionOS | Windows, ornaments, tabs | Eyes + pinch; direct touch rarely | Glass windows, depth, comfort, no edge-attached UI |
| watchOS | Vertical scroll, page, sheets | Crown, tap, double tap | One idea per screen; raise to speak and complications |

## Always-on implementation rules

- Aim for at least 44×44 pt touch targets on iOS and iPadOS; grow the interactive area when artwork is smaller.
- Use semantic colors (`Color.primary`, `secondary`, system backgrounds) and semantic text styles. Support Dark Mode and Increase Contrast without a second design.
- Support Dynamic Type. Layouts reflow. Do not clip or shrink text to fit.
- Respect `accessibilityReduceMotion`, `accessibilityReduceTransparency`, Bold Text, and Differentiate Without Color.
- Follow the system's right-to-left layout direction. Preserve direction where the content has a fixed meaning, such as media playback or a timeline. iPhone Duo's vertical control edge follows hardware rather than mirroring for RTL.
- Place interactive content within appropriate safe areas and layout margins. On iPhone Duo, account for camera and folding reserved regions; scrollable content can flow through the fold where appropriate.
- Give every control an understandable accessibility name. System text labels already provide one; icon-only controls need a meaningful alternative. Hide decorative images from assistive technology.
- Destructive actions are labeled with the verb (Delete) and confirmed when they cannot be undone. Place them away from the default button.
- Permission prompts use the system sheet. A pre-alert is allowed only to explain a benefit immediately before the system prompt. Never send people to Settings as the first step if the system prompt is still available.
- Loading states leave the chrome in place and show progress near the content. Do not block the whole app for short work.

## Writing interface copy

- Sentence case for controls, navigation titles, and buttons.
- Button labels are verbs. One or two words.
- Alerts: title says what happened, message says what to do, buttons name the action. Cancel is separate from the destructive verb.
- No "please", no "are you sure?", no error codes in the primary sentence, no "OK" when a specific verb exists.
- Use the product's name, not "app" or "application", in customer-facing strings when you mean your product.

## When you finish a UI change

Check the states and modes relevant to the task, and report what was actually verified:

- The component matches the decision table.
- Primary action is visually distinct by style, not by a random larger size.
- Empty, loading, error, and offline states are considered where the feature can encounter them.
- VoiceOver order matches visual order. Focus is not trapped.
- Dark Mode, a larger Dynamic Type size, and RTL do not collide or clip.
- Platform-only controls (menu bar, Crown, ornaments, Top Shelf) are not shown on the wrong OS.
- If iPhone Duo is in scope, compact outer, regular inner, partial fold, portrait and landscape, and Split View preserve the same task and reachable actions.


<!-- source: getting-started.md -->

# Getting started

Official section: https://developer.apple.com/design/human-interface-guidelines/getting-started

Apply these rules before platform-specific chrome. Pair with [foundations.md](foundations.md) for color, type, and accessibility.

## Design principles

URL: https://developer.apple.com/design/human-interface-guidelines/design-principles

Eight principles. Use them to break ties.

- **Purpose.** Every screen answers what this product is for. Ship the core task in the first screen after launch. Do not add a feature to fill a tab.
- **Agency.** People reach content immediately. Guided flows can be skipped. Destructive and long actions are undoable or clearly confirmed. Avoid modes that hide the rest of the app.
- **Responsibility.** The first run states what the product does. Permission copy matches the real use. Data collection is the minimum the feature needs.
- **Familiarity.** Standard components, SF Symbols, and system gestures. Once a control looks a certain way, it behaves that way everywhere in the app.
- **Flexibility.** The same task has a pointer path, a keyboard path, and a VoiceOver path. Layout survives rotation, Split View, Stage Manager, and Dynamic Type.
- **Simplicity.** One primary action. Secondary actions move to menus or toolbars. Copy is as short as the meaning allows.
- **Craft.** System fonts, materials, spacing, and motion. Prototype the real interaction, not only the static mock. Update chrome when the platform design system changes (Liquid Glass).
- **Delight.** Pick the emotion the product should create, then express it in transitions and empty states. Do not add decoration that slows the task.

## Designing for iOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-ios

iPhone is a one-hand, short-session, compact-width device. People switch apps constantly and expect to resume exactly where they were.

- Organize top-level sections with a tab bar. Drill in with a navigation stack. Use sheets for short tasks that return to the same place.
- Touch targets are at least 44×44 pt. Place frequent actions in the lower half when one-handed use matters.
- Respect the status bar, Dynamic Island, and home indicator. Use safe area insets. Do not hide the status bar unless the content is genuinely immersive, and restore it on exit.
- Support portrait. Support landscape when the content benefits (media, photos, large canvases). Do not letterbox a portrait layout in landscape.
- Launch into content, not a splash. The launch screen matches the first screen's background so the transition is invisible.
- Design for interruption: calls, notifications, multitasking on larger phones, and backgrounding. Persist state.
- Use system navigation bars, tab bars, and sheets so Liquid Glass, large titles, and scroll edge effects come for free.
- iPhone Duo is still iPhone. See that page before hard-coding a single display size.

## Designing for iPadOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados

iPad is a resizable, multi-window, pointer-capable computer that also works with touch.

- Adopt multitasking: Split View, Slide Over, Stage Manager, and multiple windows. Do not lock orientation unless the task is capture or playback that truly requires it.
- Use a sidebar for app structure when there are many top-level sections. Use a split view so the list and detail can sit together in regular width and collapse in compact width.
- Support keyboard shortcuts for every common command, and show them in the menu bar (iPadOS has a menu bar when a keyboard is attached).
- Support pointer hover, context menus, and drag and drop between apps. Pointer effects should feel native, not like a drawn cursor from a desktop port.
- Apple Pencil: hover, double tap, squeeze, and Scribble. Do not invent a pencil gesture that conflicts with system ones.
- Toolbars can be richer than on iPhone. Keep the primary action obvious.
- External displays and Stage Manager mean your window size is not the device size. Use size classes and flexible frames.

## Designing for macOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-macos

Mac users expect density, persistence, and a full keyboard.

- The menu bar is required for document and multi-command apps. Standard menus (App, File, Edit, Format, View, Window, Help) use standard items and shortcuts. See The menu bar.
- Windows are resizable. Remember size and position. Support full screen as an option, not a trap. Minimum size must still fit the primary task and Dynamic Type-scale text where applicable.
- Sidebar plus content, or a toolbar plus content, is the default structure. Toolbars hold frequent actions. Menus hold the complete set.
- Prefer columns, tables, and inspectors over full-screen flows. Destructive actions still confirm.
- Keyboard: every control is reachable. Standard shortcuts (Command-C/V/Z/S/W/Q, Command-comma for Settings) must work.
- Pointer precision allows smaller controls than iOS, but do not pack so tightly that targets become hard to hit. Use the system's control size (`ControlSize`).
- Settings live in a Settings window, not a dumped iOS Settings clone. Use grouped form style.
- Destructive menu items use the destructive role. Default buttons are trailing in dialogs.

## Designing for tvOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos

People sit across the room and navigate with a remote. Focus is the cursor.

- Every interactive item has a visible focus state. Focus moves in a predictable grid: up, down, left, right. Do not trap focus.
- Type is large. Body content is readable from about 10 feet. Do not use iPhone point sizes.
- The remote click activates the focused item. Swipe moves focus. Play/pause, menu (back), and the TV button behave as the system defines. Do not remap Back.
- Full-screen media is the content. Chrome appears on focus or transport interaction and dismisses when idle.
- Use lockups, posters, and cards with clear focus expansion. Parallax and layered images are a tvOS signature; use them on featured artwork, not on every icon.
- Text entry is painful. Prefer pickers, search suggestions, and companion-device auth over long forms. Digit entry views exist for short codes.
- Top Shelf is the app's billboard on the Home Screen. Keep it current and tappable.
- Do not rely on hover, touch, or right-click.

## Designing for visionOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos

People look at an object, then pinch (indirect), or they reach out and touch it (direct). Windows float in space. Comfort beats density.

- Use glass windows and system ornaments for toolbars and tabs. Do not glue controls to the physical screen edge; there is no screen edge.
- Prefer indirect interaction (look + pinch) for ordinary UI. Reserve direct touch for objects that invite reaching, and keep those sessions short so arms do not fatigue.
- Keep important content inside a comfortable field of view. Do not place primary controls in far periphery.
- Depth communicates hierarchy. Do not stack so many layers that people must refocus constantly. Avoid large, fast motion in the periphery.
- Immersion is opt-in and easy to leave. Transition between windowed and immersive styles smoothly. Ask before entering a Full Space that hides other apps.
- Eyes are an input, not content to stare back. Do not require a fixed head pose. Provide another way to complete any task that uses custom hand gestures.
- Text is slightly heavier and larger than on iOS so it holds up on glass. Use system styles.
- Ornaments hold navigation and actions attached to a window, not floating randomly in the room.
- Respect people nearby: dim or hide personal content when passthrough shows someone else, and do not require the wearer to move their body to proceed.

## Designing for watchOS

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos

A watch is a glance, a complication, and a short interaction. Seconds, not minutes.

- One primary idea per screen. Scroll vertically for more. Use the Digital Crown for scrolling and pickers rather than tiny drags.
- Raise-to-wake and Always On mean your UI is often a dimmed, low-motion face. Critical information must still be readable. Honor Always On guidance: no bright full-bleed animation while the wrist is down.
- Complications and widgets are the real home screen. Design them first if the feature is time-sensitive.
- Notifications: short look first, long look on linger. Actions are few.
- Double tap (finger pinch) triggers the primary action. Do not fight that gesture.
- Text is short. Use SF Compact styles. Avoid paragraphs.
- Haptics confirm outcomes. Do not fire haptics for decoration.
- Workouts and health stay readable in motion, with large numerals and high contrast.
- If a task needs a keyboard essay, move it to iPhone. watchOS text input is for short replies and dictation.

## Designing for games

URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-games

Games can invent interaction, but system chrome, permissions, and comfort rules still apply.

- Get into play immediately. Skip or shorten logos. Restore the last session.
- Fill the display. Prefer adapting aspect ratio over letterboxing. If bars remain, fill them with art, not black voids. On iPhone Duo, play every pose.
- Touch controls sit where thumbs rest and do not cover the action. Support controllers and keyboards on platforms that have them. Do not require a controller if touch is viable.
- Use system gestures only at the edges you are allowed to defer (home indicator). Provide another way out.
- Haptics and audio duck correctly during interruptions (calls, other apps). Resume music policy must be intentional.
- Welcome everyone: customizable controls, reduced motion alternatives, color-blind-safe palettes, and scalable text in menus.
- Adopt Game Center, Game Controller, and activity/achievements only with the official UI patterns. In-game menus still need a readable focus model on tvOS and a pointer model on Mac and iPad.

## Designing for iPhone Duo

See [iphone-duo.md](iphone-duo.md) for display, fold, reserved-region, arrangement-view, and vertical-control guidance.


<!-- source: iphone-duo.md -->

# Designing for iPhone Duo

Official HIG: [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo). Also read [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios). Apple introduced its Duo HIG page on September 9, 2026. Check current SDK availability before using APIs named here.

## Core model

- This is an iPhone experience that moves between an **outer display** when closed and an **inner display** when open. It also supports intermediate poses and Split View multitasking.
- Design around available space, size classes, safe areas, margins, and reserved regions. Avoid device-name checks, hard-coded screen dimensions, or a separate UI for every hinge angle.
- Start with a compact-width outer layout and a regular-width inner layout. Keep the information hierarchy, current selection, draft data, and task state continuous as the display or pose changes. The larger layout may show two levels at once, such as list and detail, without removing capabilities from compact width.
- Standard navigation, presentations, and bars already adapt. Use them before custom geometry or hinge logic.

## The displays and fold

| Situation | Design response |
| --- | --- |
| Closed, outer display | Fit the task into compact width and a shorter, wider shape. System bars move to a vertical edge to preserve content height. |
| Open, inner display | Use the regular width to expose useful detail or a second pane. Keep the same selection and action semantics. |
| Inner display in landscape | System bars generally remain vertical, preserving continuity with the outer display. |
| Inner display in portrait | System bars use the familiar horizontal arrangement. |
| Partially folded | The folding region can divide the inner display into usable areas. Move important anchored controls only as much as needed; ordinary scrollable content can remain continuous. |
| Two apps in Split View | Each app's controls can sit on its outer edge. Use safe areas for the resulting asymmetric content space. |

The outer camera region is always present and can expand into the Dynamic Island. The inner camera is hidden until active. The folding region is conditional on pose. These are **reserved regions**, not a constant center gutter. Alerts, sheets, context menus, and split views account for them through system behavior. If a custom layout needs to position a key control, inspect the reserved regions that intersect it instead of guessing a fixed hinge width.

## Choose a layout container

1. For hierarchy, prefer `NavigationSplitView` or `UISplitViewController`. The inner display can show columns together, while the outer display collapses to one pane. Keep navigation outside any arrangement view.
2. For two pieces of content with a stable relationship, consider `ArrangementView` or `UIArrangementViewController`. A **split** arrangement suits side-by-side or stacked peers; an **overlay** arrangement suits a foreground element over background content. The system can reorganize these around aspect ratio and reserved regions.
3. A custom `HStack`, `VStack`, or `ZStack` is still appropriate when its content already reflows correctly. Use arrangement views when pose-aware relocation actually improves the design; do not replace every stack mechanically.
4. For grids that cross the fold, an even number of columns can divide more cleanly. Verify that reading order and selection remain understandable. Continuous feeds, articles, lists, and documents generally keep scrolling rather than jumping to a different region.
5. For a manually anchored control, use the reserved-region APIs (`reservedRegions(kind:options:layoutDirectionBehavior:)` in SwiftUI, or the UIKit equivalent). Distinguish division regions from occlusion regions, and verify the APIs against the project's SDK.

When content moves around the fold, preserve the visual relationship between a selected item and its menu or controls. Favor a small displacement over an abrupt rearrangement. Avoid centering a primary button, playback control, or focused input on the fold when it becomes unusable.

## Navigation, toolbars, and tab bars

- Let system bars choose their axis. Avoid forcing a conventional bottom tab bar or top navigation bar onto the outer display.
- Keep relative action order stable across poses. On the vertical axis, primary navigation such as Back or Close belongs near the top, with prominent completion actions nearby.
- Group related actions with `ToolbarItemGroup` or `UIBarButtonItemGroup`. Use visibility priority for the actions that must survive compression; the system can overflow less important actions.
- Give symbol toolbar actions a meaningful title, because compact, expanded, accessibility, and overflow presentations may use different representations. Reserve the ellipsis for the system overflow menu.
- Keep controls near the content they affect. A list-specific filter can belong with the list rather than on a distant vertical bar.
- For navigation-heavy views, preserving destinations may matter more than showing every toolbar action. For task-heavy views, minimizing the tab bar may leave essential actions visible. Evaluate the actual task and the system's compression behavior.
- The vertical control edge is tied to the hardware and does not simply mirror in right-to-left languages. Still test the reading order and content layout in RTL.

## Multiple displays and cameras

Most apps only need one adapting scene. If the product has a concrete reason to show content on the outer display while the inner display is active, read Apple's [multiple displays and scenes](https://developer.apple.com/videos/play/tech-talks/111464/) guidance and verify scene-accessory APIs. If the feature is camera capture, check the [camera experience](https://developer.apple.com/videos/play/tech-talks/111465/) guidance before assuming camera direction or coordinates. Do not add a second scene merely because the hardware has two displays.

## Design and QA checklist

Check these on the current SDK's Duo simulator or hardware when available. If unavailable, report that the fold behavior is unverified.

- Outer compact and inner regular layouts preserve selection, editing state, and access to the same actions.
- Open, closed, partial fold, portrait, landscape, and app Split View do not cover tappable controls or focused text fields.
- Toolbars, tab bars, overflow menus, sheets, alerts, and context menus remain reachable and readable.
- Custom centered controls avoid active reserved regions; scrollable content retains continuity.
- Large Dynamic Type, VoiceOver, Switch Control, RTL, Dark Mode, and Reduce Motion still work in both display layouts.
- Games and immersive surfaces fill each pose appropriately and keep controls a consistent usable size.

## Primary sources

- [Apple HIG: Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)
- [Apple HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple Tech Talk: Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/)
- [Apple Tech Talk: Strike a pose with adaptive layouts](https://developer.apple.com/videos/play/tech-talks/111463/)
- [Apple Developer: SwiftUI updates](https://developer.apple.com/documentation/Updates/SwiftUI)


<!-- source: foundations.md -->

# Foundations

Official section: https://developer.apple.com/design/human-interface-guidelines/foundations

These rules apply on every screen, on every platform you support.

## Accessibility

URL: https://developer.apple.com/design/human-interface-guidelines/accessibility

Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

Treat accessibility as a layout constraint, not a postscript.

- **Vision.** Support Dynamic Type, Bold Text, Increase Contrast, Reduce Transparency, Differentiate Without Color, and Smart Invert / Dark Mode. Do not encode meaning with color alone. Keep text off busy images or scrim it. Icons that convey actions need accessibility labels.
- **Hearing.** Do not use sound as the only feedback. Pair alerts with visuals and haptics. Caption video. Honor mono audio and balance. Avoid auto-playing audio with no control.
- **Mobility.** 44×44 pt minimum on touch platforms. Do not require gestures that cannot be performed another way (a button must exist for a custom swipe). Support Switch Control, Full Keyboard Access, and Voice Control by using system controls. Avoid time-limited taps unless the task is a game and an alternative exists.
- **Speech.** Do not require speech input. If you use dictation or voice, provide a typed path.
- **Cognitive.** One task per screen where possible. Consistent navigation. Plain language. Do not flash content. Honor Reduce Motion. Avoid punishing mistakes; make undo obvious.
- **visionOS.** Indirect (look + pinch) must work. Do not require sustained arm pose or a specific body position. Custom gestures need a simpler alternative.

Test with VoiceOver, a large accessibility text size, Reduce Motion, and Increase Contrast before calling UI done.

## App icons

URL: https://developer.apple.com/design/human-interface-guidelines/app-icons

- Design a simple, recognizable mark. One idea. No text unless the letterform is the logo and remains readable at small sizes.
- Follow the platform shape: the system masks iOS, watchOS, and macOS icons. Do not draw your own rounded rect, shadow, or highlight that fights the mask.
- Use layers the platform asks for (foreground, background, and the current icon-composer / multi-layer format). Preview light, dark, and tinted appearances.
- tvOS icons are layered and parallax. visionOS icons are 3D layers viewed at an angle. watchOS icons must read at complication-adjacent sizes.
- Do not use Apple hardware, SF Symbols as the entire icon, or screenshots of the UI.
- Export the sizes and layers from the current spec page. Do not invent a master size and hope it scales.

## Branding

URL: https://developer.apple.com/design/human-interface-guidelines/branding

- Brand with color, type voice, and a few custom moments. Do not reskin system controls so they stop looking tappable.
- The app icon and a launch accent can carry the brand. Navigation bars, tab bars, and alerts should stay familiar.
- Do not mimic Apple's first-party app chrome or imply an Apple endorsement.
- Custom fonts are allowed for brand expression in marketing surfaces. UI controls stay on the system font so Dynamic Type and legibility hold.
- Keep the brand recognizable in Light, Dark, and tinted icon styles.

## Color

URL: https://developer.apple.com/design/human-interface-guidelines/color

- Prefer semantic colors: label, secondary label, separator, system background, grouped backgrounds. They adapt to Dark Mode, Increase Contrast, and elevated surfaces.
- One accent color for primary actions and selection. Define it as an asset that has light and dark variants. On macOS, respect the user's preferred accent when you are using system tint behavior.
- Do not use the same hue for a button label and the surface behind it. Primary buttons use the accent fill with a legible label.
- Liquid Glass color tints the glass layer. Use it to emphasize a control, not to recolor an entire content region.
- Inclusive color: contrast meets the platform bar (aim for WCAG AA as a floor for body text). Test color-blind combinations. Pair color with an icon or text.
- Wide-gamut displays can show P3. Provide sRGB fallbacks. Do not assume a photo's colors are your UI colors.
- System gray stacks exist for grouped lists. Use them instead of custom grays that fail in Dark Mode.
- watchOS and tvOS need higher contrast and larger color fields. visionOS glass desaturates weak colors; use the system materials rather than flat hex fills.

## Dark Mode

URL: https://developer.apple.com/design/human-interface-guidelines/dark-mode

Platforms: iOS, iPadOS, macOS, tvOS. visionOS and watchOS have their own appearance models; still avoid pure black text on pure white images.

- Use semantic colors so Dark Mode is automatic. Hard-coded hex pairs drift.
- Elevated surfaces (sheets, popovers) are lighter than the base background in iOS Dark Mode, not darker.
- Do not invert illustrations blindly. Provide dark-specific artwork when a graphic has a solid background.
- White text on a dark photo still needs a scrim. Separators are subtle, not bright lines.
- Test both appearances on the same screen. Icons that are full-color may need a dark variant or a template/hierarchical SF Symbol instead.

## Icons

URL: https://developer.apple.com/design/human-interface-guidelines/icons

- Use SF Symbols for interface icons. They align with the system font, scale with Dynamic Type, and support weights and rendering modes.
- Pick the standard symbol for a standard action (compose, share, trash, search, close). Do not draw a new share icon.
- A symbol alone is acceptable only when the meaning is universal in that context. Otherwise add a label.
- Keep optical weight consistent inside one toolbar.
- Document icons (macOS) follow the system document shape. Do not invent a new file silhouette.
- Standard action groups to reuse, not redraw: editing, selection, text formatting, search, sharing, accounts, ratings, layer order.

## Images

URL: https://developer.apple.com/design/human-interface-guidelines/images

- Provide @2x and @3x (or vector PDF/SVG in asset catalogs). Do not ship a single low-resolution bitmap.
- Use the format that matches the content: opaque photos as HEIF/JPEG, UI graphics as PDF or PNG with alpha. Support HDR and wide color only when the asset actually has that range.
- Include alt text or an accessibility label for informative images. Mark decorative images as hidden.
- Do not stretch. Use aspect-fit or aspect-fill deliberately and crop to a focal point.
- tvOS: layered images for parallax on lockups. visionOS: spatial photos and scenes are a distinct presentation; do not fake depth with a flat image in a volume. watchOS: images are small; simplify.

## Immersive experiences

URL: https://developer.apple.com/design/human-interface-guidelines/immersive-experiences

Platform: visionOS.

- Immersion styles range from mixed (passthrough visible) through progressive to full. Start in the least immersion that works. Make exit obvious and instant.
- Passthrough is someone's real room. Do not obscure hazards with opaque content at the floor. Keep a path back to surroundings.
- Comfort: avoid fast peripheral motion, large unexpected translations, and forced camera movement. If the experience moves the world, offer a stationary alternative.
- Transitions between styles should be gradual and cancellable.
- Virtual hands must not drift from real hands. If you show hands, match tracking and hide them when tracking is low confidence.
- Environments replace the room. Let people choose, and do not trap them in a dark environment without a clear dismiss.
- Ask permission before a Full Space and before hand tracking. Custom gestures exist only in Full Space.

## Inclusion

URL: https://developer.apple.com/design/human-interface-guidelines/inclusion

- Write for a global audience. Avoid idioms, jokes that do not translate, and culturally specific gestures in icons.
- Gender: do not assume pronouns, body, or family structure. Prefer the person's name or "they" when the language allows. Do not require a gendered honorific.
- Representation in illustration: vary age, body, culture, and ability. Avoid stereotypes (gendered jobs, default "user" as one demographic).
- People and settings: do not assume a quiet home, two free hands, perfect vision, or a single device.
- Language: layout for long translations (German, Finnish) and for short ones. Support RTL. Do not bake strings into images.
- Accessibility is part of inclusion, not a separate track.

## Layout

URL: https://developer.apple.com/design/human-interface-guidelines/layout

- Visual hierarchy: one primary region, clear grouping, more space around more important groups. Alignment is consistent.
- Adapt with size classes (`UserInterfaceSizeClass`), not device names. Compact width is a phone column. Regular width can hold a sidebar and detail.
- Guides: stay inside layout margins and the safe area (`safeAreaInsets`, `UILayoutGuide`, `NSLayoutGuide`). Content can extend under bars only when it scrolls and remains readable through scroll edge effects.
- Backgrounds may extend edge to edge (`backgroundExtensionEffect()` / `UIBackgroundExtensionView`). Controls do not.
- macOS: respect window margins and the toolbar. Do not pin critical buttons under the title bar.
- tvOS: use the focus grid and the safe title area. Keep type off the extreme edges.
- visionOS: layout in the window, then place the window. Do not design for a fixed monitor.
- watchOS: full-bleed content is fine; controls stay in the safe area away from the rounded corners and the Crown side when it matters.

## Materials

URL: https://developer.apple.com/design/human-interface-guidelines/materials

Two families:

- **Liquid Glass** is the functional layer. Tab bars, toolbars, sidebars, and similar chrome float above content and let content scroll beneath. System components do this automatically.
- **Standard materials** separate regions inside the content layer.

Rules:

- Do not use Liquid Glass for content backgrounds, list cards, or large decorative panels. Exception: a transient control that briefly floats over rich media.
- Apply custom glass sparingly. Overuse flattens hierarchy and hurts performance and readability.
- `Glass.regular` blurs and lifts contrast so text stays legible. Use it for controls with labels. `Glass.clear` is highly translucent; use it only over photos or video.
- The user can pick a glass look and can turn on Reduce Transparency. Your custom materials must remain legible in those modes. If they do not, you are using too much custom glass.
- Scroll edge effects (`ScrollEdgeEffectStyle`) fade content under bars. Do not draw your own gradient to fake this if the system effect is available.
- Content-layer materials: SwiftUI `Material.ultraThin`, `thin`, `regular`, `thick`. UIKit `UIBlurEffect` + `UIVibrancyEffect`. AppKit `NSVisualEffectView` with the matching material and blending mode.
- Vibrancy is for labels and separators on a blur, using the vibrancy styles (label, secondary, fill, separator). Do not place opaque gray text on a blur and call it done.
- visionOS windows are glass by default. watchOS uses dark, high-contrast materials more than blur.

## Motion

URL: https://developer.apple.com/design/human-interface-guidelines/motion

- Motion explains a change: where something came from, whether it succeeded, and what is related. It is not decoration.
- Use system transitions for push, sheet, modal, and focus. Custom animation should match system duration and curves, generally short (well under a second for UI).
- One animated idea at a time. Do not bounce every control on appear.
- Feedback: a control responds on press (highlight or glass morph) immediately. Navigation animates the hierarchy.
- Honor Reduce Motion: crossfade instead of sliding, parallax, or zoom. Essential state changes still happen; only the travel is reduced.
- visionOS: large motion in the periphery causes discomfort. Prefer opacity and small transforms. Never move the horizon unexpectedly.
- watchOS: motion is tiny and fast. Use the system indicator animations. Avoid looping full-screen effects, especially in Always On.
- Do not autoplay video or looping motion without a pause path.

## Privacy

URL: https://developer.apple.com/design/human-interface-guidelines/privacy

- Ask at the moment of need, not at first launch for a feature the person has not tried.
- The system permission alert is the request. A pre-prompt is optional and only to explain the benefit immediately before the system alert. If they deny the pre-prompt, do not show the system alert.
- Purpose strings are specific ("Shows your position on the route"), not generic ("This app needs your location").
- Tracking uses App Tracking Transparency and only when you actually track across apps and sites. Denial is a normal outcome; the app still works.
- Location button (`LocationButton` / `CLLocationButton`) is a deliberate one-shot share. Prefer it when you do not need ongoing location.
- Protect data: prefer on-device processing, passkeys and Local Authentication, and the keychain for secrets. Do not invent a password store. Do not log sensitive data.
- Offer a path to delete an account inside the app when an account can be created there.
- macOS: explain helper tools, folder access, and automation prompts in the UI that triggers them.
- visionOS: cameras and hand tracking reveal the room and body. Ask in context and minimize retention.

## Right to left

URL: https://developer.apple.com/design/human-interface-guidelines/right-to-left

- Use leading/trailing constraints, not left/right. SwiftUI `HStack` and layout margins flip when the layout direction is RTL.
- Text aligns trailing for RTL languages when you use natural alignment. Do not force left alignment on Arabic or Hebrew body text.
- Flip directional controls and icons (back chevron, forward, send in a conversation if it points "ahead"). Do not flip: playback triangles that mean play, clocks, sheet music, graphs whose axis is time in a fixed convention, numbers that read LTR inside RTL sentences, and the Apple logo.
- Progress still fills in the reading direction.
- Test the layout with a pseudolanguage or an RTL locale. Check that padding did not stay physically left.

## SF Symbols

URL: https://developer.apple.com/design/human-interface-guidelines/sf-symbols

- Symbols scale with text (`imageScale`, font-relative symbol scale) and match the adjacent font weight.
- Rendering modes: monochrome (one color), hierarchical (one color, varied opacity), palette (multiple colors), multicolor (intrinsic). Pick one mode per context. Hierarchical is the default for toolbars.
- Variable color encodes a value (signal strength, fill level). Do not use it as decoration.
- Weights and scales must match the text next to them. Do not mix ultra-light symbols with bold labels.
- Design variants exist for each platform (fill vs outline, slash for off states). Use the variant that matches the OS style.
- Animations (`SymbolEffect`) replace custom Lottie for simple state changes (bounce on appear, pulse, replace). Honor Reduce Motion.
- Custom symbols: draw on the SF Symbols template so alignment, weight, and optical metrics match. Do not drop in an unrelated SVG and call it a symbol.
- Do not use symbols as a logo or as the app icon's only graphic.

## Spatial layout

URL: https://developer.apple.com/design/human-interface-guidelines/spatial-layout

Platform: visionOS.

- Field of view: keep primary windows in front, slightly below eye level, within a comfortable distance. Recenter is a system behavior; do not fight it.
- Depth: closer objects are more important or more interactive. Keep related UI on one depth plane so the eyes do not refocus constantly.
- Scale: UI is sized for the distance it sits. Do not scale a window up to billboard size to make it "important"; move it closer or use hierarchy inside the window.
- Avoid content that intersects the wearer. Keep a comfortable near plane.
- Anchor persistent content in the world only when there is a reason (a placed object). Ordinary apps use windows that travel with the user.

## Typography

URL: https://developer.apple.com/design/human-interface-guidelines/typography

- Use the system font (SF Pro, SF Compact on watchOS, SF Pro Rounded only when the product's voice truly needs it). New York is the system serif.
- Use text styles, not raw point sizes: large title, title, title 2, title 3, headline, body, callout, subheadline, footnote, caption, caption 2. Styles carry weight, leading, and Dynamic Type.
- Hierarchy: one large title, section headlines, body. Do not skip levels or set an entire screen in headline weight.
- Dynamic Type is mandatory on iOS, iPadOS, and watchOS. Test the largest accessibility sizes. Allow wrapping. Scroll instead of truncating essential text. `lineLimit` is for secondary metadata, not for the primary message.
- Custom fonts must still scale, support bold text if possible, and cover the languages you ship. Fall back to the system font for missing scripts.
- Tracking: use the values that belong to the style. Do not tighten body text.
- tvOS styles are larger. watchOS styles are SF Compact and shorter. visionOS leans on slightly heavier weights for glass.
- Do not set text below the platform's practical minimum. If a legal line cannot fit, reveal it, do not shrink it to 9 pt.

## Writing

URL: https://developer.apple.com/design/human-interface-guidelines/writing

- Sentence case. No title case in buttons or labels. No all caps except standard trademarks and short system conventions.
- Lead with the action or the result. "Delete playlist" not "Are you sure you want to delete this playlist?"
- Buttons are verbs. Alerts: what happened, why it matters, what to do next.
- Use contractions when they sound like a person. Avoid slang, jokes in errors, and blame ("you failed").
- Be specific. "Not enough space to download" beats "Error 42".
- Address the person as "you" when needed. Do not say "the user".
- Localize every string, including accessibility labels. Leave room for expansion. Do not concatenate sentences.
- Use Apple product names correctly (iPhone, iPad, Apple Watch, Apple Vision Pro, Mac). Do not invent abbreviations.


<!-- source: patterns.md -->

# Patterns

Official section: https://developer.apple.com/design/human-interface-guidelines/patterns

Patterns are flows. Components are the controls inside them. Read both.

## Charting data

URL: https://developer.apple.com/design/human-interface-guidelines/charting-data

- A chart answers one question. Title that question in plain language.
- Pick the mark that matches the data: line for trend, bar for comparison, point for distribution, sector only for a few parts of a whole. Do not use a pie for many slices.
- Axes have units and a honest baseline. Do not truncate a bar chart baseline to exaggerate.
- Color encodes one variable and still works in color blindness and Dark Mode. Provide a text or audio alternative (Swift Charts accessibility).
- Interaction: tap a mark to see the value. Do not make the chart the only place the number exists.
- watchOS charts are summaries, not dashboards. One series, large labels.

## Collaboration and sharing

URL: https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing

- Share uses the system share sheet (`ShareLink`, activity view). Do not build a private share popup that hides system destinations.
- Show who has access and what they can do. Make "view" the default when editing is dangerous.
- Collaboration presence (avatars, cursors) must be optional and not cover content.
- Shared with You (`SWHighlight`) surfaces content someone sent in Messages. Attribute it and deep-link to the right item.
- visionOS: shared sessions should not require a specific seat or body pose. watchOS: share is usually "send to iPhone" or a short handoff, not a full collaborator list.

## Drag and drop

URL: https://developer.apple.com/design/human-interface-guidelines/drag-and-drop

Platforms: iOS, iPadOS, macOS, visionOS.

- Anything people might want elsewhere should be draggable: images, files, selections, rows.
- Lift preview shows the item, not a generic rectangle. The source stays put until the drop succeeds.
- Drop targets highlight when the drag enters and reject with a clear "no" when the type is wrong.
- Accept standard types (file URLs, images, text, `NSUserActivity`) so other apps can drop on you.
- iPad and Mac: drag between windows and apps. visionOS: drag in space should feel like moving an object, with a visible destination.
- Provide an accessibility path (`accessibilityDragSourceDescriptors` or menu actions) so drag is not the only way.

## Entering data

URL: https://developer.apple.com/design/human-interface-guidelines/entering-data

- Ask for the minimum. Prefill from the system (contacts, location button, passwords, passkeys) before a blank field.
- Order fields the way people think. Group related fields. Validate inline when the error is about one field; use an alert when the whole form fails.
- Use the right control: toggle for boolean, picker for a short known set, text field for free text, stepper for a small numeric tweak.
- Secure fields (`SecureField`, `isSecureDigitEntry`) for secrets. Never echo a password in a subtitle.
- Autofill via `textContentType`. Correct keyboard type. See Virtual keyboards.
- macOS: forms can be denser and use tab order. Return submits the default button.
- Let people paste. Do not block paste on codes they just received.

## Feedback

URL: https://developer.apple.com/design/human-interface-guidelines/feedback

- Every input gets immediate sensory feedback: highlight, haptic, sound, or movement. Silent controls feel broken.
- Feedback matches severity. A successful toggle does not use an alert. A failed payment does not use only a color change.
- Place feedback next to the thing that changed. Do not rely on a distant status bar.
- Combine channels: vision (state), haptics (confirmation), sound (only when the eyes may be elsewhere, and never as the only channel).
- watchOS: haptics carry more weight because the screen is small. Keep them short and standard.

## File management

URL: https://developer.apple.com/design/human-interface-guidelines/file-management

- Use the system document model: open, save, duplicate, rename, and the document browser or Files integration. Do not invent a private filesystem UI if Files or `DocumentGroup` already fits.
- Autosave on iOS and modern macOS. If you must ask to save, do it at close and be specific.
- Quick Look for previews. Do not build a custom previewer for PDF and images.
- iOS document launcher and file provider extensions should look like Files, not like a nested brand browser.
- macOS Finder Sync is for badges and context menus in Finder, not a second file manager.
- Title windows and navigation bars with the filename. Dirty state is visible on macOS.

## Going full screen

URL: https://developer.apple.com/design/human-interface-guidelines/going-full-screen

Platforms: iOS, iPadOS, macOS.

- Full screen is for content (video, games, canvases), not for forms.
- Always provide an obvious exit. On iOS, defer the home indicator only while it is necessary (`preferredScreenEdgesDeferringSystemGestures`) and show a cue.
- macOS full screen is a space. Remember it. The menu bar and Dock may auto-hide; do not permanently steal them (`toggleFullScreen`, `CollectionBehavior`).
- Do not enter full screen without a user action, except video playback they just started.
- Status and controls can overlay and auto-hide. The first tap or pointer move reveals them.

## Launching

URL: https://developer.apple.com/design/human-interface-guidelines/launching

- Launch fast into the last meaningful state. Do not show a branded splash longer than the system launch screen.
- The launch screen matches the first screen's empty background. No text, no logo parade, no version number. Those belong in the app if at all.
- Restore navigation depth and scroll position when people return.
- tvOS and visionOS launch screens still match the first UI. Do not flash a full-bleed marketing image.
- If startup work is required, show the real chrome with a progress indicator, not a blocking logo.

## Live-viewing apps

URL: https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps

Broadcast and live video apps (TV providers, sports, events).

- The program is the primary surface. Chrome (guide, info, controls) appears on demand and gets out of the way.
- EPG (guide) is a grid of time by channel. Current time is obvious. Navigation by remote or touch follows the grid.
- Cloud DVR: record, scheduled, and storage state are explicit. Deleting recordings confirms.
- Live badges, elapsed time, and "on now" must be accurate. Do not fake live.
- Errors (signal, auth, blackout) say what failed and the one next step.

## Loading

URL: https://developer.apple.com/design/human-interface-guidelines/loading

- If it finishes in under about a second, do not flash a spinner.
- Known length: determinate progress (`ProgressView` with a value), near the content.
- Unknown length: indeterminate indicator. Include a word if the wait can be long ("Updating library").
- Keep surrounding navigation usable. Do not modal-block the app for ordinary loads.
- Skeleton or placeholder content is better than a blank page when the layout is known.
- Failures replace the spinner with a message and a retry. Never spin forever.
- watchOS: a tiny indicator is enough. Do not cover the face.
- Background asset downloads (`BackgroundAssets`) should not look like a foreground stall.

## Managing accounts

URL: https://developer.apple.com/design/human-interface-guidelines/managing-accounts

- Offer Sign in with Apple when you offer other social logins. See that technology page.
- Account creation is as short as the product allows. Defer profile trivia until it is useful.
- Show the signed-in person (name, avatar) where account actions live. Sign out is easy to find and not visually primary.
- If the app creates an account, provide in-app account deletion, not an email maze.
- Credentials live in the keychain. Prefer passkeys. Biometrics (`LABiometryType`) unlock a credential; they are not the account.
- TV provider accounts use the system TV provider flow where it applies. watchOS often approves an account that was created on iPhone; do not rebuild a long form on the watch.

## Managing notifications

URL: https://developer.apple.com/design/human-interface-guidelines/managing-notifications

- Ask after the person understands the value, not at first launch. Denial is acceptable; do not nag on every launch.
- Integrate with Focus and interruption levels (`UNNotificationInterruptionLevel`). Only time-critical events use the highest level.
- Let people choose categories inside the app. Deep-link to system notification settings for global changes.
- Marketing notifications are opt-in, infrequent, and clearly commercial. Provide an in-app off switch.
- A notification that repeats information already on screen should not also badge and sound.
- watchOS mirrors are coordinated. Do not buzz the wrist and the phone for the same event unless that is the point.

## Modality

URL: https://developer.apple.com/design/human-interface-guidelines/modality

- Modal UI blocks the parent until the task ends. Use it for focused, short, self-contained tasks (compose, confirm, pick).
- Do not use a modal to drill through a hierarchy. Push or split instead.
- People always see how to dismiss: Cancel, Close, or a grabber plus swipe on a sheet.
- Avoid stacking modals. If a modal needs another decision, use a confirmation dialog or replace the content.
- On iPad and Mac, prefer popovers and sheets anchored to context over full-screen takeovers.
- System styles (`UIModalPresentationStyle`, SwiftUI `sheet` / `fullScreenCover`) define motion and size. Do not invent a new modal transition.

## Multitasking

URL: https://developer.apple.com/design/human-interface-guidelines/multitasking

- Assume you will be backgrounded. Save state on resign active.
- iOS: picture in picture and scene multitasking on supported devices. Do not break when the window is narrow.
- iPadOS: all window sizes from Slide Over to full screen to Stage Manager. No fixed canvas.
- macOS: multiple windows, Spaces, and full screen. Documents reopen.
- tvOS: playback may continue or yield focus. Do not fight the system screensaver and Now Playing.
- visionOS: other apps share the space. Your window can be resized and placed beside others. Full Space is the exception and must be explicit.
- Resume audio, downloads, and navigation correctly after an interruption.

## Offering help

URL: https://developer.apple.com/design/human-interface-guidelines/offering-help

- The interface should make help unnecessary. Help is for concepts that cannot be learned from the control itself.
- Tips (`TipKit`) are short, one idea, dismissible, and shown once in context. Do not stack tip tours on first launch.
- Contextual help beats a manual. On macOS and visionOS, Help menu and `help(_:)` / `NSHelpManager` open the right page.
- Do not use a tip to market a subscription.

## Onboarding

URL: https://developer.apple.com/design/human-interface-guidelines/onboarding

- Get people to the product. A single welcome screen is enough if you need one. Skip is always available.
- Do not front-load permission dialogs, account creation, and a feature carousel.
- Teach by doing, or with a tip on the control, not a five-step slideshow.
- Additional requests (notifications, tracking, reviews) come after a success, one at a time.
- If the person has used the app before, do not show onboarding again. New features get a tip, not a replay of the intro.

## Playing audio

URL: https://developer.apple.com/design/human-interface-guidelines/playing-audio

- Use the system volume. Do not draw a custom volume slider that ignores the hardware buttons (`MPVolumeView` or the system volume UI).
- Pick an `AVAudioSession` category that matches the role: playback, ambient (mixes and silences with the ringer), record, play-and-record.
- Interruptions (calls, Siri, other apps): pause, duck, or mix on purpose. Resume only if you were playing and the interruption says you should (`notifyOthersOnDeactivation`, `shouldResume`).
- Now Playing metadata and remote commands (lock screen, headset, CarPlay, watch) are part of playback, not optional.
- Background audio requires a real playback session and the proper capability. Do not play silence to stay alive.
- visionOS and watchOS: audio is spatial or intimate. Do not blast exclusive audio if the task is a short UI sound.

## Playing haptics

URL: https://developer.apple.com/design/human-interface-guidelines/playing-haptics

- Use haptics to confirm, align, or warn. Not on every scroll tick.
- Prefer system generators: notification (success, warning, error), impact (light, medium, heavy, rigid, soft), selection (detent changes).
- Custom haptics (`CoreHaptics`) match a physical event in a game or instrument. They still respect the system mute and Low Power behavior.
- macOS haptics are subtle trackpad taps (`NSHapticFeedbackPerformer`). watchOS uses `WKHapticType` and is felt more than seen.
- Provide a visual twin. Never haptic-only.
- Do not play haptics in a tight loop.

## Playing video

URL: https://developer.apple.com/design/human-interface-guidelines/playing-video

- Prefer system players (`VideoPlayer`, `AVPlayerViewController`) so PiP, AirPlay, subtitles, and transport are correct.
- Letterbox with aspect fit when the whole frame matters. Fill (`resizeAspectFill`) only when cropping is acceptable.
- Controls appear on interaction and hide during playback. Scrubbing shows time and a preview if you have one.
- Captions and audio descriptions are part of the feature. External metadata should include them.
- Silence other audio hints appropriately (`silenceSecondaryAudioHintNotification`) and duck rather than killing someone else's music unless you are the primary playback.
- TV app integration: continue watching, and exit playback back to the place they came from.
- tvOS: remote transport, not touch chrome. visionOS: video can be a window or an immersive surface; immersion is chosen, not forced. watchOS: short clips, not a theater UI.

## Printing

URL: https://developer.apple.com/design/human-interface-guidelines/printing

Platforms: iOS, iPadOS, macOS, visionOS.

- Use the system print panel (`UIPrintInteractionController`, `NSDocument` print). Do not rebuild page-range and paper pickers.
- Print layout is not the screen layout. Paginate, use margins, and provide a preview.
- Offer print from the share sheet or File menu, not as a primary toolbar item unless the app is a document app.

## Ratings and reviews

URL: https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews

- Use the system prompt (`RequestReviewAction`). It is rate-limited. Do not add your own star dialog that gates the system one.
- Ask after a success, never after a failure, never on first launch, never repeatedly after a decline.
- Do not incentivize or beg. Do not route around the prompt with a custom UI that looks like the system review dialog.

## Searching

URL: https://developer.apple.com/design/human-interface-guidelines/searching

- Search finds content. It is not a filter bar in disguise, though scope controls can refine results.
- Show recent and suggested queries (`searchSuggestions`). Results appear as the person types when the data is local or fast.
- Empty query shows suggestions or recent items, not an error. No results says that plainly and offers to broaden.
- System search (Spotlight, `CSImportExtension`) should index the same objects the in-app search finds, with Quick Look previews.
- See Search fields for placement (tab, toolbar, inline).

## Settings

URL: https://developer.apple.com/design/human-interface-guidelines/settings

- Prefer sensible defaults so most people never open Settings.
- Split settings: values people change often can live near the task. Rare, app-wide values go in Settings.
- System Settings is for system-level permissions and capabilities. Do not duplicate those screens inside the app; link to them.
- Group with headers. Use toggles, pickers, and navigation links in the system form style. Store in `UserDefaults` or a visible store, not a hidden plist the UI can desync from.
- macOS settings are a window or a settings scene, with a toolbar of categories when there are several. watchOS settings are short lists, often mirrored from iPhone.

## Undo and redo

URL: https://developer.apple.com/design/human-interface-guidelines/undo-and-redo

Platforms: iOS, iPadOS, macOS, visionOS.

- Any edit that destroys or replaces content supports undo (`UndoManager`).
- macOS: Edit menu Undo/Redo and Command-Z / Shift-Command-Z. Name the action ("Undo Rename").
- iOS: shake to undo is a system behavior for text. For richer edits, also provide an explicit Undo button because many people never shake.
- Undo stacks are per document or per context, not a single global pile of unrelated screens.
- Do not ask "Are you sure?" when undo can do the job.

## Workouts

URL: https://developer.apple.com/design/human-interface-guidelines/workouts

Platforms: iOS, iPadOS, watchOS. The watch is the primary workout surface.

- Metrics are large, high contrast, and readable in motion. One to three numbers, not a dashboard.
- Start, pause, and end are unmistakable and hard to trigger by accident. End confirms or uses a press-and-hold.
- Use WorkoutKit and HealthKit patterns. Activity rings and heart-rate presentation follow the Health pages.
- Always On during a workout stays legible and calm. Do not flash.
- iPhone is the companion for history and configuration, not a second live dashboard that disagrees with the watch.


<!-- source: components-content-layout.md -->

# Components: content, layout, and organization

Official sections:

- https://developer.apple.com/design/human-interface-guidelines/content
- https://developer.apple.com/design/human-interface-guidelines/layout-and-organization

## Charts

URL: https://developer.apple.com/design/human-interface-guidelines/charts

Use Swift Charts. A chart has marks, axes, and a description.

- Marks match the question: bar, line, point, area, or rectangle. One chart, one claim.
- Axes are labeled with units. Gridlines are quiet. Zero baseline for bars unless a break is explicit and honest.
- Descriptive content: a title and a one-line summary so VoiceOver users get the point without exploring every mark. Enable `accessibilityRespondsToUserInteraction` only when exploring marks is useful.
- Color is redundant with shape or position. Test Dark Mode and color blindness.
- watchOS: one series, large value, no dense legend.

## Image views

URL: https://developer.apple.com/design/human-interface-guidelines/image-views

- Use `Image`, `UIImageView`, or `NSImageView`. Content mode is a product decision: fit shows the whole asset, fill crops.
- Do not upscale a small bitmap. Provide the right resolution.
- Informative images need labels. Decorative ones are accessibility-hidden.
- macOS image views can be selectable and drag sources. tvOS images participate in focus and may use layered artwork. visionOS can present spatial photos (`ImagePresentationComponent`) rather than a flat well. watchOS keeps images simple and high contrast.

## Text views

URL: https://developer.apple.com/design/human-interface-guidelines/text-views

- Use `Text` for read-only copy. Use a text view (`UITextView`, `NSTextView`) when the person edits or the text is long.
- Long text scrolls inside the view or with the page, not both in a nested trap.
- Respect Dynamic Type and selection. Links look like links.
- iOS text views inside forms should not fight the keyboard. tvOS is a poor place for long reading; keep copy short.

## Web views

URL: https://developer.apple.com/design/human-interface-guidelines/web-views

Platforms: iOS, iPadOS, macOS, visionOS.

- `WKWebView` is for content you cannot reasonably make native, not for entire apps.
- Native chrome (navigation, share, progress) stays native. Do not draw a second browser toolbar in the page if the app already has one.
- Support back, reload, and open-in-Safari for untrusted or full web pages.
- Pad the page for safe areas and keyboards. Do not let web content sit under the home indicator with no inset.
- Disable arbitrary JS bridges that expose private data.

## Boxes

URL: https://developer.apple.com/design/human-interface-guidelines/boxes

Platforms: iOS, iPadOS, macOS, visionOS.

- A box (`GroupBox`, `NSBox`) groups related controls with an optional label. It is not a card style for every cell.
- One box, one topic. Do not nest boxes deeply.
- iOS grouped lists often replace boxes. macOS settings use boxes or grouped form style, not both around the same controls.

## Collections

URL: https://developer.apple.com/design/human-interface-guidelines/collections

- Collections (`UICollectionView`, `NSCollectionView`, lazy grids) show many peer items: photos, files, products.
- Items have a consistent size or a clear masonry rule. Spacing is even.
- Selection, focus, and context menus follow the platform. Empty collections have an empty state, not a blank grid.
- iOS: prefer compositional layouts that reflow. Do not build a horizontal scroller of buttons as primary navigation (that is a tab bar's job).

## Column views

URL: https://developer.apple.com/design/human-interface-guidelines/column-views

Platform: macOS. `NSBrowser`.

- A column view shows a deep hierarchy one level per column (files, categories). The rightmost column is the selection's children or preview.
- Columns scroll horizontally as depth grows. Do not use this on iOS; use a navigation stack or outline.

## Disclosure controls

URL: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls

- Disclosure triangles expand in place (`DisclosureGroup`). Disclosure buttons push a new screen or reveal a section.
- The label names the hidden content, not "More" or "Click here".
- State is obvious: collapsed vs expanded. On iOS, a chevron push is navigation, not an in-place disclosure. Do not mix them in one row.
- visionOS and iOS use the system chevron direction, which flips in RTL.

## Labels

URL: https://developer.apple.com/design/human-interface-guidelines/labels

- Labels name controls or show values. They are not buttons. If it is tappable, use a button or a link.
- Use semantic label colors: primary, secondary, tertiary, quaternary. Secondary is for metadata.
- A label above or beside a control is one phrase, not a paragraph. Helper text is secondary and optional.
- `Label` pairs a symbol and a title and adapts to toolbar vs list styles.
- macOS static text uses `labelColor` variants. watchOS labels are short and high contrast. Do not shrink a label below the text style to make it fit; reflow.

## Lists and tables

URL: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

- Lists (`List`, `UITableView`) are single-column rows. Tables (`NSTableView`, SwiftUI `Table`) are multi-column and belong on macOS and sometimes iPad.
- Row content: primary title, optional secondary line, optional trailing value or disclosure. Do not pack a dashboard into a row.
- Use system list styles (plain, inset grouped, sidebar). Grouped lists need section headers when the grouping means something.
- Swipe actions are shortcuts to frequent row actions, not the only path. Destructive swipe is trailing and confirms if it cannot be undone.
- Reorder handles, selection checks, and disclosure indicators use system accessories (`disclosureIndicator`, `UIListContentConfiguration`).
- macOS tables support sorting, column resize, and keyboard extend-selection. tvOS lists are focusable rows with large type. watchOS lists are the main navigation pattern; keep rows to one or two lines.
- Empty, loading, and search-no-results states are part of the list.

## Lockups

URL: https://developer.apple.com/design/human-interface-guidelines/lockups

Platform: tvOS. APIs include `TVLockupView`, `TVPosterView`, `TVCardView`, `TVCaptionButtonView`, `TVMonogramContentView`.

- A lockup is artwork plus a short caption that focuses as one item.
- Posters, cards, caption buttons, and monograms are the standard forms. Use them instead of custom focusable tiles.
- Titles are one or two lines. Focus expands the artwork; do not also animate a separate caption wildly.
- Progress bars on lockups show genuine continue-watching progress.

## Outline views

URL: https://developer.apple.com/design/human-interface-guidelines/outline-views

Platform: macOS. `OutlineGroup`, `NSOutlineView`.

- Outlines show a tree in one column with disclosure triangles. Use them for nested data (folders, headings), not for flat lists.
- Persist expand state when it helps. Keyboard disclosure (left/right arrow) must work.
- Do not expand everything by default if the tree is deep.

## Split views

URL: https://developer.apple.com/design/human-interface-guidelines/split-views

- Two or three panes: sidebar, content, optional inspector. `NavigationSplitView`, `UISplitViewController`, `HSplitView` / `VSplitView`, `NSSplitViewController`.
- iPhone and compact width: show one pane and push. iPad regular width: sidebar and detail. macOS: user-resizable dividers with sensible minimums.
- The detail pane is never an empty dead end in regular width if a selection exists. If nothing is selected, show a placeholder.
- tvOS split layouts still follow focus, not dragging. visionOS split views stay inside a window. watchOS rarely needs a split; do not force two columns onto a watch face.
- iPhone Duo: split views expand on the inner display, collapse on the outer, and dodge the hinge automatically when you use the system split view.

## Tab views

URL: https://developer.apple.com/design/human-interface-guidelines/tab-views

Platforms for this control: macOS and watchOS primarily. iOS uses a tab bar, not a tab view. See Tab bars.

- A tab view switches peer panes inside one window (`NSTabView`, `TabView`). People stay in place; the content changes.
- Tabs are few, short, and parallel. If there are many, use a sidebar.
- watchOS tab views are pages you swipe or turn the Crown to change. Each page is one glance.
- Do not use tabs for a sequential flow (that is navigation or a stepper).


<!-- source: components-menus-navigation.md -->

# Components: menus, actions, navigation, and search

Official sections:

- https://developer.apple.com/design/human-interface-guidelines/menus-and-actions
- https://developer.apple.com/design/human-interface-guidelines/navigation-and-search

## Activity views

URL: https://developer.apple.com/design/human-interface-guidelines/activity-views

Platforms: iOS, iPadOS, visionOS.

- The share sheet (`UIActivityViewController`, `ShareLink`) is how content leaves the app. Put your custom actions in the sheet rather than a bespoke grid of destinations.
- Share extensions and action extensions appear in the sheet. They do one job and return.
- Exclude irrelevant activity types. Do not exclude system destinations people expect (Copy, Save Image) without a reason.
- The control that opens the sheet is the share symbol, unless the action is not sharing.

## Buttons

URL: https://developer.apple.com/design/human-interface-guidelines/buttons

A button performs an action immediately. It does not toggle (that is a toggle) and it does not choose from a list (that is a pop-up or menu).

- One visually prominent style for the most likely action. Other actions use a quieter style. Do not enlarge one button to make it primary; use style.
- System styles: bordered, borderless, filled, tinted, glass, and glass prominent where the SDK offers them. Prefer those over a custom-drawn shape.
- Content is a short verb, a familiar symbol, or both. If the symbol is ambiguous, add a label or a help tooltip (macOS and visionOS show tooltips on hover).
- Roles: normal, cancel, destructive, primary. Destructive is red or the destructive role, and it is not the default focus unless the task is itself destructive.
- Press state is mandatory. System buttons provide it. Custom buttons must highlight on press or they feel dead.
- Hit target 44×44 pt on touch platforms even if the artwork is smaller.
- iOS: place the primary button where the thumb and the hierarchy agree, usually trailing or bottom in a sheet.
- macOS push buttons commit dialogs. Help buttons are the small circular "?" and only for contextual help. Image buttons need a tooltip and an accessibility label. Square bezels are for toolbars and inspectors, not for marketing CTAs.
- visionOS: buttons are glass, look-and-pinch targets, with a hover highlight driven by the system.
- watchOS: full-width buttons in the scroll view, or toolbar items in the corners. Keep labels short.

## Context menus

URL: https://developer.apple.com/design/human-interface-guidelines/context-menus

- A context menu is secondary actions on an object (long press, control-click, secondary click). It is not the only way to do a primary action.
- Keep the list short. Order by frequency. Destructive items last, with the destructive role.
- Include the actions people expect: Copy, Share, Delete, when they apply.
- iOS: preview on long press plus the menu (`contextMenu`, `UIContextMenuInteraction`). macOS: the menu is not a preview. visionOS: look and touch-and-hold, and do not require it for primary tasks.

## Dock menus

URL: https://developer.apple.com/design/human-interface-guidelines/dock-menus

Platform: macOS. `applicationDockMenu(_:)`.

- Dock menus list a few app-global actions and recent items. They are not a second menu bar.
- Items work even when no document window is key.

## Edit menus

URL: https://developer.apple.com/design/human-interface-guidelines/edit-menus

- The edit menu holds text and selection commands: cut, copy, paste, select, lookup, and your extras (`UIEditMenuInteraction`, `UIResponderStandardEditActions`, `NSMenu`).
- Do not replace system items. Append.
- iOS shows the edit menu near the selection. macOS shows it from the menu bar and as a context menu. Both must stay in sync.

## Home Screen quick actions

URL: https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions

Platforms: iOS, iPadOS.

- Long-press on the icon shows at most a handful of frequent actions (compose, search, resume).
- Each item has a short title and a symbol. Deep-link to the action, do not dump the person on a home tab.
- Do not put settings or destructive actions here.

## Menus

URL: https://developer.apple.com/design/human-interface-guidelines/menus

- Menu items are actions or choices. Labels are short. Icons reinforce, and they align.
- Group with separators. Submenus only when a group is long and cohesive. Avoid nested submenus.
- Toggled items show a checkmark or switch state, not a new label that says "Turn off".
- Destructive items use the destructive role and sit at the bottom of their group.
- In-game menus may look custom but still need readable type, focus order, and a way back.
- iOS menus attach to buttons. visionOS menus are glass and appear near the control, not across the room.
- Keyboard shortcuts are shown on macOS and iPad. See Keyboards.

## Ornaments

URL: https://developer.apple.com/design/human-interface-guidelines/ornaments

Platform: visionOS. `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`.

- Ornaments hold toolbars, tabs, and related actions, attached to a window edge.
- They float in glass and remain associated with the window when it moves.
- Do not put primary content in an ornament. Do not stack many ornaments around one window.
- Use system toolbar and tab APIs so placement and focus are correct.

## Pop-up buttons

URL: https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons

- A pop-up button shows the current choice and opens a menu to change it (`Menu` with `MenuPickerStyle`, `NSPopUpButton`, `changesSelectionAsPrimaryAction`).
- The closed state displays the selection, not the word "Choose", once a value exists.
- Use it for a mutually exclusive set that should stay visible. For an immediate command, use a pull-down button instead.
- iPadOS can use pop-up buttons in regular-width inspectors and forms.

## Pull-down buttons

URL: https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons

- A pull-down button shows a menu of commands. The button's label is the menu's name, not the last command (`showsMenuAsPrimaryAction`, `pullsDown`).
- Do not use it when selecting an option should update the button title. That is a pop-up.
- iOS and iPadOS: a pull-down in a toolbar is a compact command menu.

## The menu bar

URL: https://developer.apple.com/design/human-interface-guidelines/the-menu-bar

Platforms: macOS, and iPadOS when a keyboard is attached.

Standard order: App menu, File, Edit, Format, View, then app-specific menus, then Window, then Help.

- App menu: About, Settings, Services, Hide, Quit. Quit is Command-Q.
- File: New, Open, Close, Save, and document actions. Share and Print live here when relevant.
- Edit: Undo, Redo, Cut, Copy, Paste, Select All, and find commands.
- Format: text styling when the app edits text.
- View: show/hide sidebar, zoom, enter full screen.
- Window: minimize, zoom, bring-all-to-front, window list.
- Help: app help and search. `NSHelpManager` for contextual help.
- Dynamic items (recent documents, open windows) update while the menu is closed.
- Menu bar extras (`MenuBarExtra`, `NSStatusBar`) are for status that must be visible regardless of which app is frontmost. Keep the dropdown short. Do not duplicate the whole app.
- iPadOS menu bar follows the same order so keyboard users land in a familiar place. `CommandMenu` in SwiftUI.

## Toolbars

URL: https://developer.apple.com/design/human-interface-guidelines/toolbars

- Toolbars hold frequent actions and the current title. Rare commands stay in menus.
- Titles name the current context. Large titles on iOS collapse on scroll when you use the system bar (`prefersLargeTitles`). Do not fake a large title with a text view that slides at a different speed.
- Navigation controls (back, sidebar toggle) stay on the leading side. Primary actions trend trailing. `topBarLeading`, `topBarTrailing`, `bottomBar`, `primaryAction`, and `confirmationAction` placements exist so you do not hard-code edges.
- Group related items. Use system spacing, including flexible space on macOS (`fixedSpace` only when you truly need a fixed gap).
- Overflow extra items into a "more" menu rather than shrinking below a tappable size.
- iOS bottom toolbars are for actions on the current context, not a second tab bar.
- iPadOS toolbars can be more populated and can float. macOS toolbar items are customizable when the app has many. visionOS toolbars often live in an ornament. watchOS toolbars are a few corner actions, not a strip of five icons.
- Scroll edge effects keep titles readable over content. Use `ScrollEdgeEffectStyle` rather than an opaque bar if the platform is using glass.

## Path controls

URL: https://developer.apple.com/design/human-interface-guidelines/path-controls

Platform: macOS. `NSPathControl`.

- A path control shows a filesystem or hierarchy location and lets people jump to an ancestor.
- Use it in toolbars or inspectors of file-based apps. Do not build a fake breadcrumb of buttons on iOS; use the navigation bar.

## Search fields

URL: https://developer.apple.com/design/human-interface-guidelines/search-fields

- A search field is for querying content (`searchable`, `UISearchBar`, `NSSearchField`). Placeholder text says what will be searched ("Search notes"), not "Search".
- Scope bars and tokens narrow results. Tokens represent committed filters and can be removed individually.
- iOS placements: search as a tab (when search is a primary mode), search in the toolbar (pull-down on scroll), or an inline field on the current screen. Pick one.
- iPadOS and macOS: a toolbar search field is typical and can be always visible.
- tvOS: the field is a last resort; pair it with suggestions and a grid of results. watchOS: dictate or scribble a short query; show a few results, not a desktop results page.
- Clear button and cancel behavior follow the system. Do not submit a search that dismisses the keyboard and loses the query accidentally.

## Sidebars

URL: https://developer.apple.com/design/human-interface-guidelines/sidebars

- Sidebars are the top-level map of an iPad, Mac, or visionOS app (`NavigationSplitView` sidebar style, `sidebarAdaptable`).
- Rows are short, with a symbol and a label. Group sources (favorites, library, tags) with headers.
- Selection is persistent and obvious. Selecting a row changes the detail pane; it does not push a mystery modal.
- iOS compact width collapses the sidebar into a stack. The back button or a toolbar toggle returns to it.
- macOS sidebars can be hidden with a standard View menu command and toolbar button. Source lists use the system material and `backgroundExtensionEffect()` when content should show through.
- visionOS sidebars are glass columns in the window, not a screen-edge drawer.
- Do not put destructive actions as sidebar rows.

## Tab bars

URL: https://developer.apple.com/design/human-interface-guidelines/tab-bars

- A tab bar switches between peer top-level sections. `TabView`. On iPhone, it is the primary structure.
- Three to five tabs. If you need more, the last tab can be a "more" or search, or you should move to a sidebar on iPad.
- Each tab has a symbol and a short label. Badges show counts, not marketing.
- The selected tab is persistent across launches unless a notification deep-links elsewhere.
- iOS: the bar can minimize on scroll (`TabBarMinimizeBehavior`) to give content room, then return. Do not hide it with no way back. A bottom accessory (`TabViewBottomAccessoryPlacement`) is for a persistent mini-player or similar, not a second row of tabs.
- iPadOS: tabs may become a sidebar (`sidebarAdaptable`, `tabBarOnly`) as size grows. Support that adaptation instead of locking a phone tab bar in the center of a large display.
- tvOS: the tab bar is a focusable top row. visionOS: tabs live in an ornament.
- Do not use a tab bar for filters inside one section (use a segmented control) or for a flow of steps.

## Token fields

URL: https://developer.apple.com/design/human-interface-guidelines/token-fields

Platform: macOS. `NSTokenField`.

- Tokens represent discrete objects (recipients, tags) inside a field. People can delete a token without clearing the rest.
- Typing filters suggestions. Invalid tokens are visually distinct, not silently dropped.
- Use token fields for many peer values. A single value is a normal text field or pop-up.


<!-- source: components-presentation-input.md -->

# Components: presentation, selection, and input

Official sections:

- https://developer.apple.com/design/human-interface-guidelines/presentation
- https://developer.apple.com/design/human-interface-guidelines/selection-and-input

## Action sheets

URL: https://developer.apple.com/design/human-interface-guidelines/action-sheets

- An action sheet presents choices related to the current action, including destructive ones (`confirmationDialog`, action sheet).
- iPhone: it rises from the bottom. iPad: it anchors as a popover to the control that opened it. Never present an iPhone-style bottom sheet unanchored on iPad.
- Title is a short question only when the buttons are not self-explanatory. Buttons are verbs. Cancel is separate and is the swipe-down or the Cancel button.
- Destructive actions are visually distinct and are not the default.
- watchOS action sheets are full-screen stacks of a few buttons.

## Alerts

URL: https://developer.apple.com/design/human-interface-guidelines/alerts

- Alerts interrupt for an important message or a decision (`alert`, `UIAlertController`, `NSAlert`).
- Title: what happened, in a few words. Message: the consequence or the next step. No title that only says "Error" or "Warning".
- One to three buttons. The safest button is cancel or the default non-destructive action. The destructive button name is the verb (Delete), and it is not placed where people confirm by reflex.
- Do not use an alert for success toasts, validation of a single field, or information that can live inline.
- macOS alerts can include an accessory view and a suppression checkbox ("Do not ask again") only when that choice is safe.
- visionOS alerts stay in the window's space, readable without a head twist.
- Never stack alerts.

## Page controls

URL: https://developer.apple.com/design/human-interface-guidelines/page-controls

- Page controls show position in a small set of horizontal pages (`UIPageControl`, `PageTabViewStyle`).
- Use them for a handful of peer pages (onboarding, gallery). Do not use them for dozens of items; use a scroll position or an index.
- The control is tappable on iOS, not only a passive indicator, unless the pages are the interaction.
- Custom indicator images (`preferredIndicatorImage`) must stay legible at the dot size.
- tvOS and visionOS page indicators follow focus. watchOS uses them sparingly because the Crown already pages.

## Panels

URL: https://developer.apple.com/design/human-interface-guidelines/panels

Platform: macOS. `NSPanel`.

- Panels are auxiliary windows: inspectors, fonts, colors, or HUD overlays. They float above the document when that helps.
- HUD-style panels (`hudWindow`) are dark, transient, and for media or tools over a canvas. Text still has to meet contrast.
- Panels should not be the only place a critical action lives if they can be closed and forgotten. Remember relevant open state.

## Popovers

URL: https://developer.apple.com/design/human-interface-guidelines/popovers

- A popover presents a small related UI anchored to a control (`popover`, `UIPopoverPresentationController`, `NSPopover`).
- It dismisses on outside tap unless a choice must be explicit. Include a close path.
- iPhone compact width usually adapts a popover to a sheet. Design the content to survive that.
- macOS popovers have an arrow pointing at the source. Do not detach them.
- Do not put navigation stacks or large scrolling documents in a popover.

## Scroll views

URL: https://developer.apple.com/design/human-interface-guidelines/scroll-views

- Scroll views move content that does not fit (`ScrollView`, `UIScrollView`, `NSScrollView`). Prefer one primary scroll axis per screen. Nested vertical scroll views fight each other.
- Indicators appear while scrolling. Do not hide them unless the content is a canvas with another position cue.
- Scroll edge effects keep bars readable as content passes underneath. Use the system style (`ScrollEdgeEffectStyle`, `NSScrollEdgeEffectStyle`) instead of a hard opaque mask when you are on the glass design.
- Paging (`PagingScrollTargetBehavior`) is for full-page content, and it should snap cleanly.
- iOS: respect the keyboard inset and the home indicator. Refresh controls live at the top of vertical content.
- macOS: support trackpad, mouse wheel, and keyboard scrolling. Elasticity follows the system.
- tvOS: the remote swipe scrolls; focus may move instead of free-scrolling. Pick one model and keep it predictable.
- visionOS Look to Scroll is a system behavior. Do not disable it and also require a fatiguing drag.
- watchOS: the Digital Crown is the scroller. Content should feel continuous and not paginated unless it is a tab view.

## Sheets

URL: https://developer.apple.com/design/human-interface-guidelines/sheets

- Sheets are modal surfaces for a short task (`sheet`, `UISheetPresentationController`, `presentAsSheet`).
- iOS: use detents (medium, large) when people should see the parent. Show a grabber (`prefersGrabberVisible`) when the sheet can be dragged. Full screen (`fullScreenCover`) is for immersive tasks like a camera or a full editor.
- Toolbar: Cancel leading, confirm trailing, title in the middle when needed. The confirm button is disabled until the form is valid, not hidden.
- Swipe to dismiss is allowed when dismissal cannot lose data, or when you confirm first.
- macOS sheets attach to the parent window and block that window only.
- visionOS sheets stay with the window. watchOS sheets cover the screen and are brief.
- Do not stack sheets more than one deep.

## Windows

URL: https://developer.apple.com/design/human-interface-guidelines/windows

Platforms: iPadOS, macOS, visionOS.

- A window holds one task or one document. Title it. Remember frame and screen.
- iPadOS: support multiple scenes. Drag to create a new window where that helps (`OpenWindowAction`, scene activation). External display is a real window, not a mirror, unless mirroring is the feature.
- macOS anatomy: title bar, toolbar, traffic lights, optional sidebar, content, optional status. States: key, main, miniaturized, full screen, hidden. Restore on relaunch.
- Close means close the window. Quit is separate. Document close prompts only when there are unsaved changes the system is not autosaving.
- visionOS windows are glass planes people place in space. They resize within comfortable limits. Volumes (`VolumetricWindowStyle`) are for 3D objects, not for flat forms. Do not open a pile of windows for one flow.

## Color wells

URL: https://developer.apple.com/design/human-interface-guidelines/color-wells

- A color well shows the current color and opens the system color picker (`UIColorWell`, `UIColorPickerViewController`, `NSColorWell`).
- Use it when color is the value (drawing, themes). Do not use it to pick from three brand colors; use a swatch picker.
- macOS wells support drag-and-drop of colors. Show opacity only if alpha is meaningful.

## Combo boxes

URL: https://developer.apple.com/design/human-interface-guidelines/combo-boxes

Platform: macOS. `NSComboBox`.

- A combo box is a text field plus a list of suggestions. People can type a value that is not in the list, unless you have a reason to reject it.
- If they must pick an existing item, use a pop-up button, not a combo box.
- Filter as they type. Do not open a huge unfiltered menu.

## Digit entry views

URL: https://developer.apple.com/design/human-interface-guidelines/digit-entry-views

Platform: tvOS. `TVDigitEntryViewController`.

- Use the system digit entry view for short codes and PINs. People move focus between digits with the remote.
- Mask secrets. Do not ask for long numeric strings; offer another device to sign in.

## Image wells

URL: https://developer.apple.com/design/human-interface-guidelines/image-wells

Platform: macOS. `NSImageView` as an editable well.

- An image well accepts a dropped or chosen image and shows a thumbnail. Support delete and replace.
- Use it in inspectors (album art, avatars), not as a photo browser.

## Pickers

URL: https://developer.apple.com/design/human-interface-guidelines/pickers

- Pickers choose one value from a known set (`Picker`, `DatePicker`, `UIDatePicker`, `UIPickerView`, `NSDatePicker`).
- Use a wheel or compact date picker for dates. Use a menu-style picker for a short list on iOS. Use navigation-link style when the options need their own screen.
- Do not use a picker for two values; use a segmented control or toggle. Do not use a picker for hundreds of items if search would be faster.
- macOS date pickers can be text fields with a stepper or a calendar. Match the precision you need (date vs time vs both).
- tvOS pickers are focusable lists. watchOS uses the Crown to scrub a picker; keep the set small.

## Segmented controls

URL: https://developer.apple.com/design/human-interface-guidelines/segmented-controls

- A segmented control switches between a few mutually exclusive views or filters (`UISegmentedControl`, `NSSegmentedControl`, `Picker` with segmented style). Two to about five segments.
- Labels or symbols, not both if space is tight, and every segment is clear. Do not mix a filter and an action in one control.
- Momentary segmented controls (`isMomentary`) act as a group of buttons. Use them rarely; a normal segment shows selection.
- iOS segments are for the current screen's content, not top-level app navigation.
- macOS segments can be smaller and can act as radio-like view switchers in toolbars.
- tvOS and visionOS: focus treats the control as one group so left/right or look does not escape accidentally.

## Sliders

URL: https://developer.apple.com/design/human-interface-guidelines/sliders

- Sliders pick a value in a continuous or stepped range (`Slider`, `UISlider`, `NSSlider`). Show the current value if the position is not enough (percent, temperature).
- Label the ends when the meaning is not obvious. Use a step if only discrete values are valid.
- Provide a text field or stepper beside a slider when people need precision, especially on macOS.
- visionOS sliders are look-and-pinch or direct. watchOS sliders are often better as a Crown-driven stepper or a slider that uses the Crown. Do not require a pixel-perfect drag on a watch.

## Steppers

URL: https://developer.apple.com/design/human-interface-guidelines/steppers

- Steppers increment or decrement by a fixed step (`UIStepper`, `NSStepper`). Show the value next to them.
- Use them for small adjustments (quantity, a setting). For a wide range, use a slider or text field.
- macOS steppers attach to text fields. iOS steppers are rare in favor of pickers; use them when the value is visible and the range is modest.
- Hit targets still meet 44 pt. Do not ship two tiny plus and minus glyphs with no padding.

## Text fields

URL: https://developer.apple.com/design/human-interface-guidelines/text-fields

- A text field collects a single-line value (`TextField`, `SecureField`, `UITextField`, `NSTextField`). Multi-line content uses a text view.
- Placeholder is an example or a hint, not the only label. When the field is filled, the label must still be visible (floating label or a label above).
- Use the correct keyboard, content type, and capitalization. Secure fields for passwords.
- Validate gently: inline error under the field, in the error color, with text, not color alone.
- iOS: fields in forms scroll above the keyboard. The return key matches the action (Next, Done, Search, Go).
- macOS: tab order is logical. The default button activates on Return when a text field is focused only if that is expected; otherwise Return inserts a newline in multi-line fields.
- watchOS: prefer dictation or a picker. A text field is for very short input.

## Toggles

URL: https://developer.apple.com/design/human-interface-guidelines/toggles

- A toggle changes a state immediately and shows that state (`Toggle`, `UISwitch`, `NSSwitch`).
- Label is the thing being turned on ("Notifications"), not "Enable notifications: on".
- iOS switches take effect at once. If the change needs a confirmation or a navigation, use a button or a navigation link instead.
- macOS: switches for on/off settings, checkboxes for options that may be mixed (`allowsMixedState`) or that apply on confirm, radio buttons for one choice among a few. Do not use a checkbox as a radio or a switch as a submit button.
- Grouped form style on iOS places the switch trailing in the row.
- Disabled toggles stay visible with their label so people can see the setting exists.

## Virtual keyboards

URL: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards

- Choose `keyboardType` and `textContentType` so the system can offer the right layout and autofill (email, phone, one-time code, new password).
- Return key label (`submitLabel`, `UIReturnKeyType`) matches the action.
- Do not block the field with the keyboard. Scroll or raise the field. Add a toolbar above the keyboard (`ToolbarItemPlacement.keyboard`) for Next, Previous, or Done when the form needs it.
- Custom input views replace the keyboard only for specialized data (dates, quantities) and still need a dismiss path.
- Custom keyboards are a system-wide feature, not an in-app reskin. In-app, prefer a custom input view.
- Clicks: if you play keyboard clicks, use the system click (`playInputClick`) so the user's keyboard sound setting is honored.
- tvOS text entry is slow; offer alternatives. visionOS keyboard can be direct or indirect; do not force direct typing. watchOS uses the system scribble, dictation, or callout keyboard, not a custom QWERTY.


<!-- source: components-status-system.md -->

# Components: status and system experiences

Official sections:

- https://developer.apple.com/design/human-interface-guidelines/status
- https://developer.apple.com/design/human-interface-guidelines/system-experiences

## Activity rings

URL: https://developer.apple.com/design/human-interface-guidelines/activity-rings

Platforms: iOS, iPadOS, watchOS. `HKActivityRingView`.

- Activity rings are Apple's Move, Exercise, and Stand glyphs. Use the system view. Do not redraw the rings, recolor them, or use them as a generic progress spinner.
- Do not use ring artwork for non-activity data. For other progress, use a progress indicator or a gauge.
- On iPhone, rings are a summary that opens Fitness or your activity detail. On Apple Watch they are glanceable and accurate to HealthKit.

## Gauges

URL: https://developer.apple.com/design/human-interface-guidelines/gauges

- A gauge shows a scalar in a range (`Gauge`, `NSLevelIndicator`): current value, minimum, maximum, optional label and style (linear, circular).
- Use it for levels (battery, capacity, speed), not for multi-step tasks (that is a progress indicator).
- Label the value. Color can mark zones (normal, warning) and must not be the only encoding.
- macOS level indicators can be continuous, discrete, or rating-like. Pick the capacity style that matches the data.
- watchOS circular gauges belong in complications and workout views and stay readable at a glance.

## Progress indicators

URL: https://developer.apple.com/design/human-interface-guidelines/progress-indicators

- Determinate (`ProgressView` with a fraction, `UIProgressView`, bar style `NSProgressIndicator`) when you know the proportion. Indeterminate (spinner, spinning `NSProgressIndicator`) when you do not.
- Place the indicator next to the work. A full-screen blocker is for tasks that truly prevent interaction.
- Update smoothly. Jumping from 0 to 100 looks broken. If you cannot estimate, use indeterminate instead of a fake percent.
- iOS refresh control (`UIRefreshControl`) is the pull-to-refresh pattern. Do not add a second refresh button unless pull is unavailable.
- macOS: a spinner in a button or a bar in a sheet, sized to the context. The spinning beach-ball is the system's, not yours to imitate.
- watchOS: small spinner or a ring that does not impersonate Activity rings.
- When finished, remove the indicator and show the result. On failure, show a message and retry.

## Rating indicators

URL: https://developer.apple.com/design/human-interface-guidelines/rating-indicators

Platform: macOS.

- A rating indicator shows or edits a score, typically stars. Use the system control.
- If the rating is editable, the hit target covers each step and the value is announced to accessibility.
- Do not use stars as a decoration for "favorites" if a toggle would be clearer.

## App Shortcuts

URL: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts

- App Shortcuts are a few high-value actions Siri and Spotlight can run without setup (`AppShortcut`, App Intents).
- Phrases sound like something a person would say. Follow the editorial rules: include the app name where required, no trademark abuse, no deceptive phrase.
- The action should complete or ask a short follow-up. Deep parameter grids do not belong in a shortcut.
- Provide a visible in-app path to the same action. A shortcut is not the only entrance.
- Responses are concise. Use snippets and dialog for results, not a dumped view controller.
- iOS may show a Siri tip (`SiriTipUIView`) once. macOS shortcuts appear in Spotlight and the menu bar where appropriate.

## Complications

URL: https://developer.apple.com/design/human-interface-guidelines/complications

Platform: watchOS. Build with WidgetKit accessory families, not the legacy ClockKit templates, unless you are maintaining an old build.

- A complication is a glance that launches the app. One datapoint, updated honestly.
- Families: circular, corner, inline, rectangular. Design each you support. Content must still make sense if the tint flattens color (`WidgetRenderingMode`).
- Provide a placeholder (`placeholder(in:)`) so the gallery can show your complication before data loads.
- Do not animate. Do not cram a sentence into an inline slot.
- Legacy ClockKit templates (circular small, modular small, modular large, extra large) exist only for older faces. New work targets the modern accessory families.
- Tapping opens the relevant screen, not the app's root if a deeper screen is the point.

## Controls

URL: https://developer.apple.com/design/human-interface-guidelines/controls

Platforms: iOS, iPadOS, macOS. These are Control Center / Lock Screen controls, not generic buttons.

- A control does one action or shows one toggle people need without opening the app. Think flashlight, not a settings page.
- Use SF Symbols and a short name. Symbol effects can show state. Follow `promptsForUserConfiguration()` if the control needs a target (which device, which scene).
- Authentication policy (`IntentAuthenticationPolicy`) must match the sensitivity. Do not unlock a door from the Lock Screen without the right policy.
- Camera experiences on a locked device use Locked Camera Capture and stay inside that system's rules.
- The control and the in-app feature must agree. Do not offer a control for a feature the app hides.

## Live Activities

URL: https://developer.apple.com/design/human-interface-guidelines/live-activities

Platforms: iOS, iPadOS, macOS, watchOS. ActivityKit.

Presentations:

- **Compact** on the Lock Screen / Dynamic Island leading and trailing. A symbol and a short value.
- **Minimal** when more than one activity is active. Still recognizable.
- **Expanded** long-press or when the island expands. More detail, a small set of actions.
- **Lock Screen** banner: the fullest layout, still a glance, not a mini app.
- **StandBy** nightstand: large, calm, high contrast, readable from a distance.

Rules:

- Start a Live Activity for an ongoing real-world event (delivery, ride, game, timer). End it when the event ends. Do not use one as an ad slot.
- Update on meaningful changes. Stale data destroys trust.
- Colors work on light and dark and in tinted island styles. Use `activitySystemActionForegroundColor` and semantic colors.
- Actions are few and optional. They use buttons that fit the presentation, not a form.
- Layouts differ by platform. Check the spec tables for CarPlay, iOS, iPadOS, macOS, and watchOS dimensions before hard-coding frames. Use padding and `ContainerRelativeShape` so content follows the corner radius.
- Transitions between presentations animate layout, not a unrelated graphic.
- watchOS and macOS presentations are summaries. Do not expect the expanded iPhone layout to fit.

## Notifications

URL: https://developer.apple.com/design/human-interface-guidelines/notifications

- Anatomy: title, body, optional attachment, actions, and a badge. Title names the source or the event. Body is one or two lines of useful detail.
- Ask permission in context. See Managing notifications.
- Actions are verbs and few (two to four). Destructive actions confirm if needed.
- Badges are counts of things to do, cleared when the person deals with them. Do not badge for marketing.
- Group threads. A message notification can carry a conversation (`INSendMessageIntent` style summaries) so previews stay private when the system hides them (`hiddenPreviewsBodyPlaceholder`).
- Rich notifications (`UserNotificationsUI`) add a small custom view, not a second app.
- Sounds are short and optional. Honor silent mode.
- watchOS: a short look is a glance and a haptic; a long look appears if they linger and can include actions. Double tap can trigger the primary action. Design the short look first.
- tvOS notifications are rare and unobtrusive.

## Snippets

URL: https://developer.apple.com/design/human-interface-guidelines/snippets

Platforms: iOS, iPadOS, macOS. App Intents snippets.

- A snippet is the small visual result of a shortcut or Siri action. It shows the outcome, not a tour of the app.
- Anatomy is a title, a few facts, and optional buttons. Confirmations use the system confirmation style (`ConfirmationActionName`) for anything hard to undo.
- The snippet and the spoken dialog must agree. Do not show a success snippet while the dialog says it failed.
- Keep it static and fast. No scrolling dashboards.

## Status bars

URL: https://developer.apple.com/design/human-interface-guidelines/status-bars

Platforms: iOS, iPadOS.

- The status bar (time, signal, battery) is system UI. Do not cover it, recolor it so it becomes illegible, or draw a fake one.
- Choose a style (`preferredStatusBarStyle`, or the scroll edge effect) that contrasts with the content underneath. Light content needs a dark status bar text and the reverse.
- Hide it only for temporary media or capture, and bring it back.
- Scroll edge effects (`UIScrollEdgeEffect`, `ScrollEdgeEffectStyle`) can place content under the status bar while keeping the bar readable. Test both appearances.

## Top Shelf

URL: https://developer.apple.com/design/human-interface-guidelines/top-shelf

Platform: tvOS.

- Top Shelf is the banner above your app icon on the Apple TV Home Screen. It should show fresh, personal, or featured content, not a static logo.
- Layouts: carousel actions, carousel details, and a sectioned content row. Item styles include poster (2:3), square (1:1), 16:9, and scrolling inset banner. Use the style that matches the artwork you actually have.
- Every item is selectable and opens that item, not a generic home screen.
- Update content so the shelf does not advertise something unavailable.

## Watch faces

URL: https://developer.apple.com/design/human-interface-guidelines/watch-faces

Platform: watchOS.

- Most apps do not ship a watch face. If you share a face, use the system sharing flow.
- Do not attempt to draw over or replace the watch face. Your surface is complications, widgets, and notifications.
- Face sharing includes your complications only in the ways the system allows. Do not imply a face is required to use the app.

## Widgets

URL: https://developer.apple.com/design/human-interface-guidelines/widgets

Platforms: iOS, iPadOS, macOS, watchOS, visionOS. WidgetKit.

### Families

- System families: small, medium, large, extra large on iPad. Design each size you declare. Small is one idea. Large can be a short list, not an app UI.
- Accessory widgets on watchOS and the Lock Screen follow the complication families and must work in tinted rendering.

### Content

- Show current, personal, useful data. Tap opens the exact place in the app.
- Update on a timeline that matches how fast the data changes. Do not refresh constantly.
- Interactivity is limited to the widget interactions the system supports (buttons and toggles that run intents). No scrolling, no text fields, no navigation stacks inside the widget.
- Margins: use the system content margins. Additional padding is `padding` inside that, not a second inset that makes small widgets look empty. Text uses system styles and can grow; do not fixed-frame a sentence.
- Color: support full color, accented (tinted) rendering, and vibrant Lock Screen rendering (`WidgetRenderingMode`). In accented and vibrant modes the system washes your palette. Use the widget accent and vibrancy APIs rather than hard-coded white.
- Placeholders and previews in the gallery use sample data that looks real, with no personal data and no "Lorem".

### Platform notes

- iOS and iPadOS: Home Screen, Lock Screen, StandBy, and CarPlay where relevant. StandBy is large and distant; use big type and few elements.
- visionOS: widgets mount in the room. Respect the documented thresholds, sizes, mounting styles, and treatments. A widget is not a window and does not use ornaments.
- watchOS: widgets in the Smart Stack are glances. One primary value.
- Read the current dimension tables on the official page before locking a custom drawing canvas. Prefer flexible SwiftUI layouts over absolute frames.


<!-- source: inputs.md -->

# Inputs

Official section: https://developer.apple.com/design/human-interface-guidelines/inputs

Prefer the platform's primary input. Always leave a second path for accessibility.

## Action button

URL: https://developer.apple.com/design/human-interface-guidelines/action-button

Platforms: iOS (Action button on supported iPhones), watchOS (side button / action button behaviors).

- The hardware Action button is user-assigned. Your app can offer an action, not claim the button exclusively.
- The action should be immediate and useful from the Lock Screen or wrist: start a workout, toggle a mode, open capture. Not a settings page.
- iOS: integrate through the system control or shortcut model so people assign it themselves.
- watchOS: the side button and action gestures belong to the system first. App actions use the APIs Apple exposes for that hardware, and they never block SOS or system presses.

## Apple Pencil and Scribble

URL: https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble

Platform: iPadOS.

- Pencil is a first-class pointer plus a drawing tool. Support hover (preview before the mark), double tap (switch tools, system default is eraser or last tool), squeeze (show a tool palette or shortcuts on supported pencils), and barrel roll (rotate the tool when the tool has an orientation, such as a calligraphy nib).
- Scribble turns handwriting into text in any text field. Do not ship a custom field that blocks `UIScribbleInteraction` / `UIIndirectScribbleInteraction` unless the surface is a drawing canvas.
- Custom drawing uses PencilKit or your own canvas. Palm rejection and low latency are required. Tools (pen, pencil, eraser, lasso) should feel like the system apps.
- Hover previews must not commit a change until the tip touches.
- Provide a finger path for people who are not using a pencil, except tools that are inherently a stroke.

## Camera Control

URL: https://developer.apple.com/design/human-interface-guidelines/camera-control

Platform: iOS devices with the Camera Control.

- Camera Control is a physical control for capture: click to launch or shutter, light press for a preview, slide to change a setting.
- If you are a camera app, adopt `AVCaptureControl` and the system overlay rather than inventing a gesture on the same edge.
- Controls you expose (zoom, exposure, depth) use the system UI. Names are localized. `prominentValues` are the detents people can feel.
- Locked-camera capture (`LockedCameraCapture`) is for shooting without fully unlocking. Stay inside that flow and do not leak photos to the Lock Screen.
- Do not remap Camera Control to a non-capture action if the person expects a camera.

## Digital Crown

URL: https://developer.apple.com/design/human-interface-guidelines/digital-crown

Platforms: watchOS, visionOS.

- **Apple Watch.** The Crown scrolls, zooms, and scrubs. Use `WKCrownDelegate` or SwiftUI focus. Haptic detents mark steps in a picker. Do not also require a tiny drag for the same scroll.
- **Apple Vision Pro.** The Crown adjusts immersion or volume in experiences that opt in. Do not steal it for an unrelated in-app slider if the system is using it for immersion.
- Crown rotation is continuous and precise. Click is a separate, deliberate action. Do not fire a destructive command on a small rotation.

## Eyes

URL: https://developer.apple.com/design/human-interface-guidelines/eyes

Platform: visionOS.

- People target UI by looking at it. The system shows hover. You do not draw your own gaze cursor.
- Make targets large enough and separated enough that a glance does not select the neighbor.
- Hover is a preview, not a commit. Commit happens on pinch (indirect) or touch (direct).
- Custom hover effects are subtle: highlight, raise, or scale slightly. No flashing, no large motion, no reading "they looked, so start the video" without an intentional selection.
- Never infer attention, emotion, or identity from gaze. Do not store gaze. Do not highlight private content because someone glanced at it.
- If eyes cannot be used, the same controls still work with pointer and accessibility inputs.

## Focus and selection

URL: https://developer.apple.com/design/human-interface-guidelines/focus-and-selection

Platforms: iPadOS, macOS, tvOS, visionOS.

- Focus is which item receives input. Selection is which items are chosen. They are not always the same. On tvOS, focus is the primary cursor. On macOS, focus follows the key view and selection can be a multi-row highlight.
- Focus movement is spatial and predictable: next item in the direction pressed. Do not skip randomly.
- tvOS focus effects (scale, parallax, `UIFocusHaloEffect`) are system-driven. Every interactive view participates. Non-interactive decoration does not take focus.
- Group related controls (`focusGroupIdentifier`, `UIFocusGroupPriority`) so the remote does not wander through every glyph.
- iPadOS pointer focus and keyboard focus (Full Keyboard Access) must land on the same actions.
- visionOS focus follows the eyes. Selection is the pinch. Do not show a second focus ring that fights the system hover.
- Restore focus after a sheet closes, back to the control that opened it.

## Game controls

URL: https://developer.apple.com/design/human-interface-guidelines/game-controls

- Touch controls: thumbs reach them, they do not cover the playfield, and they can be moved or resized if the game is deep. Use `TouchController` patterns where you want system-like on-screen controls.
- Physical controllers: support Game Controller (`GCControllerElement`). Standard buttons keep their meanings (A confirm, B back, menu opens pause). Do not swap confirm and back.
- Publish controller glyphs that match the attached hardware, not a single Xbox-shaped diagram.
- Keyboards: support WASD or arrows and a pause key when the Mac or iPad has a keyboard. Do not require a controller (`GCRequiresControllerUserInteraction` only if the game truly cannot be played otherwise, and say so).
- visionOS: gaze and pinch can aim, but do not force uncomfortable gestures. Offer a controller.

## Gestures

URL: https://developer.apple.com/design/human-interface-guidelines/gestures

Standard gestures are a shared language. Do not change what they mean.

Common mappings to respect:

- Tap: activate the target.
- Long press: context menu or lift for drag, not a secret primary action.
- Swipe: delete, reveal actions, back (from the leading edge), or scroll.
- Pan or drag: move content or an object.
- Pinch: zoom. Rotate: rotate the object, not the whole app.
- Edge swipe from the leading edge: back on iOS. Edge swipe from the bottom: home. You may defer the home indicator only briefly for full-screen content, with another way out (`preferredScreenEdgesDeferringSystemGestures`).

Custom gestures:

- Only when no standard gesture expresses the idea.
- They must be discoverable (a hint or a visible control) and must have a non-gesture alternative.
- They do not override system edges.

Platform notes:

- iOS and iPadOS: the gestures above. Multi-touch is for drawing and zoom, not for secret chords.
- macOS: clicks, secondary click, scroll, pinch on a trackpad. Do not require a touch-only gesture.
- tvOS: remote click, swipe on the touch surface, and play/pause. See Remotes.
- visionOS: indirect (look + pinch, look + pinch and drag, look + two-hand zoom) and direct (touch, touch and hold, drag, swipe, two-hand zoom and rotate). Prefer indirect for UI. Custom hand gestures require a Full Space, permission, and an alternative that does not need a specific body pose.
- watchOS: tap, firm press where still supported, swipe, and double tap (finger pinch) for the primary action. Double tap is system-level; your primary action should be the one you want it to trigger.

## Gyroscope and accelerometer

URL: https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer

- Motion is an enhancement, not the only way to do a task. Shaking to undo is a system text behavior; do not add more shake commands.
- Use Core Motion for games, level tools, and fitness, with a calibration step if orientation matters.
- Do not require people to spin or tilt a device in public for an ordinary UI action.
- Honor motion permission and Low Power Mode. Stop updates when the screen is off or the feature is not visible.
- Provide a manual control (sliders, buttons) as a fallback.

## Keyboards

URL: https://developer.apple.com/design/human-interface-guidelines/keyboards

- Every interactive element is reachable by keyboard on macOS, iPadOS, and visionOS. Tab order follows reading order.
- Standard shortcuts must work: Command-C/V/X/Z/A/S/W/Q, Command-comma for Settings, Space for the default button where the platform does that. Show shortcuts in menus (`KeyboardShortcut`, `discoverabilityTitle`).
- Custom shortcuts do not override system or common ones. Prefer Command plus a letter. Document them in the menu, not only in a help page.
- Full Keyboard Access (`isFullKeyboardAccessEnabled`) users navigate with Tab even on iPhone. System controls support this; custom hit targets need focusability.
- visionOS: a hardware keyboard can be paired. Do not assume pinch is available the moment a keyboard is attached.
- Avoid shortcut collisions across contexts. When a text field is focused, single-key shortcuts must not fire.

## Nearby interactions

URL: https://developer.apple.com/design/human-interface-guidelines/nearby-interactions

Platforms: iOS, iPadOS, watchOS. Nearby Interaction framework.

- Nearby interaction is for precise ranging and direction between devices (find a friend, point at a HomePod, handoff). It is not a generic radar toy.
- Ask in context. Explain that the devices need to be close and that UWB or direction is involved. If permission is denied, offer a non-directional fallback (name, beep, manual pick).
- UI: a simple direction cue and distance. Do not show a map of strangers. Do not identify people who have not opted in.
- iPhone can point; Apple Watch can confirm proximity with haptics. Keep the watch UI to a direction and a success state.
- Stop the session when the task ends. Do not range in the background for marketing.

## Pointing devices

URL: https://developer.apple.com/design/human-interface-guidelines/pointing-devices

Platforms: iPadOS, macOS, visionOS. iOS supports pointers when a trackpad is attached.

- Pointers are precise. Hover can reveal tooltips, highlight buttons, and show pointer effects. Hover must not be required to discover a primary action.
- iPadOS pointer: the system cursor adapts (circle, rounded rect, beam). Use pointer effects and magnetism (`UIPointerAccessory`, `roundedRect`) so the cursor snaps to controls. Standard shapes (arrow, closed hand, crosshair, drag copy, drag link, contextual menu) should keep their meaning.
- macOS cursors change with the tool (arrow, I-beam, resize, crosshair). Set the cursor on the view that owns the tool, and reset it on exit. Do not hide the cursor unless you are in full-screen video and it returns on move.
- visionOS pointers exist for trackpads and accessibility. Eyes remain the default target. Pointer and eye targets must match.
- Band selection (`UIBandSelectionInteraction`) is for dragging a rectangle around items, typical on iPad and Mac. Provide shift-click and command-click selection too.
- Right-click or secondary click opens the context menu. Left click activates.

## Remotes

URL: https://developer.apple.com/design/human-interface-guidelines/remotes

Platform: tvOS.

- The remote is the only input you should require. Click selects the focused item. Menu or Back moves up the hierarchy. The TV button goes Home; do not capture it.
- Touch surface: swipe to move focus or scrub. Do not invent multi-finger remote gestures.
- Play/pause controls media. Volume is the system.
- Siri Remote and compatible game controllers should work. If you support a controller, the focus model still works with the remote.
- Always show where focus is. A remote with no visible focus is unusable from the couch.


<!-- source: technologies.md -->

# Technologies

Official section: https://developer.apple.com/design/human-interface-guidelines/technologies

Branded technologies have artwork and wording rules. Use the system button or the official asset. Do not redraw logos. Open the official page before shipping Apple Pay, Sign in with Apple, HomeKit, AirPlay, Activity, or Wallet visuals.

## AirPlay

URL: https://developer.apple.com/design/human-interface-guidelines/airplay

- Use the system route picker or `AVPlayerViewController` so AirPlay targets, audio, and video behave correctly.
- If you draw the icon yourself, use Apple's AirPlay icon (black, white, or a single custom color on a clear background). Do not recolor pieces differently, add shadows, or rotate it.
- Say "AirPlay", not "Airplay" or "air play". Say "AirPlay Audio" or "AirPlay Video" only in the way the branding page allows.
- Video can play externally (`usesExternalPlaybackWhileExternalScreenIsActive`). The in-app UI should show that playback moved, with a way to bring it back.
- Do not auto-route to a nearby TV without an explicit choice.

## Always On

URL: https://developer.apple.com/design/human-interface-guidelines/always-on

Platforms: iOS StandBy / Lock Screen and watchOS always-on display.

- The dimmed, wrist-down, or nightstand state is still your UI. Information must remain correct and legible at lower brightness.
- Remove or freeze decorative motion, video, and high-brightness fills. Redact secrets (message bodies, balances) the way the Lock Screen does when the system is locked.
- Update rarely. A ticking animation that keeps the display hot is a bug.
- Provide a layout that works when color is reduced and the screen is dim.

## App Clips

URL: https://developer.apple.com/design/human-interface-guidelines/app-clips

Platforms: iOS, iPadOS.

- An App Clip does one task immediately (pay, order, unlock) and finishes in seconds. No account wall, no onboarding carousel.
- The card is the invitation: a short title, a specific action, and your real app icon. The image and text must match the physical place or QR the person just used.
- Preserve privacy. Do not request tracking. Ask for location or notifications only if that invocation needs them, and notifications from a clip are rare.
- Offer the full app at the end with `SKOverlay`, not a modal nag at the start.
- App Clip Codes use Apple's code design. Keep the required clear space, test the printer's calibration, and use the messaging patterns on the official page. Do not redraw the code or add a logo inside the mark.
- Business clips that take payment use Apple Pay where it fits.

## Apple In-App Purchase

URL: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase

- Use StoreKit UI for purchases, offer-code redemption, refunds, and subscription management (`presentOfferCodeRedeemSheet`, `showManageSubscriptions`, `beginRefundRequest`). Do not send people to a website to buy digital goods the guidelines require to go through IAP.
- Show the price the system returns, including introductory and trial terms, before the person confirms. The system sheet is the confirmation.
- Family Sharing: if the product supports it, say so. Do not promise sharing for a product that is not set up for it.
- Subscriptions: explain what they get, the length, and that it renews. Manage and cancel are available in-app via the system manage-subscriptions UI.
- Restore purchases is available and not hidden. Help for billing problems points at Apple's billing, not a custom blame screen.
- watchOS purchases can confirm on the watch or route to iPhone. Do not build a long storefront on the watch.

## Apple Pay

URL: https://developer.apple.com/design/human-interface-guidelines/apple-pay

- Offer Apple Pay as a payment method alongside others, not as a banner that blocks checkout. If they cannot pay, follow `applePayCapabilities` and show Set Up only when setup is the real next step.
- Use the official Apple Pay button (`PKPaymentButton` / the web equivalent). Types include plain Apple Pay and Set Up Apple Pay. Styles are black, white, and white with outline. Do not change the logo, set a non-approved corner radius, or stretch the mark.
- Minimum size and clear space are on the official page. The button is at least as prominent as other checkout buttons.
- The payment sheet is the system sheet (`PKPaymentAuthorizationController`). You customize line items (`paymentSummaryItems`), shipping, and contact fields. You do not rebuild the sheet.
- Put the most likely shipping and contact defaults in the sheet so checkout is a confirm, not a form.
- Errors: data problems name the field; processing problems say the charge failed and that they can try another method. Do not dump gateway codes.
- Subscriptions and donations have specific button and sheet setups. Use the donation wording only for real donations.
- Say "Apple Pay", not "ApplePay". Do not say "Apple Pay" for a payment that does not use it.
- The Apple Pay mark (not the button) is for marketing placements described on the page. Do not invent a third graphic.

## Augmented reality

URL: https://developer.apple.com/design/human-interface-guidelines/augmented-reality

Platforms: iOS, iPadOS, visionOS. ARKit.

- AR shows virtual content in the real world. People must understand what is real. Do not occlude hazards.
- Coach placement (`ARCoachingOverlayView`) until tracking is good enough. Tell them to move the device slowly if you need a surface.
- Placement: a preview of the object follows the ray (`ARTrackedRaycast`) before they commit. Objects sit on the detected plane with believable scale and occlusion.
- Interactions: direct (tap the object) and simple. Pinch to scale only if the object should resize. Provide a reset.
- Multiuser (`isCollaborationEnabled`) shows who is here and what they are moving. Do not share camera frames silently.
- Interruptions (phone call, backgrounding) pause the session and tell them when tracking is lost, with a concrete fix (more light, slower motion).
- Icons: use the system AR mark when you label an AR action. visionOS immersive experiences follow the immersive page; do not also slap an AR badge on ordinary windows.

## CareKit

URL: https://developer.apple.com/design/human-interface-guidelines/carekit

Platforms: iOS, iPadOS.

- CareKit apps handle health tasks, charts, and contacts. Be calm, clear, and honest. This is not a place for playful error copy.
- Data and privacy: say what you store and why. HealthKit access uses the Health permission model and only the types you need. Motion and photos are separate asks, in context.
- Use CareKit task cards for "to do" care items: title, schedule, completion. Charts use the CareKit chart styles so trends are readable. Contact views make the care team reachable.
- Notifications for a dose or exercise are timely and specific, and easy to turn off.
- Use CareKit symbols as designed. Do not remix the mark into a logo.

## CarPlay

URL: https://developer.apple.com/design/human-interface-guidelines/carplay

Platform: iOS via the car display. CarPlay is a driving UI, not a phone UI stretched wide.

- Information is glanceable. Type is large. Actions are few and available without precise taps. No reading, no dense settings, no video.
- Audio apps: now playing, playlists, and simple lists. Navigation and communication follow the CarPlay templates for that category. You cannot invent a freeform layout.
- Color supports glanceability and Dark appearance. Icons are simple.
- Errors say what to do in the car ("Connect iPhone") in one line.
- The iPhone may show a companion state, but the driver interacts with the car screen. Do not require looking at the phone to complete a driving task.
- Follow the entitlement and template rules for your category. Unsupported apps do not belong on the car display.

## Game Center

URL: https://developer.apple.com/design/human-interface-guidelines/game-center

- Access Game Center with the system access point. A custom UI still has to offer the same sign-in and profile actions, and it must not mimic the system UI in a misleading way.
- Achievements: a clear name, a description of how to earn it, and artwork in the required template. Show progress for incremental achievements. Do not create achievements for spending money.
- Leaderboards: say what the score means and the time scope. Let people view friends and global when you have both. Do not shame a low score with custom chrome.
- Challenges and multiplayer use the system flows so invites and turns are consistent.
- tvOS and watchOS surfaces are reduced. A leaderboard on the watch is a summary, not a full browser.

## Generative AI

URL: https://developer.apple.com/design/human-interface-guidelines/generative-ai

- Say when content is generated. Do not present model output as a human's work, a measurement, or a fact you verified.
- Describe what the feature does in the UI, not the model brand, unless attribution is required.
- Privacy: prefer on-device (`FoundationModels`) when it meets the need. If data leaves the device, say so before it happens. Do not use private content to train a model without explicit permission.
- Inputs: show what the person is sending. Let them edit or cancel. Do not silently attach contacts, photos, or location.
- Outputs: make them editable, copyable, and dismissible. Offer a way to try again or report a bad result. Do not auto-post or auto-send.
- Mistakes are normal. Do not show a single generated answer as the only path for a high-stakes decision (health, finance, safety). Provide a non-generated way to finish the task.
- Continuous improvement (feedback, ratings on results) is opt-in and specific.

## HealthKit

URL: https://developer.apple.com/design/human-interface-guidelines/healthkit

Platforms: iOS, iPadOS, watchOS.

- Request only the sample types you need, when the person uses that feature (`requestAuthorization`). Explain the benefit in your words, then let the system sheet list the types.
- If they deny access, the feature degrades honestly. Do not re-prompt in a loop.
- Activity rings: use `HKActivityRingView` only for real Move, Exercise, and Stand data. See Activity rings.
- The Apple Health icon is used only to refer to the Health app, following the artwork rules. Do not modify it or imply Health endorses your product.
- Write copy that is careful and not diagnostic unless you are qualified and permitted. "A high heart rate reading" is not "You are having a heart attack."
- Clinical and sensitive types deserve extra clarity about storage and sharing.

## HomeKit

URL: https://developer.apple.com/design/human-interface-guidelines/homekit

- Use HomeKit words the way the Home app does: homes, rooms, accessories, services, characteristics, actions, scenes, automations, zones.
- Setup uses the system accessory setup (`performAccessorySetup`). Names should be speakable ("Kitchen lamp"), because Siri uses them.
- Do not invent a parallel house model that drifts from the Home database.
- Cameras: show a live view with clear recording state. Do not hide that a camera is recording.
- Icons: black, white, or single-color HomeKit badge from Apple's artwork. Say "HomeKit" and "the Home app" correctly. Works with Apple Home is a specific badge; do not paraphrase it into a custom seal.
- Actions must show success or failure. A light that did not turn on is not a silent no-op.

## iCloud

URL: https://developer.apple.com/design/human-interface-guidelines/icloud

- If the feature needs iCloud, say so and send people to the system sign-in if they are signed out. Do not build a fake iCloud login.
- Documents and data in iCloud show sync state: synced, syncing, conflict, or full. Conflicts are resolvable, not silently overwritten.
- Storage-full errors tell them what failed and link toward managing storage.
- Games that save progress use the system game-save patterns (`GameSave`) or CloudKit with a visible account. Progress should not vanish on reinstall if you promised cloud save.
- Key-value and CloudKit data still follows privacy rules. Do not sync secrets that belong in the keychain unencrypted.

## ID Verifier

URL: https://developer.apple.com/design/human-interface-guidelines/id-verifier

Platform: iOS.

- Request only the claims you need (for example age over a threshold via `ageAtLeast`) rather than a full license dump.
- Use the system presentation (`MobileDriversLicenseDisplayRequest`, data request, or raw data request as appropriate). The person sees what will be shared and can refuse.
- Do not store document images or raw data "just in case" if a boolean claim was enough.
- Explain why you are checking, in one sentence, before the system sheet.

## iMessage apps and stickers

URL: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers

Platforms: iOS, iPadOS.

- An iMessage app is used inside a conversation. The UI is compact, fast, and returns to the transcript.
- Stickers are expressive and respect the size classes (`MSStickerSize`). Edges are clean. No tiny unreadable text.
- App icons for the iMessage drawer follow the sticker and iMessage icon sizes on the spec page.
- Do not trap people in a store. Sending a sticker should feel like one tap.
- Respect the conversation's participants. Do not auto-send.

## Live Photos

URL: https://developer.apple.com/design/human-interface-guidelines/live-photos

- Play a Live Photo on press or hover, not in a loop on a static grid. People expect a still until they interact (`PHLivePhoto`).
- Mark Live Photos with the system badge so they are distinct from stills.
- Edits should keep or clearly discard the motion. Do not export a still and still call it a Live Photo.
- visionOS can present a Live Photo spatially when the asset supports it. Do not fake spatial from a normal photo.
- Web uses LivePhotosKit JS only with the system playback behavior.

## Mac Catalyst

URL: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst

- Decide the idiom up front: "Optimize Interface for Mac" or a scaled iPad idiom. Optimized Mac is the one that should feel like a Mac.
- Navigation: sidebars and split views, not a phone tab bar stretched across a monitor. Multiple windows for documents.
- Inputs: pointer hover, keyboard shortcuts (`UIKeyCommand`), and menus (`UIMenuBuilder`, `UICommand`). Right-click context menus.
- App icon is a Mac icon, not a rounded iOS icon sitting on a squircle you drew.
- Layout: use the Mac toolbar and settings window. Density can increase. Touch-sized padding everywhere looks wrong on a Mac, but do not go so dense that rows are hard to click.
- Settings live under the App menu (Settings…), not inside a tab called Settings if you can use a settings scene.

## Machine learning

URL: https://developer.apple.com/design/human-interface-guidelines/machine-learning

Design the role before the model:

- Critical vs complementary: if the model is wrong, can the person still finish? Critical predictions need confirmation.
- Private vs public: on-device (`Core ML`, Create ML) is the default for personal data.
- Proactive vs reactive: proactive suggestions can be ignored. Do not pop a modal for a guess.
- Visible vs invisible: invisible corrections (autocorrect) need an undo. Visible suggestions need a reason when they affect a decision.
- Dynamic vs static: if the model changes, the UI should not jump under the person's finger.

Feedback and trust:

- Explicit feedback (correct / not useful) and implicit feedback (they edited the suggestion) should actually update behavior you claim updates.
- Calibration: show confidence only if people can interpret it. A raw percentage is often worse than "likely" plus an easy override.
- Mistakes: apologize by fixing, not by a cute error. Always offer correction and a manual path.
- Multiple options beat a single opaque answer when taste or ambiguity is involved.
- Attribution: say when a prediction is automatic. Limitations belong in the UI for features that can harm (health, finance, people detection), not only in a privacy policy.

## Maps

URL: https://developer.apple.com/design/human-interface-guidelines/maps

- Use MapKit. Do not screenshot Apple Maps. Respect the legal attribution MapKit already shows; do not cover it.
- Standard gestures: pan, zoom, rotate. Do not disable them unless the map is a static figure, and then consider an image.
- Annotations (`MKAnnotationView`) are for a few places, not thousands of raw pins. Cluster. The selected pin shows a callout with a title and one action.
- Overlays (`MKOverlayLevel`) match the data (route, geofence). Do not paint the whole map a brand color.
- Place cards: use the system place card for a POI (`mapItemDetailSelectionAccessory`, selection accessory APIs) instead of a custom business page that hides hours, phone, and directions.
- Indoor maps: show the level the person is on and a level picker.
- watchOS maps are simplified and for a glance or a turn, not a browsing map.
- Privacy: show the location indicator only while location is in use, and use the system authorization styles.

## NFC

URL: https://developer.apple.com/design/human-interface-guidelines/nfc

Platforms: iOS, iPadOS. Core NFC.

- In-app reading: show a system session sheet that says what to scan and when it succeeds or fails. Keep the phone message aligned with the real tag.
- Background tag reading launches your app only for tags you are entitled to read. The launch should land on that tag's task, not the home screen.
- Do not scan in the background for unrelated traffic. Failures ("tag moved", "not supported") tell them to try again in plain language.

## Photo editing

URL: https://developer.apple.com/design/human-interface-guidelines/photo-editing

Platforms: iOS, iPadOS, macOS. PhotoKit.

- Non-destructive edits are the default. People can revert. Show that an image has adjustments.
- The original stays in the library unless they explicitly export a flattened copy. Respect edits from other apps (adjustment data).
- Tools are familiar: crop, light, color, filters. Destructive actions (delete) confirm.
- Extensions that edit inside Photos should feel like a focused tool and return to Photos when done.
- Do not upload a library to train a model because the person cropped one photo. Ask if a feature needs the image to leave the device.

## ResearchKit

URL: https://developer.apple.com/design/human-interface-guidelines/researchkit

Platforms: iOS, iPadOS.

Onboarding is a fixed ethical sequence:

1. Introduction: who you are, what the study is, and that it is research.
2. Eligibility: stop people who should not enroll. Be clear, not coy.
3. Informed consent: readable, sectioned, with comprehension checks where appropriate. Consent is not a terms-of-service dump.
4. Permission to access data: only after consent, only the types the study needs, using system prompts.

- During the study, tasks are short, progress is visible, and withdrawal is always available and as easy as joining.
- Results and encouragement do not overclaim. A survey app is not a diagnosis.
- Protect identity. Do not display participant identifiers on shared screens. Follow the consent about what you store.

## SharePlay

URL: https://developer.apple.com/design/human-interface-guidelines/shareplay

- SharePlay is a shared activity inside FaceTime or a group session. People can see who is participating and leave at any time.
- Start from the system share or the FaceTime UI (`promoting` the activity), not a custom lobby that hides who is in the call.
- Sync state so late joiners catch up (`synchronizing`). One person scrubbing video should not silently desync everyone without a visible state.
- Spatial sessions (visionOS) use spatial templates (`SpatialTemplateSeatElement`, `isSpatial`, nearby participants). Seats are suggestions. Do not require a body pose or a specific chair.
- Personas represent people. Do not overlay content that covers someone's face by default.
- A shared activity still works alone, so the app is useful without a call.

## ShazamKit

URL: https://developer.apple.com/design/human-interface-guidelines/shazamkit

- Match audio the person chooses to identify. Show listening state, then the match or a clear miss.
- Do not listen in the background. Microphone use is obvious and ends when the match ends.
- Display the song, artist, and artwork you are allowed to show. Provide the next action they expect (open in a music app) without implying Apple Music exclusivity unless that is the real link.
- Say Shazam correctly if you use the name. The recognition UI should not clone the Shazam app's branding beyond what the kit provides.

## Sign in with Apple

URL: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple

- If you offer other third-party social logins, offer Sign in with Apple (`ASAuthorizationAppleIDButton`, AuthenticationServices).
- Use the system button. Styles: black, white, white with outline. The logo and the label ("Sign in with Apple", "Sign up with Apple", "Continue with Apple") stay together. Do not recolor the logo separately, change the font, or crop the mark.
- Minimum size, corner radius, and clear space are specified on the official page. The button is at least as prominent as other login buttons.
- Custom buttons are a last resort and must follow the logo-and-text or logo-only measurements exactly. Prefer the system control.
- Ask only for the name and email scopes you need. If you ask, use the values Apple returns. Hide My Email is a real address; do not reject it.
- Do not require a second password after Sign in with Apple. Account settings still offer account deletion.

## Siri

URL: https://developer.apple.com/design/human-interface-guidelines/siri

- Integrate with App Intents so Siri, Spotlight, and Shortcuts see the same actions. Donate or provide phrases that match real tasks.
- Resolve parameters with short follow-ups, not a dumped form. Confirm destructive or paid actions.
- Dialog is short, spoken-friendly, and consistent with on-screen snippets. No emoji salad, no marketing adjectives.
- Custom vocabulary and names should be pronounceable.
- Do not say "Hey Siri" inside the app as a branded button unless you are using a system API that requires that wording. Do not impersonate Siri's voice or the Siri orb.
- Errors tell people what Siri could not do and the in-app alternative.

## Tap to Pay on iPhone

URL: https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone

Platform: iOS. ProximityReader.

- This is a merchant experience. The customer sees the iPhone as the terminal. The UI must be readable by someone standing across a counter.
- Enablement and education screens use Apple's required flows (`ProximityReaderDiscovery`, prepare, progress). Do not skip the merchant education that the API requires.
- Checkout: show the amount clearly, then the ready-for-tap state (`readyForTap`) using the system UI. The customer taps their card or phone on the indicated area.
- Results: success and failure are obvious from across the counter, with the amount and a short status. Failures (`ReadError`) say to try again or use another method. Do not show raw error codes.
- Do not brand the payment surface so heavily that the Apple-required marks and instructions disappear.
- Accessibility: the merchant can complete the flow with VoiceOver. The customer-facing side stays simple.

## VoiceOver

URL: https://developer.apple.com/design/human-interface-guidelines/voiceover

- Every control has a label, a value when it has one, and a trait (button, header, adjustable). Decorative views are hidden (`accessibilityHidden`, `isAccessibilityElement = false`).
- Group related elements (`shouldGroupAccessibilityChildren`, `accessibilityElement`) so VoiceOver does not land on each glyph of a composite control.
- Order follows visual order, which follows reading order, including RTL.
- Custom controls implement activation, increment, and escape. Charts can expose a summary plus an audio graph or rotor (`AccessibilityRotorEntry`, `UIAccessibilityCustomRotor`) rather than a hundred unlabeled marks.
- When content changes, post a notification (`AccessibilityNotification`) only for changes the person needs. Do not spam announcements.
- visionOS: VoiceOver uses look and pinch. Labels must still make sense without seeing hover.
- Test by completing the main task with the screen curtain on.

## Wallet

URL: https://developer.apple.com/design/human-interface-guidelines/wallet

- Passes are added with the system add-pass UI (`PKAddPassesViewController`, `PKAddPassButton`). Use the official Add to Apple Wallet button. Do not redraw it.
- Pass types: boarding pass, coupon, event ticket, store card, poster generic, generic. Pick the type that matches the real-world object. Fields have roles (primary, secondary, auxiliary, header). Do not put a paragraph in the primary field.
- Images: logo, icon, strip, thumbnail, footer, and background have fixed roles and size guidance on the official page. The logo is your mark, legible on the pass color. Do not add extra floating badges the pass style does not support.
- Barcodes must scan. Contrast and quiet space matter more than decoration. Test a printed and a screen scan.
- Updates (gate change, balance) update the pass. Relevance (location, time) should be real so the pass surfaces on the Lock Screen honestly.
- Order tracking uses the Wallet orders model: status, fulfillment, and a clear merchant. Do not fake shipping state.
- Identity: verification passes and ID in Wallet follow the identity flows. Do not store an ID image in your own gallery as a substitute.
- watchOS shows a simplified pass. The important field (barcode, balance, seat) must still be usable on the wrist.


<!-- source: catalog.md -->

# HIG catalog

Complete map of Apple's Human Interface Guidelines as published in the documentation index on 2026-09-27.
Official home: https://developer.apple.com/design/human-interface-guidelines
Index JSON: https://developer.apple.com/tutorials/data/index/design--human-interface-guidelines

This file is a navigation index: titles, URLs, section names, and API symbols cited by Apple. Implementation rules live in the sibling reference files. When a measurement, trademark, or asset rule is load-bearing, open the official URL.

Coverage: 158 articles, 14 collections, plus the root module.

## Human Interface Guidelines

URL: https://developer.apple.com/design/human-interface-guidelines

## Getting started

URL: https://developer.apple.com/design/human-interface-guidelines/getting-started
Guidance: [getting-started.md](getting-started.md)

### Design principles

- URL: https://developer.apple.com/design/human-interface-guidelines/design-principles
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Purpose; Agency; Responsibility; Familiarity; Flexibility; Simplicity; Craft; Delight

### Designing for iOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for iPadOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for macOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-macos
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for tvOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for visionOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for watchOS

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Best practices

### Designing for games

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-games
- Platforms: see page
- Guidance: [getting-started.md](getting-started.md)
- Sections: Jump into gameplay; Look stunning on every display; Enable intuitive interactions; Welcome everyone; Adopt Apple technologies
- Cited APIs: `Core Haptics`, `GameKit`, `GameSave`, `HealthKit`

### Designing for iPhone Duo

- URL: https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo
- Platforms: see page
- Guidance: [iphone-duo.md](iphone-duo.md)
- Sections: Anatomy; Device poses; Best practices; Dynamic layouts; Reserved regions; Split views; Arrangement views; Vertical controls
- Cited APIs: `ArrangementView`, `safeAreaInsets`, `HStack`, `Label`, `NavigationSplitView`, `ReservedRegion`, `ToolbarItemGroup`, `ToolbarItemVisibilityPriority`, `ToolbarOverflowMenu`, `ToolbarVerticalCompressionBehavior`, `VStack`, `ZStack`, `UIArrangementViewController`, `UIBarButtonItem`

## Foundations

URL: https://developer.apple.com/design/human-interface-guidelines/foundations
Guidance: [foundations.md](foundations.md)

### Accessibility

- URL: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Vision; Hearing; Mobility; Speech; Cognitive; Platform considerations; visionOS
- Cited APIs: `Accessibility`, `isVideoAutoplayEnabled`

### App icons

- URL: https://developer.apple.com/design/human-interface-guidelines/app-icons
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Layer design; Icon shape; Design; Visual effects; Appearances; Platform considerations; tvOS; visionOS; watchOS; Specifications

### Branding

- URL: https://developer.apple.com/design/human-interface-guidelines/branding
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Platform considerations

### Color

- URL: https://developer.apple.com/design/human-interface-guidelines/color
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Inclusive color; System colors; Liquid Glass color; Color management; Platform considerations; iOS, iPadOS; macOS; App accent colors; tvOS; visionOS; watchOS; Specifications; System colors; iOS, iPadOS system gray colors
- Cited APIs: `alternateSelectedControlTextColor`, `alternatingContentBackgroundColors`, `controlAccentColor`, `controlBackgroundColor`, `controlColor`, `controlTextColor`, `currentControlTint`, `disabledControlTextColor`, `findHighlightColor`, `gridColor`, `headerTextColor`, `highlightColor`, `keyboardFocusIndicatorColor`, `labelColor`

### Dark Mode

- URL: https://developer.apple.com/design/human-interface-guidelines/dark-mode
- Platforms: ios,ipados,macos,tvos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Dark Mode colors; Icons and images; Text; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `controlColor`, `labelColor`, `separator`

### Icons

- URL: https://developer.apple.com/design/human-interface-guidelines/icons
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Standard icons; Editing; Selection; Text formatting; Search; Sharing and exporting; Users and accounts; Ratings; Layer ordering; Other; Platform considerations; macOS; Document icons

### Images

- URL: https://developer.apple.com/design/human-interface-guidelines/images
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Resolution; Formats; Best practices; Platform considerations; tvOS; Parallax effect; Layered images; visionOS; Spatial photos and spatial scenes; watchOS
- Cited APIs: `NSImageView`, `filters`, `ImagePresentationComponent`, `FocusState`, `GlassBackgroundEffect`, `UIImageView`

### Immersive experiences

- URL: https://developer.apple.com/design/human-interface-guidelines/immersive-experiences
- Platforms: visionos
- Guidance: [foundations.md](foundations.md)
- Sections: Immersion and passthrough; Immersion styles; Best practices; Promoting comfort; Transitioning between immersive styles; Displaying virtual hands; Creating an environment; Platform considerations
- Cited APIs: `ARKit`, `SceneReconstructionProvider`, `CoordinateSpaceProtocol`, `ImmersionStyle`, `automatic`, `full`, `mixed`, `progressive`, `SurroundingsEffect`

### Inclusion

- URL: https://developer.apple.com/design/human-interface-guidelines/inclusion
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Inclusive by design; Welcoming language; Being approachable; Gender identity; People and settings; Avoiding stereotypes; Accessibility; Languages; Platform considerations

### Layout

- URL: https://developer.apple.com/design/human-interface-guidelines/layout
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Visual hierarchy; Adaptability; Size classes; Guides and safe areas; Platform considerations; macOS; tvOS; Grids; visionOS; watchOS
- Cited APIs: `NSLayoutGuide`, `NSPrefersDisplaySafeAreaCompatibilityMode`, `SafeAreaRegions`, `defaultWindowPlacement(_:)`, `UserInterfaceSizeClass`, `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `UICollectionViewFlowLayout`, `UILayoutGuide`, `UITraitChangeObservable`, `isAutorotating`

### Materials

- URL: https://developer.apple.com/design/human-interface-guidelines/materials
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Liquid Glass; Standard materials; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS; watchOS
- Cited APIs: `NSVisualEffectView`, `NSVisualEffectView.BlendingMode`, `NSVisualEffectView.Material`, `clear`, `regular`, `Material`, `thick`, `thin`, `ultraThin`, `glassEffect(_:in:)`, `UIBlurEffect`, `UIVibrancyEffect`, `UIVibrancyEffectStyle.fill`, `UIVibrancyEffectStyle.label`

### Motion

- URL: https://developer.apple.com/design/human-interface-guidelines/motion
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Providing feedback; Leveraging platform capabilities; Platform considerations; visionOS; watchOS
- Cited APIs: `WKInterfaceImage`

### Privacy

- URL: https://developer.apple.com/design/human-interface-guidelines/privacy
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Best practices; Requesting permission; Pre-alert screens, windows, or views; Tracking requests; Location button; Protecting data; Platform considerations; macOS; visionOS
- Cited APIs: `App Tracking Transparency`, `CLLocationButton`, `LocationButton`, `Local Authentication`, `Security`

### Right to left

- URL: https://developer.apple.com/design/human-interface-guidelines/right-to-left
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Text alignment; Numbers and characters; Controls; Images; Interface icons; Platform considerations

### SF Symbols

- URL: https://developer.apple.com/design/human-interface-guidelines/sf-symbols
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Rendering modes; Gradients; Variable color; Weights and scales; Design variants; Animations; Custom symbols; Platform considerations
- Cited APIs: `NSImage.SymbolConfiguration`, `imageScale(_:)`, `Symbols`, `SymbolEffect`, `UIImage.SymbolScale`

### Spatial layout

- URL: https://developer.apple.com/design/human-interface-guidelines/spatial-layout
- Platforms: visionos
- Guidance: [foundations.md](foundations.md)
- Sections: Field of view; Depth; Scale; Best practices; Platform considerations
- Cited APIs: `RealityKit`

### Typography

- URL: https://developer.apple.com/design/human-interface-guidelines/typography
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Ensuring legibility; Conveying hierarchy; Using system fonts; Using custom fonts; Supporting Dynamic Type; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS; watchOS; Specifications; iOS, iPadOS Dynamic Type sizes; iOS, iPadOS larger accessibility type sizes; macOS built-in text styles; tvOS built-in text styles; watchOS Dynamic Type sizes; watchOS larger accessibility type sizes; Tracking values; iOS, iPadOS, visionOS tracking values; macOS tracking values; tvOS tracking values; watchOS tracking values
- Cited APIs: `boldSystemFont(ofSize:)`, `controlContentFont(ofSize:)`, `labelFont(ofSize:)`, `menuBarFont(ofSize:)`, `menuFont(ofSize:)`, `messageFont(ofSize:)`, `paletteFont(ofSize:)`, `systemFont(ofSize:)`, `titleBarFont(ofSize:)`, `toolTipsFont(ofSize:)`, `userFixedPitchFont(ofSize:)`, `userFont(ofSize:)`, `Font.Design`, `Font.Design.default`

### Writing

- URL: https://developer.apple.com/design/human-interface-guidelines/writing
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [foundations.md](foundations.md)
- Sections: Getting started; Best practices; Platform considerations

## Patterns

URL: https://developer.apple.com/design/human-interface-guidelines/patterns
Guidance: [patterns.md](patterns.md)

### Charting data

- URL: https://developer.apple.com/design/human-interface-guidelines/charting-data
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Designing effective charts; Platform considerations
- Cited APIs: `Swift Charts`

### Collaboration and sharing

- URL: https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing
- Platforms: ios,ipados,macos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; visionOS; watchOS
- Cited APIs: `Shared with You`, `SWHighlightEvent`, `ShareLink`

### Drag and drop

- URL: https://developer.apple.com/design/human-interface-guidelines/drag-and-drop
- Platforms: ios,ipados,macos,visionos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Providing feedback; Accepting drops; Platform considerations; iOS, iPadOS; macOS; visionOS
- Cited APIs: `File Provider`, `NSUserActivity`, `accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors`

### Entering data

- URL: https://developer.apple.com/design/human-interface-guidelines/entering-data
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; macOS
- Cited APIs: `SecureField`, `isSecureDigitEntry`

### Feedback

- URL: https://developer.apple.com/design/human-interface-guidelines/feedback
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; watchOS

### File management

- URL: https://developer.apple.com/design/human-interface-guidelines/file-management
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Creating and opening files; Saving work; Quick Look previews; Platform considerations; iOS, iPadOS; Document launcher; File provider app extension; macOS; Custom file management; Finder Sync extensions
- Cited APIs: `File Provider`, `Finder Sync`, `DocumentGroupLaunchScene`

### Going full screen

- URL: https://developer.apple.com/design/human-interface-guidelines/going-full-screen
- Platforms: ios,ipados,macos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `hideDock`, `NSScreen`, `NSWindow.CollectionBehavior`, `toggleFullScreen(_:)`, `preferredScreenEdgesDeferringSystemGestures`, `fullScreenCover(item:onDismiss:content:)`

### Launching

- URL: https://developer.apple.com/design/human-interface-guidelines/launching
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Launch screens; Platform considerations; iOS, iPadOS; tvOS; visionOS

### Live-viewing apps

- URL: https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; EPG experience; Cloud DVR; Platform considerations

### Loading

- URL: https://developer.apple.com/design/human-interface-guidelines/loading
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Showing progress; Platform considerations; watchOS
- Cited APIs: `Background Assets`

### Managing accounts

- URL: https://developer.apple.com/design/human-interface-guidelines/managing-accounts
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Deleting accounts; TV provider accounts; Platform considerations; tvOS; watchOS
- Cited APIs: `User Management Entitlement`, `LABiometryType`, `kSecUseUserIndependentKeychain`, `Token revocation`

### Managing notifications

- URL: https://developer.apple.com/design/human-interface-guidelines/managing-notifications
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Integrating with Focus; Best practices; Sending marketing notifications; Platform considerations; watchOS
- Cited APIs: `INSendMessageIntent`, `User Notifications`, `UNNotificationContentProviding`, `UNNotificationInterruptionLevel`

### Modality

- URL: https://developer.apple.com/design/human-interface-guidelines/modality
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `UIModalPresentationStyle`

### Multitasking

- URL: https://developer.apple.com/design/human-interface-guidelines/multitasking
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; iOS; iPadOS; macOS; tvOS; visionOS

### Offering help

- URL: https://developer.apple.com/design/human-interface-guidelines/offering-help
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Creating tips; Platform considerations; macOS, visionOS
- Cited APIs: `NSHelpManager`, `help(_:)`, `TipKit`

### Onboarding

- URL: https://developer.apple.com/design/human-interface-guidelines/onboarding
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Additional content; Additional requests; Platform considerations
- Cited APIs: `TipKit`

### Playing audio

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-audio
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Handling interruptions; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS; watchOS
- Cited APIs: `AVAudioSession`, `AVAudioSession.Category`, `shouldResume`, `notifyOthersOnDeactivation`, `MPVolumeView`, `MusicKit`

### Playing haptics

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Custom haptics; Platform considerations; iOS; Notification; Impact; Selection; macOS; watchOS
- Cited APIs: `NSHapticFeedbackPerformer`, `Core Haptics`, `UIFeedbackGenerator`, `WKHapticType`

### Playing video

- URL: https://developer.apple.com/design/human-interface-guidelines/playing-video
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Integrating with the TV app; Loading content; Exiting playback; Platform considerations; tvOS; visionOS; watchOS
- Cited APIs: `silenceSecondaryAudioHintNotification`, `resizeAspect`, `resizeAspectFill`, `externalMetadata`, `AVKit`, `AVPlayerViewController`, `VideoPlayer`, `RealityKit`

### Printing

- URL: https://developer.apple.com/design/human-interface-guidelines/printing
- Platforms: ios,ipados,macos,visionos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; macOS
- Cited APIs: `NSDocument`, `UIPrintInteractionController`

### Ratings and reviews

- URL: https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `RequestReviewAction`

### Searching

- URL: https://developer.apple.com/design/human-interface-guidelines/searching
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Systemwide search; Platform considerations
- Cited APIs: `CSImportExtension`, `Quick Look`, `searchSuggestions(_:)`

### Settings

- URL: https://developer.apple.com/design/human-interface-guidelines/settings
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; General settings; Task-specific options; System settings; Platform considerations; macOS; watchOS
- Cited APIs: `UserDefaults`, `Preference Panes`, `Settings`

### Undo and redo

- URL: https://developer.apple.com/design/human-interface-guidelines/undo-and-redo
- Platforms: ios,ipados,macos,visionos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `UndoManager`

### Workouts

- URL: https://developer.apple.com/design/human-interface-guidelines/workouts
- Platforms: ios,ipados,watchos
- Guidance: [patterns.md](patterns.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `WorkoutKit`

## Components

URL: https://developer.apple.com/design/human-interface-guidelines/components
Guidance: [components-status-system.md](components-status-system.md)

## Content

URL: https://developer.apple.com/design/human-interface-guidelines/content
Guidance: [catalog.md](catalog.md)

### Charts

- URL: https://developer.apple.com/design/human-interface-guidelines/charts
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Anatomy; Marks; Axes; Descriptive content; Best practices; Color; Enhancing the accessibility of a chart; Platform considerations; watchOS
- Cited APIs: `NSAccessibility.Notification`, `Swift Charts`, `accessibilityRespondsToUserInteraction(_:)`, `UIAccessibility.Notification`

### Image views

- URL: https://developer.apple.com/design/human-interface-guidelines/image-views
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Content; Platform considerations; macOS; tvOS; visionOS; watchOS
- Cited APIs: `NSImageView`, `ImagePresentationComponent`, `Image`, `UIImageView`, `WKImageAnimatable`

### Text views

- URL: https://developer.apple.com/design/human-interface-guidelines/text-views
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; tvOS
- Cited APIs: `NSTextView`, `Text`, `UITextView`

### Web views

- URL: https://developer.apple.com/design/human-interface-guidelines/web-views
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `WKWebView`

## Layout and organization

URL: https://developer.apple.com/design/human-interface-guidelines/layout-and-organization
Guidance: [catalog.md](catalog.md)

### Boxes

- URL: https://developer.apple.com/design/human-interface-guidelines/boxes
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Content; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `NSBox`, `GroupBox`

### Collections

- URL: https://developer.apple.com/design/human-interface-guidelines/collections
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS
- Cited APIs: `NSCollectionView`, `UICollectionView`

### Column views

- URL: https://developer.apple.com/design/human-interface-guidelines/column-views
- Platforms: macos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSBrowser`

### Disclosure controls

- URL: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Disclosure triangles; Disclosure buttons; Platform considerations; iOS, iPadOS, visionOS
- Cited APIs: `NSButton.BezelStyle.disclosure`, `NSButton.BezelStyle.pushDisclosure`, `DisclosureGroup`

### Labels

- URL: https://developer.apple.com/design/human-interface-guidelines/labels
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations; macOS; watchOS
- Cited APIs: `labelColor`, `quaternaryLabelColor`, `secondaryLabelColor`, `tertiaryLabelColor`, `NSTextField`, `isEditable`, `Label`, `Text`, `label`, `quaternaryLabel`, `secondaryLabel`, `tertiaryLabel`, `UILabel`

### Lists and tables

- URL: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Content; Style; Platform considerations; iOS, iPadOS, visionOS; macOS; tvOS; watchOS
- Cited APIs: `NSTableView`, `List`, `ListStyle`, `UIListContentConfiguration`, `UITableView`, `UITableViewCell.AccessoryType.disclosureIndicator`

### Lockups

- URL: https://developer.apple.com/design/human-interface-guidelines/lockups
- Platforms: tvos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Cards; Caption buttons; Monograms; Posters; Platform considerations
- Cited APIs: `TVCaptionButtonView`, `TVCardView`, `TVLockupHeaderFooterView`, `TVLockupView`, `TVMonogramContentView`, `TVPosterView`

### Outline views

- URL: https://developer.apple.com/design/human-interface-guidelines/outline-views
- Platforms: macos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSOutlineView`, `OutlineGroup`

### Split views

- URL: https://developer.apple.com/design/human-interface-guidelines/split-views
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Platform considerations; iOS; iPadOS; macOS; tvOS; visionOS; watchOS
- Cited APIs: `NSSplitView.DividerStyle`, `NSSplitViewController`, `HSplitView`, `NavigationSplitView`, `VSplitView`, `UISplitViewController`

### Tab views

- URL: https://developer.apple.com/design/human-interface-guidelines/tab-views
- Platforms: macos,watchos
- Guidance: [components-content-layout.md](components-content-layout.md)
- Sections: Best practices; Anatomy; Platform considerations; iOS, iPadOS; watchOS
- Cited APIs: `NSTabView`, `TabView`

## Menus and actions

URL: https://developer.apple.com/design/human-interface-guidelines/menus-and-actions
Guidance: [catalog.md](catalog.md)

### Activity views

- URL: https://developer.apple.com/design/human-interface-guidelines/activity-views
- Platforms: ios,ipados,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Share and action extensions; Platform considerations
- Cited APIs: `UIActivity`, `UIActivityViewController`

### Buttons

- URL: https://developer.apple.com/design/human-interface-guidelines/buttons
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Style; Content; Role; Platform considerations; iOS, iPadOS; macOS; Push buttons; Square buttons; Help buttons; Image buttons; visionOS; watchOS
- Cited APIs: `NSButton`, `NSButton.BezelStyle.flexiblePush`, `NSButton.BezelStyle.smallSquare`, `isBordered`, `Button`, `capsule`, `circle`, `roundedRectangle`, `thin`, `UIButton`

### Context menus

- URL: https://developer.apple.com/design/human-interface-guidelines/context-menus
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Content; Platform considerations; iOS, iPadOS; macOS; visionOS
- Cited APIs: `popUpContextMenu(_:with:for:)`, `contextMenu(menuItems:)`, `UIContextMenuInteraction`, `UIContextMenuInteractionDelegate`, `destructive`

### Dock menus

- URL: https://developer.apple.com/design/human-interface-guidelines/dock-menus
- Platforms: macos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `applicationDockMenu(_:)`

### Edit menus

- URL: https://developer.apple.com/design/human-interface-guidelines/edit-menus
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Content; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `NSMenu`, `UIEditMenuInteraction`, `UIResponderStandardEditActions`

### Home Screen quick actions

- URL: https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions
- Platforms: ios,ipados
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations

### Menus

- URL: https://developer.apple.com/design/human-interface-guidelines/menus
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Labels; Icons; Organization; Submenus; Toggled items; In-game menus; Platform considerations; iOS, iPadOS; visionOS
- Cited APIs: `automatic`, `none`, `prominent`, `subtle`, `Menu`, `preferredElementSize`

### Ornaments

- URL: https://developer.apple.com/design/human-interface-guidelines/ornaments
- Platforms: visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `TabView`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`

### Pop-up buttons

- URL: https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations; iPadOS
- Cited APIs: `NSPopUpButton`, `MenuPickerStyle`, `changesSelectionAsPrimaryAction`

### Pull-down buttons

- URL: https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS
- Cited APIs: `pullsDown`, `MenuPickerStyle`, `showsMenuAsPrimaryAction`

### The menu bar

- URL: https://developer.apple.com/design/human-interface-guidelines/the-menu-bar
- Platforms: ipados,macos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Anatomy; Best practices; App menu; File menu; Edit menu; Format menu; View menu; App-specific menus; Window menu; Help menu; Dynamic menu items; Platform considerations; iPadOS; macOS; Menu bar extras
- Cited APIs: `NSHelpManager`, `isAlternate`, `NSStatusBar`, `CommandMenu`, `MenuBarExtra`

### Toolbars

- URL: https://developer.apple.com/design/human-interface-guidelines/toolbars
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Titles; Navigation; Actions; Item groupings; Platform considerations; iOS; iPadOS; macOS; visionOS; watchOS
- Cited APIs: `NSToolbar`, `ScrollEdgeEffectStyle`, `bottomBar`, `primaryAction`, `topBarLeading`, `topBarTrailing`, `UIBarButtonItem.SystemItem.fixedSpace`, `prefersLargeTitles`, `UIToolbar`

## Navigation and search

URL: https://developer.apple.com/design/human-interface-guidelines/navigation-and-search
Guidance: [catalog.md](catalog.md)

### Path controls

- URL: https://developer.apple.com/design/human-interface-guidelines/path-controls
- Platforms: macos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSPathControl`

### Search fields

- URL: https://developer.apple.com/design/human-interface-guidelines/search-fields
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Scope bars and tokens; Platform considerations; iOS; Search as a tab; Search in a toolbar; Search as an inline field; iPadOS, macOS; tvOS; watchOS
- Cited APIs: `NSSearchField`, `searchable(text:placement:prompt:)`, `UISearchBar`, `UISearchController`, `UISearchTextField`

### Sidebars

- URL: https://developer.apple.com/design/human-interface-guidelines/sidebars
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS; visionOS
- Cited APIs: `NSSplitViewController`, `sidebar`, `NavigationSplitView`, `sidebarAdaptable`, `backgroundExtensionEffect()`, `UICollectionLayoutListConfiguration`, `UICollectionLayoutListConfiguration.Appearance`, `UICollectionLayoutListConfiguration.Appearance.sidebar`, `UISplitViewController`

### Tab bars

- URL: https://developer.apple.com/design/human-interface-guidelines/tab-bars
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations; iOS; iPadOS; tvOS; visionOS
- Cited APIs: `TabBarMinimizeBehavior`, `TabView`, `TabViewBottomAccessoryPlacement`, `TabViewCustomization`, `sidebarAdaptable`, `tabBarOnly`, `UITab.Placement`, `UITabBar`, `UITabBarController.MinimizeBehavior`

### Token fields

- URL: https://developer.apple.com/design/human-interface-guidelines/token-fields
- Platforms: macos
- Guidance: [components-menus-navigation.md](components-menus-navigation.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSTokenField`

## Presentation

URL: https://developer.apple.com/design/human-interface-guidelines/presentation
Guidance: [catalog.md](catalog.md)

### Action sheets

- URL: https://developer.apple.com/design/human-interface-guidelines/action-sheets
- Platforms: ios,ipados,macos,tvos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; watchOS
- Cited APIs: `destructive`, `confirmationDialog(_:isPresented:titleVisibility:actions:)`, `UIAlertAction.Style.destructive`, `UIAlertController.Style.actionSheet`

### Alerts

- URL: https://developer.apple.com/design/human-interface-guidelines/alerts
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Anatomy; Content; Buttons; Platform considerations; iOS, iPadOS; macOS; visionOS
- Cited APIs: `NSAlert`, `accessoryView`, `alert(_:isPresented:actions:)`, `UIAlertController`

### Page controls

- URL: https://developer.apple.com/design/human-interface-guidelines/page-controls
- Platforms: ios,ipados,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Customizing indicators; Platform considerations; iOS, iPadOS; tvOS; visionOS; watchOS
- Cited APIs: `PageTabViewStyle`, `UIPageControl`, `UIPageControl.InteractionState`, `backgroundStyle`, `preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`

### Panels

- URL: https://developer.apple.com/design/human-interface-guidelines/panels
- Platforms: macos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; HUD-style panels; Platform considerations
- Cited APIs: `NSPanel`, `hudWindow`

### Popovers

- URL: https://developer.apple.com/design/human-interface-guidelines/popovers
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `NSPopover`, `popover(isPresented:attachmentAnchor:arrowEdge:content:)`, `UIPopoverPresentationController`

### Scroll views

- URL: https://developer.apple.com/design/human-interface-guidelines/scroll-views
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Scroll edge effects; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS; Look to Scroll; watchOS
- Cited APIs: `NSScrollEdgeEffectStyle`, `NSScrollView`, `PagingScrollTargetBehavior`, `ScrollEdgeEffectStyle`, `automatic`, `ScrollInputKind`, `look`, `ScrollView`, `UIScrollEdgeEffect.Style`, `UIScrollView`, `WKPageOrientation`

### Sheets

- URL: https://developer.apple.com/design/human-interface-guidelines/sheets
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Anatomy; Best practices; Platform considerations; iOS, iPadOS; macOS; visionOS; watchOS
- Cited APIs: `presentAsSheet(_:)`, `sheet(item:onDismiss:content:)`, `UIModalPresentationStyle`, `UIModalPresentationStyle.fullScreen`, `UISheetPresentationController`, `detents`, `prefersGrabberVisible`

### Windows

- URL: https://developer.apple.com/design/human-interface-guidelines/windows
- Platforms: ipados,macos,visionos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iPadOS; macOS; macOS window anatomy; macOS window states; visionOS; visionOS windows; visionOS volumes
- Cited APIs: `NSWindow`, `QLPreviewSceneActivationConfiguration`, `DefaultWindowStyle`, `OpenWindowAction`, `PlainWindowStyle`, `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`, `VolumetricWindowStyle`, `WindowGroup`, `collectionView(_:sceneActivationConfigurationForItemAt:point:)`, `UIWindow`, `UIWindowScene.ActivationInteraction`

## Selection and input

URL: https://developer.apple.com/design/human-interface-guidelines/selection-and-input
Guidance: [catalog.md](catalog.md)

### Color wells

- URL: https://developer.apple.com/design/human-interface-guidelines/color-wells
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; macOS
- Cited APIs: `NSColorWell`, `UIColorPickerViewController`, `UIColorWell`

### Combo boxes

- URL: https://developer.apple.com/design/human-interface-guidelines/combo-boxes
- Platforms: macos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSComboBox`

### Digit entry views

- URL: https://developer.apple.com/design/human-interface-guidelines/digit-entry-views
- Platforms: tvos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `TVDigitEntryViewController`

### Image wells

- URL: https://developer.apple.com/design/human-interface-guidelines/image-wells
- Platforms: macos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSImageView`

### Pickers

- URL: https://developer.apple.com/design/human-interface-guidelines/pickers
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS; tvOS; watchOS
- Cited APIs: `NSDatePicker`, `DatePicker`, `Picker`, `navigationLink`, `UIDatePicker`, `UIPickerView`

### Segmented controls

- URL: https://developer.apple.com/design/human-interface-guidelines/segmented-controls
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Content; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS
- Cited APIs: `NSSegmentedControl`, `NSSegmentedControl.SwitchTracking.momentary`, `segmented`, `UISegmentedControl`, `isMomentary`

### Sliders

- URL: https://developer.apple.com/design/human-interface-guidelines/sliders
- Platforms: ios,ipados,macos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS; visionOS; watchOS
- Cited APIs: `NSSlider`, `Slider`, `UISlider`

### Steppers

- URL: https://developer.apple.com/design/human-interface-guidelines/steppers
- Platforms: ios,ipados,macos,visionos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; macOS
- Cited APIs: `NSStepper`, `UIStepper`

### Text fields

- URL: https://developer.apple.com/design/human-interface-guidelines/text-fields
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS; watchOS
- Cited APIs: `NSTextField`, `SecureField`, `TextField`, `UITextField`

### Toggles

- URL: https://developer.apple.com/design/human-interface-guidelines/toggles
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; macOS; Switches; Checkboxes; Radio buttons
- Cited APIs: `NSButton.ButtonType.toggle`, `allowsMixedState`, `NSSwitch`, `ControlSize`, `GroupedFormStyle`, `Toggle`, `ToggleStyle`, `switch`, `changesSelectionAsPrimaryAction`, `UISwitch`

### Virtual keyboards

- URL: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards
- Platforms: ios,ipados,tvos,visionos,watchos
- Guidance: [components-presentation-input.md](components-presentation-input.md)
- Sections: Best practices; Custom input views; Custom keyboards; Platform considerations; iOS, iPadOS; tvOS; visionOS; watchOS
- Cited APIs: `ToolbarItemPlacement`, `keyboardType(_:)`, `submitLabel(_:)`, `textContentType(_:)`, `playInputClick()`, `UIKeyboardLayoutGuide`, `UIKeyboardType`, `inputAccessoryView`, `inputViewController`, `UIReturnKeyType`, `UITextContentType`

## Status

URL: https://developer.apple.com/design/human-interface-guidelines/status
Guidance: [catalog.md](catalog.md)

### Activity rings

- URL: https://developer.apple.com/design/human-interface-guidelines/activity-rings
- Platforms: ios,ipados,watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Platform considerations; iOS
- Cited APIs: `HKActivityRingView`

### Gauges

- URL: https://developer.apple.com/design/human-interface-guidelines/gauges
- Platforms: ios,ipados,macos,visionos,watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; Best practices; Platform considerations; macOS
- Cited APIs: `NSLevelIndicator`, `Gauge`

### Progress indicators

- URL: https://developer.apple.com/design/human-interface-guidelines/progress-indicators
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS; Refresh content controls; macOS; watchOS
- Cited APIs: `NSProgressIndicator`, `ProgressView`, `UIActivityIndicatorView`, `UIProgressView`, `UIRefreshControl`

### Rating indicators

- URL: https://developer.apple.com/design/human-interface-guidelines/rating-indicators
- Platforms: macos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `NSLevelIndicator.Style.rating`

## System experiences

URL: https://developer.apple.com/design/human-interface-guidelines/system-experiences
Guidance: [catalog.md](catalog.md)

### App Shortcuts

- URL: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts
- Platforms: ios,ipados,visionos,watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Responding to App Shortcuts; Editorial guidelines; Platform considerations; iOS, iPadOS; macOS
- Cited APIs: `App Intents`, `AppShortcutPhrase`, `init(full:supporting:systemImageName:)`, `LiveActivityIntent`, `SiriTipUIView`

### Complications

- URL: https://developer.apple.com/design/human-interface-guidelines/complications
- Platforms: watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Visual design; Circular; Corner; Inline; Rectangular; Legacy templates; Circular small; Modular small; Modular large; Extra large; Platform considerations
- Cited APIs: `CLKComplicationDataSource`, `WidgetKit`, `placeholder(in:)`, `WidgetFamily.accessoryRectangular`, `WidgetRenderingMode`

### Controls

- URL: https://developer.apple.com/design/human-interface-guidelines/controls
- Platforms: ios,ipados,macos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; Best practices; Camera experiences on a locked device; Platform considerations
- Cited APIs: `IntentAuthenticationPolicy`, `LockedCameraCapture`, `promptsForUserConfiguration()`, `controlWidgetActionHint(_:)`, `Symbols`, `SymbolEffect`, `WidgetKit`

### Live Activities

- URL: https://developer.apple.com/design/human-interface-guidelines/live-activities
- Platforms: ios, ipados, macos, watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; Compact; Minimal; Expanded; Lock Screen; StandBy; Best practices; Creating Live Activity layouts; Choosing colors; Adding transitions and animating content updates; Offering interactivity; Starting, updating, and ending a Live Activity; Presentation; Compact presentation; Minimal presentation; Expanded presentation; Lock Screen presentation; StandBy presentation; CarPlay; Platform considerations; macOS; watchOS; Specifications; CarPlay dimensions
- Cited APIs: `ActivityKit`, `SwiftUI`, `ContainerRelativeShape`, `activitySystemActionForegroundColor(_:)`, `padding(_:_:)`, `WidgetKit`, `ActivityFamily.small`

### Notifications

- URL: https://developer.apple.com/design/human-interface-guidelines/notifications
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; Best practices; Content; Notification actions; Badging; Platform considerations; watchOS; Short looks; Long looks; Double tap
- Cited APIs: `SceneKit`, `SpriteKit`, `User Notifications`, `hiddenPreviewsBodyPlaceholder`, `UNNotificationSound`, `User Notifications UI`

### Snippets

- URL: https://developer.apple.com/design/human-interface-guidelines/snippets
- Platforms: ios,ipados,macos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; Best practices; Platform considerations
- Cited APIs: `App Intents`, `ConfirmationActionName`

### Status bars

- URL: https://developer.apple.com/design/human-interface-guidelines/status-bars
- Platforms: ios,ipados
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `ScrollEdgeEffectStyle`, `UIScrollEdgeEffect`, `UIStatusBarStyle`, `preferredStatusBarStyle`

### Top Shelf

- URL: https://developer.apple.com/design/human-interface-guidelines/top-shelf
- Platforms: tvos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Dynamic layouts; Carousel actions; Carousel details; Sectioned content row; Poster (2:3); Square (1:1); 16:9; Scrolling inset banner; Platform considerations

### Watch faces

- URL: https://developer.apple.com/design/human-interface-guidelines/watch-faces
- Platforms: watchos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Best practices; Platform considerations

### Widgets

- URL: https://developer.apple.com/design/human-interface-guidelines/widgets
- Platforms: ios,ipados,macos,watchos,visionos
- Guidance: [components-status-system.md](components-status-system.md)
- Sections: Anatomy; System family widgets; Accessory widgets; Appearances; Best practices; Updating widget content; Adding interactivity; Choosing margins and padding; Displaying text in widgets; Using color; Rendering modes; Full-color; Accented; Vibrant; Previews and placeholders; Platform considerations; iOS, iPadOS; StandBy and CarPlay; visionOS; Thresholds and sizes; Mounting styles; Treatment styles; watchOS; Specifications
- Cited APIs: `ActivityKit`, `RelevanceKit`, `SwiftUI`, `ContainerRelativeShape`, `Font`, `custom(_:size:)`, `padding(_:_:)`, `widgetAccentable(_:)`, `WidgetConfiguration`, `supportedMountingStyles(_:)`, `WidgetKit`, `default`, `simplified`, `elevated`

## Inputs

URL: https://developer.apple.com/design/human-interface-guidelines/inputs
Guidance: [inputs.md](inputs.md)

### Action button

- URL: https://developer.apple.com/design/human-interface-guidelines/action-button
- Platforms: ios,watchos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Platform considerations; iOS; watchOS

### Apple Pencil and Scribble

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble
- Platforms: ipados
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Hover; Double tap; Squeeze; Barrel roll; Scribble; Custom drawing; Platform considerations
- Cited APIs: `PaperKit`, `PencilKit`, `UIIndirectScribbleInteraction`, `UIScribbleInteraction`

### Camera Control

- URL: https://developer.apple.com/design/human-interface-guidelines/camera-control
- Platforms: ios
- Guidance: [inputs.md](inputs.md)
- Sections: Anatomy; Best practices; Platform considerations
- Cited APIs: `AVCaptureControl`, `localizedValueFormat`, `prominentValues`, `LockedCameraCapture`

### Digital Crown

- URL: https://developer.apple.com/design/human-interface-guidelines/digital-crown
- Platforms: visionos,watchos
- Guidance: [inputs.md](inputs.md)
- Sections: Apple Vision Pro; Apple Watch; Platform considerations
- Cited APIs: `WKCrownDelegate`

### Eyes

- URL: https://developer.apple.com/design/human-interface-guidelines/eyes
- Platforms: visionos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Making items easy to see; Encouraging interaction; Custom hover effects; Platform considerations

### Focus and selection

- URL: https://developer.apple.com/design/human-interface-guidelines/focus-and-selection
- Platforms: ipados,macos,tvos,visionos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Platform considerations; iPadOS; tvOS; visionOS
- Cited APIs: `NSTableView`, `UICollectionView`, `UICollectionViewCell`, `focusGroupIdentifier`, `UIFocusGroupPriority`, `UIFocusHaloEffect`

### Game controls

- URL: https://developer.apple.com/design/human-interface-guidelines/game-controls
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [inputs.md](inputs.md)
- Sections: Touch controls; Physical controllers; Keyboards; Platform considerations; visionOS
- Cited APIs: `GCRequiresControllerUserInteraction`, `Game Controller`, `GCControllerElement`, `Touch Controller`

### Gestures

- URL: https://developer.apple.com/design/human-interface-guidelines/gestures
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Custom gestures; Platform considerations; iOS, iPadOS; macOS; tvOS; visionOS; Designing custom gestures in visionOS; Working with system overlays in visionOS; watchOS; Double tap; Specifications; Standard gestures
- Cited APIs: `primaryAction`, `handGestureShortcut(_:isEnabled:)`, `persistentSystemOverlays(_:)`, `UITouch`

### Gyroscope and accelerometer

- URL: https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `Core Motion`

### Keyboards

- URL: https://developer.apple.com/design/human-interface-guidelines/keyboards
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Standard keyboard shortcuts; Custom keyboard shortcuts; Platform considerations; visionOS
- Cited APIs: `isFullKeyboardAccessEnabled`, `KeyboardShortcut`, `discoverabilityTitle`

### Nearby interactions

- URL: https://developer.apple.com/design/human-interface-guidelines/nearby-interactions
- Platforms: ios,ipados,watchos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Device usage; Platform considerations; iOS; watchOS
- Cited APIs: `Nearby Interaction`

### Pointing devices

- URL: https://developer.apple.com/design/human-interface-guidelines/pointing-devices
- Platforms: ios,ipados,macos,visionos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Platform considerations; iPadOS; Pointer shape and content effects; Pointer accessories; Pointer magnetism; Standard pointers and effects; Customizing pointers; macOS; Pointers; visionOS
- Cited APIs: `arrow`, `closedHand`, `contextualMenu`, `crosshair`, `disappearingItem`, `dragCopy`, `dragLink`, `iBeam`, `iBeamCursorForVerticalLayout`, `openHand`, `operationNotAllowed`, `pointingHand`, `resizeDown`, `resizeLeft`

### Remotes

- URL: https://developer.apple.com/design/human-interface-guidelines/remotes
- Platforms: tvos
- Guidance: [inputs.md](inputs.md)
- Sections: Best practices; Gestures; Buttons; Compatible remotes; Platform considerations

## Technologies

URL: https://developer.apple.com/design/human-interface-guidelines/technologies
Guidance: [technologies.md](technologies.md)

### AirPlay

- URL: https://developer.apple.com/design/human-interface-guidelines/airplay
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Using AirPlay icons; Black AirPlay icon; White AirPlay icon; Custom color AirPlay icon; Referring to AirPlay; Platform considerations
- Cited APIs: `ambient`, `AVFoundation`, `usesExternalPlaybackWhileExternalScreenIsActive`, `AVKit`, `AVPlayerViewController`

### Always On

- URL: https://developer.apple.com/design/human-interface-guidelines/always-on
- Platforms: ios,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations

### App Clips

- URL: https://developer.apple.com/design/human-interface-guidelines/app-clips
- Platforms: ios,ipados
- Guidance: [technologies.md](technologies.md)
- Sections: Designing your App Clip; Preserving privacy; Showcasing your app; Limiting notifications; Creating App Clips for businesses; Creating content for an App Clip card; App Clip Codes; Interacting with App Clip Codes; Displaying App Clip Codes; Using clear messaging; Customizing your App Clip Code; Printing guidelines; Verifying your printer’s calibration; Legal requirements; Platform considerations
- Cited APIs: `App Clips`, `SKOverlay`

### Apple In-App Purchase

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Supporting Family Sharing; Providing help; Auto-renewable subscriptions; Making signup effortless; Supporting offer codes; Helping people manage their subscriptions; Platform considerations; watchOS
- Cited APIs: `Advanced Commerce API`, `Retention Messaging API`, `canMakePayments`, `presentOfferCodeRedeemSheet(from:options:)`, `showManageSubscriptions(in:)`, `Product.SubscriptionInfo`, `beginRefundRequest(for:in:)`, `offerCodeRedemption(options:isPresented:onCompletion:)`

### Apple Pay

- URL: https://developer.apple.com/design/human-interface-guidelines/apple-pay
- Platforms: ios,ipados,macos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Offering Apple Pay; Streamlining checkout; Customizing the payment sheet; Displaying a website icon; Handling problems; Data validation errors; Payment processing problems; Supporting subscriptions; Supporting donations; Using Apple Pay buttons; Button types; Apple Pay button; Set Up Apple Pay button; Button styles; Black; White with outline; White; Button size and position; Apple Pay mark; Referring to Apple Pay; Platform considerations
- Cited APIs: `Apple Pay on the Web`, `ApplePayButtonStyle`, `applePayCapabilities`, `oncancel`, `PKDateComponentsRange`, `PKPaymentAuthorizationController`, `PKPaymentAuthorizationViewControllerDelegate`, `cornerRadius`, `PKPaymentButtonStyle`, `PKPaymentButtonStyle.automatic`, `PKPaymentButtonType`, `PKPaymentError`, `paymentSummaryItems`, `WKInterfacePaymentButton`

### Augmented reality

- URL: https://developer.apple.com/design/human-interface-guidelines/augmented-reality
- Platforms: ios,ipados,visionos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Providing coaching; Helping people place objects; Designing object interactions; Offering a multiuser experience; Reacting to real-world objects; Communicating with people; Handling interruptions; Suggesting problem resolutions; Icons and badges; Platform considerations; visionOS
- Cited APIs: `ARKit`, `ARCoachingOverlayView`, `ARTrackedRaycast`, `isCollaborationEnabled`

### CareKit

- URL: https://developer.apple.com/design/human-interface-guidelines/carekit
- Platforms: ios,ipados
- Guidance: [technologies.md](technologies.md)
- Sections: Data and privacy; HealthKit integration; Motion data; Photos; ResearchKit integration; CareKit views; Tasks; Charts; Contact views; Notifications; Symbols and branding; Platform considerations
- Cited APIs: `Core Motion`, `HealthKit`, `requestAuthorization(toShare:read:completion:)`, `UIImagePickerController`

### CarPlay

- URL: https://developer.apple.com/design/human-interface-guidelines/carplay
- Platforms: ios
- Guidance: [technologies.md](technologies.md)
- Sections: iPhone interactions; Audio; Layout; Color; Icons and images; Error handling; Platform considerations

### Game Center

- URL: https://developer.apple.com/design/human-interface-guidelines/game-center
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Accessing Game Center; Integrating the access point; Using custom UI; Achievements; Integrating achievements into your game; Creating achievement images; Leaderboards; Challenges; Multiplayer activities; Platform considerations; tvOS; watchOS
- Cited APIs: `GameKit`

### Generative AI

- URL: https://developer.apple.com/design/human-interface-guidelines/generative-ai
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Transparency; Privacy; Models and datasets; Inputs; Outputs; Continuous improvement; Platform considerations
- Cited APIs: `Core AI`, `Foundation Models`, `Vision`

### HealthKit

- URL: https://developer.apple.com/design/human-interface-guidelines/healthkit
- Platforms: ios,ipados,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Privacy protection; Activity rings; Apple Health icon; Editorial guidelines; Platform considerations
- Cited APIs: `HealthKit`, `requestAuthorization(toShare:read:completion:)`, `HKActivityRingView`

### HomeKit

- URL: https://developer.apple.com/design/human-interface-guidelines/homekit
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Terminology and layout; Homes; Rooms; Accessories, services, and characteristics; Actions and scenes; Automations; Zones; Setup; Help people choose useful names; Siri interactions; Custom functionality; Cameras; Using HomeKit icons; Styles; Black HomeKit icon; White HomeKit icon; Custom color HomeKit icon; Referring to HomeKit; Referencing HomeKit and the Home app; Platform considerations
- Cited APIs: `HomeKit`, `performAccessorySetup(using:completionHandler:)`

### iCloud

- URL: https://developer.apple.com/design/human-interface-guidelines/icloud
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `CloudKit`, `GameSave`

### ID Verifier

- URL: https://developer.apple.com/design/human-interface-guidelines/id-verifier
- Platforms: ios
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `MobileDriversLicenseDataRequest`, `ageAtLeast(_:)`, `MobileDriversLicenseDisplayRequest`, `MobileDriversLicenseRawDataRequest`

### iMessage apps and stickers

- URL: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers
- Platforms: ios,ipados
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Specifications; Icon sizes; Sticker sizes; Platform considerations
- Cited APIs: `Messages`, `MSStickerSize`

### Live Photos

- URL: https://developer.apple.com/design/human-interface-guidelines/live-photos
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations; visionOS
- Cited APIs: `LivePhotosKit JS`, `PHLivePhoto`

### Mac Catalyst

- URL: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst
- Platforms: ipados,macos
- Guidance: [technologies.md](technologies.md)
- Sections: Before you start; Choose an idiom; Integrate the Mac experience; Navigation; Inputs; App icons; Layout; Menus; Platform considerations
- Cited APIs: `UICommand`, `UIKeyCommand`, `UIMenuBuilder`

### Machine learning

- URL: https://developer.apple.com/design/human-interface-guidelines/machine-learning
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Planning your design; The role of machine learning in your app; Critical or complementary; Private or public; Proactive or reactive; Visible or invisible; Dynamic or static; Explicit feedback; Implicit feedback; Calibration; Mistakes; Corrections; Multiple options; Confidence; Attribution; Limitations; Platform considerations
- Cited APIs: `Core ML`, `Create ML`

### Maps

- URL: https://developer.apple.com/design/human-interface-guidelines/maps
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Custom information; Place cards; Displaying place cards in a map; Adding place cards outside of a map; Indoor maps; Platform considerations; watchOS
- Cited APIs: `MapKit`, `MKAnnotationView`, `accessoryOffset`, `MKMapFeatureOptions`, `init(mapItem:displaysMap:)`, `mapView(_:selectionAccessoryFor:)`, `MKOverlayLevel`, `MKSelectionAccessory.MapItemDetailPresentationStyle`, `mapItemDetail(_:)`, `MKStandardMapConfiguration.EmphasisStyle`, `mapItemDetailSelectionAccessory(_:)`, `MapItemDetailSelectionAccessoryStyle`, `MapKit JS`, `selectionAccessory`

### NFC

- URL: https://developer.apple.com/design/human-interface-guidelines/nfc
- Platforms: ios,ipados
- Guidance: [technologies.md](technologies.md)
- Sections: In-app tag reading; Background tag reading; Platform considerations
- Cited APIs: `Core NFC`

### Photo editing

- URL: https://developer.apple.com/design/human-interface-guidelines/photo-editing
- Platforms: ios,ipados,macos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations

### ResearchKit

- URL: https://developer.apple.com/design/human-interface-guidelines/researchkit
- Platforms: ios,ipados
- Guidance: [technologies.md](technologies.md)
- Sections: Creating the onboarding experience; 1. Introduction; 2. Determine eligibility; 3. Get informed consent; 4. Request permission to access data; Conducting research; Managing personal information and providing encouragement; Platform considerations

### SharePlay

- URL: https://developer.apple.com/design/human-interface-guidelines/shareplay
- Platforms: ios,ipados,macos,tvos,visionos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations; iOS, iPadOS, macOS; visionOS; Designing shared activities; Personas; Spatial templates; Custom templates
- Cited APIs: `Group Activities`, `isNearbyWithLocalParticipant`, `SpatialTemplateSeatElement`, `isSpatial`

### ShazamKit

- URL: https://developer.apple.com/design/human-interface-guidelines/shazamkit
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Best practices; Platform considerations
- Cited APIs: `ShazamKit`

### Sign in with Apple

- URL: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Offering Sign in with Apple; Collecting data; Displaying buttons; Using the system-provided buttons; White; White with outline; Black; Button size and corner radius; Creating a custom Sign in with Apple button; Custom buttons with a logo and text; Custom logo-only buttons; Platform considerations
- Cited APIs: `Authentication Services`, `ASAuthorizationAppleIDButton`, `cornerRadius`, `WKInterfaceAuthorizationAppleIDButton`

### Siri

- URL: https://developer.apple.com/design/human-interface-guidelines/siri
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Getting your app to work with Siri; Sharing contextual information; Best practices; Customizing your app’s experience with Siri; Editorial guidelines
- Cited APIs: `App Intents`

### Tap to Pay on iPhone

- URL: https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone
- Platforms: ios
- Guidance: [technologies.md](technologies.md)
- Sections: Enabling Tap to Pay on iPhone; Educating merchants; Checking out; Displaying results; Additional interactions; Platform considerations
- Cited APIs: `ProximityReader`, `PaymentCardReader.Event.readyForTap`, `PaymentCardReader.Event.updateProgress(_:)`, `returnReadResultImmediately`, `prepare(using:)`, `PaymentCardReaderSession.ReadError`, `ProximityReaderDiscovery`

### VoiceOver

- URL: https://developer.apple.com/design/human-interface-guidelines/voiceover
- Platforms: ios,ipados,macos,tvos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Descriptions; Navigation; Platform considerations; visionOS
- Cited APIs: `Accessibility`, `AccessibilityNotification`, `accessibilityElement`, `NSAccessibilityCustomRotor`, `shouldGroupAccessibilityChildren`, `AccessibilityRotorEntry`, `accessibilityHidden(_:)`, `UIAccessibilityCustomRotor`, `isAccessibilityElement`

### Wallet

- URL: https://developer.apple.com/design/human-interface-guidelines/wallet
- Platforms: ios,ipados,macos,visionos,watchos
- Guidance: [technologies.md](technologies.md)
- Sections: Passes; Pass anatomy; Pass field types; Designing passes; Pass styles; Boarding passes; Coupons; Event tickets; Store cards; Poster generic passes; Generic passes; Pass images; Logo; Primary logo; Secondary logo; Icon; Strip image; Thumbnail; Background; Footer; Order tracking; Displaying order and fulfillment details; Identity verification; Platform considerations
- Cited APIs: `ApplePayPaymentOrderDetails`, `FinanceKit`, `FinanceKitUI`, `AddOrderToWalletButton`, `PassKit (Apple Pay and Wallet)`, `PKAddPassButton`, `PKAddPassesViewController`, `PKIdentityButton.Label`, `PKIdentityButton.Style.blackOutline`, `cornerRadius`, `age(atLeast:)`, `PKIdentityIntentToStore`, `PKPassLibrary.Capability.backgroundAddPasses`, `addPasses(_:withCompletionHandler:)`
