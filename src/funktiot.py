import sys
import time

viive = 0.5
pitkäViive = 1.0

# Tulostaa pelaajan inventaarion.
# Parametri: esineet - dict. Pelaajan inventaario.
def tulosta_inventaario(esineet):

    if esineet is None or len(esineet) == 0:
        print()
        print('Sinulla ei ole mukana mitään.')

    else:
        print()
        print('Sinulla on mukana:')
        for esine in esineet:
            print(f'- {esine.capitalize()}')

# Tulostaa pelaajan nykyisessä sijainnissa olevat esineet.
# Parametri: nyky_sijainti - dict. Sanakirja joka kuvaa nykyisen sijainnin paikan.
def listaa_esineet(nyky_sijainti):

    print()
    print('Tutkitaan mitä täältä löytyy.')

    if 'esineet' in nyky_sijainti and len(nyky_sijainti["esineet"]) > 0:
        for esine in nyky_sijainti["esineet"]:
            print(f'- {esine.capitalize()}')

    else:
        print('Tällä alueella ei ole mitään esineitä.')

# Tulostaa hahmon puheen.
# Parametri: hahmo - dict. Sanakirja, joka kuvaa hahmon ominaisuuksia ja puhuttuja lauseita.
def puhu(hahmo):

    if (hahmo["puhuttu"] == False):

        print(f'Puhut hahmon {hahmo["nimi"]} kanssa.')
        print()
        print(f'{hahmo["nimi"].capitalize()}:')
        print(hahmo["ekaDialogi"])
        print()
        hahmo["puhuttu"] == True

    else:
        print()
        print(hahmo["tokaDialogi"])

# Antaa pelaajan esineen nykyisessä sijainnissa olevalle hahmolle.
# Parametrit: nyky_sijainti - dict. Sanakirja, joka kuvaa pelaajan nykyistä sijaintia pelimaailmassa.
#             hahmot - dict. Sanakirja, joka sisältää kaikkien pelimaailman hahmojen tiedot.
#             pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
#             esine - string. Esineen nimi, joka annetaan hahmolle.
def anna(nyky_sijainti, hahmot, pelaaja, esine):

    if "hahmo" in nyky_sijainti:
        hahmo_nimi = nyky_sijainti["hahmo"]
        hahmo_info = hahmot[hahmo_nimi]

        # "Kettu"-hahmolle esineen antaminen poikkeaa muista.
        if hahmo_nimi == "kettu":
            if esine in hahmo_info.get("oikea_esine", []):
                print(hahmo_info.get("oikeaEsineDialogi"))

                del pelaaja['esineet'][esine]

                hahmo_info["oikea_esine"].remove(esine)
                pelaaja['pisteet'] += 10
                hahmo_info["puhuttu"] = True

                # Jos kaikki oikeat esineet on annettu ketulle, tarkistetaan onko peli voitettu.
                if not hahmo_info["oikea_esine"]:
                    print(hahmo_info.get("kolmasDialogi"))
                    onko_voitto(pelaaja)
            else:
                print(hahmo_info.get("vääräEsineDialogi"))

        else:
            # Jos esine on hahmon haluama oikea esine.
            if esine == hahmo_info.get("oikea_esine"):
                print()
                print(f'{hahmo_nimi.capitalize()}:')
                print(hahmo_info.get("oikeaEsineDialogi"))
                print()

                del pelaaja['esineet'][esine]

                pelaaja['pisteet'] += 10
                hahmo_info["puhuttu"] = True
                hahmo_info["esineAnnettu"] = True
                hahmo_info["kuvaus"] = hahmo_info["uusi_kuvaus"]

                # Lisää nykyiseen sijaintiin uuden esineen.
                if "uusi_esine" in nyky_sijainti:
                    uusi_esine_avain, uusi_esine_arvo = nyky_sijainti["uusi_esine"].popitem()
                    nyky_sijainti["esineet"][uusi_esine_avain] = uusi_esine_arvo
                    print(f"Paikkaan ilmestyi uusi esine: {uusi_esine_avain}!")

                    # Päivittää nykyisen sijainnin kuvauksen.
                    if "toinen_kuvaus" in nyky_sijainti:
                        nyky_sijainti["kuvaus"] = nyky_sijainti["toinen_kuvaus"]

            # Jos esine ei ole hahmon haluama esine.
            else:
                print()
                print(f'{hahmo_nimi.capitalize()}:')
                print(hahmo_info.get("vääräEsineDialogi"))
                print()

    else:
        print("Täällä ei ole ketään kelle antaa esinettä.")

