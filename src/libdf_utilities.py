def merge_on_primary_key(param_df1, param_df2, primary_key='sha256', based_on='First') -> pd.DataFrame | None:
    if param_df1 is None or len(param_df1) == 0: return param_df2.copy()
    if param_df2 is None or len(param_df2) == 0: return param_df1.copy()

    common_column_list = param_df1.columns.intersection(param_df2.columns).tolist()
    if primary_key in common_column_list:
        common_column_list.remove(primary_key)
    if based_on == 'First':
        df2_del = param_df2.drop(columns=common_column_list, errors='ignore')
        return param_df1.merge(df2_del, on=primary_key, how='inner')
    elif based_on == 'Second':
        df1_del = param_df1.drop(columns=common_column_list, errors='ignore')
        return df1_del.merge(param_df2, on=primary_key, how='inner')
    else:
        print("Argument 'based_on:' must be 'First' or 'Second'")
        return None
  
