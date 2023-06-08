import uvicorn
from fastapi import FastAPI, Request, Response
from application import JSON2PD
app = FastAPI()
response = []
@app.post("/test")
async def receive_json(request: Request):
    json_data = await request.json()
    prediction = JSON2PD(json_data)
    return prediction
if __name__ == "__main__":
    uvicorn.run(app)