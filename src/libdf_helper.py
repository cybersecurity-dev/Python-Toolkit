import pandas as pd

def classify_dataframe_columns(param_df: pd.DataFrame, print_output: bool = True) -> Dict[str, List]:

    numerical_columns = param_df.select_dtypes(include=["number"]).columns.tolist()
    integer_columns   = param_df.select_dtypes(include=["int", "Int64"]).columns.tolist()
    float_columns     = param_df.select_dtypes(include=["float"]).columns.tolist()

    string_columns      = param_df.select_dtypes(include=["string"]).columns.tolist()
    categorical_columns = param_df.select_dtypes(include=["category"]).columns.tolist()
    boolean_columns     = param_df.select_dtypes(include=["bool", "boolean"]).columns.tolist()
    datetime_columns    = param_df.select_dtypes(include=["datetime"]).columns.tolist()

    object_columns = [
        col for col in param_df.select_dtypes(include=["object"]).columns
        if col not in categorical_columns
    ]

    result = {
              "numerical_columns"  : numerical_columns,
              "integer_columns"    : integer_columns,
              "float_columns"      : float_columns,
              "string_columns"     : string_columns,
              "categorical_columns": categorical_columns,
              "boolean_columns"    : boolean_columns,
              "datetime_columns"   : datetime_columns,
              "object_columns"     : object_columns,
              "all_columns"        : param_df.columns.tolist()
             }

    if print_output:
        print(f"\nColumn classification for DataFrame\n")

        for key, cols in result.items():
            print(f"{key.replace('_', ' ').title()} ({len(cols)}):")
            print(cols if cols else "  None")
            print()

    return result
    
def print_all_columns_value_counts(param_df: pd.DataFrame, dropna: bool = False, max_values: int | None = None):
    for col in param_df.columns:
        print(f"\n{'=' * 60}")
        print(f"Column: {col}")
        print(f"Dtype : {df[col].dtype}")
        print(f"{'-' * 60}")

        vc = param_df[col].value_counts(dropna=dropna)

        if max_values is not None:
            vc = vc.head(max_values)  
        print(vc)

def find_na_in_boolean_columns(param_df: pd.DataFrame, print_output : bool = True):
    """
    Finds boolean columns that contain NA values.
    """

    # Select boolean dtype columns (bool + pandas nullable 'boolean')
    bool_cols = param_df.select_dtypes(include=["bool", "boolean"])

    # Identify boolean columns with NA
    na_bool_cols = bool_cols.columns[bool_cols.isna().any()].tolist()

    # Optional printing
    if print_output:
        if na_bool_cols:
            print("Boolean columns containing NA values:")
            for col in na_bool_cols:
                na_count = param_df[col].isna().sum()
                print(f" - {col}: {na_count} NA(s)")
        else:
            print("No boolean columns contain NA values.")

    return na_bool_cols

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

def clean_all_mixed_int_str_columns(param_df: pd.DataFrame) -> pd.DataFrame:
    for col in param_df.columns:
        types = set(param_df[col].dropna().map(type))
        if str in types and int in types:
            param_df[col] = param_df[col].apply(
                lambda x: "" if isinstance(x, int) and x == 0 else x
            )
    return param_df