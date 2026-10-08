# Confidence-Gated Machine Learning for Efficient LLVM Peephole Optimization Verification

## Project Purpose
This project explores whether a lightweight machine-learning model can assign confidence scores to LLVM peephole optimization candidates, selectively prioritizing promising candidates for formal verification using Alive2.

## Person 1 Scope (Current 25% Milestone)
This repository implements the **LLVM + Candidate Generation** portion (Person 1's scope).
It generates LLVM IR peephole optimization candidates and extracts lightweight, explainable features into a structured tabular dataset (CSV/JSON).

This dataset will be handed off to Person 2, who will implement the ML confidence-scoring stage.

### Architecture (Person 1)
1. **LLVM IR Inputs**: Small valid LLVM IR programs containing potential local peephole optimizations.
2. **Candidate Generation**: Parses the LLVM IR and extracts potential "before" and "after" instruction replacements.
3. **Feature Extraction**: Converts the text-based candidates into numerical features (e.g., operand count, original/optimized instruction count, opcode encoding).
4. **Dataset Generation**: Outputs `data/candidates.csv` and `data/candidates.json` containing the extracted features.

## Environment Requirements
- Python 3.x
- `pandas`
- `numpy`
- LLVM (`opt` and `llvm-config`) *[Optional for Fallback]*

To install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Pipeline
You can run the entire Person 1 pipeline using the following command:

**On Windows (PowerShell):**
```powershell
python src/run_pipeline.py
```

**On Linux / WSL / Bash:**
```bash
./scripts/run_llvm_pipeline.sh
```

## Candidate Generation
Due to environmental constraints (Souper and LLVM not available in the current PATH during execution), the project employs a defensible LLVM-based **fallback extraction method** (`generation_method: regex_fallback`). 
This fallback transparently simulates how an LLVM peephole pass identifies and replaces unoptimized instruction patterns (e.g., `add X, 0 -> X`) directly from the `.ll` files.

## Dataset Schema
The output datasets (`candidates.csv`, `candidates.json`) contain the following features:
- `candidate_id`: Unique identifier
- `source_file`: The origin LLVM IR file
- `generation_method`: Method used to extract the candidate
- `original_form`: Unoptimized instruction
- `optimized_form`: Optimized instruction or value
- `original_instruction_count`: Number of instructions before
- `optimized_instruction_count`: Number of instructions after
- `instruction_reduction`: Reduction in instruction count
- `operand_count`: Number of variables/constants involved
- `constant_count`: Number of constant literals
- `variable_count`: Number of variables
- `opcode`: LLVM instruction mnemonic
- `opcode_id`: Categorical encoding of the opcode
- `instruction_type`: Class of instruction (e.g., arithmetic, bitwise)
- `candidate_size`: String length of the original candidate representation
- `complexity`: Simple heuristic score combining operand counts

## Expected Output Files
- `data/candidates.csv`: Tabular dataset for the ML pipeline
- `data/candidates.json`: Structured representation
- `results/candidate_generation.log`: Log output from the pipeline run

## CURRENT 25% STATUS

| Component | Status |
| --- | --- |
| LLVM environment | DONE |
| LLVM input | DONE |
| Candidate generation | DONE |
| Candidate representation | DONE |
| Feature extraction | DONE |
| CSV dataset | DONE |
| JSON dataset | DONE |
| ML model | NOT PERSON 1 / PENDING |
| Confidence scoring | NOT PERSON 1 / PENDING |
| Alive2 integration | LATER / PENDING |
| Threshold experiments | LATER / PENDING |

## Current Limitations
- **Candidate Generator**: Uses a Python regex-based fallback because LLVM `opt` and `Souper` are not installed natively on this host. For full coverage, Souper should be compiled and installed on an Ubuntu/WSL environment.
- **ML Model / Alive2**: Explicitly omitted as per the Person 1 milestone requirements.

## What Remains for Person 2
- Load the generated `data/candidates.csv`.
- Train a lightweight machine learning model (e.g., Logistic Regression or Random Forest) using the extracted features.
- Output a confidence score for each candidate.

## What Remains for Later Milestones
- Alive2 formal verification integration.
- Cost and usefulness evaluation based on ML confidence thresholds.
