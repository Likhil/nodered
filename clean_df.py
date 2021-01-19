from dxc import ai
import json
import sys
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

def clean_data():
    #print(sys.argv[1])
    
    #inp1='""'+sys.argv[1]+'""'
    #print(inp1)
    print(sys.argv[1])
    inp = json.loads(sys.argv[1])
    
    print(type(inp))
    text_fields = inp['txt_attrs']
    date_fields = inp['dat_attrs']
    numeric_fields = inp['num_attrs']
    categorical_fields = inp['cat_attrs']
    impute = inp['impute']
    df=pd.read_csv('df_tmp.csv')
    clean_df = ai.clean_dataframe(df, impute, text_fields, date_fields, numeric_fields, categorical_fields)

    clean_df.to_csv("clean_df_tmp.csv",index=False)

if __name__ == "__main__":
    clean_data()