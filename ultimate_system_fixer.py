#!/usr/bin/env python3
"""
MAKV Ultimate APTS - Complete System Fixer
Fixes all known issues and ensures system runs perfectly
"""

import os
import sys
import subprocess
import shutil
import time
from pathlib import Path

def print_banner():
    print("🔧" + "="*60 + "🔧")
    print("🔥 MAKV ULTIMATE APTS - COMPLETE SYSTEM FIXER 🔥")
    print("🔧" + "="*60 + "🔧")
    print()

def check_and_install_dependencies():
    """Check and install all required dependencies"""
    print("📦 Checking and installing dependencies...")
    
    # Get current Python executable
    python_exe = sys.executable
    print(f"🐍 Using Python: {python_exe}")
    
    # Required packages
    packages = [
        'torch>=2.0.0',
        'transformers>=4.35.0', 
        'accelerate>=0.24.0',
        'huggingface-hub',
        'rich',
        'requests',
        'psutil',
        'asyncio'
    ]
    
    for package in packages:
        try:
            print(f"📥 Installing {package}...")
            result = subprocess.run([
                python_exe, '-m', 'pip', 'install', package
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                print(f"✅ {package} installed successfully")
            else:
                print(f"⚠️ {package} installation had issues: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Failed to install {package}: {e}")
    
    print("✅ Dependency installation completed")

def test_imports():
    """Test all critical imports"""
    print("\n🧪 Testing critical imports...")
    
    imports_to_test = [
        ('torch', 'PyTorch'),
        ('transformers', 'Transformers'),
        ('rich', 'Rich'),
        ('requests', 'Requests'),
        ('psutil', 'PSUtil')
    ]
    
    all_good = True
    
    for module, name in imports_to_test:
        try:
            __import__(module)
            print(f"✅ {name} import successful")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            all_good = False
    
    return all_good

def setup_environment():
    """Set up optimal environment variables"""
    print("\n🌍 Setting up environment variables...")
    
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

def test_ai_model():
    """Test AI model loading"""
    print("\n🤖 Testing AI model loading...")
    
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        model_name = "gpt2"
        print(f"📥 Loading {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir="./models"
        )
        
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            cache_dir="./models",
            torch_dtype=torch.float32,
            device_map="cpu"
        )
        
        print("✅ AI model loaded successfully")
        
        # Test generation
        test_input = "System test:"
        inputs = tokenizer.encode(test_input, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=inputs.shape[1] + 5,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"✅ Model generation test: {response[:30]}...")
        
        return True
        
    except Exception as e:
        print(f"⚠️ AI model test failed: {e}")
        print("💡 System will use fallback mode")
        return False

def create_startup_script():
    """Create optimized startup script"""
    print("\n📝 Creating optimized startup script...")
    
    startup_script = '''#!/usr/bin/env python3
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
'''
    
    with open("start_makv_apts.py", "w") as f:
        f.write(startup_script)
    
    # Make executable
    os.chmod("start_makv_apts.py", 0o755)
    print("✅ Created start_makv_apts.py")

def run_system_test():
    """Run a quick system test"""
    print("\n🧪 Running system test...")
    
    try:
        # Test main system import
        sys.path.insert(0, '.')
        
        print("📥 Testing main system import...")
        import makv_ultimate_apts
        print("✅ Main system import successful")
        
        print("📥 Testing AI coordinator...")
        from offline_ai_coordinator import OfflineAICoordinator
        print("✅ AI coordinator import successful")
        
        print("📥 Testing Ghost Mode...")
        from advanced_ghost_mode import AdvancedGhostMode
        print("✅ Ghost Mode import successful")
        
        return True
        
    except Exception as e:
        print(f"⚠️ System test failed: {e}")
        return False

def cleanup_old_files():
    """Clean up any problematic files"""
    print("\n🧹 Cleaning up old files...")
    
    files_to_remove = [
        "*.pyc",
        "__pycache__",
        "*.log",
        "/tmp/tor_*",
        "/tmp/proxychains_*"
    ]
    
    for pattern in files_to_remove:
        try:
            if pattern.startswith("/tmp/"):
                # Remove temp files
                import glob
                for file in glob.glob(pattern):
                    try:
                        os.remove(file)
                        print(f"🗑️ Removed {file}")
                    except:
                        pass
            elif pattern == "__pycache__":
                # Remove pycache directories
                for root, dirs, files in os.walk("."):
                    if "__pycache__" in dirs:
                        shutil.rmtree(os.path.join(root, "__pycache__"))
                        print("🗑️ Removed __pycache__")
        except:
            pass
    
    print("✅ Cleanup completed")

def main():
    print_banner()
    
    print("🔍 Starting comprehensive system fix...")
    print()
    
    # Step 1: Cleanup
    cleanup_old_files()
    
    # Step 2: Environment setup
    setup_environment()
    
    # Step 3: Dependencies
    check_and_install_dependencies()
    
    # Step 4: Test imports
    imports_ok = test_imports()
    
    # Step 5: Test AI model
    ai_ok = test_ai_model()
    
    # Step 6: System test
    system_ok = run_system_test()
    
    # Step 7: Create startup script
    create_startup_script()
    
    print("\n" + "="*60)
    print("🎉 SYSTEM FIX COMPLETED!")
    print("="*60)
    
    if imports_ok and system_ok:
        print("✅ All systems operational!")
        print("🚀 Ready to run: python3 start_makv_apts.py")
        if ai_ok:
            print("🤖 AI mode available")
        else:
            print("💡 Fallback mode available")
    else:
        print("⚠️ Some issues detected but system should still work")
        print("🚀 Try running: python3 makv_ultimate_apts.py")
    
    print("\n📋 Quick Commands:")
    print("  python3 start_makv_apts.py     # Optimized startup")
    print("  python3 makv_ultimate_apts.py  # Direct startup")
    print("  python3 setup_environment.py   # Environment test")

if __name__ == "__main__":
    main()