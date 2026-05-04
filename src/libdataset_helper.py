import pandas as pd
from typing import Tuple

def split_dataframe_wdate(param_df     : pd.DataFrame, 
                          date_col     : str   = "first_seen_utc", 
                          label_col    : str   = "label", 
                          train_ratio  : float = 0.5, 
                          val_ratio    : float = 0.2, 
                          test_ratio   : float = 0.3, 
                          random_state : int = 42) \
    -> Tuple[pd.DataFrame | None, pd.DataFrame | None, pd.DataFrame | None]:
    
    # Ensure datetime format
    param_df[date_col] = pd.to_datetime(param_df[date_col], errors="coerce", format="mixed")

    # Separate by label
    df_label1 = param_df[param_df[label_col] == 1].copy()
    df_label0 = param_df[param_df[label_col] == 0].copy()

    # --- Label = 1: Malware Date-based split ---
    df_label1 = df_label1.sort_values(date_col).reset_index(drop=True)
    n1 = len(df_label1)
    idx_train_end = int(n1 * train_ratio)
    idx_val_end = int(n1 * (train_ratio + val_ratio))

    date1 = df_label1.loc[idx_train_end - 1, date_col] if n1 > 0 else None
    date2 = df_label1.loc[idx_val_end - 1, date_col] if n1 > 0 else None
    
    date1_str = date1.strftime("%Y-%m-%d %H:%M:%S") if date1 is not None else None
    print(f"Train Date:{date1_str}")
    date2_str = date2.strftime("%Y-%m-%d %H:%M:%S") if date2 is not None else None
    print(f"Validation Date:{date2_str}")

    train1 = df_label1[df_label1[date_col] <= date1]
    val1 = df_label1[(df_label1[date_col] > date1) & (df_label1[date_col] <= date2)]
    test1 = df_label1[df_label1[date_col] > date2]

    # --- Label = 0: Benign Random split ---
    df_label0 = df_label0.sample(frac=1, random_state=random_state).reset_index(drop=True)
    n0 = len(df_label0)
    idx_train_end0 = int(n0 * train_ratio)
    idx_val_end0 = int(n0 * (train_ratio + val_ratio))

    train0 = df_label0.iloc[:idx_train_end0]
    val0 = df_label0.iloc[idx_train_end0:idx_val_end0]
    test0 = df_label0.iloc[idx_val_end0:]

    df_train = pd.concat([train1, train0], ignore_index=True)
    df_val   = pd.concat([val1, val0],     ignore_index=True)
    df_test  = pd.concat([test1, test0],   ignore_index=True)

    return df_train, df_val, df_test
