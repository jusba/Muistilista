### Sovelluksessa käytettyjä SQL-kyselyitä

#### Etusivun yhteenvetokyselyt

##### Käyttäjät, joilla ei yhtään muistettavaa asiaa
```
SELECT Account.id, Account.name FROM Account LEFT JOIN Thing ON Thing.account_id = Account.id WHERE Thing.name IS null GROUP BY Account.id HAVING COUNT(Thing.id) = 0

```
##### Tilastoja käyttäjistä
```
SELECT Account.id, Account.name, count(DISTINCT thing.id) as things, count(DISTINCT rank.id) as ranks , count(DISTINCT theme.id) as themes From Account LEFT JOIN  thing ON account.id = thing.account_id LEFT JOIN rank ON account.id = rank.account_id LEFT JOIN theme ON account.id = theme.account_id GROUP BY Account.id 

```

#### Muistettavien asioiden kyselyt

##### Asiat, joilla on monta teemaa
```
SELECT thing.id, thing.name FROM thing, thing_theme WHERE thing.id = thing_theme.thing_id GROUP BY thing.id HAVING COUNT(thing_theme.id) > 1

```
##### Kaikki tiettyyn tunnkseen liittyvät muistettavat asiat
```
SELECT thing.id AS thing_id, thing.date_created AS thing_date_created, thing.date_modified AS thing_date_modified, thing.name AS thing_name, thing.description AS thing_description, thing.account_id AS thing_account_id, thing.rank_id AS thing_rank_id 
FROM thing 
WHERE thing.account_id = ?
```
##### Kaikki tiettyyn tunnukseen liittyvät tärkeysluokat
```
SELECT rank.id AS rank_id, rank.date_created AS rank_date_created, rank.date_modified AS rank_date_modified, rank.name AS rank_name, rank.account_id AS rank_account_id 
FROM rank 
WHERE rank.account_id = ?

```
##### Kaikki tiettyyn tunnukseen liittyvät teemaluokat
```
SELECT theme.id AS theme_id, theme.date_created AS theme_date_created, theme.date_modified AS theme_date_modified, theme.name AS theme_name, theme.account_id AS theme_account_id 
FROM theme 
WHERE theme.account_id = ?

```
##### Hae tiettyyn tunnukseen liittyvät liitostaulun osat
```
SELECT thing_theme.id AS thing_theme_id, thing_theme.date_created AS thing_theme_date_created, thing_theme.date_modified AS thing_theme_date_modified, thing_theme.account_id AS thing_theme_account_id, thing_theme.thing_id AS thing_theme_thing_id, thing_theme.theme_id AS thing_theme_theme_id 
FROM thing_theme 
WHERE thing_theme.account_id = ?

```
#### Muistettavien asioiden tarkastelun kyselyt

Mukana oikeastaan kaikki edelliset, joissa haetaan tunnuksen perusteella tietoja.

##### Hae tarkasteltava asia

```
SELECT thing.id AS thing_id, thing.date_created AS thing_date_created, thing.date_modified AS thing_date_modified, thing.name AS thing_name, thing.description AS thing_description, thing.account_id AS thing_account_id, thing.rank_id AS thing_rank_id 
FROM thing 
WHERE thing.id = ?

```
##### Muokkaa tarkasteltavaa asiaa
Muokataan tietoja
```
UPDATE thing SET date_modified=CURRENT_TIMESTAMP, description=? WHERE thing.id = ?

``` 
Poistetaan liitostaulut johon ei enään yhteyttä
```
DELETE FROM thing_theme WHERE thing_theme.thing_id = ?

```
Luodaan uudet yhteystaulut
```
INSERT INTO thing_theme (date_created, date_modified, account_id, thing_id, theme_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

```
#### Asioiden poisto
```
DELETE FROM thing_theme WHERE thing_theme.thing_id = ?

```
Thing_themestä poistetaan ensin, jotta Heroku toimisi oikein.
```
DELETE FROM thing WHERE thing.id = ?
```

#### Uuden muistettavan asian lisäyksen kyselyt
Rankkiin ja teemoihin liittyvät edelliset, joissa haetaan kaikki käyttäjän id:n perusteella

