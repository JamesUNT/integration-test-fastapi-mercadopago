import logging
from typing import Optional

import requests

from fastapi import FastAPI
import google.cloud.logging

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()
app = FastAPI()


@app.get("/debug")
def debug(id: str):
    headers = {
        "Authorization": "Bearer TEST-8777561415085289-040116-7f497da405df9c5128157c84f8437639-737246994"
    }
    order_response = requests.get(
        "https://api.mercadopago.com/merchant_orders/" + id, headers=headers
    )
    logging.warning(order_response.text)
    return order_response.text


@app.post("/notifications")
def post_payment(topic: str, id: str):
    order_response = requests.get("https://api.mercadopago.com/merchant_orders/" + id)
    logging.warning(order_response.text)
    return {"topic": topic, "id": id}
