# importing required packages
from dxc import ai
import pandas as pd
import json
import sys
import pickle

#micro-service function
def microservice(trained_model, microservice_design):
    api_url = ai.publish_microservice(microservice_design, trained_model, verbose = False)
    return api_url
    

if __name__ == "__main__":
    #df = pd.read_csv('AB_NYC_2019.csv')
    #model = modeling(df)
    with open('finalized_model.pkl', 'rb') as f:
        model = pickle.load(f)
        
    string = json.loads(sys.argv[1])
    microservice_name = string["microservice_name"]
    microservice_description = string["microservice_description"]
    execution_environment_username = string["execution_environment_username"]
    api_key = string["api_key"]
    api_namespace = string["api_namespace"]
    #model_path = string["model_path"]
    
    microservice_design = {
        "microservice_name": microservice_name,
        "microservice_description": microservice_description,
        "execution_environment_username": execution_environment_username,
        "api_key": api_key,
        "api_namespace": api_namespace,
        "model_path": 'data://.my/mycollection'
    }
    
    print("api url: " + microservice(model, microservice_design))
    