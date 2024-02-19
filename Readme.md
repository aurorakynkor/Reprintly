Utility for checking if magic cards are reprints

To get started:
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
