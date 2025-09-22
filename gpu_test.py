import torch
import sys

print("=== GPU Configuration Check ===")
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA Version: {torch.version.cuda}")
    print(f"GPU Count: {torch.cuda.device_count()}")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    
    # Memory test
    try:
        x = torch.randn(1000, 1000).cuda()
        print("GPU Memory Test: PASSED")
        print(f"Current GPU Memory Usage: {torch.cuda.memory_allocated(0) / 1e9:.3f} GB")
    except Exception as e:
        print(f"GPU Memory Test: FAILED - {e}")
else:
    print("CUDA not available. Will use CPU for training.")
    
print("=== System Information ===")
print(f"Python Version: {sys.version}")