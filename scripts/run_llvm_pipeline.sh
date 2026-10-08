#!/bin/bash
echo "Running Person 1 LLVM Pipeline"
# Assume virtualenv or system python has the required packages
python3 src/run_pipeline.py > results/candidate_generation.log
cat results/candidate_generation.log
