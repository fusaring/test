# script_2_performance.py
import torch
from torchvision import models
import time

def measure_inference_time(model, input_tensor, repetitions=50, warmup=10):
    """测量模型推理的平均耗时（毫秒）"""
    # 预热（不记录时间）
    for _ in range(warmup):
        with torch.no_grad():
            _ = model(input_tensor)
    
    # 同步 GPU 计算（确保计时准确）
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    
    start_time = time.time()
    for _ in range(repetitions):
        with torch.no_grad():
            _ = model(input_tensor)
    
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    
    elapsed = time.time() - start_time
    avg_ms = (elapsed / repetitions) * 1000
    return avg_ms

def main():
    # 加载模型
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    print(f"Using device: {device}")
    
    # 测试不同的 batch size
    batch_sizes = [1, 4, 16, 32, 64]
    print("Batch size\tAvg Inference Time (ms)")
    print("--------------------------------------")
    
    for bs in batch_sizes:
        # 生成随机输入（batch_size, 3, 224, 224）
        dummy_input = torch.randn(bs, 3, 224, 224).to(device)
        avg_ms = measure_inference_time(model, dummy_input)
        print(f"{bs}\t\t{avg_ms:.2f} ms")
        
        # 可选：显存占用（仅 GPU）
        if torch.cuda.is_available():
            mem_allocated = torch.cuda.memory_allocated(device) / 1024**2  # MB
            print(f"  (GPU memory allocated: {mem_allocated:.1f} MB)")
    
if __name__ == "__main__":
    main()