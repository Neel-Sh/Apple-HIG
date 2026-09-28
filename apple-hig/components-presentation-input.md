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
