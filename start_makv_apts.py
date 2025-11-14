#!/usr/bin/env python3
"""
MAKV Ultimate APTS - Optimized Startup
"""

import os
import sys

def setup_environment():
    """Set up optimal environment"""
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
    
    os.makedirs("./models", exist_ok=True)

def main():
    print("🚀 Starting MAKV Ultimate APTS...")
    setup_environment()
    
    # Import and run main system
    try:
        from makv_ultimate_apts import main as run_apts
        run_apts()
    except Exception as e:
        print(f"❌ Error starting system: {e}")
        print("💡 Try running: python3 makv_ultimate_apts.py")

if __name__ == "__main__":
    main()
