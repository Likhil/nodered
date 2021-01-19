import pandas as pd
import pickle
import sys
import json
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

def encode(data):

    '''function to encode non-null data and replace it in the original data'''
    encoder = OrdinalEncoder()
    #retains only non-null values
    nonulls = np.array(data.dropna())
    #reshapes the data for encoding
    impute_reshape = nonulls.reshape(-1,1)
    #encode date
    impute_ordinal = encoder.fit_transform(impute_reshape)
    #encoders_store[column_name]=encoder
    #Assign back encoded values to non-null values
    data.loc[data.notnull()] = np.squeeze(impute_ordinal)
    return (data)
    
    
def custom_api():
    
    #input = json.dumps(sys.argv[1])
    input = json.loads(sys.argv[1])
    new_input={}
    for i in (input):
        new_input[i]=[input[i]]
    df=pd.DataFrame.from_dict(new_input)

    filename = "abc.pkl"
    infile = open(filename,'rb')
    trained_model = pickle.load(infile)
    #input_df=encode(df)
    
    prediction = trained_model.predict(df)
    print(prediction)
    return prediction
if __name__ == "__main__":
    custom_api()