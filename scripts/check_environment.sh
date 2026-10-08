#!/bin/bash
echo "=== Environment Check ==="
echo "OS:"
uname -a
echo ""
echo "LLVM:"
if command -v opt &> /dev/null; then
    opt --version
else
    echo "opt not found"
fi
if command -v llvm-config &> /dev/null; then
    llvm-config --version
else
    echo "llvm-config not found"
fi
echo ""
echo "Python:"
python3 --version
python3 -c "import pandas; print('pandas ' + pandas.__version__)" || echo "pandas missing"
python3 -c "import numpy; print('numpy ' + numpy.__version__)" || echo "numpy missing"
echo ""
echo "Souper:"
if command -v souper &> /dev/null; then
    souper --version || echo "souper found but failed to run version"
else
    echo "souper not found"
fi
