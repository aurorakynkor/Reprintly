Utility for checking if magic cards are reprints

**Problem:**

[Magic](https://en.wikipedia.org/wiki/Magic:_The_Gathering) is a 30 year old collectible card game. 

Due to the nature of trading card games, cards are bought and sold on the secondary market. When a new set (or collection of cards comes out), some of those new cards include cards from previous sets (to lower their cost on the secondary market).

Game stores typically buy and sell product through a third party distributor, but many game stores will often take in trades (at roughly 30-60% of the original value of the card) in exchange for store credits. This presents a challenge when cards are reprinted:

Example: Card A originally had a 20 price tag, a store bought it on a trade in for 10. However reprints were just announced that would lower the price of this card to 2$ over the course of a few months: resulting in an $8 loss for the store. 

In order for game stores to identify which cards are being reprinted (in order to avoid buying a declining asset) I created this utility which allows users to quickly input a list of cards, and determine whether or not those cards are reprints.

**To get started:**
1. Clone the repo
2. Run: docker-compose build
3. Run: docker-compose up
4. Once the server is up and running send the following request via Curl/Postman/etc.:
```
$ curl --location --request GET 'http://localhost:8008/check_reprint' \
--header 'Content-Type: application/json' \
--data '{
    "cards": ["Underworld Breach", "Thespian'\''s Stage", "Battlefield Forge", "Twilight Prophet"],
    "sets": ["mkm", "mkc", "spg", "xyz"]
}'
```
