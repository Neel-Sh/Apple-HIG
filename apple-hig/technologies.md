# Technologies

Official section: https://developer.apple.com/design/human-interface-guidelines/technologies

Branded technologies have artwork and wording rules. Use the system button or the official asset. Do not redraw logos. Open the official page before shipping Apple Pay, Sign in with Apple, HomeKit, AirPlay, Activity, or Wallet visuals.

## AirPlay

URL: https://developer.apple.com/design/human-interface-guidelines/airplay

- Use the system route picker or `AVPlayerViewController` so AirPlay targets, audio, and video behave correctly.
- If you draw the icon yourself, use Apple's AirPlay icon (black, white, or a single custom color on a clear background). Do not recolor pieces differently, add shadows, or rotate it.
- Say "AirPlay", not "Airplay" or "air play". Say "AirPlay Audio" or "AirPlay Video" only in the way the branding page allows.
- Video can play externally (`usesExternalPlaybackWhileExternalScreenIsActive`). The in-app UI should show that playback moved, with a way to bring it back.
- Do not auto-route to a nearby TV without an explicit choice.

## Always On

URL: https://developer.apple.com/design/human-interface-guidelines/always-on

Platforms: iOS StandBy / Lock Screen and watchOS always-on display.

- The dimmed, wrist-down, or nightstand state is still your UI. Information must remain correct and legible at lower brightness.
- Remove or freeze decorative motion, video, and high-brightness fills. Redact secrets (message bodies, balances) the way the Lock Screen does when the system is locked.
- Update rarely. A ticking animation that keeps the display hot is a bug.
- Provide a layout that works when color is reduced and the screen is dim.

## App Clips

URL: https://developer.apple.com/design/human-interface-guidelines/app-clips

Platforms: iOS, iPadOS.

- An App Clip does one task immediately (pay, order, unlock) and finishes in seconds. No account wall, no onboarding carousel.
- The card is the invitation: a short title, a specific action, and your real app icon. The image and text must match the physical place or QR the person just used.
- Preserve privacy. Do not request tracking. Ask for location or notifications only if that invocation needs them, and notifications from a clip are rare.
- Offer the full app at the end with `SKOverlay`, not a modal nag at the start.
- App Clip Codes use Apple's code design. Keep the required clear space, test the printer's calibration, and use the messaging patterns on the official page. Do not redraw the code or add a logo inside the mark.
- Business clips that take payment use Apple Pay where it fits.

## Apple In-App Purchase

URL: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase

- Use StoreKit UI for purchases, offer-code redemption, refunds, and subscription management (`presentOfferCodeRedeemSheet`, `showManageSubscriptions`, `beginRefundRequest`). Do not send people to a website to buy digital goods the guidelines require to go through IAP.
- Show the price the system returns, including introductory and trial terms, before the person confirms. The system sheet is the confirmation.
- Family Sharing: if the product supports it, say so. Do not promise sharing for a product that is not set up for it.
- Subscriptions: explain what they get, the length, and that it renews. Manage and cancel are available in-app via the system manage-subscriptions UI.
- Restore purchases is available and not hidden. Help for billing problems points at Apple's billing, not a custom blame screen.
- watchOS purchases can confirm on the watch or route to iPhone. Do not build a long storefront on the watch.

## Apple Pay

URL: https://developer.apple.com/design/human-interface-guidelines/apple-pay

- Offer Apple Pay as a payment method alongside others, not as a banner that blocks checkout. If they cannot pay, follow `applePayCapabilities` and show Set Up only when setup is the real next step.
- Use the official Apple Pay button (`PKPaymentButton` / the web equivalent). Types include plain Apple Pay and Set Up Apple Pay. Styles are black, white, and white with outline. Do not change the logo, set a non-approved corner radius, or stretch the mark.
- Minimum size and clear space are on the official page. The button is at least as prominent as other checkout buttons.
- The payment sheet is the system sheet (`PKPaymentAuthorizationController`). You customize line items (`paymentSummaryItems`), shipping, and contact fields. You do not rebuild the sheet.
- Put the most likely shipping and contact defaults in the sheet so checkout is a confirm, not a form.
- Errors: data problems name the field; processing problems say the charge failed and that they can try another method. Do not dump gateway codes.
- Subscriptions and donations have specific button and sheet setups. Use the donation wording only for real donations.
- Say "Apple Pay", not "ApplePay". Do not say "Apple Pay" for a payment that does not use it.
- The Apple Pay mark (not the button) is for marketing placements described on the page. Do not invent a third graphic.

