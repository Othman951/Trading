# app.py
from flask import Flask
from routes import main  # Import du blueprint défini dans routes.py

app = Flask(__name__)
app.register_blueprint(main)  # Enregistrement du blueprint

if __name__ == "__main__":
    app.run(debug=True)

