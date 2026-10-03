# Dependencies and build ownership

Phase 0 tools: Python 3.11+, Node 22+ and OpenSpec CLI 1.3.0. No Android toolchain is selected yet. Phase 1 must verify latest stable SDK/toolchain releases and pin a tested AGP/Gradle/JDK/Kotlin/KSP tuple before introducing the build.

Use version catalogue/convention plugins, central repositories, verification metadata and appropriate dependency locks. No dynamic versions or wildcard source refs. Update compiler plugins together; keep vendor constraints explicit. Prefer stable releases; expressive UI prerelease adoption requires a recorded exception. Room/Compose/Dagger compatibility is tested, not assumed from version numbers.

Keep Actions SHA-pinned and OpenSpec version-pinned. CI should use public read-only credentials. Do not copy external signing configurations, secrets, release bots or privileged workflows into this repo. Android dependency update configuration starts when a real Gradle project exists.
