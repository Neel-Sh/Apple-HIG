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