##### Uusi muistettava asia tietokantaan
```
INSERT INTO thing (date_created, date_modified, name, description, account_id, rank_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

```
##### Uusi liitostaulun kohta muistettavaa asiaa lisätessä
```
INSERT INTO thing_theme (date_created, date_modified, account_id, thing_id, theme_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
``` 

#### Tärkeysluokkien listaukseen liittyvät kyselyt
Rankkiin liittyvät edelliset, joissa haetaan kaikki käyttäjän id:n perusteella

#### Tärkeysluokkien poisto kysely

Mukana thingeihin ja rankkiin liittyvät joissa haetaan käyttäjältä kaikki.

##### Haetaan tietty tärkeys poistettavaksi kysely
```
SELECT rank.id AS rank_id, rank.date_created AS rank_date_created, rank.date_modified AS rank_date_modified, rank.name AS rank_name, rank.account_id AS rank_account_id 
FROM rank 
WHERE rank.id = ?

```
##### Poistetaan tietty tärkeys kysely
```
DELETE FROM rank WHERE rank.id = ?

```
##### Asetetaan uusi tärkeys muistettavalla asialle. (Purkkaratkaisu, sovellus kaatui aikaisemmin, jos ei asetettu)
```
SELECT thing.id AS thing_id, thing.date_created AS thing_date_created, thing.date_modified AS thing_date_modified, thing.name AS thing_name, thing.description AS thing_description, thing.account_id AS thing_account_id, thing.rank_id AS thing_rank_id 
FROM thing 
WHERE thing.rank_id = ?

```

#### Tärkeysluokkien lisäyskysely
```
INSERT INTO rank (date_created, date_modified, name, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)

```

#### Teemaluokkien luettelointi kyselyt

Aikaisemmat teeman hakuun käyttäjä id:n perusteella liittyvät

#### Teemaluokkien poisto

##### Poistetaan ensin liitostaulusta viitteet ( jotta heroku tykkää)
```
DELETE FROM thing_theme WHERE thing_theme.theme_id = ?

```
##### Kysely jolla varsinainen teemaluokka poistetaan
```
DELETE FROM theme WHERE theme.id = ?
``` 

#### Teemaluokkien tarkastelu
Mukana monet käyttäjään liittyvät kyselyt, joissa haetaan kaikki tietyn käyttäjän teemat tai thingit

##### Haetaan tietty teemaluokka

```
SELECT theme.id AS theme_id, theme.date_created AS theme_date_created, theme.date_modified AS theme_date_modified, theme.name AS theme_name, theme.account_id AS theme_account_id 
FROM theme 
WHERE theme.id = ?

``` 
##### Haetaan liitostaulukyselyn avulla thingit

```
SELECT thing_theme.id AS thing_theme_id, thing_theme.date_created AS thing_theme_date_created, thing_theme.date_modified AS thing_theme_date_modified, thing_theme.account_id AS thing_theme_account_id, thing_theme.thing_id AS thing_theme_thing_id, thing_theme.theme_id AS thing_theme_theme_id 
FROM thing_theme 
WHERE thing_theme.theme_id = ?

``` 
##### Muokataan sitä
```
UPDATE theme SET date_modified=CURRENT_TIMESTAMP, name=? WHERE theme.id = ?
```
```
SELECT thing.id AS thing_id, thing.date_created AS thing_date_created, thing.date_modified AS thing_date_modified, thing.name AS thing_name, thing.description AS thing_description, thing.account_id AS thing_account_id, thing.rank_id AS thing_rank_id 
FROM thing 
WHERE thing.name = ?

```
```
SELECT thing.id AS thing_id, thing.date_created AS thing_date_created, thing.date_modified AS thing_date_modified, thing.name AS thing_name, thing.description AS thing_description, thing.account_id AS thing_account_id, thing.rank_id AS thing_rank_id 
FROM thing 
WHERE thing.name = ?

```
```
SELECT thing_theme.id AS thing_theme_id, thing_theme.date_created AS thing_theme_date_created, thing_theme.date_modified AS thing_theme_date_modified, thing_theme.account_id AS thing_theme_account_id, thing_theme.thing_id AS thing_theme_thing_id, thing_theme.theme_id AS thing_theme_theme_id 
FROM thing_theme 
WHERE thing_theme.theme_id = ?


```
Poistetaan lopulta turha liitostaulu
```
DELETE FROM thing_theme WHERE thing_theme.id = ?

```
