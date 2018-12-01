# Käyttöohje (alustava)

Avaa sovellus `https://muistilista-tsoha-jusba.herokuapp.com/`

Sovelluksessa ei pysty tekemään paljoakaan ilman käyttäjän luomista. Käyttäjä luodaan yläpalkin kirjaudu/luo tunnus painikkeen kautta. 
Kaikki sovelluksen toiminnot ovat käyttäjäkohtaisia, joten esimerkiksi muiden tärkeysluokkia tai muistettavia asioita ei näe. Tunnistautuminen tehdään tunnuksen avulla.


##### Kirjautuminen / käyttäjän luonti

Kirjaudu/luo tunnus painikkeesta aukeavassa valikossa voi kirjautua sisälle, mahdollinen tunnuksen teko tapahtuu painamalla täältä löytyvää "Luo tunnus" painiketta.
Luo tunnus valikossa asetetaan käyttäjälle käyttäjänimi ja salasana. Sovellus ilmoittaa, jos tämä ovat virheellisiä syötteeltään. Sovellus siirtää käyttäjänsä tämän jälkeen takaisin kirjautumissivulle.

Luoduilla tunnuksilla voi kirjautua heti. Kirjautumisen jälkeen ohjelma siirtyy päävalikkoon ja kaikkit valikot ovat käytössä

##### Muistettavien asioiden lisäys

Paina yläpalkin "Lisää uusi muistettava asia painiketta. Näkymä siirtyy asioiden luomissivulle. Jos asioille ei ole luotu tärkeysluokkia, kannattaa ne luoda ensin.
Näkymässä on kolme kenttää, muistettava asia ja kuvaus ovat vapaasti kirjoitettavissa pituussäädösten puitteissa. Tärkeys kohdan valinnan taas riippuvat aikaisemmin tehdyistä tärkeysluokista.
Kaikki kentät vaativat jotain syötettä. Kun syötteet on laitettu ja käyttäjä painaa uuden muistettavan asian lisäysnappia, siirtyy näkymä niiden listaukseen.

##### Muistettavien asioiden listaus

Listausvalikossa näkyvät kaikki käyttäjän lisäämät muistettavat asiat. Niistä näkyy muistettavan asian nimi, kuvaus ja tärkeysluokka. Valikossa on kaksi painiketta, tarkastele ja poista.
Painamamalla poista, muistettava asia poistuu tietokannasta. Kuitenkin esimerkiksi siihen liittyvä tärkeysluokka jää olemaan ja pitää poistaa erikseen.

##### Muistettavien asioiden tarkasteluvalikko

Muistettavie asioita voi tarkastella yksitellen painamalla listauksessa tarkastele painiketta. Tällöin näkymä siirtyy tarkastelemaan yhtä tiettyä muistettavaa asiaa.
Asiasta näkyy kaikki sen tietokannassa oleva tiedot, sekä siihen liittyvän tärkeysluokan nimi.
Tässä valikossa on mahdollista myös muokata muistettavan asian kuvausta ja tärkeysluokkaa samalla tavalla kuin niitä lisättäisiin, mutta lomakkeet muokkaavat vain olemassaolevaa tietokohdetta.
Kuvauksen muokkauksen jälkeen näkymä siirtyy takaisin listaukseen.

##### Tärkeysluokkien lisäys

Aukeavassa valikossa pystyy lisäämään sallittujen validaattoreiden puitteissa uusia tärkeysluokkia järjestelmään. Näitä pitää lisätä ennen uusien muistettavien asioiden lisäystä.
Tärkeysluokalle annetaan nimi, joka tallentuu lisäysnappulaa painamalla tietokantaan. Tärkeysluokat lisätään muistettaviin asioihin muistettavien asioiden luomisvalikossa tai tarkasteluvalikossa.
Tärkeysluokan lisäämisen jälkeen näkymä siirtyy niiden listaukseen.

##### Tärkeysluokkien listaus

Tärkeysluokkien listauksessa näkyy lista käyttäjän luomista tärkeysluokista. Painamalla poista painiketta on mahdollista poistaa järjestelmässä olevia tärkeyskohteita.


