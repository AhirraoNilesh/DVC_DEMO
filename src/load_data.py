import os
from get_data import read_yaml,get_data
import argparse

def load_and_save(config_path):
    config=read_yaml(config_path)   
    df=get_data(config_path)   
    New_cols=[col.replace(" ","_") for col in df.columns]
    row_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(row_data_path,sep=",",index=False,header=New_cols)
    



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    Parse_arg=args.parse_args()
    load_and_save(config_path=Parse_arg.config)