## Augmented reality

URL: https://developer.apple.com/design/human-interface-guidelines/augmented-reality

Platforms: iOS, iPadOS, visionOS. ARKit.

- AR shows virtual content in the real world. People must understand what is real. Do not occlude hazards.
- Coach placement (`ARCoachingOverlayView`) until tracking is good enough. Tell them to move the device slowly if you need a surface.
- Placement: a preview of the object follows the ray (`ARTrackedRaycast`) before they commit. Objects sit on the detected plane with believable scale and occlusion.
- Interactions: direct (tap the object) and simple. Pinch to scale only if the object should resize. Provide a reset.
- Multiuser (`isCollaborationEnabled`) shows who is here and what they are moving. Do not share camera frames silently.
- Interruptions (phone call, backgrounding) pause the session and tell them when tracking is lost, with a concrete fix (more light, slower motion).
- Icons: use the system AR mark when you label an AR action. visionOS immersive experiences follow the immersive page; do not also slap an AR badge on ordinary windows.

## CareKit

URL: https://developer.apple.com/design/human-interface-guidelines/carekit

Platforms: iOS, iPadOS.

- CareKit apps handle health tasks, charts, and contacts. Be calm, clear, and honest. This is not a place for playful error copy.
- Data and privacy: say what you store and why. HealthKit access uses the Health permission model and only the types you need. Motion and photos are separate asks, in context.
- Use CareKit task cards for "to do" care items: title, schedule, completion. Charts use the CareKit chart styles so trends are readable. Contact views make the care team reachable.
- Notifications for a dose or exercise are timely and specific, and easy to turn off.
- Use CareKit symbols as designed. Do not remix the mark into a logo.

## CarPlay

URL: https://developer.apple.com/design/human-interface-guidelines/carplay

Platform: iOS via the car display. CarPlay is a driving UI, not a phone UI stretched wide.

- Information is glanceable. Type is large. Actions are few and available without precise taps. No reading, no dense settings, no video.
- Audio apps: now playing, playlists, and simple lists. Navigation and communication follow the CarPlay templates for that category. You cannot invent a freeform layout.
- Color supports glanceability and Dark appearance. Icons are simple.
- Errors say what to do in the car ("Connect iPhone") in one line.
- The iPhone may show a companion state, but the driver interacts with the car screen. Do not require looking at the phone to complete a driving task.
- Follow the entitlement and template rules for your category. Unsupported apps do not belong on the car display.

## Game Center

URL: https://developer.apple.com/design/human-interface-guidelines/game-center

- Access Game Center with the system access point. A custom UI still has to offer the same sign-in and profile actions, and it must not mimic the system UI in a misleading way.
- Achievements: a clear name, a description of how to earn it, and artwork in the required template. Show progress for incremental achievements. Do not create achievements for spending money.
- Leaderboards: say what the score means and the time scope. Let people view friends and global when you have both. Do not shame a low score with custom chrome.
- Challenges and multiplayer use the system flows so invites and turns are consistent.
- tvOS and watchOS surfaces are reduced. A leaderboard on the watch is a summary, not a full browser.

## Generative AI

URL: https://developer.apple.com/design/human-interface-guidelines/generative-ai

- Say when content is generated. Do not present model output as a human's work, a measurement, or a fact you verified.
- Describe what the feature does in the UI, not the model brand, unless attribution is required.
- Privacy: prefer on-device (`FoundationModels`) when it meets the need. If data leaves the device, say so before it happens. Do not use private content to train a model without explicit permission.
- Inputs: show what the person is sending. Let them edit or cancel. Do not silently attach contacts, photos, or location.
- Outputs: make them editable, copyable, and dismissible. Offer a way to try again or report a bad result. Do not auto-post or auto-send.
- Mistakes are normal. Do not show a single generated answer as the only path for a high-stakes decision (health, finance, safety). Provide a non-generated way to finish the task.
- Continuous improvement (feedback, ratings on results) is opt-in and specific.

## HealthKit

URL: https://developer.apple.com/design/human-interface-guidelines/healthkit

Platforms: iOS, iPadOS, watchOS.

- Request only the sample types you need, when the person uses that feature (`requestAuthorization`). Explain the benefit in your words, then let the system sheet list the types.
- If they deny access, the feature degrades honestly. Do not re-prompt in a loop.
- Activity rings: use `HKActivityRingView` only for real Move, Exercise, and Stand data. See Activity rings.
- The Apple Health icon is used only to refer to the Health app, following the artwork rules. Do not modify it or imply Health endorses your product.
- Write copy that is careful and not diagnostic unless you are qualified and permitted. "A high heart rate reading" is not "You are having a heart attack."
- Clinical and sensitive types deserve extra clarity about storage and sharing.

