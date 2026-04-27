# concat two DataFrames horizontally (columns).
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

# concat Two DataFrames vertically (rows).
def concat_and_fill(param_df1, param_df2, fill_missing_value=np.nan) -> pd.DataFrame | None:
    if param_df1 is None or len(param_df1) == 0: return param_df2.copy()
    if param_df2 is None or len(param_df2) == 0: return param_df1.copy()
    df = pd.concat([param_df1, param_df2], axis=0, sort=False) 
    df = df.fillna(fill_missing_value) # Fill missing values with the chosen value (default: np.nan)
    return df

def find_mixed_type_columns(param_df: pd.DataFrame, print_columns : bool = True) -> dict:
    mixed_columns = {}
    for col in param_df.columns:
        types = param_df[col].dropna().map(type).unique()
        if len(types) > 1:
            mixed_columns[col] = types
    
    # Optional printing
    if print_columns:
        for k, v in mixed_columns:
            print(f"Column {k} : has {v} types")
    return mixed_columns
