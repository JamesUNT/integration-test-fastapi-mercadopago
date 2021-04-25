from typing import Optional
import google.cloud.logging
from fastapi import FastAPI


cliente = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/notifications")
def post_payment(topic: str, id: int):
    logging.warning()
    return {"topic": topic, "id": id}