## HomeKit

URL: https://developer.apple.com/design/human-interface-guidelines/homekit

- Use HomeKit words the way the Home app does: homes, rooms, accessories, services, characteristics, actions, scenes, automations, zones.
- Setup uses the system accessory setup (`performAccessorySetup`). Names should be speakable ("Kitchen lamp"), because Siri uses them.
- Do not invent a parallel house model that drifts from the Home database.
- Cameras: show a live view with clear recording state. Do not hide that a camera is recording.
- Icons: black, white, or single-color HomeKit badge from Apple's artwork. Say "HomeKit" and "the Home app" correctly. Works with Apple Home is a specific badge; do not paraphrase it into a custom seal.
- Actions must show success or failure. A light that did not turn on is not a silent no-op.

## iCloud

URL: https://developer.apple.com/design/human-interface-guidelines/icloud

- If the feature needs iCloud, say so and send people to the system sign-in if they are signed out. Do not build a fake iCloud login.
- Documents and data in iCloud show sync state: synced, syncing, conflict, or full. Conflicts are resolvable, not silently overwritten.
- Storage-full errors tell them what failed and link toward managing storage.
- Games that save progress use the system game-save patterns (`GameSave`) or CloudKit with a visible account. Progress should not vanish on reinstall if you promised cloud save.
- Key-value and CloudKit data still follows privacy rules. Do not sync secrets that belong in the keychain unencrypted.

## ID Verifier

URL: https://developer.apple.com/design/human-interface-guidelines/id-verifier

Platform: iOS.

- Request only the claims you need (for example age over a threshold via `ageAtLeast`) rather than a full license dump.
- Use the system presentation (`MobileDriversLicenseDisplayRequest`, data request, or raw data request as appropriate). The person sees what will be shared and can refuse.
- Do not store document images or raw data "just in case" if a boolean claim was enough.
- Explain why you are checking, in one sentence, before the system sheet.

## iMessage apps and stickers

URL: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers

Platforms: iOS, iPadOS.

- An iMessage app is used inside a conversation. The UI is compact, fast, and returns to the transcript.
- Stickers are expressive and respect the size classes (`MSStickerSize`). Edges are clean. No tiny unreadable text.
- App icons for the iMessage drawer follow the sticker and iMessage icon sizes on the spec page.
- Do not trap people in a store. Sending a sticker should feel like one tap.
- Respect the conversation's participants. Do not auto-send.

## Live Photos

URL: https://developer.apple.com/design/human-interface-guidelines/live-photos

- Play a Live Photo on press or hover, not in a loop on a static grid. People expect a still until they interact (`PHLivePhoto`).
- Mark Live Photos with the system badge so they are distinct from stills.
- Edits should keep or clearly discard the motion. Do not export a still and still call it a Live Photo.
- visionOS can present a Live Photo spatially when the asset supports it. Do not fake spatial from a normal photo.
- Web uses LivePhotosKit JS only with the system playback behavior.

## Mac Catalyst

URL: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst

- Decide the idiom up front: "Optimize Interface for Mac" or a scaled iPad idiom. Optimized Mac is the one that should feel like a Mac.
- Navigation: sidebars and split views, not a phone tab bar stretched across a monitor. Multiple windows for documents.
- Inputs: pointer hover, keyboard shortcuts (`UIKeyCommand`), and menus (`UIMenuBuilder`, `UICommand`). Right-click context menus.
- App icon is a Mac icon, not a rounded iOS icon sitting on a squircle you drew.
- Layout: use the Mac toolbar and settings window. Density can increase. Touch-sized padding everywhere looks wrong on a Mac, but do not go so dense that rows are hard to click.
- Settings live under the App menu (Settings…), not inside a tab called Settings if you can use a settings scene.

## Machine learning

URL: https://developer.apple.com/design/human-interface-guidelines/machine-learning

Design the role before the model:

- Critical vs complementary: if the model is wrong, can the person still finish? Critical predictions need confirmation.
- Private vs public: on-device (`Core ML`, Create ML) is the default for personal data.
- Proactive vs reactive: proactive suggestions can be ignored. Do not pop a modal for a guess.
- Visible vs invisible: invisible corrections (autocorrect) need an undo. Visible suggestions need a reason when they affect a decision.
- Dynamic vs static: if the model changes, the UI should not jump under the person's finger.

