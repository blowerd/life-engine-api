# 🧙‍♂️ life-engine-api

> A tiny local “quest director” that turns everyday chores into small, gentle quests.

`life-engine-api` is the brain behind Life Engine — a cozy, game-inspired system that surfaces 2–3 reasonable tasks each day without guilt, dashboards, or productivity pressure.

Instead of managing your life, it simply whispers:

“Here are a few things you could do today.”

---

## 🌿 Vision

Make everyday self-care feel lighter and more tangible by:

- limiting choices
- encouraging small wins
- using playful language
- powering physical artifacts (quest board, desk companion, etc.)

Tone:

**tavern quest board**, not **corporate task manager**.

---

## 🧠 Philosophy

- Local-first > cloud
- Deterministic > “smart”
- Gentle > urgent
- Physical-first > screen-first
- Toy-like > tool-like
- Small > comprehensive

If it feels like enterprise software, it probably doesn’t belong here.

---

## ⚙️ Current features

- simple YAML chore catalog
- SQLite completion history
- recurrence windows (min/max days, not deadlines)
- daily quest generator (2–3 tasks)
- local REST API + CLI

No accounts.  
No streaks.  
No analytics.  
No shame mechanics.

---

## 🏗 Architecture

              life-engine-api (this repo)
                     │
        ┌────────────┴────────────┐
        │                         │
   quest board client        familiar client
   (display only)            (feedback only)


---

## 🗂 Project structure

life-engine-api/
│
├─ app/
│   ├─ main.py          # FastAPI server
│   ├─ generator.py     # quest selection logic
│   ├─ scoring.py
│   ├─ models.py
│   ├─ db.py
│   ├─ catalog.yaml     # human-editable tasks
│   └─ config.yaml
│
├─ cli/
│   └─ today.py         # print today's quests
│
├─ tests/
└─ README.md


---

## 🌱 Motivation

Sometimes you don’t need better planning.

You just need:

- fewer choices
- visible progress
- a gentle nudge

Life Engine exists to lower activation energy, not optimize your life.

