# 📚 Liane Library

## Projektübersicht

Liane Library ist eine datenbankgestützte Bibliotheksverwaltung, die im Rahmen meiner Weiterbildung im Bereich **Data Analytics und Softwareentwicklung** entstanden ist.

Das Ziel dieses Projekts war es, theoretische Kenntnisse aus **Python, SQL und Datenbanken** in einer praktischen Anwendung umzusetzen.

Die Anwendung ermöglicht die Verwaltung von Büchern, Freunden und Ausleihen. Dabei werden Datenbankmodellierung, Backend-Logik und eine interaktive Benutzeroberfläche mit **Streamlit** miteinander verbunden.

Während der Entwicklung konnte ich den vollständigen Ablauf einer datenbankgestützten Anwendung kennenlernen – von der Planung der Datenbankstruktur über die Verbindung zwischen Python und MySQL bis hin zur Umsetzung von CRUD-Funktionen und Datenvalidierungen.

---

# 🚀 Funktionen

## 📊 Dashboard

- Anzeige der Gesamtanzahl der Bücher
- Anzeige der registrierten Freunde
- Anzeige der verspäteten Ausleihen

## 📚 Bücherverwaltung

- Bücher suchen
- Neue Bücher hinzufügen
- Bücher löschen

## 👥 Freundeverwaltung

- Neue Freunde hinzufügen
- Freunde löschen
- Notizen zu Freunden speichern

## 🔄 Ausleihverwaltung

- Neue Ausleihen erstellen
- Ausleihen löschen
- Ausleihstatus aktualisieren
- Rückgabedatum ändern
- Notizen zu Ausleihen bearbeiten

---

# 🛠️ Verwendete Technologien

| Technologie | Verwendung |
|---|---|
| Python | Entwicklung der Anwendungslogik |
| Streamlit | Erstellung der interaktiven Benutzeroberfläche |
| MySQL | Speicherung und Verwaltung relationaler Daten |
| SQLAlchemy | Verbindung zwischen Python und MySQL |
| Pandas | Lesen, Verarbeiten und Analysieren von Daten |
| SQL | Erstellung und Optimierung von Datenbankabfragen |

---

# 🗄️ Datenbankstruktur

Die Anwendung basiert auf drei miteinander verbundenen Tabellen:

- **Books**
- **Friends**
- **Loans**

Die Tabelle **Loans** stellt die Beziehung zwischen Büchern und Freunden dar.

Zusätzlich werden dort wichtige Informationen gespeichert:

- Ausleihdatum
- Rückgabedatum
- Ausleihstatus
- Notizen

Durch die Verwendung von Primär- und Fremdschlüsseln werden die Beziehungen zwischen den Tabellen korrekt verwaltet und die Datenintegrität sichergestellt.

---

# 📚 Was ich gelernt habe

Durch dieses Projekt konnte ich meine Kenntnisse in folgenden Bereichen vertiefen:

- Entwicklung einer interaktiven Webanwendung mit Python und Streamlit
- Entwurf und Verwaltung einer relationalen MySQL-Datenbank
- Verbindung zwischen Python und Datenbanken mit SQLAlchemy
- Arbeiten mit Pandas zur Datenverarbeitung
- Schreiben und Optimieren von SQL-Abfragen
- Umsetzung vollständiger CRUD-Funktionen:
  - Create
  - Read
  - Update
  - Delete
- Arbeiten mit Primär- und Fremdschlüsseln
- Verwaltung von Beziehungen zwischen mehreren Datenbanktabellen
- Validierung von Benutzereingaben vor Datenbankänderungen
- Strukturierung von Code in wiederverwendbare Funktionen
- Erstellung eines Dashboards mit wichtigen Kennzahlen

---

# 💡 Herausforderungen

Eine der größten Herausforderungen bestand darin, sicherzustellen, dass Änderungen immer für den richtigen Datensatz durchgeführt werden.

Beispielsweise dürfen Ausleihstatus, Rückgabedatum oder Notizen nur aktualisiert werden, wenn das ausgewählte Buch tatsächlich von der ausgewählten Person ausgeliehen wurde.

Um dies sicherzustellen, wurden vor jeder Änderung entsprechende Validierungen eingebaut. Dadurch werden fehlerhafte Aktualisierungen verhindert und die Konsistenz der Datenbank bleibt erhalten.

Darüber hinaus konnte ich lernen, wie wichtig eine saubere Datenbankstruktur und eine klare Organisation des Codes für die Wartbarkeit einer Anwendung sind.

---

# 🔮 Zukünftige Erweiterungen

Mögliche Erweiterungen der Anwendung:

- Benutzeranmeldung und Rechteverwaltung
- Automatische Erinnerungen für überfällige Ausleihen
- Erweiterte Such- und Filterfunktionen
- Anzeige der aktuellen Verfügbarkeit von Büchern
- Verbesserte Fehlerbehandlung und Eingabevalidierung
- Erweiterung des Dashboards mit zusätzlichen Statistiken

---

# 📸 Application Screenshots

## Books Page

![Books Page](screenshots/books_page.png)

## Friends Page

![Friends Page](screenshots/friends_page.png)

## Loans Page

![Loans Page](screenshots/loans_page.png)

---

# ✅ Fazit

Dieses Projekt war ein wichtiger Schritt in meiner Entwicklung als angehende **Data Analystin und Python-Entwicklerin**.

Es hat mir ermöglicht, theoretisches Wissen praktisch anzuwenden und wertvolle Erfahrungen im Umgang mit **Python, SQL, MySQL und relationalen Datenbanken** zu sammeln.

Gleichzeitig habe ich gelernt, wie verschiedene Technologien zusammenarbeiten, um eine vollständige datenbankgestützte Anwendung zu entwickeln.

Liane Library bildet eine solide Grundlage, auf der ich zukünftig weitere Funktionen und komplexere Datenanwendungen aufbauen möchte.
