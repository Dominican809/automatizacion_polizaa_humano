"""from emisor_goval.api.auth import TokenManager
from loguru import logger
import sys

if __name__ == "__main__":
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    try:
        token = TokenManager.get_token(force_refresh=True)
        print("Token obtenido:", token)
    except Exception as e:
        print("Error al obtener token:", e) """


import requests

url = "https://humano.goval-tpa.com/api/auth/token/jwt"
params = {
    "acl": 1
}

# Use multipart/form-data
form_data = {
    "login": (None, "gapi-user_es"),
    "password": (None, "KhQH^M*wQw07Ybsg")
}

response = requests.post(url, params=params, files=form_data)

if response.status_code == 200:
    print("Token:", response.text)
else:
    print("Error:", response.status_code, response.text)
