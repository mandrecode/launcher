# Platform and persistence conventions

Implement pure domain ports in platform/persistence modules. Map Android/Room objects at the boundary. Inject dispatchers; blocking I/O stays off main. Coroutines must preserve cancellation. Never put permission checks or database work in Content composables.

On API 35+, Android is the active rule authority. API 31–34 uses owned profile activation with optional DND contribution; never conflate requested DND with effective system state. Keep backend selection and capability differences explicit. Own-rule observation cannot become a promise to discover other owners' Modes. Respect user-managed policies and snoozes. Use AlarmManager for timing boundaries and deferrable workers for reconciliation; no steady polling loop. Conditional permissions are explained and requested only for selected features.

Room owns metadata/operation journals; Launcher3 owns native workspace items. System APIs, Room and native databases do not share a transaction. Creation/deletion/migration must be idempotent with recovery. Native widget IDs are host-owned; delete only when unreferenced across all screens. Restore remaps rules and rebinds widgets with consent. Hidden profiles and private calendar/search contents never leak to diagnostics.
