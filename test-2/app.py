from flask import Flask, send_from_directory, request, jsonify, render_template_string
import os
import sqlite3

app = Flask(__name__)
GAME_FOLDER = os.path.join(os.path.dirname(__file__), "untitledplatformerv1")
DB_PATH = os.path.join(os.path.dirname(__file__), "leaderboard.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  time REAL NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.after_request
def add_headers(response):
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.route("/")
def index():
    return send_from_directory(GAME_FOLDER, "index.html")

@app.route("/<path:filename>")
def game_files(filename):
    return send_from_directory(GAME_FOLDER, filename)

@app.route("/leaderboard")
def leaderboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, time FROM leaderboard ORDER BY time ASC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    entries = [{"rank": i+1, "name": r[0], "time": round(r[1], 2)} for i, r in enumerate(rows)]
    return render_template_string(LEADERBOARD_HTML, entries=entries)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    time = data.get("time")
    if time is None:
        return jsonify({"error": "missing time"}), 400
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

from flask import Flask, send_from_directory, request, jsonify, render_template_string
import os
import sqlite3

app = Flask(__name__)
GAME_FOLDER = os.path.join(os.path.dirname(__file__), "untitledplatformerv1")
DB_PATH = os.path.join(os.path.dirname(__file__), "leaderboard.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  time REAL NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.after_request
def add_headers(response):
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.route("/")
def index():
    return send_from_directory(GAME_FOLDER, "index.html")

@app.route("/<path:filename>")
def game_files(filename):
    return send_from_directory(GAME_FOLDER, filename)

@app.route("/leaderboard")
def leaderboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, time FROM leaderboard ORDER BY time ASC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    entries = [{"rank": i+1, "name": r[0], "time": round(r[1], 2)} for i, r in enumerate(rows)]
    return render_template_string(LEADERBOARD_HTML, entries=entries)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name", "Anonymous")
    time = data.get("time")
    if time is None:
        return jsonify({"error": "missing time"}), 400
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

LEADERBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Leaderboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a1a1a; color: white; padding: 40px; }
        h1 { color: #f0c040; }
        table { border-collapse: collapse; width: 400px; margin-bottom: 40px; }
        th, td { padding: 10px 20px; text-align: left; border-bottom: 1px solid #444; }
        th { color: #f0c040; }
        input { padding: 8px; margin: 5px 0; width: 200px; }
        button { padding: 8px 20px; background: #f0c040; border: none; cursor: pointer; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Speedrun Leaderboard</h1>
    <table>
        <tr><th>Rank</th><th>Name</th><th>Time (s)</th></tr>
        {% for e in entries %}
        <tr><td>{{ e.rank }}</td><td>{{ e.name }}</td><td>{{ e.time }}</td></tr>
        {% endfor %}
    </table>

    <h2>Submit your time</h2>
    <input type="text" id="name" placeholder="Your name"><br>
    <input type="number" id="time" placeholder="Your time in seconds" step="0.01"><br>
    <button onclick="submitScore()">Submit</button>
    <p id="result"></p>

    <script>
        async function submitScore() {
            const name = document.getElementById("name").value;
            const time = parseFloat(document.getElementById("time").value);
            if (!name || isNaN(time)) {
                document.getElementById("result").innerText = "Please fill in both fields.";
                return;
            }
            const response = await fetch("/submit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, time })
            });
            const data = await response.json();
            if (data.status === "ok") {
                document.getElementById("result").innerText = "Submitted! Refresh to see the leaderboard.";
            }
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8600, ssl_context=("cert.pem", "key.pem"))