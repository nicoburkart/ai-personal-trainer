# Calories, protein and training rules

All maths in kg and cm; convert from lb (× 0.4536) and inches (× 2.54) first.

## Calories

1. Resting energy with Mifflin–St Jeor (Mifflin et al., 1990), weight in kg, height in cm, age in years:
   - Men: 10 × weight + 6.25 × height − 5 × age + 5
   - Women: 10 × weight + 6.25 × height − 5 × age − 161
   - If they don't give a sex, use the average of the two.
2. Multiply by activity, using the closest row:
   | Daily life | Factor |
   | --- | --- |
   | Mostly sitting, trains 0–1 days | 1.25 |
   | Mostly sitting, trains 2–3 days | 1.4 |
   | On their feet a lot, or sitting and trains 4–5 days | 1.55 |
   | On their feet and trains, or trains 6+ days | 1.7 |
   | Physical job and trains | 1.85 |
3. Adjust for the goal:
   - Lose fat: −15 to −25 %. Smaller deficit when they're already lean or have little time.
   - Build muscle: +5 to +10 % (the low end for experienced lifters).
   - Get stronger or fitter: maintenance.
4. Apply `references/safety.md` at the plugin root: a flag can remove the target or hold it at maintenance, and the limits set the calorie floors and rule out a deficit under BMI 20. Round to the nearest 50.
5. Expected weekly change in kg = daily deficit or surplus × 7 ÷ 7,700. Write that number in `plan.md` as the target rate.
6. Tell them it's an estimate. After 2–3 weeks of weigh-ins, `check-in` corrects it from their real trend.

## Protein

- Not in a deficit: 1.6 g per kg of body weight a day, where extra protein stops adding muscle on average. Up to 2.2 g/kg if they want more; that covers nearly everyone (Morton et al., 2018).
- In a deficit: 2.0 g/kg, to help keep muscle. For lean, trained lifters cutting hard, more can help (Helms et al., 2014, recommends 2.3–3.1 g per kg of lean mass).
- If they're very overweight (BMI over 30), ask for their goal weight and base it on that instead of current weight.
- Spread it over 3–5 meals with at least 0.4 g/kg each (Schoenfeld & Aragon, 2018). The daily total matters most.

## Carbs and fat

Fat at 25–30 % of calories (at least 0.6 g/kg), carbs fill the rest.

## Training

- Each muscle at least twice a week (Schoenfeld et al., 2016) and at least 10 hard sets per muscle per week, since more sets build more muscle up to a point (Schoenfeld et al., 2017). 10–20 is the common working range; beginners start near 10.
- Split by days: 2–3 days full body · 4 days upper/lower · 5–6 days upper/lower plus a day or two of what they want to bring up.
- Mostly compound lifts in 5–12 reps, accessories 10–20 reps, 1–3 reps in reserve.
- Progress: add reps until the top of the range, then add the smallest weight step. If a lift stalls for 3 sessions, drop 10 % and build back.
- Cardio: 2–3 sessions of 20–40 min or 7–10k steps a day, built up slowly if they run.
