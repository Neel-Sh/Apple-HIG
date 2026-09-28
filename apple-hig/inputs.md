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
