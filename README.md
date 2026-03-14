# 🎙️ Amigo — Voice Command Assistant

> **Speak. Command. Done.**

Amigo is a lightweight, browser-based **Voice Command Assistant** that listens to your voice, executes commands, and talks back to you — no typing needed. Open websites, search Wikipedia, check the time, and more — all hands-free on any device.
---
## Features

-  **Voice Recognition** — Speak naturally, Amigo understands your command
-  **Voice Reply** — Amigo speaks the response back to you in a clear male voice
-  **Open Websites** — Launch YouTube, Gmail, GitHub, Spotify and more instantly
-  **Wikipedia Search** — Get quick 2-sentence summaries on any topic
-  **Time & Date** — Ask the current time or today's date
-  **Greetings** — Responds to good morning, good evening, and more
-  **Works on All Devices** — Android, iOS, Windows, Mac — any Chrome browser
-  **Sleek Dark UI** — Animated mic orb, pulse rings, and smooth transitions
-  **Voice Selector** — Pick your preferred voice from all available system voices
---
## 🚀 Getting Started

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/amigo-voice-assistant.git
cd amigo-voice-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python app.py
```

### 4. Open in Browser

On the **same PC:**
```
http://localhost:5000
```

On **Android / iPhone (same WiFi):**
1. Find your PC's local IP — run `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Open Chrome on your phone and go to:
```
http://YOUR_PC_IP:5000
```
Example: `http://192.168.1.5:5000`

> ⚠️ Voice recognition requires **Google Chrome**. Does not work in Firefox or Safari.

---

## 🎙️ Voice Commands

### 🌐 Open Websites
| Say | Action |
|---|---|
| "Open YouTube" | Opens youtube.com |
| "Open GitHub" | Opens github.com |
| "Open Gmail" | Opens mail.google.com |
| "Open Spotify" | Opens spotify.com |
| "Open WhatsApp" | Opens web.whatsapp.com |
| "Open Netflix" | Opens netflix.com |
| "Open Reddit" | Opens reddit.com |
| "Open Twitter" | Opens twitter.com |
| "Open LinkedIn" | Opens linkedin.com |
| "Open Amazon" | Opens amazon.com |
| "Open Stack Overflow" | Opens stackoverflow.com |
| "Play music" | Opens Spotify |

### 🔍 Search & Info
| Say | Action |
|---|---|
| "Search Wikipedia for Python" | Wikipedia summary |
| "Who is Elon Musk?" | Wikipedia lookup |
| "What is machine learning?" | Wikipedia summary |
| "Tell me about India" | Wikipedia summary |

### 🕐 Time & Date
| Say | Action |
|---|---|
| "What is the time?" | Tells current time |
| "What is today's date?" | Tells today's date |
| "What day is today?" | Tells the day |

### 💬 General
| Say | Action |
|---|---|
| "Hello / Hi / Hey" | Friendly greeting |
| "Good morning / evening" | Time-matched greeting |
| "Who are you?" | Amigo introduces itself |

---

## ➕ Adding Custom Commands

Open `app.py` and add to the `COMMANDS` dictionary:

```python
"open my site": {
    "action": "open_url",
    "url": "https://mysite.com",
    "message": "Opening your site!"
},
```

For custom logic (not just URLs), add an `if` block inside `process_command()`:

```python
if "flip a coin" in query:
    import random
    result = random.choice(["Heads", "Tails"])
    return jsonify({"type": "info", "message": f"It's {result}!"})
```
---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Voice Input** | Web Speech API (browser-native) |
| **Voice Output** | Web Speech Synthesis API |
| **Data / Search** | Wikipedia Python Library |

---

## 📁 Project Structure

```
amigo/
├── app.py               # Flask backend — handles all commands
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── templates/
    └── index.html       # Frontend UI — mic, voice, commands
```

---

## 📋 Requirements

```
flask==3.0.0
wikipedia==1.4.0
requests==2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🌐 Browser Compatibility

| Browser | Voice Input | Voice Output |
|---|---|---|
| ✅ Chrome (Desktop) | Works | Works |
| ✅ Chrome (Android) | Works | Works |
| ⚠️ Safari (iOS) | Limited | Works |
| ❌ Firefox | Not supported | Works |

## 👨‍💻 Author

Built with ❤️ using Flask and the Web Speech API.

---

## 📄 License

This project is open source and free to use for personal and educational purposes.
