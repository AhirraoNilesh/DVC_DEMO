import os
import argparse
from get_data import read_yaml
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import json
import joblib
from prediction_service import prediction
import mlflow
from urllib.parse import urlparse


def evalute_metric(actual,predict):
    rmse=np.sqrt(mean_squared_error(actual,predict))
    mae=mean_absolute_error(actual,predict)

    r2=r2_score(actual,predict)
    return rmse,mae,r2



def train_and_evaluate(config_path):
    config=read_yaml(config_path)
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    random_states=config["base"]["random_state"]
    model_dir=config["model_dir"]
    alpha=config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio=config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    target=[config["base"]["target_col"]]

    train=pd.read_csv(train_data_path,sep=",")
    test=pd.read_csv(test_data_path,sep=",")

    train_y=train[target]
    test_y=test[target]
    train_x=train.drop(target,axis=1)
    test_x=test.drop(target,axis=1)

   #mlflow config
    mlflow_config=config["mlflow_config"]
    remote_server_uri=mlflow_config["remote_server_url"]
    experiment_name=mlflow_config["experiments_name"]
    registered_model=mlflow_config["registered_model_name"]


    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name=config["run_name"]) as mlops_run:

        lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_states)
        lr.fit(train_x,train_y)
        predic=lr.predict(test_x)
        (rmse,mae,r2)=evalute_metric(test_y,predic)

        #MLFLOW Changes
        mlflow.log_param("alpha",alpha)
        mlflow.log_param("l1_ratio",l1_ratio)
        mlflow.log_metric("rmse",rmse)
        mlflow.log_metric("mae",mae)
        mlflow.log_metric("r2",r2)

        tracking_url_type_store=urlparse(mlflow.get_artifact_uri()).scheme
        
        if tracking_url_type_store !="file":
            mlflow.sklearn.log_model(lr,"model",registered_model_name=registered_model)
        else:
            mlflow.sklearn.load_model(lr,"model")







        #  print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
        #  print("  RMSE: %s" % rmse)
        #  print("  MAE: %s" % mae)
        #  print("  R2: %s" % r2)
        
        #  score_file=config["reports"]["scores"]
        #  param_file=config["reports"]["params"]
        #  with open(score_file,"w") as f:
        #     scores={
        #         "rmse":rmse,
        #         "mae":mae,
        #         "r2":r2
        #     }
        #     json.dump(scores,f,indent=4)

        #  with open(param_file,"w") as f:
        #     params={
        #         "alpha":alpha,
        #         "l1_ratio":l1_ratio
        #     }
        #     json.dump(params,f,indent=4)  

        #  os.makedirs(model_dir,exist_ok=True)
        #  model_path=os.path.join(model_dir,"model.joblib")
        #  joblib.dump(lr,model_path)





    


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parse_arg=args.parse_args()
    train_and_evaluate(config_path=Parse_arg.config)

