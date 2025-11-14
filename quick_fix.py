#!/usr/bin/env python3
"""
Quick Fix for MAKV Ultimate APTS - Transformers Issue
Installs missing transformers and optimizes for immediate use
"""

import subprocess
import sys
import os

def run_cmd(cmd):
    """Run command and return success status"""
    try:
        print(f"🔧 Running: {cmd}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e.stderr}")
        return False

def main():
    print("🔥 MAKV Ultimate APTS - Quick Fix")
    print("=" * 50)
    
    # 1. Install core packages
    print("\n📦 Installing core AI packages...")
    packages = [
        "torch>=2.0.0 --index-url https://download.pytorch.org/whl/cpu",
        "transformers>=4.35.0",
        "accelerate>=0.24.0",
        "huggingface-hub",
        "tokenizers",
        "safetensors",
        "sentencepiece"
    ]
    
    for package in packages:
        cmd = f"{sys.executable} -m pip install {package} --upgrade"
        run_cmd(cmd)
    
    # 2. Set environment variables
    print("\n⚙️ Setting environment variables...")
    env_vars = {
        "TOKENIZERS_PARALLELISM": "false",
        "TRANSFORMERS_CACHE": "./models",
        "HF_HOME": "./models",
        "TORCH_HOME": "./models"
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"✅ Set {key}={value}")
    
    # 3. Create models directory
    print("\n📁 Creating models directory...")
    os.makedirs("./models", exist_ok=True)
    print("✅ Models directory created")
    
    # 4. Test imports
    print("\n🧪 Testing imports...")
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except ImportError as e:
        print(f"❌ PyTorch failed: {e}")
    
    try:
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
    except ImportError as e:
        print(f"❌ Transformers failed: {e}")
    
    try:
        import accelerate
        print(f"✅ Accelerate {accelerate.__version__}")
    except ImportError as e:
        print(f"❌ Accelerate failed: {e}")
    
    # 5. Download a lightweight model
    print("\n📥 Downloading lightweight model...")
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        model_name = "distilgpt2"  # Small, fast model
        print(f"📥 Downloading {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, 
            cache_dir="./models"
        )
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            cache_dir="./models",
            torch_dtype=torch.float32
        )
        
        print(f"✅ Successfully downloaded {model_name}")
        
    except Exception as e:
        print(f"⚠️ Model download failed: {e}")
        print("💡 System will use rule-based fallback")
    
    print("\n🎉 Quick fix complete!")
    print("🚀 You can now run: python3 makv_ultimate_apts.py")

if __name__ == "__main__":
    main()