"""
Configuration file for Pulli Kolam AI Project
"""

from pathlib import Path

# Project Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_ROOT = PROJECT_ROOT / "data"
MODEL_ROOT = PROJECT_ROOT / "models"

# Dataset Configuration
DATASET_CONFIG = {
    "raw_data_path": DATA_ROOT / "raw",
    "processed_data_path": DATA_ROOT / "processed",
    "train_split": 0.8,
    "val_split": 0.1,
    "test_split": 0.1,
    "random_seed": 42
}

# Image Processing Configuration
IMAGE_CONFIG = {
    "target_size": (224, 224),
    "channels": 3,
    "normalization_mean": [0.485, 0.456, 0.406],
    "normalization_std": [0.229, 0.224, 0.225],
    "supported_formats": ['.jpg', '.jpeg', '.png', '.bmp']
}

# Training Configuration
TRAINING_CONFIG = {
    "batch_size": 16,
    "learning_rate": 1e-4,
    "num_epochs": 100,
    "device": "auto",
    "num_workers": 2
}

# Mathematical Validation Configuration  
MATH_CONFIG = {
    "dot_detection": {
        "min_radius": 3,
        "max_radius": 15,
        "param1": 50,
        "param2": 30
    },
    "validation_rules": {
        "closed_loops": True,
        "dot_encirclement": True,
        "no_overlap": True
    }
}
