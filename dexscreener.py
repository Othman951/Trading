import requests

def get_top_pairs(limit=5):
    url = "https://api.dexscreener.com/latest/dex/pairs"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("pairs", [])[:limit]
    return []
