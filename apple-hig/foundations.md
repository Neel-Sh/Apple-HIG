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
