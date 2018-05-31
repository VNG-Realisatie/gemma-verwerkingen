# Vragen over standaardisatieproces koppelvlakken
## Wat heeft een developer nodig om een standaard te kunnen implementeren?
* Concrete real-world use case(s) in tekst en/of afbeelding van de hele keten (vakapplicatie-service-datamodel)
* Architectuur: context van de te realiseren api/service
* Koppelvlak semantisch informatiemodel: betekenis en structuur van gegevens (uitleg over informatiemodel: wat is AN20? wat betekent kardinaliteit voor het datamodel, welke overwegingen bij het implementeren van een datamodel zijn gemaakt)
* Voorbeeld datamodel, op basis van overwegingen hierboven.
* Open API Specificatie (voor json) of xsd (voor xml)
* Referentie implementatie
  * Testen van consumerapplicatie en testen van providerapplicatie (referentie implementatie kan scenario's afspelen voor versturen van berichten
* Voorbeeldberichten (cookbook met samenstelling en verwerking van berichten). Liefst gebaseerd op de (punt 1) use case(s)
* Referentie implementatie van service EN applicatie moeten getest kunnen worden met de voorbeeldberichten
  * Referentie implementaties moeten makkelijk op developer omgeving worden opgezet (bijv. docker).

## In welke vorm moeten koppelvlakstandaard-deelproducten worden aangeboden
* In GITHUB
* In vorm waarmee bijdrageproces te doen is (code/markdown/tekst; niet MS word, Enterprise Architect, pdf, enz)

## Hoe wil je kunnen bijdragen aan een standaard?
* Via pull requests
* Op welke deelproducten?
  * Functionele beschrijving
    * User stories
  * Architectuur
    * (bijvoorbeeld processen, use cases)
    * Architectuur wordt nu gemodelleerd in Bizzdesign
  * Informatiemodellen
    * Informatiemodellen worden nu gemodelleerd in UML in tool Enterprise Architect. Deze ondersteunt git niet. Bovendien zijn er complexe afspraken over de manier van modelleren.
  * Koppelvlakdocumentatie
  * Berichtspecificatie
    * Op dit moment worden berichtspecificaties (OAS of XSD) gegenereerd vanuit UML modellen, waarmee consistentie naar informatiemodel, consistentie naar technische onderlaagafspraken en consistentie tussen specificatie en documentatie wordt gewaarborgd. Tooling voor berichtmodellen ondersteunt git niet.
  * Referentie implementatie
    * Bijdragen moeten automatisch getest worden tegen bestaande referentie implementaties. 
* Welke voorwaarden zijn er aan de tussenproducten?
  * Bewerkbaar zonder dure, voor developers niet gangbare tooling
  * Bij bekijken pull request zijn de verschillen te zien, ondersteund door github: tekstbestanden

## Wat moet koppelvlakbeheerder controleren om bijdrage te beoordelen?
* Consistentie tussen deelproducten, dus verwerking over hele stack (bijv. wijziging in bericht ook verwerkt in referentie implementatie)
* Reden/uitleg over wijziging
* Reacties met overeenstemming uit community: afstemmen pull request met andere leveranciers en gemeenten

## Hoe passen huidige maatregelen voor stimuleren implementatie van standaarden hierin?
* Compliancy
* Convenant
* Softwarecatalogus

* Of alternatief op deze drie?

# Eisen aan het koppelvlakspecificatieproces
We kennen drie soorten betrokkenen in het proces:
* Belanghebbenden, zoals gemeenten en leveranciers
  * Gemeenten willen "plug en play" interoperabiliteit en portabiliteit
  * Gemeenten willen weten welke standaarden ze kunnen/moeten/mogen vereisen (in een aanbesteding)
  * Gemeenten willen weten welke referentiecomponenten relevant zijn voor bedrijfsprocessen (bijvoorbeeld voor Jeugdzorg een jeugdzorgapplicatie, Digikoppelingadapter en CORV)
  * Leveranciers willen weten aan welke standaarden hun applicaties ze moeten voldoen
  * Leveranciers willen weten voor hun applicatie (een standaard/referentiecomponent) welke koppelingen ze moeten implementeren of kunnen gebruiken
  * Leveranciers en gemeenten (die zelf ontwikkelen) willen een standaard (kunnen) implementeren
  * Leveranciers willen investeringen in standaarden terugverdienen
  * Leveranciers en gemeenten (die zelf ontwikkelen) willen kunnen bijdragen aan een standaard, o.a. functionaliteit toe te kunnen voegen en (oorzaken voor) interoperabiliteitsproblemen op te laten lossen
* Gebruikers van de standaard, developers bij leveranciers en gemeenten
  * Willen makkelijk en snel koppelingen implementeren
  * Duidelijke (eenduidige) en eenvoudg/snel toegankelijke specificatie en definitie van de standaard (lage leercurve, betaalbare implementatie)
  * Specificatie en definitie in een vorm die aansluit bij de werkwijze en tooling die ze gebruiken bij implementatie
  * Implementaties kunnen testen
  * Kunnen bijdragen aan de standaard om snel verbeteringen (correcties of uitbreidingen) op de standaard door te voeren, zodat ze deze ook zonder vertraging kunnen gebruiken in hun implementatie
  * Kunnen bijdragen op een manier die eenvoudig is, weinig tijd kost, en aansluit op de manier waarop ze in hun werk gewend zijn bij te dragen aan specicaties
* VNG Realisatie
  * Wil de consistentie binnen en tussen standaarden bewaken
    * Tussen de koppelvlakstandaard en de GEMMA architectuur
    * Tussen informatiemodellen en berichtdefinities (xsd of oas)
    * Tussen berichtdefinities (xsd of oas) en berichtspecificaties
    * Tussen berichtdefinities en koppelvlakoverstijgende uitwissenafspraken (StUF onderlaag of API strategie)
    * In structuur van objecttypen in berichten tussen verschillende koppelvlakken (koppelvlakoverstijgend uitwisselingsgegevensmodel)
    * Tussen referentieimplementatie en berichtdefinities en koppelvlakoverstijgende uitwisselafspraken
    * In de wijze waarop de standaard wordt gespecificeerd/gedocumenteerd
  * Wil de kwaliteit van standaarden bewaken (garanderen)
    * Code te genereren op basis van xsd of oas
    * Bruikbaar voor verschillende platformen (java, .Net, Python, ...)
    * Geen dubbelingen
    * Eenduidig
    * Sluit aan bij objectgeoriëntatie
  * Wil dat de belangen van verschillende belanghebbenden worden afgewogen, zodat bij beslissingen over standaarden voldoende rekening houden met alle belanghebbenden
    * Meerdere belanghebbenden zijn betrokken bij het ontwikkelen of beoordelen van de (wijziging op) standaard
    * Meerdere belanghebbenden hebben gereageerd op (de wijziging op) de standaard
    * Wanneer er tegengestelde meningen zijn, afwegen van de meningen en komen tot een beslissing
  * Willen het proces voor ontwikkelen en beheren van de standaarden goed loopt en goed gevolgd wordt
  * Wil dat kennis en ontwikkeling van standaarden hergebruik kunnen maken van wat geleerd wordt bij het ontwikkelen of implementeren van standaarden.
    * Bijvoorbeeld door keuzes "op te tillen" naar een koppelvlakoverkoepelend niveau:
      * StUF onderlaag of API strategie (structuur en verwerking van berichten),
      * Uitwisselingsgegevensmodel (structuur van entiteittypen)

# Vorm en plek voor standaardisatieproducten en samenwerking
* Gemeenten benaderen de standaard minder technisch, of vanuit architectuur. GEMMAonline is hiervoor de aangewezen plek. Voor hun is een algemeen verhaal over doel en functionaliteit (relatief weinig detail) relevant, plus positionering in de architectuur.
* Managers en architecten bij leveranciers (die moeten weten welke standaarden moeten worden ondersteund en welke api's ze moeten realiseren) benaderen de standaard vanuit een overzicht van referentie applicatiearchitectuur: welke standaarden moet een referentiecomponent leveren; en vervolgens vanuit de standaard: welke api's moeten worden ondersteund of kunnen worden gebruikt. GEMMAonline is hiervoor de aangewezen plek.
* Developers willen bondige, maar duidelijke en specifieke beschrijving van de functionaliteit van te realiseren koppelvlakken (api's of services). Developers willen toegang tot deze informatie op de manier die ze gewend zijn bij ontwikkelwerk. Developers willen kunnen bijdragen aan de standaard om deze zo snel mogelijk aan te passen wanneer ze issues tegenkomen. Github is hiervoor de aangewezen plek.

Het gaat dus om het scheiden van de mediums voor ontsluiting van informatie over standaarden, toegespitst op gebruik per doelgroep.

# Standaardisatieproducten voor developers
Hieronder staan de soorten (deel)producten (documenten, bestanden) die samen een koppelstandaard vormen. Al deze producten zijn opgnomen in een Github repository.

## User stories
* Worden als issue gemaakt in Github
* Alleen wanneer relevant voor de api, bijvoorbeeld omdat het een proces/keten betreft

## Functionele beschrijving
* Algemene functionele beschrijving, voor hele koppelvlakstandaard
* Context in de architectuur, bijvoorbeeld welke referentiecomponenten betrokken zijn, welk domein, welk proces, welke keten
* Beschrijving in markdown (tekst met eventueel plaatje)
* Berichtinteracties
* Te ondersteunen functionaliteit per referentiecomponent
* Indien van toepassing: procesflows, user stories en/of use cases
* Beschrijving wordt gemaakt in markdown (tekst met eventueel plaatje)

N.B. inhoud van het bericht (welke elementen/attributen er in het bericht zitten) is hier nooit relevant, want daarvoor is de API specificatie.

## Koppelvlak conceptueel/semantisch informatiemodel
* Een koppelvlak gebruikt meestal (of altijd?) deelverzameling zijn van referentie-informatiemodel(len) en/of domeinmodel
* Informatiemodel (als referentiemodel of domeinmodel) is apart te beheren standaardisatie-object
* Informatiemodel is (ook) publiek online benaderbaar als webpagina, te hyperlinken per objecttype

TODO: bepalen in welke vorm het aangeboden kan worden zodat het toegankelijk is, overzichtelijk is (relaties tussen objecttypen, overzicht van gehele domein), ernaar te verwijzen is vanuit berichtspecificatie, bijdrage te leveren is door gebruikers (developers))

## Uitwisselingsgegevensmodel (UGM)
* Definieert gegevensstructuur (de structuur van entiteittypen)
* VNG Realisatie gebruikt het UGM om te bevorderen dat dezelfde gegevens op dezelfde manier worden opgenomen in verschillende berichten in evt. verschillende koppelvlakstandaarden.
* VNG Realisatie beheert dit model. Is in principe intern ding voor VNG Realisatie.
* Aanpassingen aan het model worden gevoed vanuit semantische informatiemodellen en vanuit koppelvlakontwikkeleing en -beheer. Bijvoorbeeld wanneer op een koppelvlak een pull request wordt gedaan op een berichtdefintie, kan de beheerder van het Uitwisselingsgegevensmodel ervoor kiezen dit over te nemen in het UGM.

## Uitwisseltechniek

> Ik [joeri] zou dit niet zo uitsplitsen maar uitwisseltechniek, api spec en berichtdefinitie is gewoon een OAS. De AOS biedt ook ALLES om de API documentatie te genereren.
> Deze OAS: https://ztc-staging.maykin.nl/api/v1/schema.json
> Ziet er (met alleen maar wat opmaak) zo uit: https://ztc-staging.maykin.nl/api/v1/schema/

* Beschrijft standaard patronen en afhandeling, zoals functionaliteit voor identificatie en authenticatie, pagineren, foutafhandeling, verwijzen naar gerelateerde objecten, enz.
* Is koppelvlakoverstijgend en (dus) apart te beheren standaardisatie-object
* Beschrijving in markdown (tekst met eventueel plaatjes)
* Als startpunt voor API's nemen we de API strategie en URI strategie zoals die voor Digitaal Stelsel Omgevingswet (DSO) is gemaakt.
* Gestreeft wordt naar landelijke, overheidsbrede API strategie.
* De uitwisseltechniek bevat zoveel mogelijk uitwerking in (technische) voorbeelden van wat beschreven/gespecificeerd staat.

## API specificatie
* Berichtinteractie
* Te ondersteunen functionaliteit
* Indien van toepassing: procesflow, user storie en/of use case
* Beschrijving in markdown (tekst met eventueel plaatje)
* Wordt alleen gemaakt wanneer dit nodig is, bijvoorbeeld omdat er plaatjes gebruikt worden of uitgebreide functionele of technische specificatie nodig is. In de berichtdefinitie wordt (in het geval open api specificatie) al de interactie, foutafhandeling, functionele beschrijving en link naar semantisch/conceptuele objectdefinitie opgenomen

N.B. inhoud van het bericht (welke elementen/attributen er in het bericht zitten) is hier nooit relevant, want daarvoor is de berichtdefinitie

## Berichtdefinitie
* Is de technische en (in zekere mate) functionele definitie van de berichtinteractie en het bericht
* Voor soap/xml berichten gaat het om wsdl's en xsd's
* Voor rest/json berichten gaat het om open api specificaties (OAS 3)
* Voor zover mogelijk ook functionele beschrijving van de api/service en de elementen (incl. voorbeeldwaarde) opgenomen
* In de API toelichting wordt een link naar uitgebreidere conceptuele definitie van heb object en elementen in het semantisch informatiemodel
* Vanuit de technische berichtdefinitie (wsdl/xsl of OAS) moet code te genereren zijn voor de belangrijkste programmeertalen.

## Referentieimplementatie
* Voor elke API wordt een referentieimplementatie gemaakt waarmee ontwikkelaars hun software kunnen testen.
* Er wordt een referentieimplementatie gemaakt die gebruikt kan worden voor het testen van een consumerapplicatie (door het simuleren van de provider), en er wordt een referentieimplementatie gemaakt die gebruikt kan worden voor het testen van een API provider (door het simuleren van een consumerapplicatie).
* De code van de referentieimplementatie is open source.
* In principe wordt de referentieimplementatie in één (programmeer)taal gemaakt.

# Standaardisatieproducten voor overige Belanghebbenden
Hieronder staan de soorten (deel)producten (documenten, bestanden) die samen een koppelstandaard vormen, zoals deze worden gemaakt ten behoeve van verschillende belanghebbenden (anders dan developers die het koppelvlak implementeren).
Deze belanghebbenden zijn bijvoorbeeld managers en architecten bij een gemeenten en leveranciers. Deze documentatie is gericht op het invullen van de volgende behoeften van belanghebbenden:
* Gemeenten willen weten welke standaarden ze kunnen/moeten/mogen vereisen (in een aanbesteding)
* Gemeenten willen weten welke referentiecomponenten relevant zijn voor bedrijfsprocessen (bijvoorbeeld voor Jeugdzorg een jeugdzorgapplicatie, Digikoppelingadapter en CORV)
* Leveranciers willen weten aan welke standaarden hun applicaties ze moeten voldoen
* Leveranciers willen weten voor hun applicatie (een standaard/referentiecomponent) welke koppelingen ze moeten implementeren of kunnen gebruiken

## Koppelvlakbeschrijving
* Wordt gepubliceerd op gemmaonline.nl (als webpagina en/of als te downloaden pdf).
* Wordt gemaakt en beheerd door VNG realisatie
* Bevat een algemene functionele beschrijving voor de koppelvlakstandaard
* Beschrijft de context in de architectuur, bijvoorbeeld welke referentiecomponenten betrokken zijn, welk domein, welk proces, welke keten
* Beschrijft welke API's in de koppelvlakstandaard zijn opgenomen.
* Beschrijft per referentiecomponent welke API's verplicht of optioneel kunnen/moeten worden geïmplementeerd, en in welke rol (consumer of provider).
* Bevat een link naar de koppelvlakspecificaties (zie [Standaardisatieproducten voor developers](#standaardisatieproducten-voor-developers))
