#!/usr/bin/env python3
#
#
#
#
#
#
# Skapad av Isac Lagerström
#
# Senast ändrad 01-15-2026

import time
import platform

system = platform.system() #"platform" modulen har denna funktion för att se vilket operativsystem som kör detta skript.

print("Söker OS...")

if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows upptäckt. Scriptet fortsätter..")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()

else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()


#AV test signatur baserad på en EICAR test fil. Innehållet är ofarligt bara för att testa AV.
eicar_str = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with open ("AV-TESTARE.txt", "w") as f:
    f.write(eicar_str)
    print("Skriver EICAR test signaturen till filen...", end="")

time.sleep(3) #Väntar på att AV/EDR ska agera.
print(" Klar.")

print("Läser genom filen och söker efter EICAR test signaturen...")
try:
    with open ("AV-TEST-OFARLIG.txt", "r") as f:
        file_contents = f.read()

    #Checkar om filens innehåll matchar EICAR signaturen
    if file_contents == eicar_str:
        print("Filen innehåller fortfarande test signaturen, vilket betyder att den inte har uppmärkts av ditt antivirus eller EDR.")
        input("tryck ENTER för att avbryta.")

#Exception för om filen inte kan hittas, vilket betyder att antivirus funkar.
except Exception as e:
    print("""Filen kunde inte läsas! 
        Ditt antivirus har troligen tagit bort eller lagt flien i karantän.
        Ditt AV eller EDR verkar fungera väl med att,
        identifiera kända virus signaturer!
        
        Om du använder Windows Defender och vill verifiera detektionen:
        
        - Tryck på Win+R och skriv in eventvwr.msc
        - öppna Applications and Services Logs
        - Navigera till Microsoft/Windows/Windows Defender/Operational.
        
        I denna log, bör du se event ID 1116 för virus detektion och
        1117 för antivirusets agerande så som karantän eller borttagningar.""")
    input("Tryck ENTER för att avsluta.")