# Kysyy pelaajalta kahden inventaariossa olevan esineen nimeä, ja yhdistää ne jos ne ovat "miekka" ja "kahva".
# Parametri: pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
def yhdistä_esineet(pelaaja):

    print()

    try:
        esine1 = input("Anna ensimmäinen esineen nimi: ").strip()
        esine2 = input("Anna toinen esineen nimi: ").strip()

        if not all(map(str.isalpha, esine1)) or not all(map(str.isalpha, esine2)):
            raise ValueError("Esineen nimi voi sisältää vain kirjaimia.")

        if esine1 in pelaaja['esineet'] and esine2 in pelaaja['esineet']:

            if (esine1 == "miekka" and esine2 == "kahva") or (esine1 == "kahva" and esine2 == "miekka"):
                del pelaaja['esineet']['kahva']
                del pelaaja['esineet']['miekka']

                pelaaja['esineet']['hallasapeli'] = "Muinainen koristeellinen miekka, jonka terä tuntuu jäätävältä."
                print()
                print("Kiinnitit kahvan miekkaan. Miekka on maaginen, ja sen terä hohkaa kylmää.")
                print(f"Inventaarioosi ilmestyi uusi esine: hallasapeli!")
                pelaaja['pisteet'] += 20

            else:
                print()
                print("Näitä kahta ei voi yhdistää keskenään.")

        elif esine1 in pelaaja['esineet'] or esine2 in pelaaja['esineet']:
            print()
            print("Sinulla on vain toinen näistä esineistä.")

        else:
            print()
            print("Sinulla ei ole näitä esineitä.")

    except ValueError as virhe:
        print(f"Virhe: {virhe}")

# Ottaa esineen nykyisestä sijainnista ja lisää sen pelaajan inventaarioon.
# Parametrit: esine - string. Otettavan esineen nimi.
#             paikka - dict. Pelaajan nykyinen sijainti.
#             inventaario - dict. Pelaajan inventaario, johon esine lisätään.
def ota_esine(esine, paikka, inventaario):

    if len(inventaario) == 6:
            print('Sinulla on jo kuusi esinettä mukanasi, et voi ottaa mukaan enempää.')

    elif esine in inventaario:
        print('Sinulla on jo sellainen mukana.')

    elif esine == 'kaikki':
        for objekti, kuvaus in paikka['esineet'].items():
            inventaario[objekti] = kuvaus
        paikka['esineet'] = {}
        print("Kaikki esineet otettu.")

    else:
        if esine in paikka['esineet']:
            inventaario[esine] = paikka['esineet'][esine]

            del paikka['esineet'][esine]
            print(f"{esine.capitalize()} otettu.")

            # Päivittää nykyisen sijainnin kuvauksen.
            if "uusi_kuvaus" in paikka:
                paikka["kuvaus"] = paikka["uusi_kuvaus"]

        # Jos pelaaja koittaa ottaa hahmon.
        elif 'hahmo' in paikka:
            if esine in paikka['hahmo']:
                hahmon_nimi = paikka['hahmo']
                print(f'Se on mahdotonta, {hahmon_nimi} on liian suuri, että voisit edes nostaa sitä.')

        elif esine == 'kukka' or esine == 'kivi':
            print('Et voi ottaa mukaasi sitä.')

        else:
            print('Ei täällä ole sellaista.')

# Pudottaa esineen pelaajan inventaariosta nykyiseen sijaintiin.
# Parametrit: esine - string. Pudotettavan esineen nimi.
#             paikka - dict. Pelaajan nykyinen sijainti.
#             inventaario - dict. Pelaajan inventaario, johon esine lisätään.
def pudota_esine(esine, paikka, inventaario):

    if esine in inventaario:
        paikka['esineet'][esine] = inventaario[esine]

        del inventaario[esine]
        print(f"{esine.capitalize()} pudotettu.")

    else:
        print('Ei sinulla ole sellaista.')

