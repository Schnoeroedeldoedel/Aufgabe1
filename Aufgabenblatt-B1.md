TH Wildau | INW | Telematik | Internetprogrammierung

---

Client-/Server-Anwendung mit WebSockets und XML
===============================================


Im Rahmen des [Open-Data-Ansatzes](https://de.wikipedia.org/wiki/Open_Data) stellen verschiedene Bundes- und Landesinstitutionen ausgewählte Daten zur öffentlichen Verwendung zur Verfügung, z.B. [Berlin Open Data](https://daten.berlin.de/) oder [DatenAdler Brandenburg](https://datenadler.de/).  

Im Rahmen dieses Aufgabenblattes sollen die Daten der [Kurse der Berliner Volkshochschulen](https://daten.berlin.de/datensaetze/kurse-der-berliner-volkshochschulen) verwendet werden. Diese Daten stehen als [XML-Dokument](https://vhsit.berlin.de/VHSKURSE/OpenData/Kurse.xml) zur Verfügung.[^1] Auf Grundlage dieser Daten ist folgendes Anwendungsszenario zu bearbeiten.  

[^1]: Die Daten stehen auch im JSON-Format zur Verfügung. Im Rahmen dieses Aufgabenblattes sollen die XML-Daten verwendet werden.


Anwendungsszenario
------------------

Ein Server verwaltet die Kurse. Clients können diese Daten abrufen und bearbeiten. Die Kommunikation zwischen Client und Server erfolgt mittels WebSockets.  

Hinweise:  

- In <Klammern> angegebene Informationen beziehen sich auf die entspr. Elemente im XML-Dokument.  
- Die im Folgenden verwendete Bezeichnung "Funktion" beschreibt eine fachliche Funktion und impliziert nicht, dass dies technisch zwingend als Python-Funktion umzusetzen ist. Über die Form der Umsetzung entscheiden Sie.  


Es sind die folgenden Funktionen umzusetzen:

Funktion "Daten abrufen":  

1. Ein Client ruft vom Server eine Liste der verfügbaren Kurse ab. Der Server liefert <name> und <untertitel> und (relevant für den nächsten Schritt) die Beschreibung/Struktur des gesamten Schemas sowie <guid> oder <nummer>.  
2. Ein Client ruft nun anhand der im Schema hinterlegten Elemente bzw. Attribute konkrete (ausgewählte) Daten (Elemente bzw. Attribute) ab (<guid> bzw. <nummer> sind zur eindeutigen Kursreferenz erforderlich).[^2]  
3. Der Server liefert die ausgewählten Daten im gewünschten Format (siehe weitere Anforderungen im Abschnitt Aufgabenstellung) an den Client.  
4. Ein Client gibt die abgerufenen Daten (auf der Konsole oder im Webbrowser in lesbarem (!) Format) aus.  

[^2]: Hinweis: Je nach angegebenen Daten kann dies einen konkreten Kurs oder mehrere Kurse betreffen.


Funktion "Kurs buchen":  

1. Ein Client ruft vom Server den Kurskatalog ab.[^3]  
2. Ein Client erfasst die Daten zur Kursbuchung mittels Nutzereingaben.  
   Als Daten sind Informationen über die Kursinteressenten (Name, Adresse, Telefonnummer oder E-Mail-Adresse) und die zu buchenden Kurse (<guid> bzw. <nummer>) zu erfassen.[^4]  
3. Ein Client sendet die erfassten Daten an den Server.[^5]  
4. Der Server prüft die Daten auf Schema-Konformität und inhaltliche Korrektheit (d.h. ob es die <guid> bzw. <nummer> auch gibt), speichert sie (im Erfolgsfall) und sendet dem Client (je nach Fall) eine Bestätigungsmeldung.[^6]  

[^3]: Hier könnte die Lösung zu obiger Funktion "Daten abrufen" (wieder)verwendet werden. Es sind aber alle Daten zum gesuchten Kurs zu liefern.  
[^4]: Die Angabe von im entspr. XML Schema hinterlegten Pflichtdaten (siehe weitere Anforderungen im Abschnitt Aufgabenstellung) ist auf Client-Seite zu prüfen.  
[^5]: Es steht Ihnen frei, jeweils nur einen Kurs oder mehrere Kurse gleichzeitig buchen zu lassen. Im letzten Fall müssen unter Punkt 1 die Daten mehrerer Kurse geliefert werden.  
[^6]: Optional sind weitere fachliche Prüfungen. So kann es bspw. sinnvoll sein zu prüfen, ob durch eine Buchung die max. Teilnehmerzahl überschritten wird. In dem Fall müsste die Buchung abgelehnt und der Client eine entspr. Meldung erhalten. 
Es wäre ebenfalls denkbar, solche abgelehnten Buchungen auf eine Warteliste zu setzen.  


Funktion "Buchungen anzeigen":  

1. Ein Client ruft vom Server eine Übersicht der von ihm gebuchten Kurse ab.[^7]  
2. Der Server liefert die Daten im gewünschten Format (siehe weitere Anforderungen im Abschnitt Aufgabenstellung) an den Client.[^8]  
3. Ein Client gibt die abgerufenen Daten (auf der Konsole oder im Webbrowser in lesbarem (!) Format) aus.  

[^7]: Eine Authentifizierung ist wünschenswert, aber optional.  
[^8]: Zu jedem Kurs sind mindestens folgende Daten zu liefern: <name>, <untertitel>, <beginn_datum>, Dauer in Tagen sowie die Anzahl der Buchungen.  


Aufgabenstellung
----------------

Erstellen Sie eine Client-/Server-Anwendung mittels Python[^9], mit der das beschriebene Szenario bearbeitet werden kann. Es wird folgendes Vorgehen empfohlen:  

1. Erzeugen Sie ein XML-Schema für das XML-Dokument. Als Hilfestellung bei der Untersuchung der Struktur steht Ihnen das formatierte Dokument `Kurse_snippet.xml` zur Verfügung, das einen Auszug aus der Datei `Kurse.xml` enthält.[^10]  

Für die Erzeugung eines XML Schemas können Sie geeignete externe Dienste verwenden. Ein entspr. generiertes XML-Schema ist allerdings zu prüfen und ggf. zu ergänzen.  
Erweiterte Regeln, z.B. `<minimale_teilnehmerzahl> <= <maximale_teilnehmerzahl>`, sind optional. Die Möglichkeit steht ab [XML Schema 1.1](https://www.w3.org/TR/xmlschema11-1/#cAssertions) zur Verfügung. Im Fall einer Anwendung wäre zu prüfen, ob diese Erweiterung von den verwendeten Modulen zum Validieren der XML-Dokumente gegen ein XML Schema unterstützt wird.  

Auf der o.a. Webseite "Kurse der Berliner Volkshochschulen" ist notiert, dass die Daten regelmäßig aktualisiert werden. Es ist zu prüfen, ob die aktuellen Daten lokal vorliegen (siehe weitere Anforderungen). Sie können davon ausgehen, dass sich das Schema mit neuen Daten nicht ändert.  

2. Erstellen Sie ein XML-Schema für das Speichern von Kundenprofilen im Rahmen der Funktion "Kurs buchen". Mit Hilfe dieses Schemas sind die entspr. XML-Dokumente zu erstellen und zu prüfen.  


Die obigen Punkte können Sie teamübergreifend bearbeiten. Kooperationen sind allerdings von allen beteiligten Teams anzugeben.  

Zum Speichern von gebuchten Kursen ist das Kurs-XML-Dokument zu erweitern. Betroffene Kurse sind an geeigneter Stelle um folgende Elemente zu ergänzen (Beispiel):  

        <buchung>
            <kunde>12345</kunde>
            <kunde>67890</kunde>
        </buchung>

Für jeden buchenden Kunden ist ein Eintrag vorzusehen. Die Werte/IDs zu <kunde> müssen einen Bezug zum unter Punkt 2 erstellten XML-Dokument haben. Die angegebenen Elemente sind ebenfalls im XML-Schema vorzusehen.  


Weitere Anforderungen:  

- Der Server prüft beim Start, ob aktuelle Kursdaten vorliegen. Ist das nicht der Fall, sind die aktuellen Kursdaten zu laden. Da die XML-Datei mehrere MB groß ist, wird empfohlen, dem Anwender dies mittels [Fortschrittsbalken](https://www.geeksforgeeks.org/progress-bars-in-python/) anzuzeigen.  
- Jede verwendete XML-Datei muss valides XML enthalten. Das ist durch Abgleich mit dem jeweiligen XML-Schema sicherzustellen. Das Schema wird vom Server verwaltet.  
- Ein Client sendet Daten immer als XML-Dokument an den Server. Das Dokument soll ebenfalls dem jeweiligen XML-Schema entsprechen. Der Server soll zusätzlich prüfen, ob das vom Client gesendete XML-Dokument dem entspr. XML-Schema entspricht. Im Fehlerfall ist der Client geeignet zu benachrichtigen.  
- Das Format der an den Client zu liefernden Daten legt der Client im Rahmen des Abrufs fest. Das Format der übertragenen Daten kann XML, CSV oder (optional) JSON sein. Das zu verwendende Format ist auf Client-Seite in einer Konfigurationsdatei oder Umgebungsvariablen zu speichern. Änderungen am Abrufformat sollen möglich sein, ohne die Client-Anwendung neu starten zu müssen.  
- Achten Sie auf eine sinnvolle Ausnahme- und Fehlerbehandlung.  
- Client und Server sollen jeweils in einer Endlosschleife laufen. Das Beenden kann entweder über geeignete Nutzereingaben oder allgemeinen Programmabbruch (Ctrl-C) erfolgen.  
- (optional) Die Anwendung soll auch mit mehreren (parallel arbeitenden) Instanzen der Client-Anwendung funktionieren.  

[^9]: Für die Client-Ausgabe im Webbrowser können Sie Flask verwenden.  
[^10]: Dieser Auszug soll beim Verständnis des Schemas helfen. Für die eigtl. Verarbeitung im Rahmen der oben beschriebenen Funktionen ist die vollständige Kursliste der Datei `Kurse.xml` zu verwenden.  


Bearbeitungshinweise
--------------------

Die Aufgabe ist Teil der Leistungsbewertung (siehe Prüfungsschema). Sie können die Aufgabe einzeln oder in 2er-Teams bearbeiten. Kooperationen sind zwingend von allen Beteiligten anzugeben.  
Laden Sie Ihre Lösungen bis zum 26.04.2022 20.00 Uhr als ZIP-Datei im entspr. Abgabebereich im Moodle-Kurs hoch.  

Die ZIP-Datei soll enthalten:  

- Liste der aus der Aufgabenstellung abgeleiteten Anforderungen (verwenden Sie zur Beschreibung die bekannten [Anforderungsschablonen](https://blog.sophist.de/2018/03/28/anforderungsschablonen-der-master-plan-fuer-gute-anforderungen/)) (Dateiendung .pdf)
- erstellte Python-Skripte (Dateiendung .py) bzw. falls mittels Flask umgesetzt weitere Dateien/Verzeichnisse  
- erstellte XML-Dokumente (Dateiendung .xml) und XML Schema-Dokumente (Dateiendung .xsd)  
- Namen der Teammitglieder und Angabe von Kooperationen (Dateiendung .txt oder .md); Geben Sie bitte zusätzlich Ihren Arbeitsaufwand für die o.a. Funktionen bzw. die in der Aufgabenstellung genannten Punkte an.  

Sollten Python-Module zu installieren sein, ist dies als separate Datei `requirements.txt` anzugeben.[^11] Es wird davon ausgegangen, dass die Lösung in einer [virtuellen Python-Umgebung](https://docs.python.org/3/tutorial/venv.html) ausgeführt wird.  

Hinweis: Die von o.a. Quelle geladene Datei `Kurse.xml` ist NICHT abzugeben.  

[^11]: Siehe [The Python Requirements File and How to Create it](https://learnpython.com/blog/python-requirements-file/)


---

Letzte Änderung: 2022-04-13

