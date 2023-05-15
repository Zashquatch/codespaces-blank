def beregn_loenn(timebetaling, prosent_stilling):
    dagsloenn = timebetaling * 7.5
    ukeloenn = dagsloenn * 5
    maanedloenn = dagsloenn * 22
    aarsloenn = maanedloenn * 12 * (prosent_stilling / 100)

    return dagsloenn, ukeloenn, maanedloenn, aarsloenn


while True:
    valg = input("Hva vil du regne ut ifra? (Time/Måned/År): ")

    if valg.lower() == "time":
        timebetaling = float(input("Skriv inn timebetaling: "))
        prosent_stilling = float(input("Skriv inn prosent stilling: "))
        dagsloenn, ukeloenn, maanedloenn, aarsloenn = beregn_loenn(timebetaling, prosent_stilling)

    elif valg.lower() == "måned":
        maanedslonn = float(input("Skriv inn månedslønn: "))
        prosent_stilling = float(input("Skriv inn prosent stilling: "))
        dagsloenn = maanedslonn / 22
        ukeloenn = dagsloenn * 5
        timebetaling = dagsloenn / 7.5
        aarsloenn = maanedslonn * 12 * (prosent_stilling / 100)

    elif valg.lower() == "år":
        aarsloenn = float(input("Skriv inn årslønn: "))
        prosent_stilling = float(input("Skriv inn prosent stilling: "))
        maanedloenn = aarsloenn / 12
        dagsloenn = maanedloenn / 22
        ukeloenn = dagsloenn * 5
        timebetaling = dagsloenn / 7.5
        aarsloenn = aarsloenn * (prosent_stilling / 100)

    else:
        print("Ugyldig valg. Vennligst velg Time, Måned eller År.")
        continue

    sekundloenn = timebetaling / 3600
    minutloenn = timebetaling / 60

    sekundloenn = round(sekundloenn, 2)
    minutloenn = round(minutloenn, 2)
    dagsloenn = round(dagsloenn, 2)
    ukeloenn = round(ukeloenn, 2)
    maanedloenn = round(maanedloenn, 2)
    aarsloenn = round(aarsloenn, 2)

    print(f"Sekundlønn: {sekundloenn} kr/sek")
    print(f"Minuttlønn: {minutloenn} kr/min")
    print(f"Timelønn: {timebetaling} kr/time")
    print(f"Dagslønn: {dagsloenn} kr/dag")
    print(f"Ukelønn: {ukeloenn} kr/uke")
    print(f"Månedslønn: {maanedloenn} kr/måned")
    print(f"Årslønn: {aarsloenn} kr/år")
    print()
