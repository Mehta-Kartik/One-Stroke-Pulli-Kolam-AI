"""
Data Loading Utilities for Pulli Kolam Dataset
"""

import os
import cv2
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PulliKolamDataLoader:
    """Simple data loader for Pulli Kolam images"""
    
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.bmp']
        self.image_files = self._discover_images()
        logger.info(f"Found {len(self.image_files)} images")
    
    def _discover_images(self):
        """Find all image files"""
        image_files = []
        for ext in self.supported_formats:
            image_files.extend(list(self.data_path.rglob(f'*{ext}')))
            image_files.extend(list(self.data_path.rglob(f'*{ext.upper()}')))
        return sorted(list(set(image_files)))
    
    def load_image(self, image_path):
        """Load a single image"""
        try:
            image = cv2.imread(str(image_path))
            if image is not None:
                return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return None
        except Exception as e:
            logger.error(f"Error loading {image_path}: {e}")
            return None
    
    def get_dataset_stats(self):
        """Get basic dataset statistics"""
        stats = {
            'total_images': len(self.image_files),
            'valid_images': 0,
            'image_sizes': []
        }
        
        # Sample first 10 images for quick stats
        for img_path in self.image_files[:10]:
            image = self.load_image(img_path)
            if image is not None:
                stats['valid_images'] += 1
                stats['image_sizes'].append(image.shape[:2])
        
        return stats

# Test function
if __name__ == "__main__":
    loader = PulliKolamDataLoader("../../data/raw")
    stats = loader.get_dataset_stats()
    print(f"Dataset stats: {stats}")
