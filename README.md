# Builders — Design at Loka

The Product Design hub: the work Design has built, the tools behind it, and one place to start something new.

It serves three groups without labelling anyone by role:

- **Sales** — show clients real work and set honest expectations about AI.
- **Designers** — find tools and patterns, and start new projects from a shared method.
- **Managers** — see what Design is working on and how far along it is.

**Live prototype:** <https://claude.ai/artifact/WrkumH6buxNVsfCxaNjxWv>
**Designs:** Figma — *AI OS — Exploration*, page **v2 · Builders hub** (section *Site map — shareable*).

---

## Run it

The hub is one self-contained HTML file. No server, no install.

```bash
open index.html            # macOS
xdg-open index.html        # Linux
```

## Build it

`index.html` is generated. Edit the sources, then rebuild:

```bash
python3 build.py
```

Python 3.8+ only — no packages needed. Commit the rebuilt `index.html` with your source changes.

## Structure

```
├── index.html                      ← generated, the hub itself
├── build.py                        ← assembles index.html
├── src/
│   └── hub.html                    ← the hub: markup, styles, data, logic
├── vendor/
│   └── ui-patterns-library.html    ← the UI Patterns library, used as-is
├── assets/
│   └── fronts/<family>.webp        ← AI Card family fronts, exported from Figma
└── docs/
    └── decisions.md                ← design decisions and what's still open
```

## How the pieces connect

```
AI Card ──► Capability ──► Pattern ──► Project
(24, 6 families)  (12)      (31, live)   (Work)
```

- **AI Cards** are rebuilt in code from the Figma deck values (colour, glow, grain, type). The six family fronts are WebP exports.
- **Capabilities and patterns** come straight from the UI Patterns library: names, descriptions, surfaces, use/avoid, pairings, and every live demo. Demos run inside shadow roots so the hub's styles never touch them.
- **The system map** (`MAPN` in `src/hub.html`) links each card to capabilities and patterns. Every “See it in a product”, card detail and project trace reads from it.
- **Projects** (`PROJECTS` in `src/hub.html`) are sample data for now.

## Common changes

| To… | Edit |
|---|---|
| Add or update a pattern | `vendor/ui-patterns-library.html` — then rebuild |
| Change which patterns a card maps to | `MAPN` in `src/hub.html` |
| Add a project | `PROJECTS` in `src/hub.html` |
| Card limits, needs, pairings | `DETAIL` in `src/hub.html` |
| Re-export a card front | Figma → PNG @2x → convert to WebP → `assets/fronts/<family>.webp` |
| Add a workshop format | `FORMATS` in `src/hub.html` |

Family ids: `understand`, `communicate`, `think`, `action`, `explain`, `collab`.

## Design rules

- **Colour lives in the visuals only.** The interface is black, grey and white; colour appears in AI Cards, live patterns and project previews.
- **Show, don't tell.** Patterns are always live demos, never screenshots. No placeholder visuals.
- **No rigid process.** Blueprints are seven optional sections, filled in any order. Work shows a free “Now” line, not fixed stages.
- **Every page answers:** where am I, what can I do here, where do I go next.

More in [`docs/decisions.md`](docs/decisions.md).

## Accessibility & behaviour

- Light and dark mode — follows the system until someone picks; picking the system's own theme returns to following it.
- Keyboard: ⌘K / Ctrl K opens search; every control has a visible focus ring; search is a proper combobox.
- Respects *Reduce motion*.
- Responsive down to phone width; search becomes full-screen on phones.

## Storage

Blueprints in progress and projects added from a blueprint are saved in the browser (`localStorage`, keys `builders:*`). They are per person and per browser — a shared backend is on the roadmap.
