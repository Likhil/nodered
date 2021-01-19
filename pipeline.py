from dxc import ai
import json
import sys
import csv
import pickle
from pymongo import MongoClient

def data_pipeline():


    
    input = json.loads(sys.argv[1])
    db_connect = MongoClient(input["connection_string"])
    database=db_connect[input['database_name']]
    collection=database[input['collection_name']]

    pipe = input["pipeline"]
    df = ai.access_data_from_pipeline(collection, pipe)
    df.columns = df.columns.str.replace('_id.','')
    df.to_csv("dfp_tmp.csv",index=False)
    
    print("all steps executed")

if __name__ == "__main__":
    data_pipeline()
