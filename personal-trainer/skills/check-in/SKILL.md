---
name: check-in
description: Logs the user's workouts, weigh-ins and how their week went, and adjusts their targets or training from the trend. Use when the user reports a session ("I did legs", "bench 80 kg for 8"), a weight or measurement, what they ate, or asks "how am I doing", "am I on track", "how's my progress".
---

# Check in

Record what the user reports in `log.md`, then judge their progress from their own numbers. `<plugin>` is the plugin's root folder (`${CLAUDE_PLUGIN_ROOT}` in Claude, `../../` from this skill's folder elsewhere). Read `<plugin>/references/safety.md` first: it decides whether you may adjust anything.

## 1. Log

Append to `log.md` under today's date. Never edit old entries.

- Weigh-ins: weight, and waist if they give it. Morning, after the toilet, before food. Daily or a few times a week both work; if weighing makes them anxious, once a week is fine.
- Sessions: exercise, sets × reps × weight, and how hard it felt. If a report is ambiguous ("3x9, 3x8"), log your best reading and ask.
- Food: whether they roughly hit their protein and calories, and anything that got in the way.

If they ask how they're doing, answer from the log; don't just log.

## 2. Judge the trend

- **Weight:** compare this calendar week's average weigh-in with last week's, never single days. Compare the weekly change with the target rate in `plan.md`.
- **Strength:** is each main lift going up in reps or weight over the last 2–3 weeks?
- **Adherence:** sessions done against planned, and protein days hit.

## 3. Adjust

With a safety flag, never cut calories, add them back if weight is falling, and keep following the training rules below. With a warning sign, new or on file in `profile.md`, don't cut calories or add training. Otherwise, only change targets after 2–3 weeks of data, and say why.

- Losing fat, and the weekly average dropped less than half the target rate for two weeks while adherence was good: cut 100–150 kcal a day (mostly from carbs and fat, never below the floors), or add 2,000 steps a day.
- Losing more than 1 % of body weight a week, or strength is falling: add 100–150 kcal.
- Building muscle, and weight isn't moving up: add 100–150 kcal.
- A lift stalled for 3 sessions: drop it 10 % and build back, or swap to a close variation.
- Missed sessions keep piling up: shorten the sessions or cut a day rather than keep a plan they don't do.
- Lifts that hit the top of their rep range on every set: add the smallest weight step next time.

Write any change into `plan.md` with the date and the reason.

## 4. Reply

Three to five lines: what the numbers say, one thing they did well, the one change (or "no change, keep going"), and what to report next time.
