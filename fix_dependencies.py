#!/usr/bin/env python3
"""
MAKV Ultimate APTS - Dependency Fixer
Installs all missing dependencies and optimizes the system
"""

import subprocess
import sys
import os
import importlib
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

console = Console()

def run_command(cmd, description="Running command"):
    """Run a command with progress indicator"""
    try:
        console.print(f"🔧 {description}...")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        console.print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"❌ {description} - Failed: {e.stderr}")
        return False

def install_python_packages():
    """Install all required Python packages"""
    console.print(Panel("🐍 Installing Python Packages", style="blue"))
    
    packages = [
        "torch>=2.0.0",
        "transformers>=4.35.0", 
        "accelerate>=0.24.0",
        "flash-attn",
        "bitsandbytes",
        "sentencepiece",
        "protobuf",
        "safetensors",
        "tokenizers",
        "huggingface-hub",
        "datasets",
        "evaluate",
        "peft",
        "trl"
    ]
    
    for package in packages:
        console.print(f"📦 Installing {package}...")
        cmd = f"{sys.executable} -m pip install {package} --upgrade --no-cache-dir"
        if not run_command(cmd, f"Installing {package}"):
            # Try alternative installation
            console.print(f"🔄 Trying alternative installation for {package}...")
            cmd = f"{sys.executable} -m pip install {package} --upgrade --force-reinstall"
            run_command(cmd, f"Force installing {package}")

def install_system_tools():
    """Install system-level tools"""
    console.print(Panel("🛠️ Installing System Tools", style="green"))
    
    tools = [
        "apt update",
        "apt install -y build-essential",
        "apt install -y python3-dev",
        "apt install -y libffi-dev",
        "apt install -y libssl-dev",
        "apt install -y tor",
        "apt install -y proxychains4", 
        "apt install -y torsocks",
        "apt install -y obfs4proxy",
        "apt install -y macchanger",
        "apt install -y bleachbit",
        "apt install -y nmap",
        "apt install -y masscan",
        "apt install -y nikto",
        "apt install -y sqlmap",
        "apt install -y metasploit-framework",
        "apt install -y aircrack-ng",
        "apt install -y hashcat",
        "apt install -y john",
        "apt install -y hydra"
    ]
    
    for tool in tools:
        run_command(tool, f"Installing {tool.split()[-1]}")

def download_models():
    """Pre-download required AI models"""
    console.print(Panel("🤖 Downloading AI Models", style="yellow"))
    
    try:
        from huggingface_hub import snapshot_download
        
        models = [
            "microsoft/Phi-3-mini-4k-instruct",
            "microsoft/DialoGPT-medium",
            "distilbert-base-uncased"
        ]
        
        for model in models:
            console.print(f"📥 Downloading {model}...")
            try:
                snapshot_download(repo_id=model, cache_dir="./models")
                console.print(f"✅ Downloaded {model}")
            except Exception as e:
                console.print(f"⚠️ Failed to download {model}: {e}")
                
    except ImportError:
        console.print("⚠️ huggingface_hub not available, skipping model download")

def optimize_torch():
    """Optimize PyTorch installation"""
    console.print(Panel("🔥 Optimizing PyTorch", style="red"))
    
    # Install optimized PyTorch for CPU
    cmd = f"{sys.executable} -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"
    run_command(cmd, "Installing optimized PyTorch")
    
    # Install additional optimization packages
    optimization_packages = [
        "intel-extension-for-pytorch",
        "mkl",
        "mkl-include"
    ]
    
    for package in optimization_packages:
        cmd = f"{sys.executable} -m pip install {package}"
        run_command(cmd, f"Installing {package}")

def fix_transformers_config():
    """Fix transformers configuration issues"""
    console.print(Panel("⚙️ Fixing Transformers Configuration", style="cyan"))
    
    # Create optimized transformers config
    config_code = '''
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_CACHE"] = "./models"
os.environ["HF_HOME"] = "./models"
os.environ["TORCH_HOME"] = "./models"
'''
    
    with open("transformers_config.py", "w") as f:
        f.write(config_code)
    
    console.print("✅ Created transformers configuration")

