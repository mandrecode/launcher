# Owned UI conventions

Contract per screen: immutable UiState/UiEvent/UiEffect; StateFlow/UDF; thin ViewModel with no Activity/Context; Screen coordinates lifecycle/navigation/platform launches; Content renders state and callbacks. Persist critical permission/setup requests with acknowledgement rather than relying solely on one-shot effects.

Shared Material 3 Expressive design system: semantic surface roles, typography/motion/haptics, split settings rows, dialogs and 48dp interactive targets. Native resources bridge tokens where feasible. Google Sans Flex needs pinned source/hash/OFL notices before import. No proprietary APK asset extraction.

Strings are resources and localization changes travel together. No production previews; debug/screenshot source sets only. Adaptive owned UI uses window classes; native workspace uses native profiles. Predictive Back must support cancellation, sheets, editor and IME without double handlers. Test RTL/large text/light/dark. Real widget/provider UI remains provider-controlled.
