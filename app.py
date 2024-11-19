from fastapi import FastAPI
from pydantic import BaseModel
from hash import hash_url

app = FastAPI()

class HashRequest(BaseModel):
    url: str

@app.post("/do_url")
def _(req: HashRequest):
    res = hash_url(req.url)
    return str(res)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)