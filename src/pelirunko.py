import time
from kartta import kartta
from yhteydet import yhteydet
from hahmot import hahmot
from esineet import esineet
from funktiot import tulosta_inventaario
from funktiot import puhu
from funktiot import listaa_esineet
from funktiot import anna
from funktiot import yhdistä_esineet
from funktiot import ota_esine
from funktiot import pudota_esine
from funktiot import kayta_esine
from funktiot import katso_objektia
from funktiot import mene_suunta
from funktiot import katso_suunta
from funktiot import alkutekstit
from funktiot import lopputekstit
from funktiot import info
from funktiot import tulosta_komennot
from funktiot import muunna_ilmansuunta
from funktiot import tulosta_kaikki_esineet

"""Tekstiseikkailupeli

Tämä on kevään 2024 Python-ohjelmointikurssin loppuharjoitustyö.
Peli ajetaan tästä tiedostosta, ja toimiakseen tarvitsee samassa kansiossa
olevat tiedostot hahmot.py, yhteydet.py, kartta.py, esineet.py ja
funktiot.py.

Tekijä Noora Nevalainen
"""

# Pelaaja sanakirja
pelaaja = {}

# Viive time.sleep() funktiota varten
viive = 0.5

print('-' * 50)

# Pelaajan nimen kysyminen
while True:
    try:
        pelaajan_nimi = input("Anna pelaajan nimi: ").strip()

        if len(pelaajan_nimi) == 0:
            raise ValueError('Tyhjä nimi.')

        if not pelaajan_nimi.isalpha():
            raise ValueError('Erikoismerkkejä tai numeroita nimessä.')

        pelaaja['nimi'] = pelaajan_nimi
        break

    except ValueError as virhe:
        print(f'Epäkelpo nimi: {virhe} \nKirjoita pelaajan nimi isoilla ja/tai pienillä kirjaimilla.')
        print()

print()

# Pelaajan pistemäärä
pelaaja['pisteet'] = 0

# Pelaajan esineet
pelaaja['esineet'] = {
                    "hamsteri": "Pieni jyrsijä, joka tykkää matkata taskussa. \nMistä se tänne oikein tuli? Ehkä hamsterikin on elämänsä seikkailulla, ja etsii sopivaa paikkaa minne tehdä pesä."
}

# Pelin aloituspaikka
nyky_sijainti = "niitty"

# Lukee pelaajan syötteen, sekä siistii ja pilkkoo sen osiin.
# Palauttaa: list - Lista jossa syöte on jaettu osiin.
def lue_komento():
    print('-' * 20)
    komento = input('> ').lower().strip()

    return komento.split()

# Tarkistaa onko pelaajan antama komento "lopeta".
# Parametri: komento - list, pelaajan syöte.
# Palauttaa: bool, palauttaa True jos komento on "lopeta", muutoin False.
def onko_lopetus(komento):

    if len(komento) == 1 and komento[0] == 'lopeta':
        return True

    else:
        return False

# Suorittaa toiminnon pelaajan syötteen perusteella, joka koostuu yhdestä sanasta.
# Parametri: verbi - string, pelaajan yksisanainen komento.
def yksisana(verbi):

    if verbi == 'katsele' or verbi == 'katso':
        print(kartta[nyky_sijainti]["kuvaus"])

    elif verbi == 'tutki' or verbi == 'esineet':
        listaa_esineet(kartta[nyky_sijainti])

    elif verbi == 'yhdistä':
        print('Mitkä kaksi esinettä haluat yhdistää?')
        yhdistä_esineet(pelaaja)

    elif verbi == "mukana" or verbi == "inventaario":
        tulosta_inventaario(pelaaja['esineet'])

    elif verbi == "sijainti":
        print(f'Olet paikassa {kartta[nyky_sijainti]["nimi"].lower()}.')

    elif verbi == "vinkki" or verbi == "vihje":
        print(kartta[nyky_sijainti]["vinkki"])

    elif verbi == "puhu":
        print("Tarkenna kenelle haluat puhua. (Esim. puhu kissa)")

    elif verbi == "ota":
        print("Tarkenna minkä haluat ottaa. (Esim. ota lyhty)")

    elif verbi == "pudota":
        print("Tarkenna minkä haluat pudottaa. (Esim. pudota lyhty)")

    elif verbi == "mene":
        print("Tarkenna minne haluat mennä. (Esim. mene pohjoinen)")

    elif verbi == "anna":
        print("Tarkenna mitä haluat antaa. (Esim. anna marja)")

    elif verbi == "info" or verbi == "ohjeet":
        info(kartta[nyky_sijainti])

    elif verbi == "komennot":
        tulosta_komennot(kartta[nyky_sijainti])

    elif verbi == "pisteet":
        print(f"Pistemääräsi: {pelaaja['pisteet']}/140 pistettä.")

    else:
        print(f'En tunnista komentoa: {verbi}.')

