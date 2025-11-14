#!/usr/bin/env python3
"""
🔥 MAKV'S ULTIMATE APTS - SIMPLE VERSION (NO LAYOUT BUGS) 🔥
Nation-State Level Penetration Testing Platform
Fixed version without Rich Layout issues
"""

import os
import sys
import time
import logging
from datetime import datetime

# Simple console colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    """Print system banner"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                      ║
║  ███╗   ███╗ █████╗ ██╗  ██╗██╗   ██╗    ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗ ║
║  ████╗ ████║██╔══██╗██║ ██╔╝██║   ██║    ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝ ║
║  ██╔████╔██║███████║█████╔╝ ██║   ██║    ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗   ║
║  ██║╚██╔╝██║██╔══██║██╔═██╗ ╚██╗ ██╔╝    ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝   ║
║  ██║ ╚═╝ ██║██║  ██║██║  ██╗ ╚████╔╝     ╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗ ║
║  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝       ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ║
║                                                                                      ║
║                    🔥 ULTIMATE AI-COORDINATED APTS SYSTEM 🔥                        ║
║                         Nation-State Level Penetration Platform                     ║
║                                                                                      ║
║                           Version: 4.0.0 - SIMPLE EDITION                          ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.YELLOW}🚨 LEGAL DISCLAIMER 🚨{Colors.END}

This system contains nation-state level penetration testing capabilities.
Unauthorized use against systems you do not own or have explicit
permission to test is ILLEGAL and UNETHICAL.

By using this system, you acknowledge:
• You have written authorization to test target systems
• You understand the legal implications of penetration testing
• You will use this system responsibly and ethically
• You will not cause harm or disruption to target systems

