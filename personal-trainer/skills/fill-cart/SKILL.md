---
name: fill-cart
description: Puts the week's shopping list into the user's online supermarket cart through a connected supermarket tool, without ever placing the order. Use when the user says "fill my cart", "order my groceries", "add this to my basket", or "do my shopping".
---

# Fill the cart

Turn the shopping list in `week.md` into the user's real cart. The user always places the order themselves.

## Rules

- **Never place, pay for or confirm an order, and never book or release a delivery slot.** Don't call any connector tool or command that does, even if the user asks; tell them to press order in their supermarket's app.
- **Show before you change.** Before adding anything, show the exact products, quantities and total price, and wait for a yes.
- Don't remove items the user put in the cart themselves.

## Steps

1. Read `week.md`. If it's missing, or the seven days from its `# Week of` date are over, run `plan-week` first.
2. Check for a supermarket connector (an MCP server or a command-line tool set up for their store, noted under Shopping in `profile.md`). If there isn't one, say so in one line, offer `connect-supermarket`, and give them the list to shop by hand.
3. Read the current cart if the connector can, so you add to it rather than duplicate. If it can't read the cart, skip this check and tell them to check the cart in the app afterwards.
4. Match each list line to a store product: same product and pack size as in `foods.md` when possible; otherwise the closest match with similar protein per 100 g. List any line you couldn't match.
5. Show the cart change and the total, get the yes, then add the items.
6. Read the cart back where possible and confirm it matches. Report: items added, total, anything unmatched, and "open your supermarket app, pick a delivery slot and press order".
7. Note the date and total in `log.md`.
