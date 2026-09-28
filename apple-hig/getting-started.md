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
