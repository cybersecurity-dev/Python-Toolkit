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
