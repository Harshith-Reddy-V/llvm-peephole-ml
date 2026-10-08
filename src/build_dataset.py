import os
import json
import pandas as pd

def validate_dataset(df):
    """
    Validates dataset quality and prints a summary.
    """
    print("\n--- Validating Dataset ---")
    
    # Check for empty
    if df.empty:
        print("ERROR: Dataset is empty.")
        return False
        
    # Check uniqueness of candidate_id
    if df['candidate_id'].nunique() != len(df):
        print("ERROR: Candidate IDs are not unique.")
        return False
        
    # Check for required columns
    required_cols = [
        "candidate_id", "source_file", "generation_method", "original_form",
        "optimized_form", "original_instruction_count", "optimized_instruction_count",
        "instruction_reduction", "operand_count", "constant_count", "variable_count",
        "opcode", "opcode_id", "instruction_type", "candidate_size", "complexity"
    ]
    for col in required_cols:
        if col not in df.columns:
            print(f"ERROR: Missing required column: {col}")
            return False
            
    # Check for nulls in critical text fields
    for col in ["original_form", "optimized_form", "source_file", "generation_method"]:
        if df[col].isnull().any() or (df[col] == "").any():
            print(f"ERROR: Found null/empty values in {col}.")
            return False
            
    print("Dataset validation passed!")
    
    print("\n--- Dataset Summary ---")
    print(f"Total candidates: {len(df)}")
    print(f"Source files: {df['source_file'].nunique()}")
    print(f"Opcode categories: {df['opcode'].unique()}")
    print(f"Average candidate size: {df['candidate_size'].mean():.2f}")
    print(f"Average instruction reduction: {df['instruction_reduction'].mean():.2f}")
    print(f"Unique candidate patterns: {df['original_form'].nunique()}")
    
    return True

def save_dataset(features_list, output_csv, output_json):
    """
    Saves the extracted features to CSV and JSON formats.
    """
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    # Save CSV
    df = pd.DataFrame(features_list)
    df.to_csv(output_csv, index=False)
    
    # Save JSON (nested under 'features')
    json_data = []
    for f in features_list:
        rec = {
            "candidate_id": f["candidate_id"],
            "source_file": f["source_file"],
            "generation_method": f["generation_method"],
            "original_form": f["original_form"],
            "optimized_form": f["optimized_form"],
            "features": {
                "original_instruction_count": f["original_instruction_count"],
                "optimized_instruction_count": f["optimized_instruction_count"],
                "instruction_reduction": f["instruction_reduction"],
                "operand_count": f["operand_count"],
                "constant_count": f["constant_count"],
                "variable_count": f["variable_count"],
                "opcode": f["opcode"],
                "opcode_id": f["opcode_id"],
                "instruction_type": f["instruction_type"],
                "candidate_size": f["candidate_size"],
                "complexity": f["complexity"]
            }
        }
        json_data.append(rec)
        
    with open(output_json, 'w') as jf:
        json.dump(json_data, jf, indent=2)
        
    return df
