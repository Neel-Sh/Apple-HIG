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
