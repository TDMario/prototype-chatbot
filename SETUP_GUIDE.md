# Projekt Setup Guide

Dieser Guide beschreibt, wie du das Projekt lokal installieren und starten kannst.

---

## ✅ Voraussetzungen

- Python 3.10 oder neuer installiert
- Git installiert

---

## 🧭 Schritte zur lokalen Installation

### 1. 🔽 Repository klonen

```bash
git clone https://github.com/TDMario/prototype-chatbot.git
cd dein-projekt
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

Erstelle eine `.env` im Hauptverzeichnis mit folgendem Inhalt:

```ini
OPENAI_API_KEY=sk-xxxxx
OPENAI_ASSISTANT_ID=asst-xxxxx
```

---

### 5. 🚀 Projekt starten (API + Frontend mit Live Reload)

```bash
python dev.py
```

Damit starten:

- Das **Backend (FastAPI)** unter: [http://localhost:8000](http://localhost:8000)
- Das **Frontend (HTML, CSS, JS)** unter: [http://localhost:5500/index.html](http://localhost:5500/index.html)

---

## 🧹 Optional: Anforderungen aktualisieren

```bash
pip freeze > requirements.txt
```

---