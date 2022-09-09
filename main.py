from fastapi import FastAPI
from pydantic import BaseModel
import textblob

class Item(BaseModel):
    data: str

app = FastAPI()

@app.get("/sentimentAnalysis/")
async def root(data: str):
    ans= None
    analysis = textblob.TextBlob(data).sentiment
    res = analysis.polarity
    if res < 0:
        ans = "Negative"
    elif res == 0:
        ans = "Nuetral"
    elif res > 0:
        ans = "Positive"
    return {"result": ans}