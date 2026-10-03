# Domain ownership

One pure Kotlin domain module, organized by capability. No Android, Compose, Room/DataStore types or native Launcher3 classes. Business ports define needed capabilities; adapters translate results into typed success/unavailable/permission-lost/unknown states. Do not invent a modes-domain module without an accepted ADR.

Use injected clock/dispatchers where needed; time rules are deterministic and testable for DST/timezone/overnight boundaries. Resolution is stable under overlap. Critical operations are durable and idempotent. Simple settings need no use-case wrapper unless orchestration grows. Test invariants and failure boundaries, not one-to-one implementation details.
