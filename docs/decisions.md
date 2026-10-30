# Design decisions

Why the hub works the way it does. Newest first within each area.

## Structure

- **Two places to browse, one action.** The nav is *Work* and *Explore*. *Start a project* is a button, not a section — it creates something, so it opens a focused task (no main nav, just Close).
- **Organised by what people want to do, not by role.** Sales, designers and managers all use the same pages; nothing is labelled “for Sales”.
- **Breadcrumbs, not a back button.** People land deep from search and shared links, where “back” is ambiguous. Trails have meaningful middle steps (*Work › In progress › Project*, *Explore › UI Patterns › Capability › Pattern*). On phones the trail collapses to “‹ Parent”. Going back restores scroll position.
- **Hidden for now:** *How we work*, and the workshop format pages (no documented agendas yet).

## Landing

- Identity first (“Design at Loka, in one place.”), then one sentence with three verbs, then two equal actions: **Start a project** and **Search everything**.
- A live pill replaces the eyebrow: what's new, or “Continue” when a blueprint is open.
- Two section cards (Work, Explore), each with real-need shortcuts.

## Work

- **Status by fill level, in black and white:** Scoping (empty, dashed) → In progress (half) → Shipped (full, with a check). Readable at a glance without colour.
- **“Now”, not stages.** In-progress projects show a free line written by the team, because the process differs per project.
- Project pages: problem · what we built · what happened / now, the patterns used (live), and an *AI Card → Capability → Pattern* trace.

## Start a project (blueprint)

- **Sections, not steps.** Seven optional sections in any order; progress reads “n of 7 sections filled”.
- **The blueprint is the section list** — click any section to jump to it.
- Paths only prefill: new client, existing project, Loka project, or a sample client (nothing saved).
- The finished blueprint has Edit / Add per section and *Add to Work* (creates the project as Scoping).

## Explore

- **Real tools first**, workshop formats as a light list, system map last.
- **One template for every tool page:** header with one primary action → *In one minute* → the tool itself (the only variable block) → detail on demand → seen in our work → facts.
- The type of a resource decides its group and template — adding a tool means filling data, not designing a page.

## Visual & interaction

- Interface in black, grey and white; colour only in visuals. Inter for the UI; Helvetica Neue on the cards, as in the deck.
- One motion system: shared durations and a spring curve; hover only on pointer devices; press feedback everywhere; focus rings that settle into place; everything off under *Reduce motion*.
- **No hover underlines.** Links reveal an arrow or dim, rows get a soft plate, card content zooms inside its frame.
- Features that don't exist yet are shown as **disabled buttons with a “Soon” tag** (*Start a draft*, *Add to a draft*).

## Open

- **Shared storage** for blueprints and added projects (today: per browser).
- **Content to replace or review:** project data is sample; card needs/limits exist for five cards; workshop “Use when” lines need team review.
- **Future:** workshop agendas and resources, guides, *How we work*, the draft builder connection from the hub.
- **Undecided:** whether Work gets a *Present* mode for client calls.
