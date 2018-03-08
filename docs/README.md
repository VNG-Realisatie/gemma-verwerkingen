# gemma-verwerkingen
De standaard 'gemma-verwerkingen' wordt toegepast binnen NLX om te zorgen dat berichtuitwisseling veilig en verantwoord plaatsvindt. Je vind hier een aanzet tot beschrijving van de standaard. De standaard is nog in opbouw dus zullen er de komende maanden regelmatig aanpassingen plaats vinden. De informatie die er nu staat is onder voorbehoud.

## Inleiding tot NLX
NLX is een open-source interorganisatorisch systeem dat gefedereerde authenticatie, veilige verbinding en protocolling mogelijk maakt in een grootschalig, dynamisch API-landschap. De noodzaak voor het creëren van NLX komt voort uit de Common Ground visie van de Nederlandse gemeenten, die tot doel heeft de huidige monolithische informatiesystemen van Nederlandse gemeenten (en een bredere overheid) te veranderen of vervangen door een geavanceerde ‘API-eerst strategie’ software-landschap, waarmee wordt voldaan aan de maatschappelijke vraag naar automatisering, transparantie en privacy.

In deze visie kunnen organisaties API's die door andere organisaties worden aangeboden, net zo gemakkelijk gebruiken als hun eigen API's, terwijl kerngegevensobjecten alleen worden gemanipuleerd door degene die administratief verantwoordelijk is. NLX zal functioneren als een peer-to-peer-architectuur en functioneert aan de rand van het netwerk van elke organisatie. Verzoeken van de ene organisatie naar de andere worden gerouteerd via NLX-knooppunten die in beide organisaties zijn geplaatst, via een beveiligde peer-to-peer-verbinding. Gedistribueerd ontwerp, waar mogelijk volgens federatieconcepten, wordt gebruikt omdat het essentieel is voor schaalbaarheid en prestaties.

## Gegevensbescherming
Bij het ontwerpen van NLX moeten verschillende Europese kaders en voorschriften worden overwogen. Een van deze voorschriften is de Algemene Verordening Gegevensbescherming (GDPR). De AVG stelt richtlijnen vast voor de verwerking van persoonsgegevens van personen binnen de Europese Economische Ruimte (EER) en is gebaseerd op het fundamentele recht op eerbiediging van het privé- en gezinsleven - vaak aangeduid als het recht op privacy - van de Europese Verdrag inzake mensenrechten.

De AVG zet de beginselen uiteen voor gegevensbescherming, aansprakelijkheid en de rechten van de betrokkene. Deze principes zijn van invloed op NLX, omdat API's die persoonsgegevens verwerken, worden geleverd door de NLX-infrastructuur.

De GDPR definieert de principes van de verwerking van persoonsgegevens en de rechtmatigheid van dergelijke verwerking en is gebaseerd op richtlijnen die sinds de jaren tachtig bestaan, de OESO-richtlijnen. Deze beginselen omvatten eerlijke en rechtmatige verwerking, rechten van betrokkenen, transparantie en informatiebeveiliging

NLX werkt conform de GDPR-principes voor gegevensbescherming. NLX logt de nodige informatie om naleving te kunnen bewijzen, en daarmee de toegangsrechten van de betrokkene te verbeteren.

## NLX API's en de GDPR
De GDPR bevat de volgende principes:
1. Doelspecificatie (waarom doe je dit?)
2. Juridische redenen (met name relevant zijn instemming, wetgeving, algemeen belang, contract en legitiem belang)
3. Transparantie
4. Informatiebeveiliging
5. Rechten van betrokkenen
6. Retentie

Tussen A en B moet een contract worden gesloten om de redenen en gronden voor gegevensoverdracht vast te stellen. Dit kan een geautomatiseerd en gestandaardiseerd proces zijn om de verwerking van de contracten te vergemakkelijken, vergelijkbaar met overeenkomsten voor gegevensverwerking.
Via de API-transactielogboeken is het mogelijk om
- een API-aanroep te traceren naar de organisatie die het proces heeft gestart
- de transactie te identificeren
- vast te stellen of de transactie succesvol was.

Verplicht:
- Authenticatie (is A wie hij zegt dat hij is?)
- Overdrachtsregels (wat is A toegestaan om te ontvangen?)
  - Is toegestaan om de service aan te vragen (gecontroleerd door NLX-knooppunt)
  - Is toegestaan om bepaalde gegevens binnen de service aan te vragen (geautoriseerd door resource).
- Is de overdracht succesvol verlopen?
- Als een oproep niet eerder is geautoriseerd, moet NLX de serviceaanvraag retourneren. De bron kan overdracht van gegevens op ad-hocbasis autoriseren.

Om dit te bereiken is er een autorisatiematrix die in aanbestedingsprocedures kan worden opgenomen.
1. Autorisatie van diensten
2. Goedkeuren van legitieme gegevensoverdrachten

De inhoud van de matrix is vergelijkbaar met de records van verwerkingsactiviteiten die zijn opgelegd in het kader van de AVG.
Zowel NLX-outway als NLX-inway loggen alle overdrachtsgegevens in API-transactielogboeken. Deze logboeken kunnen worden gebruikt voor controledoeleinden en om naleving aan te tonen.

