import pickle
import pandas as pd
import json
filename = "my_model.pickle"
loaded_model = pickle.load(open(filename, "rb"))
def JSON2PD(json_data):
    df = pd.DataFrame(json_data,index=['0'])
    y_predicted = loaded_model.predict(df)
    myList = y_predicted.tolist()
    encodedNumpyData = json.dumps(myList)
    return encodedNumpyData