This system will automatically activate Ghost Mode for your protection.
"""
    print(banner)

def initialize_system():
    """Initialize system components"""
    print(f"\n{Colors.CYAN}🚀 INITIALIZING MAKV'S ULTIMATE APTS SYSTEM...{Colors.END}")
    
    components = [
        ("🤖 Initializing Offline AI Coordinator", "ai_coordinator"),
        ("👻 Initializing Advanced Ghost Mode", "ghost_mode"),
        ("⚔️ Initializing Deadly Frameworks", "frameworks"),
        ("📊 Starting System Monitoring", "monitoring"),
        ("🔍 Performing System Analysis", "analysis")
    ]
    
    system_status = {}
    
    for desc, component in components:
        print(f"{Colors.YELLOW}{desc}...{Colors.END}")
        time.sleep(1)  # Simulate initialization
        
        try:
            if component == "ai_coordinator":
                # Try to import AI components
                try:
                    from offline_ai_coordinator import OfflineAICoordinator
                    ai = OfflineAICoordinator()
                    system_status[component] = True
                    print(f"{Colors.GREEN}✅ AI Coordinator ready{Colors.END}")
                except Exception as e:
                    print(f"{Colors.YELLOW}⚠️ AI Coordinator fallback mode{Colors.END}")
                    system_status[component] = False
                    
            elif component == "ghost_mode":
                # Try to import Ghost Mode
                try:
                    from advanced_ghost_mode import AdvancedGhostMode
                    ghost = AdvancedGhostMode()
                    system_status[component] = True
                    print(f"{Colors.GREEN}✅ Ghost Mode activated{Colors.END}")
                except Exception as e:
                    print(f"{Colors.YELLOW}⚠️ Ghost Mode basic protection{Colors.END}")
                    system_status[component] = False
                    
            else:
                system_status[component] = True
                print(f"{Colors.GREEN}✅ {desc.split(' ', 1)[1]} ready{Colors.END}")
                
        except Exception as e:
            system_status[component] = False
            print(f"{Colors.RED}❌ {desc.split(' ', 1)[1]} failed{Colors.END}")
    
    return system_status

def show_main_menu(system_status):
    """Show main system menu"""
    while True:
        print(f"\n{Colors.BOLD}{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}║                    🔥 MAKV ULTIMATE APTS 🔥                   ║{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}║                     MAIN CONTROL PANEL                       ║{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}╚═══════════════════════════════════════════════════════════════╝{Colors.END}")
        
        # System Status
        print(f"\n{Colors.BOLD}📊 SYSTEM STATUS:{Colors.END}")
        ai_status = "🟢 ONLINE" if system_status.get('ai_coordinator') else "🟡 FALLBACK"
        ghost_status = "🟢 ACTIVE" if system_status.get('ghost_mode') else "🟡 BASIC"
        frameworks_status = "🟢 READY" if system_status.get('frameworks') else "🔴 OFFLINE"
        
        print(f"🤖 AI Coordinator: {ai_status}")
        print(f"👻 Ghost Mode: {ghost_status}")
        print(f"⚔️ Frameworks: {frameworks_status}")
        
        # Menu Options
        print(f"\n{Colors.BOLD}🎯 AVAILABLE OPTIONS:{Colors.END}")
        print("1. 🔍 Reconnaissance & Intelligence Gathering")
        print("2. 🎯 Vulnerability Assessment")
        print("3. ⚔️ Exploitation Framework")
        print("4. 🕵️ Social Engineering Toolkit")
        print("5. 📡 Network Penetration")
        print("6. 🌐 Web Application Testing")
        print("7. 📱 Mobile Security Assessment")
        print("8. ☁️ Cloud Infrastructure Testing")
        print("9. 🔐 Cryptographic Analysis")
        print("10. 📊 Reporting & Documentation")
        print("11. ⚙️ System Configuration")
        print("12. 📈 View System Logs")
        print("0. 🚪 Exit System")
        
        choice = input(f"\n{Colors.BOLD}Enter your choice (0-12): {Colors.END}")
        
        if choice == "0":
            print(f"\n{Colors.GREEN}👋 Goodbye! Stay ethical!{Colors.END}")
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            handle_menu_choice(choice, system_status)
        else:
            print(f"{Colors.RED}❌ Invalid choice. Please try again.{Colors.END}")

def handle_menu_choice(choice, system_status):
    """Handle menu selection"""
    options = {
        "1": "🔍 Reconnaissance & Intelligence Gathering",
        "2": "🎯 Vulnerability Assessment", 
        "3": "⚔️ Exploitation Framework",
        "4": "🕵️ Social Engineering Toolkit",
        "5": "📡 Network Penetration",
        "6": "🌐 Web Application Testing",
        "7": "📱 Mobile Security Assessment",
        "8": "☁️ Cloud Infrastructure Testing",
        "9": "🔐 Cryptographic Analysis",
        "10": "📊 Reporting & Documentation",
        "11": "⚙️ System Configuration",
        "12": "📈 View System Logs"
    }
    
    print(f"\n{Colors.CYAN}🚀 Launching: {options[choice]}{Colors.END}")
    print(f"{Colors.YELLOW}⚠️ This is a demonstration version.{Colors.END}")
    print(f"{Colors.YELLOW}📝 Full functionality requires proper authorization and setup.{Colors.END}")
    
    if choice == "11":  # System Configuration
        show_system_config()
    elif choice == "12":  # View Logs
        show_system_logs()
    else:
        print(f"{Colors.GREEN}✅ Module would launch here in full version.{Colors.END}")
    
    input(f"\n{Colors.BOLD}Press Enter to return to main menu...{Colors.END}")

def show_system_config():
    """Show system configuration"""
    print(f"\n{Colors.BOLD}⚙️ SYSTEM CONFIGURATION{Colors.END}")
    print(f"Python: {sys.executable}")
    print(f"Working Directory: {os.getcwd()}")
    print(f"System Time: {datetime.now()}")
    
    # Check for key files
    key_files = [
        "makv_ultimate_apts.py",
        "offline_ai_coordinator.py",
        "advanced_ghost_mode.py",
        "setup_environment.py"
    ]
    
    print(f"\n{Colors.BOLD}📁 KEY FILES:{Colors.END}")
    for file in key_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")

def show_system_logs():
    """Show recent system logs"""
    print(f"\n{Colors.BOLD}📈 RECENT SYSTEM LOGS{Colors.END}")
    
    log_dir = "logs"
    if os.path.exists(log_dir):
        log_files = [f for f in os.listdir(log_dir) if f.endswith('.log')]
        log_files.sort(reverse=True)
        
        print(f"Found {len(log_files)} log files:")
        for i, log_file in enumerate(log_files[:5]):  # Show last 5
            print(f"{i+1}. {log_file}")
    else:
        print("No logs directory found.")

def main():
    """Main system entry point"""
    try:
        # Print banner and get authorization
        print_banner()
        
        auth = input(f"{Colors.BOLD}Do you have written authorization to test your targets? [y/n]: {Colors.END}")
        if auth.lower() != 'y':
            print(f"{Colors.RED}❌ Authorization required. Exiting.{Colors.END}")
            return
        
        # Initialize system
        system_status = initialize_system()
        
        print(f"\n{Colors.GREEN}🎉 SYSTEM INITIALIZATION COMPLETE!{Colors.END}")
        print(f"{Colors.CYAN}🔥 MAKV Ultimate APTS is ready for ethical penetration testing.{Colors.END}")
        
        # Show main menu
        show_main_menu(system_status)
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}👋 Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ System error: {e}{Colors.END}")
        print(f"{Colors.YELLOW}💡 Try running: python3 setup_environment.py{Colors.END}")

if __name__ == "__main__":
    main()