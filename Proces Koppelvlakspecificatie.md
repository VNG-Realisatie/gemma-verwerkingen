# Wat heeft een developer nodig om een standaard te kunnen implementeren?
* Architectuur
* Koppelvlak semantisch informatiemodel: betekenis en structuur van gegevens
* Open API Specificatie (voor json) of xsd (voor xml)
* Referentie implementatie
  * Testen van consumerapplicatie en testen van providerapplicatie (referentie implementatie kan scenario's afspelen voor versturen van berichten
* Voorbeeldberichten (cookbook met samenstelling en verwerking van berichten)

# In welke vorm moeten koppelvlakstandaard-deelproducten worden aangeboden
* In GITHUB
* In vorm waarmee bijdrageproces te doen is (code/mark down/tekst; niet MS word, Enterprise Architect, pdf, enz)

# Hoe wil je kunnen bijdragen aan een standaard?
* Via pull requests
* Op welke deelproducten?
  * Architectuur 
    * (bijvoorbeeld processen, use cases)
    * Architectuur wordt nu gemodelleerd in Bizzdesign
  * Informatiemodellen
    * Informatiemodellen worden nu gemodelleerd in UML in tool Enterprise Architect. Deze ondersteunt git niet. Bovendien zijn er complexe afspraken over de manier van modelleren.
  * Koppelvlakdocumentatie
  * Berichtspecificatie 
    * Op dit moment worden berichtspecificaties (OAS of XSD) gegenereerd vanuit UML modellen, waarmee consistentie naar informatiemodel, consistentie naar technische onderlaagafspraken en consistentie tussen specificatie en documentatie wordt gewaarborgd. Tooling voor berichtmodellen ondersteunt git niet.
  * Referentie implementatie
* Welke voorwaarden zijn er aan de tussenproducten?
  * Bewerkbaar zonder dure, voor developers niet gangbare tooling
  * Bij bekijken pull request zijn de verschillen te zien, ondersteund door github: tekstbestanden

# Wat moet koppelvlakbeheerder controleren om bijdrage te beoordelen?
* Consistentie tussen deelproducten, dus verwerking over hele stack (bijv. wijziging in bericht ook verwerkt in referentie implementatie)
* Reden/uitleg over wijziging
* Reacties met overeenstemming uit community: afstemmen pull request met andere leveranciers en gemeenten

# Hoe passen huidige maatregelen voor stimuleren implementatie van standaarden hierin?
* Compliancy
* Convenant
* Softwarecatalogus

* Of alternatief?
