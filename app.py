@app.route("/")
def dashboard():
    pairs = get_top_pairs()
    print(pairs)  # pour les logs
    analysis = analyze_market(pairs)
    return render_template("index.html", pairs=pairs, analysis=analysis)
