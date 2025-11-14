#!/usr/bin/env python3
"""
MAKV Ultimate APTS - Environment Setup
Sets up optimal environment for the system
"""

import os
import sys

def setup_environment():
    """Set up optimal environment variables"""
    print("🔧 Setting up environment...")
    
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
    
    # Create models directory
    os.makedirs("./models", exist_ok=True)
    print("✅ Created models directory")

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

def main():
    print("🔥 MAKV Ultimate APTS - Environment Setup")
    print("=" * 50)
    
    setup_environment()
    success = test_components()
    
    if success:
        print("\n🎉 Environment setup complete!")
        print("🚀 All components working - AI mode available")
    else:
        print("\n⚠️ Some components failed - fallback mode available")
    
    print("\n🚀 Ready to run: python3 makv_ultimate_apts.py")

if __name__ == "__main__":
    main()