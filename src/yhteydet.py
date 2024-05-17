# Tämä sanakirja kuvaa pelimaailman paikkojen väliset yhteydet.
yhteydet = {
    "niitty": {
        "pohjoinen": "metsän_siskäynti",
        "itä": None,
        "etelä": "polku_rantaan",
        "länsi": "polku_vuori"
    },

    "metsän_siskäynti": {
        "pohjoinen": "marjametsä",
        "itä": None,
        "etelä": "niitty",
        "länsi": "taistelutanner"
    },

    "alttari": {
        "pohjoinen": "luola_etu",
        "itä": "pimeä_aukio",
        "etelä": "metsä",
        "länsi": None
    },

    "pimeä_aukio": {
        "pohjoinen": None,
        "itä": "marjametsä",
        "etelä": None,
        "länsi": "alttari"
    },

    "metsä": {
        "pohjoinen": "alttari",
        "itä": None,
        "etelä": None,
        "länsi": None
    },

    "sienikehä": {
        "pohjoinen": None,
        "itä": None,
        "etelä": "metsä_itä",
        "länsi": None
    },

    "marjametsä": {
        "pohjoinen": None,
        "itä": "metsä_itä",
        "etelä": "metsän_siskäynti",
        "länsi": "pimeä_aukio"
    },

    "metsä_itä": {
        "pohjoinen": "sienikehä",
        "itä": None,
        "etelä": "puu",
        "länsi": "marjametsä"
    },

    "vuori": {
        "pohjoinen": None,
        "itä": "polku_vuori",
        "etelä": "rakennus",
        "länsi": None
    },

    "taistelutanner": {
        "pohjoinen": None,
        "itä": "metsän_siskäynti",
        "etelä": "polku_vuori",
        "länsi": None
    },

    "puu": {
        "pohjoinen": "metsä_itä",
        "itä": None,
        "etelä": None,
        "länsi": None
    },

    "luola_etu": {
        "pohjoinen": None,
        "itä": "luola",
        "etelä": "alttari",
        "länsi": None
    },

    "luola": {
        "pohjoinen": None,
        "itä": "lähde",
        "etelä": None,
        "länsi": "luola_etu"
    },

    "polku_vuori": {
        "pohjoinen": "taistelutanner",
        "itä": "niitty",
        "etelä": "polku_rakennus",
        "länsi": "vuori"
    },

    "polku_rakennus": {
        "pohjoinen": "polku_vuori",
        "itä": "polku_rantaan",
        "etelä": None,
        "länsi": "rakennus"
    },

    "polku_rantaan": {
        "pohjoinen": "niitty",
        "itä": "ranta",
        "etelä": None,
        "länsi": "polku_rakennus"
    },

    "kivi": {
        "pohjoinen": None,
        "itä": None,
        "etelä": "ranta",
        "länsi": None
    },

    "ranta": {
        "pohjoinen": "kivi",
        "itä": None,
        "etelä": None,
        "länsi": "polku_rantaan"
    },

    "rakennus": {
        "pohjoinen": "vuori",
        "itä": "polku_rakennus",
        "etelä": None,
        "länsi": None
    },

    "lähde": {
        "pohjoinen": None,
        "itä": None,
        "etelä": None,
        "länsi": "luola"
    }
}