# Käyttää pelaajan inventaariossa olevan esineen.
# Parametrit: esine - string. Käytettävän esineen nimi.
#             paikka - dict. Pelaajan nykyinen sijainti.
#             inventaario - dict. Pelaajan inventaario, josta esine käytetään.
#             esineLista - dict. Sanakirja jossa kuvataan esineitä.
#             pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
def kayta_esine(esine, paikka, inventaario, esineLista, pelaaja):

    if esine in inventaario:
        if paikka.get('oikea_esine') == esine:

            print()
            print(paikka.get("oikeaEsineDialogi"))
            print(esineLista[esine]["esineKäytettyDialogi"])
            paikka["oikeaEsineKäytetty"] = True

            del inventaario[esine]

            pelaaja['pisteet'] += 10

            # Lisää nykyiseen sijaintiin uuden esineen.
            if "uusi_esine" in paikka:
                uusi_esine_avain, uusi_esine_arvo = paikka["uusi_esine"].popitem()
                paikka["esineet"][uusi_esine_avain] = uusi_esine_arvo
                print(f"Paikkaan ilmestyi uusi esine: {uusi_esine_avain}!")

            # Lisää nykyiseen sijaintiin uuden hahmon.
            elif "uusi_hahmo" in paikka:
                paikka["hahmo"] = paikka.pop("uusi_hahmo")
                paikka["kuvaus"] = paikka["uusi_kuvaus_hahmo"]
                print(f"Paikkaan ilmestyi uusi hahmo, {paikka["hahmo"]}!")

            # Päivittää nykyisen sijainnin kuvauksen.
            elif "uusi_kuvaus" in paikka:
                paikka["kuvaus"] = paikka["uusi_kuvaus"]

        else:
            print("Tämä ei ole oikea paikka käyttää sitä.")
    else:
        print("Sinulla ei ole sellaista esinettä.")

# Tulostaa esineen tai hahmon kuvauksen.
# Parametrit: esine - string. Katsottavan esineen tai hahmon nimi.
#             paikka - dict. Pelaajan nykyinen sijainti.
#             inventaario - dict. Pelaajan inventaario, jossa esine voi olla.
#             hahmot - dict. Sanakirja joka kuvaa hahmoja.
def katso_objektia(esine, paikka, inventaario, hahmot):

    if esine in paikka.get("esineet", []):
        print(paikka["esineet"][esine])

    elif esine in inventaario:
        print(inventaario[esine])

    elif esine in paikka.get("hahmo", []):
        hahmo_nimi = esine
        print()
        print(hahmot[hahmo_nimi]["kuvaus"])

    elif esine == 'kukka' or esine == 'luonnonkukka':
        print("Onpas hieno kukka. Noniin, eipäs jäädä haaveilemaan tänne.")

    elif esine == 'kivi':
        print("Kivi näyttää siltä, että sen voisi saada halki jollain.")

    else:
        print("Täällä ei ole sellaista.")

# Liikkuminen pelaajan haluttuun suuntaan, jos se on mahdollista.
# Parametrit: ilmansuunta - string. Pelaajan syöttämä ilmansuunta.
#             kohti_paikka - dict. Sanakirja joka kuvaa nykyisen sijainnin yhteyksiä muihin sijainteihin.
#             nykyinen_sijainti - dict. Pelaajan nykyinen sijainti.
#             hahmot - dict. Sanakirja joka kuvaa hahmoja.
# Palauttaa: dict - Pelaajan uusi sijainti pelimaailmassa.
def mene_suunta(ilmansuunta, kohti_paikka, nykyinen_sijainti, hahmot):
    suunta = ilmansuunta

    if kohti_paikka[suunta]:
        uusi_sijainti = kohti_paikka[suunta]

        # Tarkistaa onko nykyisessä paikassa hahmo, joka estäisi liikkumiseen haluttuun suuntaan.
        if "hahmo" in nykyinen_sijainti and nykyinen_sijainti["hahmo"]:
            hahmo_nimi = nykyinen_sijainti["hahmo"]
            hahmo_info = hahmot.get(hahmo_nimi)

            if hahmo_info:

                if hahmo_info["esineAnnettu"] == False and nykyinen_sijainti.get("estetty_suunta") == suunta:
                    print(f"{hahmot[hahmo_nimi]["nimi"].capitalize()} estää sinua menemästä tähän suuntaan.")

                    return nykyinen_sijainti

                else:
                    return uusi_sijainti

        # Tarkistaa onko oikea esine käytetty nykyisessä paikassa, jotta liikkuminen on mahdollista haluttuun suuntaan.
        elif "oikeaEsineKäytetty" in nykyinen_sijainti:

            if nykyinen_sijainti["oikeaEsineKäytetty"] == False and nykyinen_sijainti.get("estetty_suunta") == suunta:
                print("Tarvitset jonkun esineen apua mennäksesi tähän suuntaan.")

                return nykyinen_sijainti

            else:
                return uusi_sijainti

        else:
            return uusi_sijainti
    else:
        print("Tässä suunnassa ei ole mitään.")

        return nykyinen_sijainti

