import os
import yaml
import pandas as pd
import argparse

def read_yaml(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config



def get_data(config_path):
    config=read_yaml(config_path)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path,sep=",",encoding='utf-8')
    #print(df.head())
    return df

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parse_arg=args.parse_args()
    get_data(config_path=parse_arg.config)



