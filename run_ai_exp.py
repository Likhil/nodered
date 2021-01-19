from dxc import ai
import json
import sys
import pickle
import pandas as pd


def run_ai_experiment(df):
    input_data = json.loads(sys.argv[1])
    target = input_data["target"]
    if input_data["model"] == 'classification':
        
        model = ai.tpot_classification()
    if input_data["model"] == 'regression':
        model = ai.tpot_regression()
    verbose = input_data["verbose"]
    maxtimemin = input_data["maxtimemin"]
    if isinstance(maxtimemin, str):
        maxtimemin = eval(maxtimemin)
    maxevaltime = input_data["maxevaltime"]
    if isinstance(maxevaltime, str):
        maxevaltime = eval(maxevaltime)    
    warmstart = input_data["warmstart"]
    exportpipe = input_data["exportpipe"]
    configdict = input_data["configdict"]
    scoring = input_data["scoring"]
    if scoring == 'None':
        scoring = None
    if configdict == 'None':
        configdict = None
    else:
        configdict = eval(configdict)
    if exportpipe == 'False':
        exportpipe = False
    else:
        exportpipe = True
    if warmstart == 'False':
        warmstart = False
    else:
        warmstart = True
        
    experiment_design = {
    "model": model,
    "labels": df[target],
    "data": df,
     "meta_data": {
       target: "output"
      }
    }
    
    trained_model = ai.run_experiment(experiment_design, verbose = verbose, max_time_mins = maxtimemin, max_eval_time_mins = maxevaltime, config_dict = configdict, warm_start = warmstart, export_pipeline = exportpipe, scoring = scoring)
    
    filename = 'finalized_model.pkl'
    pickle.dump(model, open(filename, 'wb'))
    try:
        print("<br> <br>Please find the Trained Model as below:<br> <br> %s" %(trained_model[1:2]))
    except:
        print("<br> <br>Please find the Trained Model as below:<br> <br> %s" %(trained_model))
    return trained_model

if __name__ == "__main__":
    df = pd.read_csv("dfp_tmp.csv")
    run_ai_experiment(df)
    