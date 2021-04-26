from typing import Optional

import requests

from fastapi import FastAPI
import google.cloud.logging

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()
app = FastAPI()


@app.get("/{id}")
def read_id(id: str):
    order_response = requests.get("https://api.mercadopago.com/merchant_orders/" + id)
    logging.warning(order_response.text)
    payment_response = requests.get("https://api.mercadopago.com/v1/payments/" + id)
    logging.warning(payment_response.text)


@app.post("/notifications")
def post_payment(topic: str, id: int):
    logging.warning(f"topic: {topic}\nid: {id}")
    return {"topic": topic, "id": id}
