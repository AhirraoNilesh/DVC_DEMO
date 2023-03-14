#Split raw data
#save it in data/processed folder
import os
import argparse
from get_data import read_yaml
import pandas as pd
from sklearn.model_selection import train_test_split


def split_and_saved_data(config_path):
    config=read_yaml(config_path)
    train_data_path=config["split_data"]["train_path"]
    test_data_path=config["split_data"]["test_path"]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    split_ratio=config["split_data"]["test_size"]
    random_states=config["base"]["random_state"]

    df=pd.read_csv(raw_data_path,sep=",")

    train_,test_=train_test_split(df,test_size=split_ratio,random_state=random_states)

    train_.to_csv(train_data_path,sep=",",index=False,encoding='utf-8')
    test_.to_csv(test_data_path,sep=",",index=False,encoding='utf-8')




if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parse_arg=args.parse_args()
    split_and_saved_data(config_path=Parse_arg.config)


