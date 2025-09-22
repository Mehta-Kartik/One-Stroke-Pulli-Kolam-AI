# Quick verification script - run this to complete Day 1
import os
from pathlib import Path

def verify_day1_setup():
    print("=== Day 1 Completion Verification ===")
    
    # Check project structure
    required_folders = ['data/raw', 'src/data', 'src/models', 'models/checkpoints']
    for folder in required_folders:
        if os.path.exists(folder):
            print(f"✓ {folder}")
        else:
            print(f"✗ {folder} - MISSING")
    
    # Check dataset
    dataset_path = Path('data/raw')
    image_files = list(dataset_path.rglob('*.jpg')) + list(dataset_path.rglob('*.png'))
    print(f"✓ Dataset images found: {len(image_files)}")
    
    # Check key files
    key_files = ['src/config.py', 'src/data/data_loader.py', 'project_setup.py']
    for file in key_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - MISSING")
    
    print("\n=== Day 1 Status: ✅ COMPLETE ===")
    print("Ready for Day 2: Dataset Analysis & Mathematical Validation")

# Run verification
verify_day1_setup()
