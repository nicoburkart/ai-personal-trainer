# AI Personal Trainer

A personal trainer you run in Claude, meant as a starting point. It plans your training and your week of meals around your protein goal, builds the shopping list from real nutrition labels, and fills your supermarket cart where your store has a connector. You always press order yourself.

It is a handful of Markdown files and one small script, so you can read all of it and change it.

## Install

- **Claude desktop app (Cowork):** Plugins → Add marketplace → paste `nicoburkart/ai-personal-trainer` → install **Personal Trainer**. Or download `personal-trainer.plugin` from Releases and use **Upload plugin**.
- **Claude Code:** `/plugin install personal-trainer --marketplace nicoburkart/ai-personal-trainer`
- **ChatGPT / Codex:** `codex plugin marketplace add nicoburkart/ai-personal-trainer`, then `codex plugin add personal-trainer@buildwithnico`

Then open a folder for it (for example `Personal Trainer`) and say **"set me up"**.

## What you need

- A paid Claude plan (Pro or above), or ChatGPT for Codex. Nothing else to pay for.
- Optional: a connector for your supermarket. Say "connect my supermarket". It knows connectors for Mercadona (Spain), Kroger (USA) and Picnic (Netherlands, Germany, France) and sets them up with ordering blocked. With any other store you shop from the list.

## What's inside

Everything is in `personal-trainer/`.

| Path | What it does |
| --- | --- |
| `skills/setup/` | The interview. `references/targets.md` holds the maths for calories, protein and training |
| `skills/plan-week/` | The week of meals and the shopping list |
| `skills/fill-cart/` | Puts the list in your supermarket cart |
| `skills/check-in/` | Logs workouts and weigh-ins and adjusts the plan |
| `skills/coach/` | Every other training or food question |
| `skills/connect-supermarket/` | Sets up a supermarket connector. `references/known-connectors.md` lists the stores |
| `references/safety.md` | The health rules for calories, weight loss and warning signs |
| `scripts/food.py` | Looks up nutrition labels in Open Food Facts |

What it knows about you stays in Markdown files in the folder you work in: `profile.md`, `plan.md`, `foods.md`, `week.md`, `log.md`.

## Make it yours

Fork this repo, then edit the files yourself or ask Claude to. Install your fork the same way, with your GitHub name in place of `nicoburkart`. Ideas for a first change:

- **A weekly run.** Schedule a task (in Cowork: `/schedule`) that says "plan my week". To let it fill the cart without asking, give `fill-cart` a spending limit first.
- **Your health data.** Connect your health or fitness app and tell `check-in` to read your workouts and weight from it.
- **Your supermarket.** Find a connector for your store, have Claude check its code, and add a row to `known-connectors.md`.

## Not medical advice

If you have a medical condition, take medication, are pregnant or breastfeeding, are under 18, or have a history of eating disorders, check with a doctor first. The trainer won't set a calorie deficit in those cases.

## For maintainers

`python3 check.py` validates the plugin and the marketplace. `python3 check.py --build` also builds the Cowork upload, `dist/personal-trainer.plugin`.
