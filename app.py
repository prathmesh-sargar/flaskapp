from flask import Flask, render_template,jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "environment": os.environ.get("APP_ENV", "unknown")
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))



    # local running command : 
    #  docker run --env-file .env -p 5000:5000 flaskapp