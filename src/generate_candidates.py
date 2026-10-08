import os
import re
import glob

def generate_candidates_from_file(filepath):
    """
    Reads an LLVM IR file and extracts potential peephole optimization candidates.
    Since Souper and LLVM 'opt' are unavailable in this environment, this uses a 
    defensible regex-based fallback to identify common local instruction-level 
    transformations where the mapping can be reasonably determined.
    """
    candidates = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        line = line.strip()
        
        # Look for standard peephole patterns
        
        # 1. add X, 0 -> X
        match = re.search(r'%\w+\s*=\s*add\s+\w+\s+(%\w+),\s*0', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "add"
            })
            continue
            
        # 2. sub X, 0 -> X
        match = re.search(r'%\w+\s*=\s*sub\s+\w+\s+(%\w+),\s*0', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "sub"
            })
            continue

        # 3. mul X, 1 -> X
        match = re.search(r'%\w+\s*=\s*mul\s+\w+\s+(%\w+),\s*1', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "mul"
            })
            continue
            
        # 4. xor X, 0 -> X
        match = re.search(r'%\w+\s*=\s*xor\s+\w+\s+(%\w+),\s*0', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "xor"
            })
            continue
            
        # 5. and X, -1 -> X
        match = re.search(r'%\w+\s*=\s*and\s+\w+\s+(%\w+),\s*-1', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "and"
            })
            continue
            
        # 6. or X, 0 -> X
        match = re.search(r'%\w+\s*=\s*or\s+\w+\s+(%\w+),\s*0', line)
        if match:
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {match.group(1)}",
                "opcode": "or"
            })
            continue
            
        # 7. Constant folding: add C1, C2
        match = re.search(r'%\w+\s*=\s*add\s+\w+\s+(\d+),\s*(\d+)', line)
        if match:
            c1, c2 = int(match.group(1)), int(match.group(2))
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {c1 + c2}",
                "opcode": "add"
            })
            continue
            
        # 8. Constant folding: sub C1, C2
        match = re.search(r'%\w+\s*=\s*sub\s+\w+\s+(\d+),\s*(\d+)', line)
        if match:
            c1, c2 = int(match.group(1)), int(match.group(2))
            candidates.append({
                "source_file": os.path.basename(filepath),
                "generation_method": "regex_fallback",
                "original_form": line,
                "optimized_form": f"{line.split('=')[0].strip()} = {c1 - c2}",
                "opcode": "sub"
            })
            continue

    return candidates

def main():
    input_dir = 'input'
    ll_files = glob.glob(os.path.join(input_dir, '*.ll'))
    
    all_candidates = []
    candidate_id = 1
    
    for ll_file in ll_files:
        print(f"Processing {ll_file}...")
        file_candidates = generate_candidates_from_file(ll_file)
        for c in file_candidates:
            c["candidate_id"] = candidate_id
            all_candidates.append(c)
            candidate_id += 1
            
    print(f"Total candidates generated: {len(all_candidates)}")
    return all_candidates

if __name__ == "__main__":
    main()
