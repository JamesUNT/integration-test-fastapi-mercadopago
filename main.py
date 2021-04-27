from typing import Optional
from fastapi import FastAPI

import requests

import google.cloud.logging
import logging

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()
app = FastAPI()


@app.get("/")
def read_id():
    # order_response = requests.get("https://api.mercadopago.com/merchant_orders/" + id)
    # logging.warning(order_response.text)
    # payment_response = requests.get("https://api.mercadopago.com/v1/payments/" + id)
    # logging.warning(payment_response.text)
    return {"Hello": "World"}


@app.post("/notifications")
def post_payment(topic: str, id: str):
    order_response = requests.get("https://api.mercadopago.com/merchant_orders/" + id)
    logging.warning(order_response.text)
    payment_response = requests.get("https://api.mercadopago.com/v1/payments/" + id)
    logging.warning(payment_response.text)
    return {"topic": topic, "id": id}
