import os
import requests
from flask import Flask, send_from_directory
from main import TOKEN
app = Flask(__name__)

@app.route('/web3_products.json')
def get_products():
    return send_from_directory('.', 'web3_products.json')

@app.route('/images/<file_id>')
def get_image(file_id):
    file_path = f"images/{file_id}.jpg"

    if os.path.exists(file_path):
        return send_from_directory("images", f"{file_id}.jpg")


    file_info = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}").json()
    file_path_tg = file_info["result"]["file_path"]
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path_tg}"

    img_data = requests.get(file_url).content
    os.makedirs("images", exist_ok=True)
    with open(file_path, "wb") as file:
        file.write(img_data)

    return send_from_directory("images", f"{file_id}.jpg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
