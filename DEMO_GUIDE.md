# Faculty Demonstration Guide (Person 1: LLVM + Candidate Generation)

This document provides a simple, step-by-step script for demonstrating the 25% milestone of the Compiler Design BTech Project. 

## Presentation Explanation
*What to say when explaining your work:*

> "My portion, Person 1, handles the LLVM-side pipeline. We provide LLVM IR inputs, obtain peephole optimization candidates through the candidate-generation stage, represent each candidate as an original and optimized form, extract lightweight structural features, and store the resulting records in a structured dataset. This dataset is then used by Person 2 for the ML confidence-scoring stage."

## Demonstration Steps

### STEP 1: Show the LLVM Inputs
1. Open the folder `input/` in your IDE.
2. Open `basic_arithmetic.ll`.
3. **Say:** *"Here is the LLVM input. It contains simple unoptimized instructions like `add i32 %a, 0`."*

### STEP 2: Run the Pipeline
1. Open your terminal in the project root.
2. Run the pipeline script:
   ```bash
   python src/run_pipeline.py
   ```
3. **Say:** *"Now, I'll run the candidate generation pipeline. Since Souper/LLVM binaries are not available in this specific Windows environment, the script uses a documented, transparent LLVM-based fallback that programmatically identifies these peephole transformations."*

### STEP 3: Show the Terminal Output
1. Point to the terminal output where it says:
   ```
   === CANDIDATE GENERATION ===
   Processing input\basic_arithmetic.ll...
   Processing input\bitwise.ll...
   Processing input\constant_ops.ll...
   Total candidates generated: 8
   ```
2. **Say:** *"Here is the generator processing the IR files and finding 8 optimization candidates."*

### STEP 4: Show the Extracted Features
1. Open `src/extract_features.py`.
2. **Say:** *"For each candidate, this feature extractor determines simple, explainable heuristics—like original instruction count, optimized instruction count, operand counts, and opcode IDs. We intentionally avoid deep learning or embeddings here."*

### STEP 5: Show the Final CSV Dataset
1. Open `data/candidates.csv`.
2. **Say:** *"Here is `candidates.csv`. You can see the original form (`add x, 0`), the optimized form (`x`), and all the extracted features in a tabular format."*

### STEP 6: Explain the Handoff
1. Point to the bottom of the CSV file.
2. **Say:** *"This CSV is the final output of Person 1. It is directly passed to Person 2, who will load it using Pandas to train the Machine Learning model for confidence scoring. Note that ML confidence scores and Alive2 verifications are intentionally NOT implemented yet, as they belong to the next project stages."*
