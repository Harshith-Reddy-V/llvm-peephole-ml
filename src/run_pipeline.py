import os
import sys
from generate_candidates import main as generate_main
from extract_features import extract_features
from build_dataset import save_dataset, validate_dataset

def main():
    print("=== LLVM ENVIRONMENT ===")
    # Attempt to check LLVM in system (though we know it's missing in this setup)
    llvm_check = os.popen('opt --version 2>&1').read()
    if "not recognized" in llvm_check or "not found" in llvm_check.lower() or not llvm_check:
        print("LLVM/opt not found in PATH. Using defensible Python regex fallback for candidate generation.")
    else:
        print(f"LLVM found:\n{llvm_check.strip()}")
    
    print("\n=== CANDIDATE GENERATION ===")
    candidates = generate_main()
    
    print("\n=== FEATURE EXTRACTION ===")
    print(f"Processing {len(candidates)} candidates...")
    features_list = []
    for c in candidates:
        features = extract_features(c)
        features_list.append(features)
    print("Feature extraction complete.")
    
    print("\n=== DATASET ===")
    csv_path = os.path.join('data', 'candidates.csv')
    json_path = os.path.join('data', 'candidates.json')
    
    df = save_dataset(features_list, csv_path, json_path)
    
    print(f"CSV saved to: {csv_path}")
    print(f"JSON saved to: {json_path}")
    
    validate_dataset(df)
    
if __name__ == "__main__":
    main()
