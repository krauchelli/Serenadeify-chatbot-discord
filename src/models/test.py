import sys
import pandas as pd

jsonSample = {
    "name": "John",
    "age": 30,
}
jsonSample = pd.DataFrame([jsonSample])  # Convert the data to a DataFrame

data_received = sys.argv[1]  # Access the data
data_received = pd.read_json(data_received)  # Convert the data to a DataFrame
print(data_received)  # Do something with the data