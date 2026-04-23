# uke11-prosjekt
uke 11
interessegruppe spill. var syk mandag-onsdag, brukte tiden jeg hadde på torsdag for å se på oppgaven og se videoer om hvordan man eksporterer godot spill

(etter hvert gikk jeg for den lette metoden, og la i stedet selve source code inn i en mappe i stedet for å installere templates og eksportere spillet hit)

planen er å gjøre hele spillet om til ett level som er ca. 4-5 ganger så lang som det jeg har nå, og legge til ulike måter å få spilleren til å bli irritert/lei av spillet. så langt har jeg en bevegende plattform, falske blokker som man kan falle gjennom, en dødelig spiker og en killzone under mappet som teleporterer deg til start om man faller av. jeg tror disse målene er realistiske

---------------------------------------------------
# uke 16 logg
Mandag
Gjorde ikke noe særlig

Tirsdag
Prøvde å eksportere spillet mitt til HTML5, men fikk meldingen «failed to fetch» når jeg åpnet spillet. Jeg tenker at det var fordi nettleseren ikke hadde tilgang til de filene, og derfor kunne ikke spillet lastes inn.

Onsdag


Torsdag
fikk hoste siden lokalt og på en server, men brukte ngrok (nesten det samme som å hoste server via itch.io, bare at ngrok er dev server og kan ikke være live 24/7). vurderte å gjøre det via flask også, men var ikke motivert nok

Fredag
Laget en dør jeg skal eventuelt bruke for hvert level. I level 1, så trenger man 6 coins for å åpne døra i slutten av levelet. Koden funker greit, men når jeg fikk mer enn 6 coins, så krasjet spillet med errormeldingen «Attempt to call function 'unlock' in base 'previously freed' on a null instance.»
Det skjedde fordi queue_free() fjerner døren helt, og når GameManager prøver å bruke door.unlock(), så finnes ikke døra lenger. Det fører til at spillet krasjer når koden prøver å bruke den

https://files.catbox.moe/4nepn7.png

https://files.catbox.moe/h7yy40.png
   
har lært hvordan man hoster server med ngrok. sendte ulike venner lenken til spillet mitt, de synes det var gøy (selv om spillet er kort).
blitt litt mer kjent med godot og powershell kommandoer
