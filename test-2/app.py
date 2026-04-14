from flask import Flask, send_from_directory
import os

app = Flask(__name__)

GAME_FOLDER = os.path.join(os.path.dirname(__file__), "untitledplatformerv1")

@app.after_request
def add_headers(response):
    # Required for Godot 4 if using threads (safe to include even without threads)
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.route("/")
def index():
    return send_from_directory(GAME_FOLDER, "index.html")

@app.route("/<path:filename>")
def game_files(filename):
    return send_from_directory(GAME_FOLDER, filename)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=8600)