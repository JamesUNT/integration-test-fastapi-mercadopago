from typing import Optional
import google.cloud.logging
from fastapi import FastAPI


client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/notifications")
def post_payment(topic: str, id: int):
    logging.warning(f"topic: {topic}\nid: {id}")
    return {"topic": topic, "id": id}
