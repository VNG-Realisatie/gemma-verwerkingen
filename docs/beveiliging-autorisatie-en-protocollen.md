# Beveiliging, autorisatie en protocollen

## Inleiding
Hieronder wordt beschreven hoe de standaard 'gemma-verwerkingen' bijdraagt aan beveiliging en privacy-bescherming. 

## Doel
De functionarissen gegevensbescherming (FG's) moeten borgen dat een organisatie voldoet aan de eisen van de AVG. De opzet van de Common Ground zorgt ervoor dat deze taak in hoge mate wordt gefaciliteerd, gestructureerd en tot op zekere hoogte wordt geautomatiseerd. Ook diverse overige taken die voortkomen uit de AVG worden in hoge mate ondersteund. Denk daarbij aan het beantwoorden van verzoeken van burgers tot inzicht in opvragingen van zijn/haar persoonsgegevens.

## Organisatie
Belangrijk uitgangspunt is dat organisaties elkaar vertrouwen op organisatieniveau. Elke combinatie van 2 individuele orgnisaties (hierna A en B) heeft een verwerkingsovereenkomst, waarin staat welke gegevens A van B mag opvragen, B van A mag opvragen, A aan B mag verstrekken en B aan A mag verstrekken. De overeenkomst is gedetailleerd tot attribuutniveau. 
Bijvoorbeeld:
- elke gemeente mag van elke gemeente BRP-gegevens opvragen en binnen de BRP een alle persoonskenmerken;
- elke gemeente mag van een kadastraal object voornaam, achternaam en zakelijk recht op een perceel opvragen maar niet geboortedatum 

Hoewel er dus tussen elk tweetal organisaties een overeenkomst moet zijn, zal (bijvoorbeeld) het kadaster niet met elke gemeente andere leveringsvoorwaarden willen hebben, dus hierin zal verregaand gestandaardiseerd moeten worden.

Er is een verwerkingsregister bij de organisatie die gegevens opvraagt en een verwerkingsregister bij de organisate die gegevens verstrekt. Gemeenten en andere organisaties kunnen beide rollen vervullen. Een afspraak over welke bevragingen tussen organisaties mogelijk zijn wordt altijd aan beide kanten vastgelegd. Daarbij wordt ook de rol vastgelegd, namelijk vrager of verstrekker. Deze rol ligt vast op organisatieniveau.

## NLX
NLX is een gateway (of poortwachter) die in het Common-Ground-project wordt gebouwd. De NLX-software wordt als open source ter beschikking gesteld via Github. Elke organisatie heeft minimaal 1 eigen NLX-node. Deze node wordt gerealiseerd in de vorm van een lokale installatie (on premise dus) van de NLX. De gateway handelt op een veilige manier berichten af. Dit zijn berichten tussen organisaties maar ook berichten binnen de organisatie. Hij weet welke gegevens met wie uitgewisseld mogen worden en zorgt ervoor dat deze afspraak wordt gehandhaafd. Maar hij kijkt niet of op basis van de juiste grondslag of met het juiste doel gegevens worden opgevraagd. De gemeente moet er zelf voor zorgen dat ze niet onrechtmatig gegevens opvraagt. De gemeente die gegevens opvraagt bij een andere organisatie geeft dus niet doel en grondsag van deze bevraging door.

## Verwerkingsregister binnen NLX
NLX kent een verwerkingsregister (ook wel validatieregister genoemd). Hierin wordt vastgelegd welke bevraging mag worden uitgevoerd op basis van welke grondslag en binnen welke processtap. Voor een gedetailleerde beschrijving, zie het voorlopige @informatiemodel van het verwerkingsregister. NLX biedt een user-interface om het verwerkingsregister te kunnen vullen en beheren.

NB het informatiemodel is op dit moment nog niet uitgekristalliseerd. Nu lijkt het erop dat er binnen een proces meerdere processtappen (kunnen) zijn (1 op n dus) en binnen een processtap weer meerdere verwerkingsactiviteiten. Een verwerkingsactiviteit is een specifieke bevraging op een specifieke gegevensverzameling. Dit gaat verder dan de huidige wettelijke eisen voor het artikel-30-register. Daarvoor is slechts vereist dat je per proces vastlegt welke categorieën persoonsgegevens en welke bijzondere persoonsgegevens je verwerkt op basis van welke grondslag. De detaillering die NLX aanbrengt is echter noodzakelijk voor goed gemeeentelijk privacymanagement en om taken op het gebied van verantwoordlng te kunnen automatiseren.

## Logging binnen NLX
Om vast te kunnen wie wanneer en waarvoor informatie heeft opgevraagd of verstrekt legt NLX een aantal berichtkenmerken vast in logfiles. Voor detailinformatie hierover zie het betreffende @informatiemodel. Iedere gelogde bevraging kent een verwijzing naar een regel in het verwerkingsregister.

## Logfiles per applicatie
Niet binnen NLX, maar wel noodzakelijk voor de hele opzet, moet elke aangesloten applicatie die persoonsgegevens verwerkt ook een logfile (auditrail) bijhouden. Dit is dus een eis die gemeenten aan leveranciers moeten stellen (wat niet nieuw is maar vaak nog wel aandacht behoeft). Vanuit Common Ground gaan we voorschrijven hoe zo'n log eruit moet zien. Hiervoor is een apart document @[logging requirements voor applicaties]. Deze voorschriften zijn nodig om geautomatiseerde auditing mogelijk te maken.

## Audits
Met de beschreven opzet wordt dus elke bevraging gelogd in 2 verwerkingsregisters en in 2 applicatielogfiles (bij vrager en leverancier). Met deze gecombineerde registers/logfiles kan automatisch auditing worden toegepast. M.a.w. de gemeente kan laten zien of alle verwerkingen rechtmatig zijn geweest.

In de AVG heeft de burger ook een rol als auditor. Hij kan opvragen welke bevragingen er over hem zijn uitgevoerd. Dit recht heeft hij nu al en dit kan, met de huidige stand van informatievoorziening bij gemeenten, heel veel handwerk kosten. Dankzij de opzet vanuit Common Ground kan dat automatisch en vrijwel real time, of, iets minder ambitieus, binnen een dag op verzoek.

## Aandachtspunten
1. Afgezien van privacygevoelige gegevens, zijn er gegevens die op andere gronden gevoelig zijn en bescherming behoeven, namelijk: openbare orde / financieel / auteursrechtelijk / overige zware belangen van de gemeente. (Hier is nog geen definitieve classificatie voor.) Het omgaan met deze overige gevoelige gegevens kan helemaal of bijna helemaal volgens hetzelfde stramien.
2. Het zou voor de implementatie een enorm voordeel zijn als gemeentelijke processen worden gestandaardiseerd vanuit het perspectief van gegevensbeveiliging. Dat maakt het mogelijk voor alle gemeenten om eenvoudig processtappen te koppelen aan grondslagen en verwerkingsactiviteiten. Kanttekening: lokale varianten moeten mogelijk blijven, al was het maar omdat elke gemeente via de APV eigen grondslagen kan creëren.
3. Bij binnengemeentelijke uitwisseling van privacygevoelige gegevens via nlx moeten gebruikers en procesgegevens in de header van de berichten worden meegegeven.
