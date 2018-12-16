# Käyttöohje 

Avaa sovellus `https://muistilista-tsoha-jusba.herokuapp.com/`

Sovelluksessa ei pysty tekemään paljoakaan ilman käyttäjän luomista. Käyttäjä luodaan yläpalkin kirjaudu/luo tunnus painikkeen kautta. 
Kaikki sovelluksen toiminnot ovat käyttäjäkohtaisia, joten esimerkiksi muiden tärkeysluokkia tai muistettavia asioita ei näe. Tunnistautuminen tehdään tunnuksen avulla.


##### Kirjautuminen / käyttäjän luonti

Kirjaudu/luo tunnus painikkeesta aukeavassa valikossa voi kirjautua sisälle, mahdollinen tunnuksen teko tapahtuu painamalla täältä löytyvää "Luo tunnus" painiketta.
Luo tunnus valikossa asetetaan käyttäjälle käyttäjänimi ja salasana. Sovellus ilmoittaa, jos tämä ovat virheellisiä syötteeltään. Sovellus siirtää käyttäjänsä tämän jälkeen takaisin kirjautumissivulle.

Luoduilla tunnuksilla voi kirjautua heti. Kirjautumisen jälkeen ohjelma siirtyy päävalikkoon ja kaikkit valikot ovat käytössä

##### Muistettavien asioiden lisäys

Paina yläpalkin "Lisää uusi muistettava asia painiketta. Näkymä siirtyy asioiden luomissivulle. Jos asioille ei ole luotu tärkeysluokkia tai teemoja, kannattaa ne luoda ensin.
Näkymässä on neljä kenttää, muistettava asia ja kuvaus ovat vapaasti kirjoitettavissa pituussäädösten puitteissa. Tärkeys kohdan vaihtoehdot taas riippuvat aikaisemmin tehdyistä tärkeysluokista. Teema kohdassa voi valita yhden tai useamman teemeluokan aikaisemmin luotujen teemaluokkien perusteella. Useamman vaihtoehdon voi valita pitämällä Ctrl pohjassa.  

Kaikki kentät vaativat jotain syötettä. Kun syötteet on laitettu ja käyttäjä painaa uuden muistettavan asian lisäysnappia, siirtyy näkymä niiden listaukseen.

##### Muistettavien asioiden listaus

Listausvalikossa näkyvät kaikki käyttäjän lisäämät muistettavat asiat. Niistä näkyy muistettavan asian nimi, kuvaus, tärkeysluokka ja sille asetetut teemaluokat. Valikossa on kaksi painiketta, tarkastele ja poista.
Painamamalla poista, muistettava asia poistuu tietokannasta. Kuitenkin esimerkiksi siihen liittyvät tärkeys- ja teemaluokat  jäävät olemaan ja ne pitää poistaa erikseen.

##### Muistettavien asioiden tarkasteluvalikko

Muistettavie asioita voi tarkastella yksitellen painamalla listauksessa tarkastele painiketta. Tällöin näkymä siirtyy tarkastelemaan yhtä tiettyä muistettavaa asiaa.    
Asiasta näkyy kaikki sen tietokannassa oleva tiedot, sekä siihen liittyvät tärkeysluokat ja teemaluokat.
Tässä valikossa on mahdollista myös muokata muistettavan asian kuvausta, tärkeys- ja teemaluokkaa samalla tavalla kuin niitä lisättäisiin, mutta lomakkeet muokkaavat vain olemassaolevaa tietokohdetta.
Kuvauksen muokkauksen jälkeen näkymä siirtyy takaisin listaukseen.

##### Tärkeysluokkien lisäys

Aukeavassa valikossa pystyy lisäämään sallittujen validaattoreiden puitteissa uusia tärkeysluokkia järjestelmään. Näitä pitää lisätä ennen uusien muistettavien asioiden lisäystä.
Tärkeysluokalle annetaan nimi, joka tallentuu lisäysnappulaa painamalla tietokantaan. Tärkeysluokat lisätään muistettaviin asioihin muistettavien asioiden luomisvalikossa tai tarkasteluvalikossa.
Tärkeysluokan lisäämisen jälkeen näkymä siirtyy niiden listaukseen.

##### Tärkeysluokkien listaus

Tärkeysluokkien listauksessa näkyy lista käyttäjän luomista tärkeysluokista. Painamalla poista painiketta on mahdollista poistaa järjestelmässä olevia tärkeyskohteita.

##### Teemaluokkien lisäys

Painettessa yläpalkista lisää uusi teema, siirtyy kuva niiden lisäysvalikkoon. Aukeavassa valikossa voi lisätä teemaluokkia järjestelmään annettujen pituussäädösten rajoissa. Teemaluokalla annetaan nimi, jonka jälkeen se lisätään tietokantaan nappia painamalla. Tämän jälkeen sivu vaihtuu teemaluokkien listaukseen.

##### Teemaluokkien listaus

Teemaluokkien listauksessa näkyy kaikki käyttäjän luomat teemaluokat nimen perusteella. Valikossa on kaksi painiketta, tarkastele ja poista. Painamalla poista, teemaluokka poistuu järjestelmästä. Painamalla tarkastele kuva taas siirtyy teemaluokkien tarkastelusivulle. 

##### Teemaluokkien tarkasteluvalikko

Tässä valikossa näkyy teemaluokkaan liittyviä tietoja, sen nimi, id, sitä käyttävät muistettavat asiat, sen tekijän id ja ajankohtatiedot. Kaikki tiedot liittyvät yhteen tiettyyn listauksen kautta avattuun teemaan. Valikossa on mahdollista myös muokata teeman nimeä, sekä valita muistettavia asioita, joilta kyseinenen teemaluokka poistetaan. On mahdollista muokata pelkästään teeman nimeä olemalla valitsematta yhtään muistettavaa asiaa listauksesta. Poistettaessa teemaa muistettavilta asioilta, poistuu vain sillä hetkellä käsiteltävä oleva teema näiltä. Muut teemat jäävät vielä muistettaville asioille. Useampia kohteita voi valita pitämällä Ctrl pohjassa. Painettuaan muokkaa teemaa painiketta, ikkuna siirtyy takaisin teemojen listaukseen ja muutokset päivittyvät tietokantaan.

##### Yleistä

Poistaessa kiireellisyys- tai teemaluokkia, jäävät niihin liittyvät muistettavat asiat ilman näitä ominaisuuksia. Kannattaa siis huomioida tämä tai muokata muistettaville asioille sitten uudet kiirellisyys- tai teemaluokat.

