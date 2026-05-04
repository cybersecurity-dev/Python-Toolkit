def split_dataframe_wdate(param_df     : pd.DataFrame, 
                          date_col     : str   = "first_seen_utc", 
                          label_col    : str   = "label", 
                          train_ratio  : float = 0.5, 
                          val_ratio    : float = 0.2, 
                          test_ratio   : float = 0.3, 
                          random_state : int = 42) \
    -> Tuple[pd.DataFrame | None, pd.DataFrame | None, pd.DataFrame | None]:
    
    return None, None, None
