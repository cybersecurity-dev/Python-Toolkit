import json
import pandas as pd
import torch
import shutil
import os
import joblib
import datetime
import time

def save_datasets(X_train, y_train, X_val, y_val, X_test, y_test, prefix : str = "", output_dir : Path = './output') -> bool:
    exact_dir = ""
    if not prefix:
        exact_dir = f"unknow_feature_set_{datetime.date.today().strftime("%d_%m_%y")}"
    else:
        exact_dir = f"{prefix}_{datetime.date.today().strftime("%d_%m_%y")}"
    try:    
        X_train.to_parquet(f"{output_dir}/datasets/{exact_dir}/X_train.parquet")
        joblib.dump(y_train, f"{output_dir}/datasets/{exact_dir}/y_train.pkl")
        X_val.to_parquet(f"{output_dir}/datasets/{exact_dir}/X_val.parquet")
        joblib.dump(y_val, f"{output_dir}/datasets/{exact_dir}/y_val.pkl")
        X_test.to_parquet(f"{output_dir}/datasets/{exact_dir}/X_test.parquet")
        joblib.dump(y_test, f"{output_dir}/datasets/{exact_dir}/y_test.pkl")
        return True
    except Exception as e:
        print(f"Error saving datasets: {e}")
        return False

def load_datasets(prefix : str = "", date_str: str = "", load_dir : Path = './output'):
    exact_dir = ""
    if not prefix:
        if not date_str:
            exact_dir = f"unknow_feature_set_{date_str}" 
        else:
            exact_dir = f"unknow_feature_set_{datetime.date.today().strftime("%d_%m_%y")}"      
    else:
        if not date_str:
            exact_dir = f"{prefix}_{datetime.date.today().strftime("%d_%m_%y")}"
        else:
            exact_dir = f"{prefix}_{date_str}"
    try:  
        X_train = pd.read_parquet(f"{load_dir}/{exact_dir}/X_train.parquet")
        y_train = joblib.load(f"{load_dir}/{exact_dir}/y_train.pkl")
        X_val   = pd.read_parquet(f"{load_dir}/{exact_dir}/X_val.parquet")
        y_val   = joblib.load(f"{load_dir}/{exact_dir}/y_val.pkl")
        X_test  = pd.read_parquet(f"{load_dir}/{exact_dir}/X_test.parquet")
        y_test  = joblib.load(f"{load_dir}/{exact_dir}/y_test.pkl")
        return X_train, y_train, X_val, y_val, X_test, y_test
    except Exception as e:
        print(f"Error loading datasets: {e}")
        return None, None, None
