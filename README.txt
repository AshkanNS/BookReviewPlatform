Bokrecensionsplattform

Plattformen är som ett levande bibliotek med olika böcker. Det finns olika genrer och författare som man kan bläddra igenom samt lägga till och recensera böcker.
De funktioner som finns tillgängliga på den här Plattformen är de som enligt uppgift är implementerade.

GET /books - Hämtar alla böcker i databasen. Du ska kunna filtrera på titel, författare och/eller genre via en parameter i search-query. Exempelvis: /books?genre=biography
POST /books - Lägger till en eller flera böcker i databasen.
GET /books/{book_id} - Hämtar en enskild bok.
PUT /books/{book_id} - Uppdaterar information om en enskild bok.
DELETE /books/{book_id} - Tar bort en enskild bok
POST /reviews -  Lägger till en ny recension till en bok.
GET /reviews - Hämtar alla recensioner som finns i databasen
GET /reviews/{book_id} - Hämtar alla recensioner för en enskild bok.
GET /books/top - Hämtar de fem böckerna med högst genomsnittliga recensioner.

här använda jag de exemplet som fanns i uppgiften av Wikipedia
GET /author - Hämtar en kort sammanfattning om författaren och författarens mest kända verk. Använd externa API:er för detta.

Har även lagt till två tester som man kan köra igenom och prova

Har noterat en del av källorna jag använt där jag sökt inspiration samt hjälp med Plattformen:
Corey Shafer som är en väldigt populär programmerare på Youtube hade ett par bra videos som man kunde följa och lära sig massa
Tech with Tim lika så

https://flask.palletsprojects.com/en/3.0.x/
Väldigt informationsrik sida med massor av info samt tip o trix

https://dagster.io/blog/python-project-best-practices
Massa bra tips på hur jag skulle strukturera projektet vilket hjälpte mig enormt med att sen kunna fullfölja vad som behövs göras etc.

hel del google sökningar o även tips från klass kamrater var också till hjälp.