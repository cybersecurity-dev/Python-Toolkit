import pandas as pd

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

def find_na_in_boolean_columns(param_df: pd.DataFrame, print_columns : bool = True):
    """
    Finds boolean columns that contain NA values.
    """

    # Select boolean dtype columns (bool + pandas nullable 'boolean')
    bool_cols = param_df.select_dtypes(include=["bool", "boolean"])

    # Identify boolean columns with NA
    na_bool_cols = bool_cols.columns[bool_cols.isna().any()].tolist()

    # Optional printing
    if print_columns:
        if na_bool_cols:
            print("Boolean columns containing NA values:")
            for col in na_bool_cols:
                na_count = param_df[col].isna().sum()
                print(f" - {col}: {na_count} NA(s)")
        else:
            print("No boolean columns contain NA values.")

    return na_bool_cols
