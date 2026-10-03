# Product scope

**Promise:** a Pixel-like launcher for Android phones, elevated by reliable system-driven Modes and QoL features.

Three layers: clean Launcher3 standalone engine → feasible Pixel presentation → Mandre Launcher additions. This repo starts fresh; MVP findings are historical research, not certified product behavior.

[Capability table](feature-plan.md) covers 103 audited capabilities plus nine foundation/addition rows. [CSV](feature-plan.csv) carries priorities and planned phases. [Reference policy](support-and-reference.md) defines what parity evidence means. [Modes icons](android-modes-icons.md) records exact source resources.

Initial features: owned Android Modes linked to independent native workspaces/backgrounds/grids; optional indicator; real Google Search and At a Glance widgets; owned Wallpaper & Style; optional themed drawer icons; double-tap empty Home to lock. Basic features and safe recovery remain free. Premium presets, extra icon styles, advanced gestures/automation and owned broader search remain later evaluations.

Discard unavailable private predictions, Discover/Smartspace services, proprietary search intelligence and privileged Recents replacement. Adapt blur and achievable animations. Missing Google providers use explicit fallback/configuration states; widgets default to requested-on when supported.

No exact import of Pixel's private workspace database. No general discovery/copy of other owners' Android Modes. Templates must be labelled as rules newly created by Mandre Launcher. Platform quotas and user-managed policies are respected.

Phases: 0 foundation; 1 clean engine and update rehearsal; [1.5 Home presentation evaluation](compose-presentation-evaluation.md) with an explicit native/hybrid/Compose decision gate; 2 Pixel baseline and gesture work; 3 reliable Modes/workspaces; 4 automation/onboarding; 5 QoL/adaptability/restore; 6 beta/distribution. Each phase has its own accepted change and evidence gates; starting phase 0 does not authorize implementation of the others.

Minimum SDK direction: API 31, pending actual port verification. Legacy API 31–34 profiles use local activation and a default-visible pill with permanent alternate Home-menu access; modern API 35+ observes owned system rules. Optional DND integration is separately capability/permission-gated.