# Palauttaa katsotussa ilmansuunnassa olevan sijainnin nimen, jos siellä on jotain.
# Parametrit: ilmansuunta - string. Pelaajan valitsema ilmansuunta.
#             kohti_paikka - dict. Sanakirja joka kuvaa nykyisen sijainnin yhteyksiä muihin sijainteihin.
# Palauttaa: dict tai None. Sijainnin nimi valitsemassa ilmansuunnassa, tai None, jos sijaintia ei ole.
def katso_suunta(ilmansuunta, kohti_paikka):
    suunta = ilmansuunta

    if kohti_paikka[suunta]:
        katsottu_paikka = kohti_paikka[suunta]

        return katsottu_paikka

    else:
        return None

# Muuntaa annetun ilmansuunnan perusmuotoon.
# Parametri: suunta - string. Pelaajan antama ilmansuunta, joka voi olla taivutetussa muodossa (esim. pohjoiseen).
# Palauttaa: string tai None. Perusmuoto ilmansuunnasta, tai None jos ilmansuuntaa ei tunnistettu.
def muunna_ilmansuunta(suunta):

    if suunta.startswith("pohjoi"):
        return "pohjoinen"

    elif suunta.startswith("itä"):
        return "itä"

    elif suunta.startswith("etelä"):
        return "etelä"

    elif suunta.startswith("län"):
        return "länsi"

    else:
        return None

# Tarkistaa onko pelaaja voittanut pelin pistemäärän perusteella. Päättää pelin, jos pistemäärä on tavoitettu.
# Parametri: pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
def onko_voitto(pelaaja):

    if pelaaja['pisteet'] >= 140:
        print()
        print("Onneksi olkoon, voitit pelin!")
        lopputekstit(pelaaja)
        sys.exit()

# Tulostaa kaikki pelimaailman sijainnit ja niissä olevat esineet.
# Ei listaa esineitä, joiden ilmestymiseen tarvitsee hahmon tai toisen esineen apua.
# Parametri: pelimaailma - dict. Sanakirja, joka sisältää kaikki sijainnit ja tiedot niistä.
def tulosta_kaikki_esineet(pelimaailma):

    for nimi, sijainti in pelimaailma.items():
        esineet = sijainti.get("esineet")
        nimi = sijainti.get("nimi")

        if esineet:
            print(f"Sijainti: {nimi}")
            print("Esineet:")

            for esine, kuvaus in esineet.items():
                print(f"- {esine}: {kuvaus}")

        else:
            print(f"Sijainti: {nimi}")
            print("Ei esineitä tässä sijainnissa.")

        print()

# Tulostaa pelin alkutekstit ja ohjeet pelaamiseen.
# Parametrit: pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
#             paikka - dict. Pelaajan nykyinen sijainti.
def alkutekstit(pelaaja, paikka):

    print(f'Tervetuloa pelaamaan {pelaaja['nimi']}!')
    time.sleep(viive)
    print('\nTämä on tekstiseikkailupeli nimeltä Mysteerimetsä.')
    print('Tehtäväsi on tutkia maailmaa, kerätä esineitä ja esineiden avulla edetä syvemmälle metsän siimekseen.')
    print('Eri toiminnoista kerääntyy pelaajalle pisteitä.')
    print('\nKuinka pelata:')
    print('-' * 20)

    print('Peliä pelataan antamalla yksi- tai kaksisanaisia komentoja.')
    print('\nLiikkuminen: mene ilmansuuntaan')
    print('Sijainti: sijainti')
    print('Ympäristön katselu: katso')
    print('Ilmansuunnan katselu: katso ilmansuuntaan')
    print('Esineen katselu: katso esine')
    print('Esineiden komentoja: ota, pudota, anna, käytä')
    print('Pelaajan inventaario, mihin otetut esineet menevät: mukana')
    print('Tarkemmat ohjeet pelaamiseen: ohjeet')
    print('Lopeta peli: lopeta')
    print('-' * 20)

    print()
    time.sleep(pitkäViive)
    print(paikka["kuvaus"])

    time.sleep(viive)
    print('\nMitä haluat tehdä?\n')

# Tulostaa pelin lopputekstit pelin päättyessä, ja pelaajan lopullisen pistemäärän.
# Parametri: pelaaja - dict. Sanakirja, jossa on pelaajan tiedot.
def lopputekstit(pelaaja):

    print(f'Kiitos pelistä {pelaaja['nimi']}! Sait {pelaaja['pisteet']}/140 pistettä.\n')

