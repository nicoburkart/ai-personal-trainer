---
name: setup
description: First-run interview that personalizes the personal trainer. Use when there is no profile.md yet, or when the user says "set me up", "start", "personalize", "change my goal", "I moved", or their weight, schedule or goal has changed a lot.
---

# Setup

Interview the user, then write `profile.md`, `plan.md` and `log.md` in their working folder. Keep it to a few minutes. `<plugin>` below is the plugin's root folder (the one containing `skills/` and `references/`; `${CLAUDE_PLUGIN_ROOT}` in Claude, `../../` from this skill's folder elsewhere).

If `profile.md` already exists, this is an update: read the three files, ask only about what changed, and edit in place. Keep the `Safety flags` and `Warning signs` lines and everything under Shopping, and append to `log.md`.

## 1. Folder

If the working folder holds other things, suggest a dedicated folder (for example `Personal Trainer`) that they open every time, so their profile and log stay together. Continue in whatever folder they choose.

## 2. Interview

Ask one short question at a time, in plain words, and accept rough answers. Offer examples so they can answer fast. If they give several answers at once, take them all and skip ahead.

1. Main goal: lose fat, build muscle, get stronger, or get fitter? Any date (holiday, wedding, event)?
2. Age, sex, height and current weight. Ask which units they use (kg/cm or lb/ft) and keep them for everything you show; convert to kg and cm for the maths.
3. Health, optional: "Any health conditions or medication, pregnancy or breastfeeding, or past problems with eating or dieting? You can skip this."
4. Activity outside training: mostly sitting, on their feet a lot, or physical job? Rough daily steps if they know.
5. Training: how many days a week can they train, how long per session, and where (gym, home with what equipment, outdoors)? How long have they trained, and any injuries or exercises they hate?
6. Food: diet style (anything, vegetarian, vegan, halal...), allergies, foods they love or won't eat, how much they want to cook (time per day), and roughly how many meals a day.
7. Shopping: which supermarket, and which country/city? Weekly food budget?

Then apply `<plugin>/references/safety.md`. Record the result as a `Safety flags:` line in `profile.md` (`none`, or the flags that apply). If a flag applies, do what that file says for it, and leave any target it removes out of steps 3 and 4.

## 3. Targets

Work out daily calories and protein with `<plugin>/skills/setup/references/targets.md`. Show the result in three lines: calories, protein, and the expected weekly change, each with its one-line reason. Ask if it looks right before saving.

## 4. Write the files

- `profile.md`: everything they told you, grouped under Goal, Body, Health, Activity, Training, Food, Shopping, with today's date, plus the `Safety flags:` line.
- `plan.md`: Targets (calories, protein, carbs/fat split, expected rate of change, with the reasoning), and a Training section: the weekly split, the exercises per day with sets × reps and starting effort (leave 1–3 reps in reserve), and how to progress. Use the same `targets.md` for the training rules.
- `log.md`: a heading and the first entry: today's date and starting weight.

## 5. Next steps

In two lines, offer:

1. Plan this week's meals and shopping list now (`plan-week`).
2. Connect their supermarket so the agent can fill the cart (`connect-supermarket`).
