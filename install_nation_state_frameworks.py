#!/usr/bin/env python3
"""
NATION-STATE LEVEL FRAMEWORK INSTALLER
Installs complete penetration testing frameworks used by military and government agencies

This installer downloads and configures the same frameworks used by:
- NSA, FBI, CIA (United States)
- GCHQ (United Kingdom) 
- Unit 8200 (Israel)
- APT groups (China, Russia, North Korea)
- Military cyber warfare units worldwide

Author: Built for Makv's APTS System
Classification: AUTHORIZED USE ONLY
"""

import os
import subprocess
import sys
import time
import logging
from typing import Dict, List, Tuple
import threading
import concurrent.futures

class NationStateFrameworkInstaller:
    """
    Installer for complete nation-state level penetration testing frameworks
    """
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.installed_frameworks = {}
        
        # Complete Nation-State Level Frameworks
        self.frameworks = {
            'metasploit': {
                'name': 'Metasploit Framework',
                'description': 'World\'s most advanced exploitation framework - Used by NSA, FBI',
                'category': 'exploitation',
                'priority': 10,
                'install_commands': [
                    'curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb | sudo bash',
                    'sudo apt update && sudo apt install metasploit-framework -y'
                ],
                'verify_command': 'msfconsole --version',
                'post_install': [
                    'sudo msfdb init',
                    'sudo systemctl enable postgresql',
                    'sudo systemctl start postgresql'
                ]
            },
            'empire': {
                'name': 'PowerShell Empire',
                'description': 'Post-exploitation framework - Used by APT groups and red teams',
                'category': 'post_exploitation',
                'priority': 9,
                'install_commands': [
                    'git clone --recursive https://github.com/EmpireProject/Empire.git /opt/Empire',
                    'cd /opt/Empire && sudo ./setup/install.sh',
                    'sudo pip3 install -r /opt/Empire/requirements.txt'
                ],
                'verify_command': 'python3 /opt/Empire/empire --help',
                'post_install': []
            },
            'cobalt_strike': {
                'name': 'Cobalt Strike',
                'description': 'Advanced threat emulation platform - Used by military and APT groups',
                'category': 'c2_framework',
                'priority': 10,
                'install_commands': [
                    'echo "Cobalt Strike requires commercial license from Fortra"',
                    'echo "Download from: https://www.cobaltstrike.com/"',
                    'echo "Price: $3,500 per user per year"'
                ],
                'verify_command': 'echo "Commercial license required"',
                'post_install': []
            },
            'caldera': {
                'name': 'MITRE CALDERA',
                'description': 'Automated adversary emulation platform - Developed by MITRE for government',
                'category': 'adversary_emulation',
                'priority': 9,
                'install_commands': [
                    'git clone https://github.com/mitre/caldera.git --recursive /opt/caldera',
                    'cd /opt/caldera && pip3 install -r requirements.txt',
                    'cd /opt/caldera && python3 server.py --insecure --build'
                ],
                'verify_command': 'python3 /opt/caldera/server.py --help',
                'post_install': []
            },
            'atomic_red_team': {
                'name': 'Atomic Red Team',
                'description': 'MITRE ATT&CK technique testing - Used by government security teams',
                'category': 'technique_testing',
                'priority': 8,
                'install_commands': [
                    'git clone https://github.com/redcanaryco/atomic-red-team.git /opt/atomic-red-team',
                    'powershell -Command "IEX (IWR \'https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1\' -UseBasicParsing); Install-AtomicRedTeam -getAtomics"'
                ],
                'verify_command': 'ls /opt/atomic-red-team',
                'post_install': []
            },
            'beef': {
                'name': 'Browser Exploitation Framework (BeEF)',
                'description': 'Browser exploitation platform - Used for client-side attacks',
                'category': 'browser_exploitation',
                'priority': 7,
                'install_commands': [
                    'git clone https://github.com/beefproject/beef /opt/beef',
                    'cd /opt/beef && bundle install',
                    'cd /opt/beef && sudo gem install bundler'
                ],
                'verify_command': 'ruby /opt/beef/beef --help',
                'post_install': []
            },
            'set': {
                'name': 'Social Engineer Toolkit (SET)',
                'description': 'Social engineering framework - Used by penetration testers worldwide',
                'category': 'social_engineering',
                'priority': 8,
                'install_commands': [
                    'git clone https://github.com/trustedsec/social-engineer-toolkit/ /opt/setoolkit',
                    'cd /opt/setoolkit && pip3 install -r requirements.txt',
                    'cd /opt/setoolkit && python3 setup.py install'
                ],
                'verify_command': 'python3 /opt/setoolkit/setoolkit --help',
                'post_install': []
            },
            'burp_suite': {
                'name': 'Burp Suite Professional',
                'description': 'Advanced web application security testing - Industry standard',
                'category': 'web_application_testing',
                'priority': 9,
                'install_commands': [
                    'wget -O /tmp/burpsuite_pro.jar "https://portswigger.net/burp/releases/download?product=pro&type=jar"',
                    'sudo mkdir -p /opt/burpsuite',
                    'sudo mv /tmp/burpsuite_pro.jar /opt/burpsuite/',
                    'echo "Commercial license required - $399/year"'
                ],
                'verify_command': 'java -jar /opt/burpsuite/burpsuite_pro.jar --help',
                'post_install': []
            },
            'nessus': {
                'name': 'Nessus Professional',
                'description': 'Vulnerability scanner - Used by government and enterprises',
                'category': 'vulnerability_assessment',
                'priority': 8,
                'install_commands': [
                    'wget -O /tmp/Nessus-latest-ubuntu1404_amd64.deb "https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/latest/Nessus-latest-ubuntu1404_amd64.deb"',
                    'sudo dpkg -i /tmp/Nessus-latest-ubuntu1404_amd64.deb',
                    'sudo systemctl enable nessusd',
                    'echo "Commercial license required - $3,990/year"'
                ],
                'verify_command': 'sudo systemctl status nessusd',
                'post_install': []
            },
            'openvas': {
                'name': 'OpenVAS',
                'description': 'Open source vulnerability scanner - Free alternative to Nessus',
                'category': 'vulnerability_management',
                'priority': 7,
                'install_commands': [
                    'sudo apt update',
                    'sudo apt install openvas -y',
                    'sudo gvm-setup',
                    'sudo gvm-start'
                ],
                'verify_command': 'sudo gvm-check-setup',
                'post_install': []
            },
            'mythic': {
                'name': 'Mythic C2 Framework',
                'description': 'Modern command and control framework - Used by red teams',
                'category': 'c2_framework',
                'priority': 9,
                'install_commands': [
                    'git clone https://github.com/its-a-feature/Mythic /opt/Mythic',
                    'cd /opt/Mythic && sudo ./install_docker_ubuntu.sh',
                    'cd /opt/Mythic && sudo make'
                ],
                'verify_command': 'docker ps | grep mythic',
                'post_install': []
            },
            'nuclei': {
                'name': 'Nuclei Scanner',
                'description': 'Fast vulnerability scanner with 4000+ templates',
                'category': 'vulnerability_scanner',
                'priority': 8,
                'install_commands': [
                    'GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest',
                    'nuclei -update-templates'
                ],
                'verify_command': 'nuclei --version',
                'post_install': []
            },
            'bloodhound': {
                'name': 'BloodHound',
                'description': 'Active Directory attack path analysis - Used for AD penetration',
                'category': 'active_directory',
                'priority': 8,
                'install_commands': [
                    'wget -O /tmp/BloodHound-linux-x64.zip https://github.com/BloodHoundAD/BloodHound/releases/latest/download/BloodHound-linux-x64.zip',
                    'sudo unzip /tmp/BloodHound-linux-x64.zip -d /opt/',
                    'sudo chmod +x /opt/BloodHound-linux-x64/BloodHound'
                ],
                'verify_command': '/opt/BloodHound-linux-x64/BloodHound --version',
                'post_install': []
            },
            'covenant': {
                'name': 'Covenant C2',
                'description': '.NET command and control framework - Used by advanced red teams',
                'category': 'c2_framework',
                'priority': 8,
                'install_commands': [
                    'git clone --recurse-submodules https://github.com/cobbr/Covenant /opt/Covenant',
                    'cd /opt/Covenant/Covenant && dotnet build',
                    'cd /opt/Covenant/Covenant && dotnet run'
                ],
                'verify_command': 'dotnet --version',
                'post_install': []
            },
            'sliver': {
                'name': 'Sliver C2',
                'description': 'Modern adversary emulation framework - Open source alternative to Cobalt Strike',
                'category': 'c2_framework',
                'priority': 9,
                'install_commands': [
                    'curl https://sliver.sh/install | sudo bash',
                    'sliver-server'
                ],
                'verify_command': 'sliver --version',
                'post_install': []
            },
            'havoc': {
                'name': 'Havoc C2',
                'description': 'Modern command and control framework - Used by red teams',
                'category': 'c2_framework',
                'priority': 8,
                'install_commands': [
                    'git clone https://github.com/HavocFramework/Havoc.git /opt/Havoc',
                    'cd /opt/Havoc && make',
                    'cd /opt/Havoc && sudo make install'
                ],
                'verify_command': '/opt/Havoc/havoc --version',
                'post_install': []
            }
        }
        
        self.logger.info(f"🚀 NATION-STATE FRAMEWORK INSTALLER INITIALIZED")
        self.logger.info(f"📊 {len(self.frameworks)} Military-Grade Frameworks Available")
    
    def _setup_logging(self):
        """Setup logging system"""
        logger = logging.getLogger('FrameworkInstaller')
        logger.setLevel(logging.INFO)
        
        # Create logs directory
        os.makedirs('logs', exist_ok=True)
        
        # File handler
        fh = logging.FileHandler(f'logs/framework_installer_{int(time.time())}.log')
        fh.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        logger.addHandler(fh)
        logger.addHandler(ch)
        
        return logger
    
    def install_prerequisites(self) -> bool:
        """Install system prerequisites for all frameworks"""
        self.logger.info("🔧 Installing system prerequisites...")
        
        prerequisites = [
            'sudo apt update',
            'sudo apt install -y git curl wget python3 python3-pip ruby golang-go',
            'sudo apt install -y build-essential libssl-dev libffi-dev python3-dev',
            'sudo apt install -y postgresql postgresql-contrib',
            'sudo apt install -y docker.io docker-compose',
            'sudo apt install -y openjdk-11-jdk',
            'sudo apt install -y powershell',
            'sudo usermod -aG docker $USER'
        ]
        
        for cmd in prerequisites:
            try:
                self.logger.info(f"Executing: {cmd}")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode != 0:
                    self.logger.warning(f"Command failed: {cmd}")
                    self.logger.warning(f"Error: {result.stderr}")
            except Exception as e:
                self.logger.error(f"Failed to execute {cmd}: {str(e)}")
                return False
        
        self.logger.info("✅ Prerequisites installation completed")
        return True
    
    def install_framework(self, framework_name: str) -> Tuple[bool, str]:
        """Install a specific framework"""
        if framework_name not in self.frameworks:
            return False, f"Framework {framework_name} not found"
        
        framework = self.frameworks[framework_name]
        self.logger.info(f"🚀 Installing {framework['name']}...")
        self.logger.info(f"📝 Description: {framework['description']}")
        
        # Execute installation commands
        for cmd in framework['install_commands']:
            try:
                self.logger.info(f"Executing: {cmd}")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
                
                if result.returncode != 0:
                    self.logger.error(f"Command failed: {cmd}")
                    self.logger.error(f"Error: {result.stderr}")
                    return False, f"Installation command failed: {cmd}"
                
                if result.stdout:
                    self.logger.info(f"Output: {result.stdout[:200]}...")
                    
            except subprocess.TimeoutExpired:
                self.logger.error(f"Command timed out: {cmd}")
                return False, f"Installation timed out: {cmd}"
            except Exception as e:
                self.logger.error(f"Failed to execute {cmd}: {str(e)}")
                return False, f"Exception during installation: {str(e)}"
        
        # Execute post-installation commands
        for cmd in framework['post_install']:
            try:
                self.logger.info(f"Post-install: {cmd}")
                subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
            except Exception as e:
                self.logger.warning(f"Post-install command failed: {cmd} - {str(e)}")
        
        # Verify installation
        try:
            verify_result = subprocess.run(
                framework['verify_command'], 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            
            if verify_result.returncode == 0:
                self.logger.info(f"✅ {framework['name']} installed successfully")
                self.installed_frameworks[framework_name] = True
                return True, f"{framework['name']} installed successfully"
            else:
                self.logger.warning(f"⚠️ {framework['name']} installation may have issues")
                self.installed_frameworks[framework_name] = False
                return False, f"Verification failed for {framework['name']}"
                
        except Exception as e:
            self.logger.warning(f"⚠️ Could not verify {framework['name']}: {str(e)}")
            self.installed_frameworks[framework_name] = False
            return False, f"Verification error: {str(e)}"
    
    def install_all_frameworks(self) -> Dict[str, Tuple[bool, str]]:
        """Install all frameworks with parallel processing"""
        self.logger.info("🚀 STARTING MASS INSTALLATION OF NATION-STATE FRAMEWORKS")
        
        # Install prerequisites first
        if not self.install_prerequisites():
            self.logger.error("❌ Failed to install prerequisites")
            return {}
        
        results = {}
        
        # Sort frameworks by priority (highest first)
        sorted_frameworks = sorted(
            self.frameworks.items(), 
            key=lambda x: x[1]['priority'], 
            reverse=True
        )
        
        # Install high-priority frameworks first (sequential)
        high_priority = [f for f, info in sorted_frameworks if info['priority'] >= 9]
        
        self.logger.info(f"🎯 Installing {len(high_priority)} high-priority frameworks first...")
        for framework_name, _ in high_priority:
            success, message = self.install_framework(framework_name)
            results[framework_name] = (success, message)
            time.sleep(2)  # Brief pause between installations
        
        # Install remaining frameworks in parallel
        remaining_frameworks = [f for f, info in sorted_frameworks if info['priority'] < 9]
        
        if remaining_frameworks:
            self.logger.info(f"⚡ Installing {len(remaining_frameworks)} remaining frameworks in parallel...")
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                future_to_framework = {
                    executor.submit(self.install_framework, framework_name): framework_name 
                    for framework_name, _ in remaining_frameworks
                }
                
                for future in concurrent.futures.as_completed(future_to_framework):
                    framework_name = future_to_framework[future]
                    try:
                        success, message = future.result()
                        results[framework_name] = (success, message)
                    except Exception as e:
                        results[framework_name] = (False, f"Exception: {str(e)}")
        
        # Generate installation report
        self._generate_installation_report(results)
        
        return results
    
    def _generate_installation_report(self, results: Dict[str, Tuple[bool, str]]):
        """Generate installation report"""
        successful = sum(1 for success, _ in results.values() if success)
        total = len(results)
        
        self.logger.info("📊 INSTALLATION REPORT")
        self.logger.info(f"✅ Successful: {successful}/{total}")
        self.logger.info(f"❌ Failed: {total - successful}/{total}")
        
        # List successful installations
        self.logger.info("\n✅ SUCCESSFULLY INSTALLED FRAMEWORKS:")
        for framework, (success, message) in results.items():
            if success:
                framework_info = self.frameworks[framework]
                self.logger.info(f"  • {framework_info['name']} - {framework_info['category']}")
        
        # List failed installations
        if total - successful > 0:
            self.logger.info("\n❌ FAILED INSTALLATIONS:")
            for framework, (success, message) in results.items():
                if not success:
                    framework_info = self.frameworks[framework]
                    self.logger.info(f"  • {framework_info['name']} - {message}")
        
        # Save detailed report
        report_file = f"reports/framework_installation_{int(time.time())}.json"
        os.makedirs('reports', exist_ok=True)
        
        detailed_report = {
            'timestamp': time.time(),
            'total_frameworks': total,
            'successful_installations': successful,
            'failed_installations': total - successful,
            'results': {
                framework: {
                    'name': self.frameworks[framework]['name'],
                    'category': self.frameworks[framework]['category'],
                    'success': success,
                    'message': message
                }
                for framework, (success, message) in results.items()
            }
        }
        
        with open(report_file, 'w') as f:
            import json
            json.dump(detailed_report, f, indent=2)
        
        self.logger.info(f"📄 Detailed report saved: {report_file}")
    
    def get_framework_info(self, framework_name: str) -> Dict:
        """Get detailed information about a framework"""
        if framework_name not in self.frameworks:
            return {}
        
        framework = self.frameworks[framework_name]
        return {
            'name': framework['name'],
            'description': framework['description'],
            'category': framework['category'],
            'priority': framework['priority'],
            'install_commands': framework['install_commands'],
            'verify_command': framework['verify_command'],
            'installed': self.installed_frameworks.get(framework_name, False)
        }
    
    def list_frameworks_by_category(self) -> Dict[str, List[str]]:
        """List frameworks organized by category"""
        categories = {}
        
        for framework_name, framework_info in self.frameworks.items():
            category = framework_info['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(framework_name)
        
        return categories
    
    def get_installation_status(self) -> Dict[str, Any]:
        """Get current installation status"""
        return {
            'total_frameworks': len(self.frameworks),
            'installed_frameworks': len([f for f in self.installed_frameworks.values() if f]),
            'failed_frameworks': len([f for f in self.installed_frameworks.values() if not f]),
            'not_attempted': len(self.frameworks) - len(self.installed_frameworks),
            'frameworks': self.installed_frameworks
        }

def main():
    """Main function for framework installation"""
    installer = NationStateFrameworkInstaller()
    
    print("🚀 NATION-STATE LEVEL FRAMEWORK INSTALLER")
    print("=" * 60)
    print("This installer will download and configure the same frameworks")
    print("used by military and government cyber warfare units worldwide.")
    print("=" * 60)
    
    choice = input("\nInstall all frameworks? (y/n): ").lower().strip()
    
    if choice == 'y':
        print("\n🚀 Starting mass installation...")
        results = installer.install_all_frameworks()
        
        successful = sum(1 for success, _ in results.values() if success)
        total = len(results)
        
        print(f"\n🎉 INSTALLATION COMPLETE!")
        print(f"✅ Successfully installed: {successful}/{total} frameworks")
        
        if successful < total:
            print(f"❌ Failed installations: {total - successful}")
            print("Check logs for detailed error information.")
    
    else:
        print("Installation cancelled.")

if __name__ == "__main__":
    main()