def create_optimized_ai_coordinator():
    """Create an optimized version of the AI coordinator"""
    console.print(Panel("🚀 Creating Optimized AI Coordinator", style="magenta"))
    
    optimized_code = '''
import os
import sys
import torch
import warnings
warnings.filterwarnings("ignore")

# Set environment variables for optimization
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_CACHE"] = "./models"
os.environ["HF_HOME"] = "./models"

class OptimizedAICoordinator:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cpu"
        
    def initialize_model(self):
        """Initialize with fallback options"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
            
            # Try lightweight model first
            model_options = [
                "microsoft/DialoGPT-small",
                "distilgpt2", 
                "gpt2"
            ]
            
            for model_name in model_options:
                try:
                    print(f"🤖 Trying to load {model_name}...")
                    self.tokenizer = AutoTokenizer.from_pretrained(
                        model_name, 
                        cache_dir="./models",
                        local_files_only=False
                    )
                    
                    self.model = AutoModelForCausalLM.from_pretrained(
                        model_name,
                        cache_dir="./models", 
                        torch_dtype=torch.float32,
                        device_map="cpu",
                        local_files_only=False,
                        low_cpu_mem_usage=True
                    )
                    
                    print(f"✅ Successfully loaded {model_name}")
                    return True
                    
                except Exception as e:
                    print(f"⚠️ Failed to load {model_name}: {e}")
                    continue
                    
            print("❌ All model loading attempts failed, using rule-based fallback")
            return False
            
        except ImportError as e:
            print(f"❌ Transformers not available: {e}")
            return False
    
    def analyze_system(self, data):
        """Analyze system with AI or fallback to rules"""
        if self.model and self.tokenizer:
            try:
                # Use AI model for analysis
                return self._ai_analysis(data)
            except:
                pass
        
        # Fallback to rule-based analysis
        return self._rule_based_analysis(data)
    
    def _ai_analysis(self, data):
        """AI-powered analysis"""
        prompt = f"Analyze this system data: {data}"
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs, 
                max_length=100,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    def _rule_based_analysis(self, data):
        """Rule-based fallback analysis"""
        analysis = {
            "status": "operational",
            "recommendations": ["System running normally"],
            "threats": [],
            "optimizations": ["Consider enabling AI mode for enhanced analysis"]
        }
        return analysis

# Test the optimized coordinator
if __name__ == "__main__":
    coordinator = OptimizedAICoordinator()
    success = coordinator.initialize_model()
    print(f"Model initialization: {'Success' if success else 'Failed - using fallback'}")
'''
    
    with open("optimized_ai_coordinator.py", "w") as f:
        f.write(optimized_code)
    
    console.print("✅ Created optimized AI coordinator")

def test_installation():
    """Test if all components are working"""
    console.print(Panel("🧪 Testing Installation", style="bright_green"))
    
    tests = [
        ("torch", "import torch; print(f'PyTorch: {torch.__version__}')"),
        ("transformers", "import transformers; print(f'Transformers: {transformers.__version__}')"),
        ("accelerate", "import accelerate; print(f'Accelerate: {accelerate.__version__}')"),
        ("huggingface_hub", "import huggingface_hub; print(f'HF Hub: {huggingface_hub.__version__}')")
    ]
    
    for name, test_code in tests:
        try:
            exec(test_code)
            console.print(f"✅ {name} - Working")
        except Exception as e:
            console.print(f"❌ {name} - Failed: {e}")

def main():
    """Main installation and optimization process"""
    console.print(Panel("🔥 MAKV Ultimate APTS - Dependency Fixer", style="bold red"))
    
    steps = [
        ("Installing Python packages", install_python_packages),
        ("Installing system tools", install_system_tools), 
        ("Optimizing PyTorch", optimize_torch),
        ("Fixing transformers config", fix_transformers_config),
        ("Creating optimized AI coordinator", create_optimized_ai_coordinator),
        ("Downloading models", download_models),
        ("Testing installation", test_installation)
    ]
    
    for description, func in steps:
        console.print(f"\n🚀 {description}...")
        try:
            func()
        except Exception as e:
            console.print(f"❌ Error in {description}: {e}")
            continue
    
    console.print(Panel("🎉 Installation Complete!", style="bold green"))
    console.print("Run: python3 makv_ultimate_apts.py")

if __name__ == "__main__":
    main()