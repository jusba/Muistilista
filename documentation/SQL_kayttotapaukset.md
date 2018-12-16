### Sovelluksessa käytettyjä SQL-kyselyitä

#### Etusivun yhteenvetokyselyt

###### Käyttäjät, joilla ei yhtään muistettavaa asiaa
´´´
SELECT Account.id, Account.name FROM Account LEFT JOIN Thing ON Thing.account_id = Account.id WHERE Thing.name IS null GROUP BY Account.id HAVING COUNT(Thing.id) = 0

´´´
