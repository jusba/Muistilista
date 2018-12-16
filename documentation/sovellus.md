## Muistilista

#### Sovelluksen rajoitteet

Sovellus on käytettävyydeltään varsin vaikea, kun sitä verrataan muihin samantyylisin websovelluksiin.  Se on kankean ja vanhanaikaisen oloinen, eikä sen käyttö ole tehokasta. Esim. kun halutaan lisätä uusia muistettavia asioita, täytyy ensin käydä lisäilemässä niille tärkeys- ja teemaluokkia. Käytöstä tulee tällöin varsin vaivalloista ja hidasta. Tätä voisi ehkä parantaa lisäominaisuuksilla ja etenkin Html elementtien päivityksellä, mutta nyt aika ja osaaminen ei riitä siihen.

Varsinaisia bugejakin on, muistettaville asioille tulee joku satunnainen tärkeys, jos niiden olemassa oleva tärkeys poistetaan. Tämä luotiin sitä varten, jotta sovelluksen tietokanta toimii Herokussa, paikallisesti se toimi aikaisemmin kunnolla. Muitakin bugeja varmasti löytyy, dokumentoin niitä tähän, kun löytyy.

Osa sovelluksen redirecteistä ja muista uudelle sivulle siirtävistä funktioista on huonosti suunniteltu. Ne siirtävät käyttäjän välillä epätehokkaasti ja käyttäjä joutuu tekemään useamman ylimääräisen klikkauksen.

Kuten aikaisemmin oli esillä, sovelluksen Html elementit kaipaisivat päivitystä, nyt välillä etenkin, jos on paljon tekstiä ja se on pitkää, on eri kohteita vaikea erottaa toisistaan. Tätä olisi kohtuullisen helppo korjata tarvittavan ajan ja osaamisen kanssa, mutta nyt sovelluksen esittämä tieto on välillä vaikealukuista.

#### Työn puuttavat ominaisuudet

Työstä tärkeimpänä puuttuu todennäköisesti sisäkkäisten teemaluokkien asetus, mitä luvattiin. Tämä osoittautui annetussa ajassa liian haastavaksi.  Sovellus kuitenkin toimii onneksi ilmankin tätä ominaisuutta.

Todennäköisesti myös yhtä tärkeä puuttuva ominaisuus on kunnollinen ulkoasu. Työn html elementit ovat sekavia, niitä ei käytetä oikein ja tämän takia myös ulkoasu ei ole ammattimainen. Syy tähän on osaamisen ja ajan puute. Jos sovellusta haluaa jatkokehittää, niin on ulkoasun korjaaminen ensimmäinen tavoite.

Ikävästi ei toimiva ja paljon aikaa vienyt ominaisuus oli ylläpitäjäkäyttäjän luonti. Sitä ei vain jostain yliluonnollisesta syystä saatu toteutettua sovellukseen ja pudotin sen lopulta pois, sillä sen vaatima ajanmäärä alkoi olla liikaa. Tästä johtuen myös dokumentaation teon kanssa tuli kiire.

#### Dokumentaation vastaavuus valmiiseen työhön

Työ vastaa itseasiassa yllättävän hyvinkin dokumentaatioon. Lähtökohta sovellukselle oli varsin simppeli, joten tämä ei ole toisaalta yllättävää. Myöskään ennen aloitusta luodussa dokumentaatiossa ei määritelty esimerkiksi ulkoasuun liittyviä seikkoja, mitkä jäivät työssä vajaaksi. Ainoa suoraan dokumentaatiosta puuttuva asia oli juuri teemaluokkien  sisäkkäisyyden puuttuminen.

#### Omia ajatuksia työstä

Suoraan sanottuna työssä ei olisi ollut minkäänlaisia mahdollisuuksia ilman hyviä ohjeita. Suurin osa työn koodista on apinoitu tai jatkettu ohjeista saadun koodin perusteella. Sivuaineilijana vaikeus tuntui korostuvan. Työssä oli mukana paljon asioita, joista aikaisempi kokemukseni on hyvin rajattu. Esimerkiksi html kanssa toimimisesta ei ole oikeastaan mitään aikaisempaa kokemusta ja tietokannoista tikapen kauttakin jo yli vuosi.

Vaikeuksia aiheutti eniten loppupelissä varmaan pikkuasioihin takertuminen. Esimerkiksi queryjen kautta tietokantaan vaikuttaminen oli minulle varsin uutta ja näiden kanssa oli paljon ongelmia. Samoin kuin muutenkin tietokannan id ja foreing key:den kanssa toimiminen oli välillä haastavaa. Päivien kulku tuntui varsin samalta, joku asia ei toimi sovelluksessa -> korjaa se -> sovellus ei toimi enää herokussa kunnolla -> korjaa ongelma -> sovellus ei toimi kunnoilla enää paikallisesti jne. Pikkuvikojen korjailuun kului huomattavasti aikaa, mikä sitten jäi pois sovelluksen ulkoasun parantamisesta ja dokumentaatiosta. Aika loppui kesken

Yllättävää kyllä, sovellusta tehdessä tunsin myös oppivani jotain. Aluksi en ymmärtänyt ollenkaan eri views ja models tiedostojen funktiota tai mitään ohjelman pakkausrakenteesta. Alku siis menikin vain suoraan ohjeita apinoidessa. Kuitenkin hiljalleen pidemmälle edetessä ja ajan kuluessa aloin jonkin verran ymmärtämään päärakenteita tällaisesta sovelluksesta, ja osasin paremmin tuoda ohjeista erkanevia omia asioitani sovellukseen. Mielenkiintoinen kokemus siis tältä kannalta.