Feedback and trust:

- Explicit feedback (correct / not useful) and implicit feedback (they edited the suggestion) should actually update behavior you claim updates.
- Calibration: show confidence only if people can interpret it. A raw percentage is often worse than "likely" plus an easy override.
- Mistakes: apologize by fixing, not by a cute error. Always offer correction and a manual path.
- Multiple options beat a single opaque answer when taste or ambiguity is involved.
- Attribution: say when a prediction is automatic. Limitations belong in the UI for features that can harm (health, finance, people detection), not only in a privacy policy.

## Maps

URL: https://developer.apple.com/design/human-interface-guidelines/maps

- Use MapKit. Do not screenshot Apple Maps. Respect the legal attribution MapKit already shows; do not cover it.
- Standard gestures: pan, zoom, rotate. Do not disable them unless the map is a static figure, and then consider an image.
- Annotations (`MKAnnotationView`) are for a few places, not thousands of raw pins. Cluster. The selected pin shows a callout with a title and one action.
- Overlays (`MKOverlayLevel`) match the data (route, geofence). Do not paint the whole map a brand color.
- Place cards: use the system place card for a POI (`mapItemDetailSelectionAccessory`, selection accessory APIs) instead of a custom business page that hides hours, phone, and directions.
- Indoor maps: show the level the person is on and a level picker.
- watchOS maps are simplified and for a glance or a turn, not a browsing map.
- Privacy: show the location indicator only while location is in use, and use the system authorization styles.

## NFC

URL: https://developer.apple.com/design/human-interface-guidelines/nfc

Platforms: iOS, iPadOS. Core NFC.

- In-app reading: show a system session sheet that says what to scan and when it succeeds or fails. Keep the phone message aligned with the real tag.
- Background tag reading launches your app only for tags you are entitled to read. The launch should land on that tag's task, not the home screen.
- Do not scan in the background for unrelated traffic. Failures ("tag moved", "not supported") tell them to try again in plain language.

## Photo editing

URL: https://developer.apple.com/design/human-interface-guidelines/photo-editing

Platforms: iOS, iPadOS, macOS. PhotoKit.

- Non-destructive edits are the default. People can revert. Show that an image has adjustments.
- The original stays in the library unless they explicitly export a flattened copy. Respect edits from other apps (adjustment data).
- Tools are familiar: crop, light, color, filters. Destructive actions (delete) confirm.
- Extensions that edit inside Photos should feel like a focused tool and return to Photos when done.
- Do not upload a library to train a model because the person cropped one photo. Ask if a feature needs the image to leave the device.

## ResearchKit

URL: https://developer.apple.com/design/human-interface-guidelines/researchkit

Platforms: iOS, iPadOS.

Onboarding is a fixed ethical sequence:

1. Introduction: who you are, what the study is, and that it is research.
2. Eligibility: stop people who should not enroll. Be clear, not coy.
3. Informed consent: readable, sectioned, with comprehension checks where appropriate. Consent is not a terms-of-service dump.
4. Permission to access data: only after consent, only the types the study needs, using system prompts.

- During the study, tasks are short, progress is visible, and withdrawal is always available and as easy as joining.
- Results and encouragement do not overclaim. A survey app is not a diagnosis.
- Protect identity. Do not display participant identifiers on shared screens. Follow the consent about what you store.

## SharePlay

URL: https://developer.apple.com/design/human-interface-guidelines/shareplay

- SharePlay is a shared activity inside FaceTime or a group session. People can see who is participating and leave at any time.
- Start from the system share or the FaceTime UI (`promoting` the activity), not a custom lobby that hides who is in the call.
- Sync state so late joiners catch up (`synchronizing`). One person scrubbing video should not silently desync everyone without a visible state.
- Spatial sessions (visionOS) use spatial templates (`SpatialTemplateSeatElement`, `isSpatial`, nearby participants). Seats are suggestions. Do not require a body pose or a specific chair.
- Personas represent people. Do not overlay content that covers someone's face by default.
- A shared activity still works alone, so the app is useful without a call.

## ShazamKit

URL: https://developer.apple.com/design/human-interface-guidelines/shazamkit

- Match audio the person chooses to identify. Show listening state, then the match or a clear miss.
- Do not listen in the background. Microphone use is obvious and ends when the match ends.
- Display the song, artist, and artwork you are allowed to show. Provide the next action they expect (open in a music app) without implying Apple Music exclusivity unless that is the real link.
- Say Shazam correctly if you use the name. The recognition UI should not clone the Shazam app's branding beyond what the kit provides.

