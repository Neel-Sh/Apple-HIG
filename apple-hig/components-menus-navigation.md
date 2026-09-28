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
