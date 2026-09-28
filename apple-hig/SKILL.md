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
