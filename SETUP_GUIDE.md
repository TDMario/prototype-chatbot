# Projekt Setup Guide

Dieser Guide beschreibt die Schritte zur lokalen Installation und Ausführung des Projekts.

---

## ✅ Voraussetzungen

- Python 3.10 oder neuer installiert
- Git installiert

---

## 🧭 Schritte zur lokalen Installation

### 1. 🔽 Repository klonen

```bash
git clone https://github.com/TDMario/prototype-chatbot.git
cd projekt
```

---

### 2. 🧪 Virtuelle Umgebung erstellen und aktivieren

```bash
# Erstellen (nur beim ersten Mal)
python -m venv venv

# Aktivieren:

# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat

# Linux/macOS
source venv/bin/activate
```

---

### 3. 📦 Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

### 4. 📁 .env Datei erstellen

Im Hauptverzeichnis eine Datei `.env` mit folgendem Inhalt anlegen:

```ini
OPENAI_API_KEY=sk-xxxxx
OPENAI_ASSISTANT_ID=asst-xxxxx
```

#### 🔑 API Key & Assistant ID erhalten

Für die Verwendung von OpenAI sind zwei Werte erforderlich:

1. Ein **OpenAI API Key**, der nach der Registrierung unter [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) generiert werden kann. Eine offizielle Anleitung ist hier verfügbar: [https://platform.openai.com/docs/quickstart](https://platform.openai.com/docs/quickstart)

2. Eine **Assistant ID**, die mit folgendem Befehl generiert wird, sobald die virtuelle Umgebung aktiv ist und der API Key gesetzt wurde:

```bash
python create_assistant.py
```

Die dabei ausgegebene ID anschließend ebenfalls in der `.env` eintragen.

> ⚠️ Hinweis: Die Nutzung der OpenAI API ist kostenpflichtig. Preisdetails sind unter [https://platform.openai.com/pricing](https://platform.openai.com/pricing) einsehbar.

---

### 5. 🚀 Projekt starten (API + Frontend mit Live Reload)

```bash
python dev.py
```

Dabei werden gestartet:

- Das **Backend (FastAPI)** unter: [http://localhost:8000](http://localhost:8000)
- Das **Frontend (HTML, CSS, JS)** unter: [http://localhost:5500/index.html](http://localhost:5500/index.html)

---

## 🧹 Optional: Anforderungen aktualisieren

```bash
pip freeze > requirements.txt
```

---
