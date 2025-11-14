#!/usr/bin/env python3
"""
MAKV Ultimate APTS - Environment Setup
Simple environment setup and testing script
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    print("🔧 MAKV APTS Environment Setup 🔧")
    print("="*40)

def check_python():
    """Check Python version and executable"""
    print(f"🐍 Python Version: {sys.version}")
    print(f"🐍 Python Executable: {sys.executable}")
    
    if sys.version_info < (3, 8):
        print("⚠️ Warning: Python 3.8+ recommended")
    else:
        print("✅ Python version OK")

def setup_environment():
    """Set up optimal environment variables"""
    print("\n🌍 Setting up environment variables...")
    
    # Set environment variables for optimal performance
    env_vars = {
        "TOKENIZERS_PARALLELISM": "false",
        "TRANSFORMERS_CACHE": "./models",
        "HF_HOME": "./models", 
        "TORCH_HOME": "./models",
        "TRANSFORMERS_OFFLINE": "0",
        "HF_HUB_OFFLINE": "0"
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"✅ Set {key}={value}")
    
    # Create necessary directories
    dirs = ["models", "logs", "temp", "data"]
    for dir_name in dirs:
        os.makedirs(f"./{dir_name}", exist_ok=True)
        print(f"✅ Created {dir_name}/ directory")

def test_components():
    """Test all system components"""
    print("\n🧪 Testing system components...")
    
    # Test imports
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except ImportError as e:
        print(f"❌ PyTorch: {e}")
        return False
    
    try:
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
    except ImportError as e:
        print(f"❌ Transformers: {e}")
        return False
    
    # Test model loading with lightweight model
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        print("🤖 Testing model loading...")
        model_name = "gpt2"  # Small, reliable model
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir="./models"
        )
        
        # Add pad token if it doesn't exist
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            cache_dir="./models",
            torch_dtype=torch.float32,
            device_map="cpu"
        )
        
        print(f"✅ Successfully loaded {model_name}")
        
        # Test generation
        test_input = "System analysis:"
        inputs = tokenizer.encode(test_input, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=inputs.shape[1] + 10,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"✅ Model generation test: {response[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"⚠️ Model loading failed: {e}")
        print("💡 System will use rule-based fallback")
        return False

def test_system_files():
    """Test if main system files exist"""
    print("\n📄 Checking system files...")
    
    required_files = [
        "makv_ultimate_apts.py",
        "offline_ai_coordinator.py", 
        "advanced_ghost_mode.py"
    ]
    
    all_present = True
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} missing")
            all_present = False
    
    return all_present

def main():
    print_header()
    
    # Basic checks
    check_python()
    setup_environment()
    
    # File checks
    files_ok = test_system_files()
    
    # Component tests
    success = test_components()
    
    print("\n" + "="*40)
    print("🎯 ENVIRONMENT SETUP COMPLETE")
    print("="*40)
    
    if success and files_ok:
        print("✅ Environment ready!")
        print("🚀 All components working - AI mode available")
    else:
        print("⚠️ Some issues detected")
        if not files_ok:
            print("💡 Make sure you're in the correct directory")
        if not success:
            print("💡 Fallback mode available")
    
    print(f"\n📍 Current directory: {os.getcwd()}")
    print(f"📍 Python path: {sys.executable}")
    print("\n🚀 Ready to run: python3 makv_ultimate_apts.py")

if __name__ == "__main__":
    main()