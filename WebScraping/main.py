from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_data():
    url = "https://www.opinautos.com/co"
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        info = soup.find_all("div", {
            "class": "HomeInfographic__title"
        })

        content = [item.text.strip() for item in info]

        return jsonify({"data": content}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 
