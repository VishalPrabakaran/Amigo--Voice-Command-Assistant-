from flask import Flask, render_template, request, jsonify
import wikipedia
import datetime
import re

app = Flask(__name__)

# ── Word-boundary helpers ─────────────────────────────────────────────────────
def has_word(word: str, text: str) -> bool:
    """Match `word` as a WHOLE word only using regex word boundaries."""
    return bool(re.search(rf"\b{re.escape(word)}\b", text))

def has_phrase(phrase: str, text: str) -> bool:
    """Match a multi-word phrase with word boundaries on both ends."""
    return bool(re.search(rf"\b{re.escape(phrase)}\b", text))
# ─────────────────────────────────────────────────────────────────────────────

COMMANDS = {
    "open youtube":       {"action": "open_url", "url": "https://youtube.com",        "message": "Opening YouTube for you!"},
    "open google":        {"action": "open_url", "url": "https://google.com",         "message": "Opening Google!"},
    "open github":        {"action": "open_url", "url": "https://github.com",         "message": "Opening GitHub!"},
    "open stackoverflow": {"action": "open_url", "url": "https://stackoverflow.com",  "message": "Opening Stack Overflow!"},
    "open spotify":       {"action": "open_url", "url": "https://spotify.com",        "message": "Opening Spotify, enjoy the music!"},
    "play music":         {"action": "open_url", "url": "https://spotify.com",        "message": "Opening Spotify for music!"},
    "open whatsapp":      {"action": "open_url", "url": "https://web.whatsapp.com",   "message": "Opening WhatsApp Web!"},
    "open twitter":       {"action": "open_url", "url": "https://twitter.com",        "message": "Opening Twitter!"},
    "open reddit":        {"action": "open_url", "url": "https://reddit.com",         "message": "Opening Reddit!"},
    "open gmail":         {"action": "open_url", "url": "https://mail.google.com",    "message": "Opening Gmail!"},
    "open netflix":       {"action": "open_url", "url": "https://netflix.com",        "message": "Opening Netflix!"},
    "open linkedin":      {"action": "open_url", "url": "https://linkedin.com",       "message": "Opening LinkedIn!"},
    "open amazon":        {"action": "open_url", "url": "https://amazon.com",         "message": "Opening Amazon!"},
}

GREETINGS = [
    "Hey there! Amigo is ready to help.",
    "Hello! What can I do for you today?",
    "Hi! Amigo at your service.",
    "Hey! Great to hear from you.",
]

def get_time_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_command():
    data  = request.get_json()
    query = data.get("query", "").lower().strip()

    if not query or query == "none":
        return jsonify({"type": "error", "message": "I didn't catch that. Try again!"})

    # ── Greetings (multi-word first) ──────────────────────────────────────────
    if has_phrase("good morning", query):
        return jsonify({"type": "greeting", "message": "Good morning! I'm Amigo. How can I help you today?"})
    if has_phrase("good afternoon", query):
        return jsonify({"type": "greeting", "message": "Good afternoon! I'm Amigo. How can I help you today?"})
    if has_phrase("good evening", query):
        return jsonify({"type": "greeting", "message": "Good evening! I'm Amigo. How can I help you today?"})

    # ── Identity ──────────────────────────────────────────────────────────────
    # FIX: checked before single-word "hi" so "who are you" isn't mis-greeted
    if any(has_phrase(p, query) for p in ["who are you", "what are you", "are you", "your name"]):
        return jsonify({"type": "info", "message": "I'm Amigo, your intelligent voice assistant. I can open websites, search Wikipedia, tell you the time, and much more!"})

    # ── Wikipedia / Search ────────────────────────────────────────────────────
    # FIX: moved ABOVE the single-word greeting check so "who is chief minister"
    #      never accidentally matches "hi" that speech recognition may prepend.
    if any([
        has_word("wikipedia", query),
        has_word("search", query),
        has_phrase("who is", query),   
        has_phrase("what is", query),  
        has_phrase("tell me about", query),
    ]):
        search_query = query
        for strip_word in ["tell me about", "wikipedia", "search for", "search", "who is", "what is"]:
            search_query = search_query.replace(strip_word, "").strip()
        if search_query:
            try:
                results = wikipedia.summary(search_query, sentences=2)
                return jsonify({"type": "wikipedia", "message": f"According to Wikipedia: {results}", "query": search_query})
            except wikipedia.exceptions.DisambiguationError:
                return jsonify({"type": "wikipedia", "message": f"There are multiple results for '{search_query}'. Could you be more specific?"})
            except Exception:
                return jsonify({"type": "error", "message": f"Couldn't find Wikipedia results for '{search_query}'."})

    # ── Greetings (single words) ──────────────────────────────────────────────
    if any(has_word(w, query) for w in ["hello", "hi", "hey"]):
        greeting = get_time_greeting()
        return jsonify({"type": "greeting", "message": f"{greeting}! I'm Amigo. How can I help you today?"})

    # ── Jokes ─────────────────────────────────────────────────────────────────
    if has_word("joke", query):
        return jsonify({"type": "info", "message": "Ha! I wish I could tell jokes, but I'm better at opening websites and searching Wikipedia. Try asking me something else!"})

    # ── Time ──────────────────────────────────────────────────────────────────
    if has_word("time", query):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({"type": "info", "message": f"The current time is {now}."})

    # ── Date ──────────────────────────────────────────────────────────────────
    if has_word("date", query) or has_word("today", query):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return jsonify({"type": "info", "message": f"Today is {today}."})

    # ── Known URL commands ────────────────────────────────────────────────────
    for command, details in COMMANDS.items():
        if has_phrase(command, query):
            return jsonify({"type": "open_url", "message": details["message"], "url": details["url"], "site": command.replace("open ", "").title()})

    # ── Fallback ──────────────────────────────────────────────────────────────
    return jsonify({"type": "unknown", "message": f"I heard '{query}', but I'm not sure how to help with that. Try asking me to open a website or search Wikipedia!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
