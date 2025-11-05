# helper_fun.py
import pandas as pd
import os

output_file = "allocation_records.xlsx"

def save_to_excel(record: dict):
    """
    Save a form submission to allocation_records.xlsx with a unique ID.
    """
    # Check if file exists
    if os.path.exists(output_file):
        records_df = pd.read_excel(output_file, engine='openpyxl')
    else:
        records_df = pd.DataFrame(columns=['ID'] + list(record.keys()))

    # Generate new ID
    new_id = len(records_df) + 1
    record_with_id = {'ID': new_id, **record}

    # Convert record dict to DataFrame
    record_df = pd.DataFrame([record_with_id])

    # Concatenate and save
    records_df = pd.concat([records_df, record_df], ignore_index=True)
    records_df.to_excel(output_file, index=False)
    print(f"Record saved successfully with ID {new_id}")
