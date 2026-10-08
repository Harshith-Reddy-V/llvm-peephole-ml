import re

# Simple mapping of opcodes to IDs for ML pipeline
OPCODE_MAP = {
    "add": 1,
    "sub": 2,
    "mul": 3,
    "div": 4,
    "and": 5,
    "or": 6,
    "xor": 7,
    "shl": 8,
    "lshr": 9,
    "ashr": 10
}

def get_instruction_type(opcode):
    if opcode in ["add", "sub", "mul", "div"]:
        return "arithmetic"
    if opcode in ["and", "or", "xor", "shl", "lshr", "ashr"]:
        return "bitwise"
    return "other"

def count_operands(form_str):
    """
    Naively counts operands by splitting on spaces and commas, 
    ignoring the assignment and opcode.
    """
    if "=" not in form_str:
        return 0
    rhs = form_str.split("=")[1].strip()
    parts = re.split(r'[,\s]+', rhs)
    # Remove the opcode and type (e.g., 'add', 'i32')
    operands = [p for p in parts if p.startswith('%') or p.isdigit() or (p.startswith('-') and p[1:].isdigit())]
    return len(operands)

def count_constants(form_str):
    if "=" not in form_str:
        return 0
    rhs = form_str.split("=")[1].strip()
    parts = re.split(r'[,\s]+', rhs)
    constants = [p for p in parts if p.isdigit() or (p.startswith('-') and p[1:].isdigit())]
    return len(constants)

def count_variables(form_str):
    if "=" not in form_str:
        return 0
    rhs = form_str.split("=")[1].strip()
    parts = re.split(r'[,\s]+', rhs)
    variables = [p for p in parts if p.startswith('%')]
    return len(variables)

def extract_features(candidate):
    """
    Takes a candidate dictionary and returns a new dictionary with extracted features.
    """
    features = candidate.copy()
    
    orig = candidate["original_form"]
    opt = candidate["optimized_form"]
    opcode = candidate["opcode"]
    
    # 1. Instruction counts (for peepholes, often 1 -> 0 or 1 -> 1)
    # Since these are simple single-line patterns, original count is 1.
    orig_inst_count = 1
    # If opt is just an assignment (e.g. %x = %a or %x = 5), it's 0 real operations.
    if "=" in opt:
        rhs = opt.split("=")[1].strip()
        opt_inst_count = 1 if any(op in rhs for op in OPCODE_MAP.keys()) else 0
    else:
        opt_inst_count = 0
    
    features["original_instruction_count"] = orig_inst_count
    features["optimized_instruction_count"] = opt_inst_count
    features["instruction_reduction"] = orig_inst_count - opt_inst_count
    
    # 2. Operands, constants, variables (based on original form)
    features["operand_count"] = count_operands(orig)
    features["constant_count"] = count_constants(orig)
    features["variable_count"] = count_variables(orig)
    
    # 3. Opcode encoding
    features["opcode_id"] = OPCODE_MAP.get(opcode, 0)
    features["instruction_type"] = get_instruction_type(opcode)
    
    # 4. Complexity measures
    # Simple complexity: number of operands + constants + variables
    features["candidate_size"] = len(orig)
    features["complexity"] = features["operand_count"] + features["constant_count"] + features["variable_count"]
    
    return features
