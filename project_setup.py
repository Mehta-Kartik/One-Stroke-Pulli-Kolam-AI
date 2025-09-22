"""
Project Setup Script - Verify installation and environment
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version too old: {version.major}.{version.minor}")
        return False

def check_packages():
    """Check required packages"""
    required = ['torch', 'cv2', 'numpy', 'matplotlib', 'sklearn']
    missing = []
    
    for package in required:
        try:
            if package == 'cv2':
                import cv2
                print(f"✓ OpenCV: {cv2.__version__}")
            elif package == 'torch':
                import torch
                print(f"✓ PyTorch: {torch.__version__}")
            elif package == 'numpy':
                import numpy
                print(f"✓ NumPy: {numpy.__version__}")
            elif package == 'matplotlib':
                import matplotlib
                print(f"✓ Matplotlib: {matplotlib.__version__}")
            elif package == 'sklearn':
                import sklearn
                print(f"✓ Scikit-learn: {sklearn.__version__}")
        except ImportError:
            missing.append(package)
            print(f"✗ {package} - MISSING")
    
    return len(missing) == 0

def check_structure():
    """Check project structure"""
    required_dirs = [
        'data/raw', 'data/processed', 
        'src/data', 'src/models', 'src/utils',
        'models/checkpoints'
    ]
    
    all_good = True
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✓ {dir_path}")
        else:
            print(f"✗ {dir_path} - MISSING")
            all_good = False
    
    return all_good

def main():
    """Run complete setup check"""
    print("=== Project Setup Verification ===\n")
    
    print("Checking Python version:")
    python_ok = check_python_version()
    
    print("\nChecking packages:")
    packages_ok = check_packages()
    
    print("\nChecking project structure:")
    structure_ok = check_structure()
    
    print("\n" + "="*40)
    if python_ok and packages_ok and structure_ok:
        print("✅ Setup Complete! Ready for development.")
    else:
        print("❌ Setup issues found. Please fix and re-run.")

if __name__ == "__main__":
    main()
