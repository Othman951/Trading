from flask import Flask, render_template
from dexscreener import get_top_pairs
from gpt_analysis import analyze_market

app = Flask(__name__)

@app.route('/')
def dashboard():
    pairs = get_top_pairs()
    analysis = analyze_market(pairs)
    return render_template('dashboard.html', pairs=pairs, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
