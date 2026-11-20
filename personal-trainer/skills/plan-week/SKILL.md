---
name: plan-week
description: Plans the user's week of meals and the shopping list that hits their calorie and protein targets, using real nutrition labels. Use when the user says "plan my week", "what should I eat this week", "make my shopping list", "meal plan", or "I'm going shopping".
---

# Plan the week

Write `week.md`: a day-by-day meal plan and one shopping list, built from foods the user actually buys, that lands within ±5 % of their daily calories and at or above their daily protein. `<plugin>` is the plugin's root folder (`${CLAUDE_PLUGIN_ROOT}` in Claude, `../../` from this skill's folder elsewhere). Follow `<plugin>/references/safety.md`. Where it leaves `plan.md` without targets, plan regular meals with a protein source in each and skip the calorie and protein rules below.

## 1. Read

Read `profile.md` (food preferences, cooking time, meals a day, supermarket, budget, safety flags), `plan.md` (targets, training days), `foods.md` if it exists, and the last two weeks of `log.md` for anything that changes the plan (missed meals, foods they're sick of, a new weight). If there's no profile, run `setup` first.

## 2. Foods with real numbers

- Start from `foods.md`. If it's thin, ask what they usually buy (5–10 staples).
- Look up each food without numbers: `python3 <plugin>/scripts/food.py search <name> --country <their country>`, or `... barcode <ean>`. The script spaces searches out on its own; run lookups one at a time. If a supermarket connector is connected, search the store first for the exact product, pack size and price, then look up its barcode.
- Use the store's product when you can, so the list matches what they'll actually buy. Fresh meat, fish and produce usually aren't in Open Food Facts: use the pack label or a standard value and mark it `(label)` or `(standard)`. Skip any result without both calories and protein.
- Save every food you used to `foods.md` as a table: food, store product name, pack size, kcal / protein / carbs / fat per 100 g, price, barcode, source.

## 3. Plan

- Repeat meals. Most people eat 3–5 different meals a week; plan that way unless they asked for variety. Respect their cooking time.
- Put more carbs around training days if they train hard; otherwise keep days similar.
- Give each main meal a protein source of at least 0.4 g per kg of body weight.
- Compute each day's calories and protein from `foods.md` (grams × per-100 g ÷ 100) and adjust portions until every day is within ±5 % of calories and at or above protein.

## 4. Shopping list

- Add up grams per food across the week, round up to whole packs, and subtract what they say they still have.
- Group by store section. Each line: product, packs × size, price if known.
- Total the price and compare with their budget. If it's over, offer the cheapest swap that keeps protein.

## 5. Write and report

Write `week.md` starting with the heading `# Week of YYYY-MM-DD`, the first of the seven days the plan covers. Then: the targets, the meals (foods with grams, kcal and protein per meal), a day-by-day table with daily totals only, a short prep note (what to batch-cook on which day), and the shopping list.

In chat, report in four lines or fewer: average daily calories and protein against target, the price against budget, and the next step: `fill-cart` if a supermarket is connected, otherwise "take this list to the shop" plus the offer to `connect-supermarket`.
