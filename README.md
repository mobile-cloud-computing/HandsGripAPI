# HandsGripAPI
Run the main.py file from Server. You need uvicorn webserver installed.
The server has access to the AI model for predicting strength.
It receives POST request and accepts data in JSON format.

After running the server, run the Client.py from root directory.
Client send POST request in the defined JSON format (see code for example data) and receive the prediction response back from the server in JSON.

Please don't forget to install dependencies / libraries in your virtualenv.


INPUT FORMAT of API:  

json_payload = {
    "light": 155.8271,
    "gender": 1,
    "size": 152.88,
    "age": 24
}

Light Value
Gender  0 Female / 1 Male
Size  handsize = length (cm) * breadth (cm), you can use a ruler to measure your handsize. length and breadth measures can be learned from online
age