## Sign in with Apple

URL: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple

- If you offer other third-party social logins, offer Sign in with Apple (`ASAuthorizationAppleIDButton`, AuthenticationServices).
- Use the system button. Styles: black, white, white with outline. The logo and the label ("Sign in with Apple", "Sign up with Apple", "Continue with Apple") stay together. Do not recolor the logo separately, change the font, or crop the mark.
- Minimum size, corner radius, and clear space are specified on the official page. The button is at least as prominent as other login buttons.
- Custom buttons are a last resort and must follow the logo-and-text or logo-only measurements exactly. Prefer the system control.
- Ask only for the name and email scopes you need. If you ask, use the values Apple returns. Hide My Email is a real address; do not reject it.
- Do not require a second password after Sign in with Apple. Account settings still offer account deletion.

## Siri

URL: https://developer.apple.com/design/human-interface-guidelines/siri

- Integrate with App Intents so Siri, Spotlight, and Shortcuts see the same actions. Donate or provide phrases that match real tasks.
- Resolve parameters with short follow-ups, not a dumped form. Confirm destructive or paid actions.
- Dialog is short, spoken-friendly, and consistent with on-screen snippets. No emoji salad, no marketing adjectives.
- Custom vocabulary and names should be pronounceable.
- Do not say "Hey Siri" inside the app as a branded button unless you are using a system API that requires that wording. Do not impersonate Siri's voice or the Siri orb.
- Errors tell people what Siri could not do and the in-app alternative.

## Tap to Pay on iPhone

URL: https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone

Platform: iOS. ProximityReader.

- This is a merchant experience. The customer sees the iPhone as the terminal. The UI must be readable by someone standing across a counter.
- Enablement and education screens use Apple's required flows (`ProximityReaderDiscovery`, prepare, progress). Do not skip the merchant education that the API requires.
- Checkout: show the amount clearly, then the ready-for-tap state (`readyForTap`) using the system UI. The customer taps their card or phone on the indicated area.
- Results: success and failure are obvious from across the counter, with the amount and a short status. Failures (`ReadError`) say to try again or use another method. Do not show raw error codes.
- Do not brand the payment surface so heavily that the Apple-required marks and instructions disappear.
- Accessibility: the merchant can complete the flow with VoiceOver. The customer-facing side stays simple.

## VoiceOver

URL: https://developer.apple.com/design/human-interface-guidelines/voiceover

- Every control has a label, a value when it has one, and a trait (button, header, adjustable). Decorative views are hidden (`accessibilityHidden`, `isAccessibilityElement = false`).
- Group related elements (`shouldGroupAccessibilityChildren`, `accessibilityElement`) so VoiceOver does not land on each glyph of a composite control.
- Order follows visual order, which follows reading order, including RTL.
- Custom controls implement activation, increment, and escape. Charts can expose a summary plus an audio graph or rotor (`AccessibilityRotorEntry`, `UIAccessibilityCustomRotor`) rather than a hundred unlabeled marks.
- When content changes, post a notification (`AccessibilityNotification`) only for changes the person needs. Do not spam announcements.
- visionOS: VoiceOver uses look and pinch. Labels must still make sense without seeing hover.
- Test by completing the main task with the screen curtain on.

## Wallet

URL: https://developer.apple.com/design/human-interface-guidelines/wallet

- Passes are added with the system add-pass UI (`PKAddPassesViewController`, `PKAddPassButton`). Use the official Add to Apple Wallet button. Do not redraw it.
- Pass types: boarding pass, coupon, event ticket, store card, poster generic, generic. Pick the type that matches the real-world object. Fields have roles (primary, secondary, auxiliary, header). Do not put a paragraph in the primary field.
- Images: logo, icon, strip, thumbnail, footer, and background have fixed roles and size guidance on the official page. The logo is your mark, legible on the pass color. Do not add extra floating badges the pass style does not support.
- Barcodes must scan. Contrast and quiet space matter more than decoration. Test a printed and a screen scan.
- Updates (gate change, balance) update the pass. Relevance (location, time) should be real so the pass surfaces on the Lock Screen honestly.
- Order tracking uses the Wallet orders model: status, fulfillment, and a clear merchant. Do not fake shipping state.
- Identity: verification passes and ID in Wallet follow the identity flows. Do not store an ID image in your own gallery as a substitute.
- watchOS shows a simplified pass. The important field (barcode, balance, seat) must still be usable on the wrist.
