from dxc import ai
import json
import sys
import pandas as pd
import pickle


def write_mongoDB():
    string = json.loads(sys.argv[1])
    connection_string = string["connection_string"]
    collection_name = string["collection_name"]
    database_name = string["database_name"]
    data_source = string["data_source"]
    cleaner = string["cleaner"]
    
    data_layer = {
        "connection_string": connection_string,
        "collection_name": collection_name,
        "database_name": database_name,
        "data_source":data_source,
        "cleaner":cleaner
    }


    df=pd.read_csv('clean_df_tmp.csv')

    data2 = ai.write_raw_data(data_layer, df)
    print("<br> Please find the above current status of your collections: <br>")
    print("<br> Below is the response from Mongo DB:<br> ")
    print(data2)
    
    return data2

if __name__ == "__main__":
    write_mongoDB()
