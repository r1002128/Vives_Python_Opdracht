# Opdracht Programming in Python

## Author
Khena Jacobs
khena.jacobs@student.vives.be

## Versioning
0.1.0 Initial setup

0.2.0 Adding all missing commands & finalize README.md

## Introductie
Deze opdracht is in functie van het vak Programming in Python waar we op zelfstandige basis een Python toepassing moeten bouwen op basis van gegeven criteria.

## Database
De database die we gebruiken voor deze oefening komt van een publieke repository waar er meerdere voorbeelden beschikbaar zijn. Wij gebruiken 'car_crashes.db' (https://github.com/davidjamesknight/SQLite_databases_for_learning_data_science/blob/main/car_crashes.db). 

We plaatsen de database onder de folder /data en vergeten niet de db naam (en het juiste pad) toe te voegen aan een aangemaakte bestand settings.py. Je kan een voorbeeld terugvinden van hoe de variabele noemt onder settings-example.py


## Gebruik van het script
Het script laat toe om drie commando's (get, add en export) te gebruiken. We starten het script door het met python3 te runnen. Alle input wordt via CLI ingegeven en dus niet als een systeem variabele.

python3 main.py

### Get
Het get-commando wordt gebruikt om een specifieke rij uit de database op te vragen op basis van een ID. Wanneer dit commando wordt uitgevoerd, moet een geldig ID worden opgegeven. Het systeem zal de rij met de overeenkomende ID uit de database halen en de gegevens weergeven.

## Add

Met het add-commando kunnen nieuwe gegevens aan de database worden toegevoegd. De gebruiker geeft een ID en initialen op (bestaande uit exact 2 karakters). Er wordt alleen gecontroleerd op de lengte van de initialenstring om ervoor te zorgen dat deze precies 2 karakters bevat. Andere validaties worden niet uitgevoerd voor dit voorbeeld.

## Export

Het export-commando wordt gebruikt om gegevens uit een specifieke tabel van de database naar een CSV-bestand te exporteren. De gebruiker geeft een bestandsnaam en een tabelnaam op. Het systeem zorgt ervoor dat de bestandsnaam altijd eindigt op ".csv" om een correct CSV-bestand te genereren.
