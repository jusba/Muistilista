# Asennusohje

 #### Ohjelman käyttö paikallisesti

Kloona github repo (https://github.com/jusba/Muistilista.git) tai lataa samalta sivulta ohjelman Zip koneellesi.

Luo virtuaaliympäristö (asenna venv tarvittaessa ennen)
```
python3 -m venv venv
```
Aktivoi se
```
source venv/bin/activate
```
Lataa tarvittavat kirjastot ja palvelimet. Voi
mahdollisesti ohittaa myös kaksi seuraavaa kohtaa `pip install -r requirements.txt`komennolla
```
pip install Flask
pip install gunicorn
pip install flask-sqlalchemy
pip install flask-wtf
pip install flask-login
pip install psycopg2
```
Virtuaaliympäristöjä varten riippuvuudet
```
pip freeze | grep -v pkg-resources > requirements.txt
```
Käynnistä sovellus samasta kansiosta run.py tiedoston kanssa
```
python3 run.py
```
Tämän jälkeen sovellus pitäisi löytyä osoitteesta `localhost:5000/` (voi olla muukin paikallinen osoite). Sovellus sulkeutuu ctrl + c komennolla

#### Jatko herokuun

Luo sovellukselle paikka herokuun
```
heroku create Muistilista-tsoha-demo

```
Paikalliseen versionhallintaan tieto herokusta
```
git remote add heroku https://git.heroku.com/muistilista-tsoha-demo.git
```


Kerro herokulle, että sovellus on siellä 
```
heroku config:set HEROKU=1
```
Luo sovellukseen tietokanta
```
heroku addons:add heroku-postgresql:hobby-dev
```
Työnnä kaikki herokuun
```
git add .
git commit -m "Initial commit"
git push heroku master
```

Sovellus pitäisi sitten löytyä `https://git.heroku.com/muistilista-tsoha-demo.git` tai minkä osoitteen annoitkaan. Heroku voi vaatio kirjautumista jossain vaiheessa, minkä toteutat `heroku login` komennolla
