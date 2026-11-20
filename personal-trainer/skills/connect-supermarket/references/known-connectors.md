# Known supermarket connectors

Community projects, none official. Checked in November 2026: the stars and last-update dates below are from then. Still review the code at the commit you install (see the skill), since projects change.

| Store | Country | Connector | Type | Can it read the cart? | Notes |
| --- | --- | --- | --- | --- | --- |
| Mercadona | Spain | [ivorpad/mercadona-cli](https://github.com/ivorpad/mercadona-cli) (338 ★, updated Oct 2026, no licence file) | Command-line tool (Go) | Yes | Search, prices, cart. Has checkout and delivery-slot commands: remove them from the source before building and deny them. Login is imported from a browser session export and stored unencrypted in the home folder; the export file contains the password, so delete it after import. The repo also ships its own Claude skill that can place orders, and an `npx` shortcut that runs the unpatched tool: use neither. |
| Kroger and Kroger-owned stores | USA | [CupOfOwls/kroger-mcp](https://github.com/CupOfOwls/kroger-mcp) (84 ★, updated Oct 2026, MIT) | MCP (Python) | No, add only | Uses Kroger's public API with the user's own developer app keys, which they type into the config themselves. Can add to the cart but can't remove items or fully read the cart. |
| Picnic | Netherlands, Germany, France | [ivo-toby/mcp-picnic](https://github.com/ivo-toby/mcp-picnic) (123 ★, updated Nov 2026, MIT) | MCP (Node) | Yes | Unofficial. Adds to cart with quantities. Has delivery-slot tools such as `picnic_set_delivery_slot`: check the code for every tool that books a slot or places or changes an order, and block them all. Its setup puts the Picnic password in plain text in the MCP config, and a two-factor code passes through the chat: tell the user before they decide, and have them type the password into the config themselves. |

To support another store, add a row here.
