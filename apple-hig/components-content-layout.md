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
