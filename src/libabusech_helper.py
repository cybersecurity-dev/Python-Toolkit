def download_and_clean_sslblacklist(url: str,
                                    output_csv_path: Path = "./data/sslblacklist_clean.csv",
                                    skip_lines: int = 9) -> pd.DataFrame:
    # Download CSV
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    # Remove first N lines (comments)
    lines = response.text.splitlines()
    cleaned_csv_text = "\n".join(lines[skip_lines:])

    output_csv_path.write_text(cleaned_csv_text, encoding="utf-8")

    # Load into DataFrame with explicit column names
    df_sslblacklist = pd.read_csv(StringIO(cleaned_csv_text),
                                  header=None,
                                  names=["Listingdate", "SHA1", "Listingreason"])

    return df_sslblacklist
