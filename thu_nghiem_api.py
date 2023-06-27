from src.get_result import Get_result
from fastapi import FastAPI
from datetime import datetime
import time

get_result = Get_result()
app = FastAPI()

@app.post("/extract_event")
def extract_event(text : str):
    custom_datetime = datetime(2023, 5, 9, 0, 0, 0)
    start = time.time()
    result = get_result.get_result(custom_datetime,text)
    return {
        "Result :" : result,
        "Time :" : time.time() - start
    }


