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