# Tulostaa pelin tarkemmat ohjeet.
# Parametri: paikka - dict. Pelaajan nykyinen sijainti.
def info(paikka):

    print('Ohjeet pelin pelaamiseen:')
    print('-' * 20)

    print('Peliä pelataan antamalla yksi- tai kaksisanaisia komentoja.')
    print('*' * 3)
    print('Liikkuminen tapahtuu kulkemalla ilmansuuntien mukaan.')
    print('Liikkuminen: mene ilmansuuntaan, esim. "mene pohjoiseen".')
    print('Tämän hetkinen sijainti: sijainti')
    print('*' * 3)
    print('Ympäristöä, ilmansuuntaa tai esineitä tutkitaan katselemalla.')
    print('Ympäristön katselu: katso')
    print('Ilmansuunnan katselu: katso ilmansuunta, esim. "katso pohjoinen"')
    print('Esineen katselu: katso esine, esim. "katso miekka".')
    print('*' * 3)
    print('Pelimaailmassa on paljon esineitä, jotka ovat tärkeässä roolissa pelissä.')
    print('Jokaisella esineellä on vain yksi oikea käyttötarkoitus,')
    print('jonka jälkeen ne tuhoutuvat tai poistuvat inventaariosta.')
    print('Esineisiin kohdistuvia komentoja: ota, pudota, anna, käytä, esim. "ota marja".')
    print('Näiden lisäksi on yksisanainen komento: yhdistä.')
    print('Yhdistä komennolla voit yhdistää kaksi eri esinettä kerran pelin aikana.')
    print('*' * 3)
    print('Pelaajan mukaansa ottamat esineet menevät inventaarioon, josta niitä voi käyttää.')
    print('Pelaajan inventaarion katselu: mukana -TAI- inventaario')
    print('*' * 3)
    print('Pelimaailmassa voi olla esineitä, jotka saat listaksi komennolla: esineet')
    print('*' * 3)
    print('Pelimaailmassa on hahmoja, joita voit katsella, joille voit puhua ja antaa esineitä.')
    print('Hahmon katselu: katso hahmo, esim "katso kissa"')
    print('Esineen antaminen hahmolle: anna esine, esim "anna marja"')
    print('Hahmolle puhuminen: puhu hahmo, esim "puhu kissa".')
    print('*' * 3)
    print('Tämän hetkinen pistemääräsi: pisteet')
    print('*' * 3)
    print('Jos et tiedä mitä tehdä pelimaailmassa,')
    print('saat vinkin komennolla: vinkki -TAI- vihje')
    print('*' * 3)
    print('Jos olet pudottanut esineen jonnekin, etkä muista enää minne,')
    print('saat kaikki pelin sijainnit ja esineet näkyville komennolla:')
    print('näytä kaikki')
    print('*' * 3)
    print('Näe kaikki pelissä toimivat komennot antamalla komento: komennot')
    print('Kun haluat lopettaa pelin,')
    print('voit poistua pelistä: lopeta')
    print('-' * 20)
    print()

    time.sleep(pitkäViive)
    print(paikka["kuvaus"])

    time.sleep(viive)
    print('\nMitä haluat tehdä?\n')

# Tulostaa kaikki pelissä käytettävät komennot.
# Parametri: paikka - dict. Pelaajan nykyinen sijainti.
def tulosta_komennot(paikka):

    print('Kaikki pelissä käytettävissä olevat komennot:')
    print('-' * 20)

    print('katso')
    print('katsele')
    print('tutki')
    print('mene ilmansuuntaan')
    print('katso ilmansuuntaan')
    print('katsele ilmansuuntaan')
    print('katso hahmo')
    print('puhu hahmo')
    print('käytä esine')
    print('anna esine')
    print('katso esine')
    print('katsele esine')
    print('ota esine')
    print('ota kaikki')
    print('pudota esine')
    print('lopeta')
    print('info')
    print('ohjeet')
    print('komennot')
    print('vinkki')
    print('vihje')
    print('esineet')
    print('inventaario')
    print('yhdistä')
    print('sijainti')
    print('laita esine')
    print('aseta esine')
    print('pisteet')
    print('näytä kaikki')
    print('-' * 20)
    print()

    time.sleep(pitkäViive)
    print(paikka["kuvaus"])

    time.sleep(viive)
    print('\nMitä haluat tehdä?\n')