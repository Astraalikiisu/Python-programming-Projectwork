# Tämä sanakirja sisältää pelimaailman paikat, ja kuvaa niiden ominaisuuksia ja mahdollisia tapahtumia.
kartta = {
    "niitty": {
        "nimi": "Avoin kukkaniitty",
        "kuvaus": "Olet avoimella niityllä, jossa kasvaa erilaisia luonnonkukkia. Ympärilläsi näet erilaisia alueita. \nEdessäsi on polku, joka vie kohti metsän reunaa. Takanasi näet polun, joka vie kohti järven rantaa. \nLännessä näet polun, joka johtaa vuorille.",
        "esineet": {},
        "vinkki": "Lähde ympäröiville alueille etsimään esineitä.",
    },

    "metsän_siskäynti": {
        "nimi": "Metsän sisäänkäynti",
        "kuvaus": "Olet metsän sisäänkäynnillä. Sisäänkäyntiä peittää vanha ja paksu köynnöskasvusto, joka tekee kulun mahdottomaksi syvemmälle metsään.",
        "uusi_kuvaus": "Olet metsän sisäänkäynnillä. Sisäänkäynti on nyt avoin, hakattuasi köynnöksiä kirveellä.",
        "esineet": {},
        "oikea_esine": "kirves",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Hakkaat kirveellä köynnökset tieltäsi.",
        "estetty_suunta": "pohjoinen",
        "vinkki": "Päästäksesi köynnöksistä eteenpäin pohjoiseen, tarvitset jotain terävää millä hakata."
    },

    "alttari": {
        "nimi": "Alttari",
        "kuvaus": "Olet saapunut metsän syvimpään osaan, ja vastassasi on yhtäkkiä kallioseinämä. \nHämärässä näet kivisen alttarin, johon on sytytetty kaksi pientä kynttilää. \nAlttarin pinnalla on erikoisen muotoinen kolo, aivan kuin siihen sopisi jokin esine. \nMetsä jatkuu etelään.",
        "uusi_kuvaus": "Olet saapunut metsän syvimpään osaan. Hämärässä näet alttarin, johon on sytytetty kaksi pientä kynttilää. \nAlttarille asettamasi patsas on avannut tien luolan sisäänkäynnille. \nMetsä jatkuu etelään. ",
        "esineet": {},
        "oikea_esine": "patsas",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Asetat patsaan alttarille. Sen muoto sopii täydellisesti alttarilla olevaan koloon.",
        "estetty_suunta": "pohjoinen",
        "vinkki": "Tarvitset veden ääreltä esineen, jonka asettaa alttarille.",
    },

    "pimeä_aukio": {
        "nimi": "Pimeä aukio",
        "kuvaus": "Olet metsän keskellä, jota vallitsee pahaenteinen pimeys. \nEt näe eteesi, ja eteneminen vaikeakulkuisessa maastossa olisi kohtalokasta. ",
        "uusi_kuvaus": "Olet metsän keskellä, jota vallitsee pahaenteinen pimeys. \nSytyttämäsi lyhty valaisee tien aukion läpi.",
        "esineet": {},
        "oikea_esine": "lyhty",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Otat lyhdyn esiin. Sen valossa näet edetä synkän aukion läpi.",
        "estetty_suunta": "länsi",
        "vinkki": "Tarvitset valonlähteen jotta voit edetä.",
    },

    "metsä": {
        "nimi": "Metsä",
        "kuvaus": "Olet kävellyt suoraan mesikämmenen valtakuntaan. Edessäsi on suuri pörröinen karhu.",
        "toinen_kuvaus": "Olet mesikämmenen valtakunnassa. Karhu on siirtynyt sivummalle istumaan.",
        "hahmo": "karhu",
        "esineet": {},
        "oikeaEsineKäytetty": False,
        "uusi_esine": {
            "smaragdi": "Taianomainen vihreä smaragdi. Tunnet jalokivessä metsän voiman."
        },
        "vinkki": "Metsän valtias haluaa että annat hänelle syötävää.",
    },

    "sienikehä": {
        "nimi": "Sienikehä",
        "kuvaus": "Olet saapunut metsässä sienikehän äärelle. Valkoiset sienet kasvavat ympyrän muotoisessa kehässä. \nKehässä on jotain mystistä.",
        "uusi_kuvaus": "Olet saapunut metsässä sienikehän äärelle. Valkoiset sienet kasvavat ympyrän muotoisessa kehässä. \nMaa sienikehän keskeltä on kaivettu ylös.",
        "esineet": {},
        "oikea_esine": "lapio",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Kaivat lapiolla sienikehän keskeltä. \nMaaperän mukana nousee jokin kimalteleva, kämmeneen mahtuva esine.",
        "uusi_esine": {
            "rubiini": "Välkehtivä punainen rubiini. Jalokivi tuntuu kädessäsi lämpimältä."
        },
        "vinkki": "Tarvitset esineen jolla kaivaa sienikehän keskeltä."
    },

    "marjametsä": {
        "nimi": "Marjametsä",
        "kuvaus": "Olet tiheässä metsässä. Ympärillä kasvaa marjapuskia.",
        "esineet": {
            "marja": "Punainen ja mehukas marja. Tiedät kumminkin että tämä lajike on ihmisen mielestä pahanmakuinen."
        },
        "vinkki": "Poimi täältä matkaasi esine.",
    },

    "metsä_itä": {
        "nimi": "Itäinen metsä",
        "kuvaus": "Olet metsän itäisessä osassa. \nNäet täältä hyvin metsän eri osiin, etelässä on suuri puu, pohjoisessa jonkinlainen muodostelma, ja lännessä marjapensaita.",
        "esineet": {},
        "vinkki": "Kulje täältä metsän eri osiin.",
    },

    "vuori": {
        "nimi": "Kaivos",
        "kuvaus": "Olet hylätyssä kaivoksessa. Täältä on aikojen saatossa louhittu erilaisia mineraaleja. \nErityisesti yksi suuri kivi kiinnittää huomiosi, se vaikuttaa kätkevän sisäänsä jotain.",
        "uusi_kuvaus": "Olet hylätyssä kaivoksessa. Täältä on aikojen saatossa louhittu erilaisia mineraaleja. \nHakkaamasi kivi on haljennut, paljastaen kristallin.",
        "esineet": {},
        "oikea_esine": "hakku",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Hakkaat kiveä hakulla. Kivi halkeaa ja sen sisältä ilmestyy kristalli.",
        "uusi_esine": {
            "kristalli": "Lumoavan kirkas valkoinen kristalli, joka hohtaa heikossa valossa."
        },
        "vinkki": "Löydät aarteen kun hakkaat kiveä sopivalla esineellä.",
    },

    "taistelutanner": {
        "nimi": "Taistelutanner",
        "kuvaus": "Olet keskellä aukeaa, jossa on muinoin käyty suuri taistelu. \nMaastossa on jäänteitä aseista ja varustuksista, mutta suurin osa on jo ehtinyt hajota aikojen saatossa. \nHuomaat kumpareella miekan, jonka terä on puoliksi maan peitossa.",
        "uusi_kuvaus": "Olet keskellä aukeaa, jossa on muinoin käyty suuri taistelu. \nMaastossa on jäänteitä aseista ja varustuksista, mutta suurin osa on jo ehtinyt hajota aikojen saatossa.",
        "esineet": {
            "miekka": "Miekan terä, joka näyttää kuuluneen yhden käden miekkaan. Vaikka se on vanha, se on silti terävä. \nMiekan kahva on hävinnyt."
        },
        "vinkki": "Ota täältä mukaasi terävä esine.",
    },

    "puu": {
        "nimi": "Suuri puu",
        "kuvaus": "Olet suuren puun luona. Puu on vanha, ja sen latvat kohoavat korkealle ylös. \nPuun rungossa on kolo, joka on niin pieni ettei kätesi mahdu siitä.",
        "uusi_kuvaus": "Olet suuren puun luona. Puu on vanha, ja sen latvat kohoavat korkealle ylös. \nPuun rungossa on kolo, joka on niin pieni ettei kätesi mahdu siitä.",
        "esineet": {},
        "oikea_esine": "hamsteri",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Hamsteri kiipeää puun koloon ja katoaa sinne. Hetken päästä se ilmestyy kolosta, suussaan pieni ametisti.",
        "uusi_esine": {
            "ametisti": "Lumoava, violetti ametisti, joka hohtaa heikossa valossa."
        },
        "vinkki": "Tarvitset pienen eläimen apua tutkiaksesi puun kolon.",
    },

    "luola_etu": {
        "nimi": "Luola",
        "kuvaus": "Olet luolan sisällä. Silmilläsi kestää hetki tottua hämärään. \nLuola laajentuu itään, ja sisäänkäynti sijaitsee etelässä.",
        "esineet": {},
        "vinkki": "Täällä ei ole mitään, voit edetä syvemmälle luolaan tai mennä takaisin metsään.",
    },

    "luola": {
        "nimi": "Suden luola",
        "kuvaus": "Olet syvemmällä luolassa. Edessäsi on valtava harmaa susi, joka vartioi luolaa.",
        "uusi_kuvaus": "Olet syvemmällä luolassa. Edessäsi on valtava harmaa susi, jolla on miekka suussa. Susi antaa kulkea sinun eteenpäin.",
        "hahmo": "susi",
        "esineet": {},
        "oikeaEsineKäytetty": False,
        "estetty_suunta": "itä",
        "vinkki": "Susi haluaa sinulta terävän esineen, jonka se on kadottanut taistelutantereelle.",
    },

    "polku_vuori": {
        "nimi": "Pohjoinen polku",
        "kuvaus": "Olet niityllä jonka keskellä kulkee polku. \nPolku haarautuu; läntinen haara vie vuorta kohti, itäinen ja eteläinen haara vievät kohti niittyjä. Jokin kimaltaa kaukana pohjoisessa.",
        "esineet": {},
        "vinkki": "Kulje täältä muille alueille."
    },

    "polku_rakennus": {
        "nimi": "Eteläinen polku",
        "kuvaus": "Olet niityllä jonka keskellä kulkee polku. Länteen katsoessa näet että polku vie kaukaiselle mökille. Polku haarautuu itään.\nNäet kumpareen päällä maahan pystyyn jätetyn lapion.",
        "uusi_kuvaus": "Olet niityllä jonka keskellä kulkee polku. Länteen katsoessa näet että polku vie kaukaiselle mökille. Polku haarautuu itään.",
        "esineet": {
            "lapio": "Vanha lapio joka soveltuu kaivamiseen."
        },
        "vinkki": "Ota täältä matkaasi esine."
    },

    "polku_rantaan": {
        "nimi": "Itäinen polku",
        "kuvaus": "Olet polulla, josta näkee kauas idässä sijaitsevaan rantaan. Polun toinen pää vie takaisin niityille. \nHuomaat maassa pienen esineen, tarkemmalla silmäyksellä se on kahva.",
        "uusi_kuvaus": "Olet polulla, josta näkee kauas idässä sijaitsevaan rantaan. Polun toinen pää vie takaisin niityille.",
        "esineet": {
            "kahva": "Kahva, joka näyttää kuuluneen miekkaan. Ehkä miekka on vielä jossain olemassa?"
        },
        "vinkki": "Kulje täältä muille alueille.",
    },

    "kivi": {
        "nimi": "Suuri kivi",
        "kuvaus": "Olet saapunut suuren kiven äärelle. Kiven takana näet maassa repun josta pilkottaa pieni kirves.",
        "uusi kuvaus": "Olet saapunut suuren kiven äärelle. Kiven takana näet maassa repun, jonka sisällä ei ole enää mitään.",
        "esineet": {
            "kirves": "Pieni kirves, joka soveltuu esimerkiksi köynnösten hakkaamiseen."
            },
        "vinkki": "Ota täältä mukaasi esineet."
    },

    "ranta": {
        "nimi": "Järven ranta",
        "kuvaus": "Olet saapunut järven rannalle. Järven pinta värähtelee, ja hetkessä veden syvyyksistä nousee eteesi jättimäinen vaskitsa.",
        "toinen_kuvaus": "Olet järven rannalla. Suuri vaskitsa on osittain veden alla, sen pää vedenpinnan yläpuolella.",
        "hahmo": "vaskitsa",
        "esineet": {},
        "oikeaEsineKäytetty": False,
        "uusi_esine": {
            "patsas": "Eläinhahmoinen patsas, mutta et tunnista mitä eläintä se kuvastaa. Patsas muistuttaa rituaali- tai palvontaesinettä. "
        },
        "vinkki": "Anna vaskitsalle sen haluama esine, jonka voit löytää kaivoksesta. Muista käydä myös pohjoisessa suunnassa."
    },

    "rakennus": {
        "nimi": "Vanha puumökki",
        "kuvaus": "Olet hylätyn pienen puumökin sisällä.\nMökin katto on osittain lahonnut, ja mökki on ollut pitkään luonnonvoimien armoilla. \nTäällä on erilaisia kaivostyöskentelyyn sopivia esineitä.",
        "esineet": {
            "lyhty": "Lyhty, joka mahdollistaa pimeässä kulkemisen.",
            "hakku": "Painava, metallipäinen hakku. Soveltuu kivien louhimiseen."
        },
        "vinkki": "Ota täältä esineitä matkaasi. Voit tarkastella alueelta löytyviä esineitä 'esineet'-komennolla.",
    },

    "lähde": {
        "nimi": "Ametistilähde",
        "kuvaus": "Olet hohtavan lähteen äärellä. Violetteja ametisteja kasvaa luolan seinistä ja lähteen pohjalla. \nVesi on kirkasta, ja lähteestä heijastuu valoa luolan ametistiseinämiin. \nSinulle tulee olo, että et ole täällä yksin.",
        "uusi_kuvaus": "Olet hohtavan lähteen äärellä. Violetteja ametisteja kasvaa luolan seinistä ja lähteen pohjalla. \nVesi on kirkasta, ja lähteestä heijastuu valoa luolan ametistiseinämiin.",
        "uusi_kuvaus_hahmo": "Olet hohtavan lähteen äärellä. Violetteja ametisteja kasvaa luolan seinistä ja lähteen pohjalla. \nVesi on kirkasta, ja lähteestä heijastuu valoa luolan ametistiseinämiin. \nLähteessä seisoo hahmo, joka näyttää ketulta.",
        "hahmo": {},
        "uusi_hahmo": "kettu",
        "esineet": {},
        "oikea_esine": "ametisti",
        "oikeaEsineKäytetty": False,
        "oikeaEsineDialogi": "Heität ametistin lähteeseen.",
        "vinkki": "Aseta ametisti lähteeseen, niin jotain tapahtuu.",
    },
}