# Suorittaa toiminnon pelaajan syötteen perusteella, joka koostuu kahdesta sanasta.
# Parametrit: verbi - string, objekti - string. Pelaajan kaksisanainen komento.
def kaksisanaa(verbi, objekti):

    # Määrittää nyky_sijainti -muuttujan globaaliksi, jotta muuttujan arvoa voi muuttaa kaksisanaa-funktion sisällä.
    global nyky_sijainti

    if verbi == 'ota':
        ota_esine(objekti, kartta[nyky_sijainti], pelaaja['esineet'])

    elif verbi == 'pudota':
        pudota_esine(objekti, kartta[nyky_sijainti], pelaaja['esineet'])

    # Pelissä liikkuminen, hyväksyy ilmansuunnista perusmuodot sekä taivutetut versiot.
    # Taivutetut ilmansuunnat kuten "pohjoiseen", muutetaan perusmuotoon.
    elif verbi == 'mene' and any(objekti.startswith(suunta) for suunta in ["pohjoi", "itä", "etelä", "län"]):
        ilmansuunta = muunna_ilmansuunta(objekti)

        if ilmansuunta:
            uusi_sijainti = mene_suunta(ilmansuunta, yhteydet[nyky_sijainti], kartta[nyky_sijainti], hahmot)

            if uusi_sijainti != kartta[nyky_sijainti]:
                nyky_sijainti = uusi_sijainti
                print(f"Menet suuntaan {ilmansuunta} ja saavut paikkaan: {kartta[nyky_sijainti]['nimi'].lower()}.")
                print()
                print(kartta[nyky_sijainti]["kuvaus"])

    # Ilmansuuntaan katsominen, hyväksyy ilmansuunnista perusmuodot sekä taivutetut versiot.
    # Taivutetut ilmansuunnat kuten "pohjoiseen", muutetaan perusmuotoon.
    elif (verbi == 'katsele' or verbi == 'katso') and any(objekti.startswith(suunta) for suunta in ["pohjoi", "itä", "etelä", "län"]):
        ilmansuunta = muunna_ilmansuunta(objekti)

        if ilmansuunta:
            katsottu_paikka = katso_suunta(ilmansuunta, yhteydet[nyky_sijainti])

            if katsottu_paikka:
                print(f'Näkyvissä suunnassa {ilmansuunta}' + f': {kartta[katsottu_paikka]['nimi'].lower()}.')
            else:
                print(f"Et näe mitään suunnassa {ilmansuunta}.")

    elif verbi == 'katsele' or verbi == 'katso':
        katso_objektia(objekti, kartta[nyky_sijainti], pelaaja['esineet'], hahmot)

    elif verbi == 'puhu':
        if objekti in (kartta[nyky_sijainti]["hahmo"]):
            puhu(hahmot[objekti])
        else:
            print(f'Täällä ei ole sen nimistä kelle puhua.')

    elif verbi == 'anna':
        if objekti in pelaaja['esineet']:
            anna(kartta[nyky_sijainti], hahmot, pelaaja, objekti)
        else:
            print("Sinulla ei ole sellaista esinettä.")

    elif verbi == 'käytä' or verbi == 'laita' or verbi == 'aseta':
        kayta_esine(objekti, kartta[nyky_sijainti], pelaaja['esineet'], esineet, pelaaja)

    elif verbi == 'näytä' and objekti == 'kaikki':
        tulosta_kaikki_esineet(kartta)

    else:
        print(f'En tunnista komentoa: {verbi} {objekti}.')

# Pelin pääsilmukka, joka lukee ja käsittelee pelaajan antaman komennon.
def peli():

    while True:
        komento = lue_komento()

        if onko_lopetus(komento):
            break

        try:
            if not all(map(str.isalpha, komento)):
                raise ValueError("Komento sisältää numeroita tai erikoismerkkejä.")

        except ValueError as virhe:
            print(f"Virhe: {virhe}")
            print("Anna yksi- tai kaksisanainen komento, joka koostuu pelkistä kirjaimista. Esim. 'katso' tai 'mene pohjoiseen'.")
            continue

        pituus = len(komento)

        if pituus == 0:
            continue

        elif pituus == 1:
            verbi = komento[0]
            yksisana(verbi)

        elif pituus == 2:
            verbi = komento[0]
            objekti = komento[1]
            kaksisanaa(verbi, objekti)

        else:
            print("Epäkelpo komento. Anna yksi- tai kaksisanainen komento, esim. 'katso' tai 'mene pohjoiseen'.")

# Tarkistaa ajetaanko tämä skripti päämoduulista.
if __name__ == '__main__':
    alkutekstit(pelaaja, kartta[nyky_sijainti])
    peli()
    lopputekstit(pelaaja)