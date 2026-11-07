
import requests

BASE_URL = "https://www.freetogame.com/api"


def obtener_juegos():

    try:
        respuesta = requests.get(
            f"{BASE_URL}/games",
            timeout=20
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException as error:
        print("Error al consultar videojuegos:", error)
        return []


def buscar_juego(nombre):

    try:
        respuesta = requests.get(
            f"{BASE_URL}/games",
            params={"category": nombre},
            timeout=20
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException as error:
        print("Error:", error)
        return []


def obtener_detalle(game_id):

    try:
        respuesta = requests.get(
            f"{BASE_URL}/game",
            params={"id": game_id},
            timeout=20
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException as error:
        print("Error:", error)
        return {}
