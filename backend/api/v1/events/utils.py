import requests
from rest_framework import status
import pyzbar.pyzbar as pyzbar
from PIL import Image
import io

from config.settings import PROVERKA_CHEKA_API_TOKEN


def decode_qr_code_from_image(image):
    try:
        img = Image.open(io.BytesIO(image.read()))
        decoded_objects = pyzbar.decode(img)
        if decoded_objects:
            return decoded_objects[0].data.decode("utf-8")
        return None
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None


def get_receipt_info_by_qr_raw(qr_raw: str) -> dict:
    url = "https://proverkacheka.com/api/v1/check/get"
    token = PROVERKA_CHEKA_API_TOKEN

    try:
        response = requests.get(
            url,
            json={
                "qrraw": qr_raw,
                "token": token,
            },
            timeout=10,
        )
        print(response.json())

        if response.status_code == status.HTTP_200_OK:
            return response.json()
        return {"code": response.status_code, "error": "API request failed"}

    except requests.exceptions.RequestException as e:
        return {"code": 500, "error": str(e)}
