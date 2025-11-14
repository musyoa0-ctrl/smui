# 🔄 Update Existing SMUI Repository and Run

## 📥 Since you already have the smui directory, use these commands:

### **Option 1: Update Existing Repository (Recommended)**
```bash
cd smui
git fetch origin
git checkout feature/apts-nation-state-penetration-framework
git pull origin feature/apts-nation-state-penetration-framework
python3 ultimate_system_fixer.py
python3 start_makv_apts.py
```

### **Option 2: Fresh Clone (Remove old directory first)**
```bash
rm -rf smui
git clone https://github.com/musyoa0-ctrl/smui.git
cd smui
git checkout feature/apts-nation-state-penetration-framework
python3 ultimate_system_fixer.py
python3 start_makv_apts.py
```

### **Option 3: One-Line Update and Run**
```bash
cd smui && git fetch origin && git checkout feature/apts-nation-state-penetration-framework && git pull origin feature/apts-nation-state-penetration-framework && python3 ultimate_system_fixer.py && python3 start_makv_apts.py
```

## 🚀 Quick Commands for Your Situation

Since you already have the `smui` directory, run this:

```bash
cd smui && git pull origin feature/apts-nation-state-penetration-framework && python3 ultimate_system_fixer.py && python3 start_makv_apts.py
```

Or if you want to be extra sure everything is updated:

```bash
cd smui && git fetch origin && git reset --hard origin/feature/apts-nation-state-penetration-framework && python3 ultimate_system_fixer.py && python3 start_makv_apts.py
```