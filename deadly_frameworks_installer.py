#!/usr/bin/env python3
"""
MAKV'S DEADLY FRAMEWORKS INSTALLER
Advanced Nation-State Level Penetration Testing Frameworks

This installer deploys the most advanced and deadly penetration testing
frameworks used by nation-state actors, APT groups, and professional
red teams worldwide.

CLASSIFICATION: AUTHORIZED USE ONLY
VERSION: 3.0.0 - DEADLY ARSENAL

Author: Built for Makv
License: Authorized Use Only
"""

import asyncio
import json
import time
import os
import sys
import logging
import subprocess
import shutil
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import platform

class DeadlyFrameworksInstaller:
    """
    Installer for the most advanced penetration testing frameworks
    """
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.install_dir = Path.home() / "makv_deadly_frameworks"
        self.install_dir.mkdir(exist_ok=True)
        
        # The most deadly frameworks used by nation-state actors
        self.deadly_frameworks = {
            # TIER 1: NATION-STATE C2 FRAMEWORKS
            'sliver': {
                'name': 'Sliver C2 Framework',
                'category': 'c2_framework',
                'tier': 1,
                'lethality': 10,
                'description': 'Modern Go-based C2 framework with advanced evasion capabilities',
                'used_by': ['NSA', 'APT groups', 'Professional red teams'],
                'capabilities': [
                    'Cross-platform implants (Windows/Linux/macOS)',
                    'HTTP(S)/DNS/mTLS/WireGuard communication',
                    'In-memory execution and process injection',
                    'Advanced evasion techniques',
                    'Multiplayer teamserver support',
                    'Extensible with custom modules'
                ],
                'install_method': 'binary_download',
                'install_url': 'https://github.com/BishopFox/sliver/releases/latest/download/sliver-server_linux',
                'post_install': ['chmod +x sliver-server_linux', './sliver-server_linux daemon'],
                'stealth_level': 10,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            'havoc': {
                'name': 'Havoc C2 Framework',
                'category': 'c2_framework',
                'tier': 1,
                'lethality': 10,
                'description': 'Advanced multi-platform C2 framework with modern architecture',
                'used_by': ['APT groups', 'Nation-state actors', 'Advanced red teams'],
                'capabilities': [
                    'Modern teamserver with web UI',
                    'Cross-platform demon agents',
                    'Advanced post-exploitation modules',
                    'OPSEC-safe operations',
                    'Custom payload generation',
                    'Sophisticated evasion techniques'
                ],
                'install_method': 'git_build',
                'install_url': 'https://github.com/HavocFramework/Havoc.git',
                'build_commands': [
                    'cd client && make',
                    'cd ../teamserver && go build .',
                    'cd ../payloads && make'
                ],
                'stealth_level': 10,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            'mythic': {
                'name': 'Mythic C2 Framework',
                'category': 'c2_framework',
                'tier': 1,
                'lethality': 9,
                'description': 'Cross-platform, post-exploitation framework with containerized architecture',
                'used_by': ['Red teams', 'APT simulation', 'Advanced penetration testers'],
                'capabilities': [
                    'Containerized agent management',
                    'Web-based interface',
                    'Cross-platform payload support',
                    'Advanced logging and reporting',
                    'Collaborative operations',
                    'Extensive payload library'
                ],
                'install_method': 'docker_compose',
                'install_url': 'https://github.com/its-a-feature/Mythic.git',
                'build_commands': [
                    'sudo ./install_docker_ubuntu.sh',
                    'make'
                ],
                'stealth_level': 9,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            'covenant': {
                'name': 'Covenant C2 Framework',
                'category': 'c2_framework',
                'tier': 1,
                'lethality': 8,
                'description': '.NET-based C2 framework for Windows-focused operations',
                'used_by': ['Windows-focused red teams', 'APT groups', 'Nation-state actors'],
                'capabilities': [
                    '.NET-based grunt implants',
                    'PowerShell and C# task execution',
                    'Advanced Windows post-exploitation',
                    'AMSI and ETW bypass',
                    'Process injection techniques',
                    'Collaborative interface'
                ],
                'install_method': 'dotnet_build',
                'install_url': 'https://github.com/cobbr/Covenant.git',
                'build_commands': [
                    'cd Covenant && dotnet build',
                    'cd ../Covenant.API && dotnet build'
                ],
                'stealth_level': 8,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            # TIER 2: ADVANCED EXPLOITATION FRAMEWORKS
            'metasploit_pro': {
                'name': 'Metasploit Framework (Enhanced)',
                'category': 'exploitation',
                'tier': 2,
                'lethality': 9,
                'description': 'World\'s most advanced exploitation framework with custom modules',
                'used_by': ['All nation-state actors', 'Professional penetration testers'],
                'capabilities': [
                    '2000+ exploits and payloads',
                    'Advanced post-exploitation',
                    'Custom payload generation',
                    'Evasion modules',
                    'Database integration',
                    'Automated exploitation'
                ],
                'install_method': 'package_manager',
                'install_commands': [
                    'curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall',
                    'chmod 755 msfinstall',
                    './msfinstall'
                ],
                'stealth_level': 7,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            'empire': {
                'name': 'PowerShell Empire',
                'category': 'post_exploitation',
                'tier': 2,
                'lethality': 9,
                'description': 'PowerShell-based post-exploitation framework',
                'used_by': ['APT groups', 'Nation-state actors', 'Advanced red teams'],
                'capabilities': [
                    'PowerShell-based agents',
                    'Advanced persistence techniques',
                    'Credential harvesting',
                    'Lateral movement modules',
                    'Evasion techniques',
                    'Collaborative operations'
                ],
                'install_method': 'git_install',
                'install_url': 'https://github.com/BC-SECURITY/Empire.git',
                'install_commands': [
                    'sudo ./setup/install.sh',
                    'sudo ./setup/reset.sh'
                ],
                'stealth_level': 8,
                'firewall_bypass': True,
                'av_evasion': True
            },
            
            # TIER 3: ADVANCED EVASION AND PAYLOAD GENERATION
            'veil': {
                'name': 'Veil Framework',
                'category': 'evasion',
                'tier': 3,
                'lethality': 8,
                'description': 'Advanced payload generation and AV evasion framework',
                'used_by': ['Red teams', 'APT groups', 'Penetration testers'],
                'capabilities': [
                    'Advanced AV evasion techniques',
                    'Multiple payload formats',
                    'Encoding and obfuscation',
                    'Custom payload generation',
                    'Signature evasion',
                    'Multi-stage payloads'
                ],
                'install_method': 'git_install',
                'install_url': 'https://github.com/Veil-Framework/Veil.git',
                'install_commands': [
                    './config/setup.sh --force --silent'
                ],
                'stealth_level': 9,
                'firewall_bypass': False,
                'av_evasion': True
            },
            
            'thefatrat': {
                'name': 'TheFatRat',
                'category': 'payload_generation',
                'tier': 3,
                'lethality': 7,
                'description': 'Massive exploiting tool with advanced payload generation',
                'used_by': ['Red teams', 'Penetration testers', 'Security researchers'],
                'capabilities': [
                    'Cross-platform payload generation',
                    'Android APK backdoors',
                    'Windows executable backdoors',
                    'PowerShell backdoors',
                    'Persistence mechanisms',
                    'Social engineering payloads'
                ],
                'install_method': 'git_install',
                'install_url': 'https://github.com/screetsec/TheFatRat.git',
                'install_commands': [
                    'chmod +x setup.sh',
                    './setup.sh'
                ],
                'stealth_level': 6,
                'firewall_bypass': False,
                'av_evasion': True
            },
            
            # TIER 4: ADVANCED NETWORK TOOLS
            'chisel': {
                'name': 'Chisel Tunneling Tool',
                'category': 'tunneling',
                'tier': 4,
                'lethality': 8,
                'description': 'Fast TCP/UDP tunnel over HTTP for firewall bypass',
                'used_by': ['APT groups', 'Red teams', 'Nation-state actors'],
                'capabilities': [
                    'HTTP tunneling',
                    'SOCKS5 proxy',
                    'Reverse tunneling',
                    'Port forwarding',
                    'Firewall bypass',
                    'Encrypted communication'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install github.com/jpillora/chisel@latest'
                ],
                'stealth_level': 9,
                'firewall_bypass': True,
                'av_evasion': False
            },
            
            'ligolo': {
                'name': 'Ligolo-ng',
                'category': 'tunneling',
                'tier': 4,
                'lethality': 8,
                'description': 'Advanced tunneling tool for network pivoting',
                'used_by': ['Red teams', 'APT groups', 'Advanced penetration testers'],
                'capabilities': [
                    'Network pivoting',
                    'Multi-hop tunneling',
                    'TUN interface creation',
                    'Advanced routing',
                    'Encrypted tunnels',
                    'Cross-platform support'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install github.com/nicocha30/ligolo-ng/cmd/agent@latest',
                    'go install github.com/nicocha30/ligolo-ng/cmd/proxy@latest'
                ],
                'stealth_level': 9,
                'firewall_bypass': True,
                'av_evasion': False
            },
            
            # TIER 5: ADVANCED RECONNAISSANCE
            'amass': {
                'name': 'OWASP Amass',
                'category': 'reconnaissance',
                'tier': 5,
                'lethality': 7,
                'description': 'Advanced subdomain enumeration and network mapping',
                'used_by': ['All professional penetration testers', 'Bug bounty hunters'],
                'capabilities': [
                    'Advanced subdomain enumeration',
                    'DNS enumeration',
                    'Network mapping',
                    'ASN discovery',
                    'Certificate transparency',
                    'API integration'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install -v github.com/owasp-amass/amass/v4/...@master'
                ],
                'stealth_level': 8,
                'firewall_bypass': False,
                'av_evasion': False
            },
            
            'nuclei': {
                'name': 'Nuclei Scanner',
                'category': 'vulnerability_scanning',
                'tier': 5,
                'lethality': 8,
                'description': 'Fast vulnerability scanner with 4000+ templates',
                'used_by': ['Bug bounty hunters', 'Red teams', 'Security researchers'],
                'capabilities': [
                    '4000+ vulnerability templates',
                    'Custom template creation',
                    'Fast parallel scanning',
                    'Integration with other tools',
                    'Automated exploitation',
                    'Continuous monitoring'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest'
                ],
                'stealth_level': 6,
                'firewall_bypass': False,
                'av_evasion': False
            },
            
            # TIER 6: ADVANCED WEB APPLICATION TESTING
            'httpx': {
                'name': 'httpx',
                'category': 'web_testing',
                'tier': 6,
                'lethality': 7,
                'description': 'Fast and multi-purpose HTTP toolkit',
                'used_by': ['Bug bounty hunters', 'Web application testers'],
                'capabilities': [
                    'HTTP probing',
                    'Technology detection',
                    'Response analysis',
                    'Custom headers',
                    'Pipeline integration',
                    'Fast scanning'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest'
                ],
                'stealth_level': 7,
                'firewall_bypass': False,
                'av_evasion': False
            },
            
            'katana': {
                'name': 'Katana Web Crawler',
                'category': 'web_crawling',
                'tier': 6,
                'lethality': 6,
                'description': 'Next-generation crawling and spidering framework',
                'used_by': ['Web application testers', 'Bug bounty hunters'],
                'capabilities': [
                    'Advanced web crawling',
                    'JavaScript parsing',
                    'Endpoint discovery',
                    'Form analysis',
                    'Custom filters',
                    'Pipeline integration'
                ],
                'install_method': 'go_install',
                'install_commands': [
                    'go install github.com/projectdiscovery/katana/cmd/katana@latest'
                ],
                'stealth_level': 6,
                'firewall_bypass': False,
                'av_evasion': False
            },
            
            # TIER 7: ADVANCED SOCIAL ENGINEERING
            'set': {
                'name': 'Social Engineer Toolkit',
                'category': 'social_engineering',
                'tier': 7,
                'lethality': 8,
                'description': 'Advanced social engineering framework',
                'used_by': ['Red teams', 'Social engineering specialists'],
                'capabilities': [
                    'Spear-phishing campaigns',
                    'Website cloning',
                    'Credential harvesting',
                    'USB/DVD attacks',
                    'Wireless attacks',
                    'Mass mailer'
                ],
                'install_method': 'git_install',
                'install_url': 'https://github.com/trustedsec/social-engineer-toolkit.git',
                'install_commands': [
                    'python3 setup.py install'
                ],
                'stealth_level': 5,
                'firewall_bypass': False,
                'av_evasion': False
            },
            
            # TIER 8: ADVANCED PERSISTENCE AND BACKDOORS
            'pupy': {
                'name': 'Pupy RAT',
                'category': 'remote_access',
                'tier': 8,
                'lethality': 7,
                'description': 'Cross-platform RAT and post-exploitation tool',
                'used_by': ['APT groups', 'Advanced red teams'],
                'capabilities': [
                    'Cross-platform support',
                    'In-memory execution',
                    'File operations',
                    'Keylogging',
                    'Screenshot capture',
                    'Network pivoting'
                ],
                'install_method': 'git_install',
                'install_url': 'https://github.com/n1nj4sec/pupy.git',
                'install_commands': [
                    'git submodule init',
                    'git submodule update',
                    'pip3 install -r requirements.txt'
                ],
                'stealth_level': 6,
                'firewall_bypass': True,
                'av_evasion': True
            }
        }
        
        self.installation_status = {}
        self.failed_installations = []
    
    def _setup_logging(self):
        """Setup logging system"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | INSTALLER | %(message)s',
            handlers=[
                logging.FileHandler(log_dir / f"deadly_frameworks_{int(time.time())}.log"),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)
    
    async def install_all_frameworks(self):
        """Install all deadly frameworks"""
        self.logger.info("🔥 STARTING INSTALLATION OF DEADLY FRAMEWORKS...")
        self.logger.info(f"📊 Total frameworks to install: {len(self.deadly_frameworks)}")
        
        # Check system requirements
        await self._check_system_requirements()
        
        # Install prerequisites
        await self._install_prerequisites()
        
        # Install frameworks by tier (most deadly first)
        frameworks_by_tier = {}
        for name, info in self.deadly_frameworks.items():
            tier = info['tier']
            if tier not in frameworks_by_tier:
                frameworks_by_tier[tier] = []
            frameworks_by_tier[tier].append((name, info))
        
        # Install tier by tier
        for tier in sorted(frameworks_by_tier.keys()):
            self.logger.info(f"🎯 Installing TIER {tier} frameworks...")
            
            for framework_name, framework_info in frameworks_by_tier[tier]:
                try:
                    self.logger.info(f"⚔️ Installing {framework_info['name']}...")
                    success = await self._install_framework(framework_name, framework_info)
                    
                    if success:
                        self.installation_status[framework_name] = 'installed'
                        self.logger.info(f"✅ {framework_info['name']} installed successfully")
                    else:
                        self.installation_status[framework_name] = 'failed'
                        self.failed_installations.append(framework_name)
                        self.logger.error(f"❌ {framework_info['name']} installation failed")
                        
                except Exception as e:
                    self.installation_status[framework_name] = 'error'
                    self.failed_installations.append(framework_name)
                    self.logger.error(f"💥 {framework_info['name']} installation error: {e}")
                
                # Small delay between installations
                await asyncio.sleep(2)
        
        # Generate installation report
        await self._generate_installation_report()
        
        self.logger.info("🎉 DEADLY FRAMEWORKS INSTALLATION COMPLETE!")
        return self.installation_status
    
    async def _check_system_requirements(self):
        """Check system requirements"""
        self.logger.info("🔍 Checking system requirements...")
        
        # Check OS
        os_name = platform.system()
        if os_name not in ['Linux', 'Darwin']:
            self.logger.warning(f"⚠️ OS {os_name} may not be fully supported")
        
        # Check architecture
        arch = platform.machine()
        self.logger.info(f"🖥️ Architecture: {arch}")
        
        # Check available disk space
        disk_usage = shutil.disk_usage(self.install_dir)
        free_gb = disk_usage.free / (1024**3)
        
        if free_gb < 10:
            self.logger.warning(f"⚠️ Low disk space: {free_gb:.2f}GB available")
        else:
            self.logger.info(f"💾 Disk space: {free_gb:.2f}GB available")
        
        # Check internet connectivity
        try:
            response = requests.get('https://github.com', timeout=5)
            if response.status_code == 200:
                self.logger.info("🌐 Internet connectivity: OK")
            else:
                self.logger.warning("⚠️ Internet connectivity issues detected")
        except:
            self.logger.error("❌ No internet connectivity")
    
    async def _install_prerequisites(self):
        """Install system prerequisites"""
        self.logger.info("📦 Installing system prerequisites...")
        
        prerequisites = [
            'git', 'curl', 'wget', 'build-essential', 'python3-pip',
            'golang-go', 'docker.io', 'docker-compose', 'nodejs', 'npm'
        ]
        
        for prereq in prerequisites:
            try:
                # Check if already installed
                result = subprocess.run(['which', prereq], capture_output=True, text=True)
                if result.returncode == 0:
                    self.logger.info(f"✅ {prereq} already installed")
                    continue
                
                # Install prerequisite
                self.logger.info(f"📥 Installing {prereq}...")
                install_result = subprocess.run([
                    'sudo', 'apt-get', 'install', '-y', prereq
                ], capture_output=True, text=True, timeout=300)
                
                if install_result.returncode == 0:
                    self.logger.info(f"✅ {prereq} installed successfully")
                else:
                    self.logger.warning(f"⚠️ Failed to install {prereq}")
                    
            except subprocess.TimeoutExpired:
                self.logger.warning(f"⚠️ Installation of {prereq} timed out")
            except Exception as e:
                self.logger.warning(f"⚠️ Error installing {prereq}: {e}")
    
    async def _install_framework(self, name: str, info: Dict[str, Any]) -> bool:
        """Install a specific framework"""
        framework_dir = self.install_dir / name
        framework_dir.mkdir(exist_ok=True)
        
        try:
            install_method = info['install_method']
            
            if install_method == 'git_install' or install_method == 'git_build':
                return await self._install_git_framework(name, info, framework_dir)
            elif install_method == 'binary_download':
                return await self._install_binary_framework(name, info, framework_dir)
            elif install_method == 'go_install':
                return await self._install_go_framework(name, info)
            elif install_method == 'package_manager':
                return await self._install_package_framework(name, info)
            elif install_method == 'docker_compose':
                return await self._install_docker_framework(name, info, framework_dir)
            elif install_method == 'dotnet_build':
                return await self._install_dotnet_framework(name, info, framework_dir)
            else:
                self.logger.error(f"Unknown install method: {install_method}")
                return False
                
        except Exception as e:
            self.logger.error(f"Framework installation error: {e}")
            return False
    
    async def _install_git_framework(self, name: str, info: Dict[str, Any], framework_dir: Path) -> bool:
        """Install framework from Git repository"""
        try:
            # Clone repository
            clone_result = subprocess.run([
                'git', 'clone', '--recursive', info['install_url'], str(framework_dir)
            ], capture_output=True, text=True, timeout=600)
            
            if clone_result.returncode != 0:
                self.logger.error(f"Git clone failed: {clone_result.stderr}")
                return False
            
            # Change to framework directory
            os.chdir(framework_dir)
            
            # Run install commands
            if 'install_commands' in info:
                for command in info['install_commands']:
                    self.logger.info(f"Running: {command}")
                    result = subprocess.run(
                        command, shell=True, capture_output=True, text=True, timeout=1800
                    )
                    if result.returncode != 0:
                        self.logger.warning(f"Command failed: {result.stderr}")
            
            # Run build commands if specified
            if 'build_commands' in info:
                for command in info['build_commands']:
                    self.logger.info(f"Building: {command}")
                    result = subprocess.run(
                        command, shell=True, capture_output=True, text=True, timeout=1800
                    )
                    if result.returncode != 0:
                        self.logger.warning(f"Build failed: {result.stderr}")
            
            return True
            
        except subprocess.TimeoutExpired:
            self.logger.error("Installation timed out")
            return False
        except Exception as e:
            self.logger.error(f"Git installation error: {e}")
            return False
        finally:
            # Return to original directory
            os.chdir(self.install_dir)
    
    async def _install_binary_framework(self, name: str, info: Dict[str, Any], framework_dir: Path) -> bool:
        """Install framework from binary download"""
        try:
            binary_url = info['install_url']
            binary_name = binary_url.split('/')[-1]
            binary_path = framework_dir / binary_name
            
            # Download binary
            self.logger.info(f"Downloading {binary_name}...")
            response = requests.get(binary_url, timeout=300)
            
            if response.status_code == 200:
                with open(binary_path, 'wb') as f:
                    f.write(response.content)
                
                # Run post-install commands
                if 'post_install' in info:
                    os.chdir(framework_dir)
                    for command in info['post_install']:
                        subprocess.run(command, shell=True, capture_output=True, timeout=300)
                    os.chdir(self.install_dir)
                
                return True
            else:
                self.logger.error(f"Download failed: HTTP {response.status_code}")
                return False
                
        except Exception as e:
            self.logger.error(f"Binary installation error: {e}")
            return False
    
    async def _install_go_framework(self, name: str, info: Dict[str, Any]) -> bool:
        """Install Go-based framework"""
        try:
            for command in info['install_commands']:
                self.logger.info(f"Running Go install: {command}")
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=600
                )
                if result.returncode != 0:
                    self.logger.error(f"Go install failed: {result.stderr}")
                    return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Go installation error: {e}")
            return False
    
    async def _install_package_framework(self, name: str, info: Dict[str, Any]) -> bool:
        """Install framework using package manager"""
        try:
            for command in info['install_commands']:
                self.logger.info(f"Running package install: {command}")
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=1800
                )
                if result.returncode != 0:
                    self.logger.warning(f"Package install warning: {result.stderr}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Package installation error: {e}")
            return False
    
    async def _install_docker_framework(self, name: str, info: Dict[str, Any], framework_dir: Path) -> bool:
        """Install Docker-based framework"""
        try:
            # Clone repository first
            clone_result = subprocess.run([
                'git', 'clone', info['install_url'], str(framework_dir)
            ], capture_output=True, text=True, timeout=600)
            
            if clone_result.returncode != 0:
                return False
            
            os.chdir(framework_dir)
            
            # Run build commands
            for command in info['build_commands']:
                self.logger.info(f"Running Docker build: {command}")
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=3600
                )
                if result.returncode != 0:
                    self.logger.warning(f"Docker build warning: {result.stderr}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Docker installation error: {e}")
            return False
        finally:
            os.chdir(self.install_dir)
    
    async def _install_dotnet_framework(self, name: str, info: Dict[str, Any], framework_dir: Path) -> bool:
        """Install .NET-based framework"""
        try:
            # Install .NET if not present
            dotnet_check = subprocess.run(['which', 'dotnet'], capture_output=True)
            if dotnet_check.returncode != 0:
                self.logger.info("Installing .NET...")
                subprocess.run([
                    'wget', 'https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb',
                    '-O', 'packages-microsoft-prod.deb'
                ], capture_output=True, timeout=300)
                subprocess.run(['sudo', 'dpkg', '-i', 'packages-microsoft-prod.deb'], capture_output=True)
                subprocess.run(['sudo', 'apt-get', 'update'], capture_output=True, timeout=300)
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'dotnet-sdk-6.0'], capture_output=True, timeout=600)
            
            # Clone and build
            clone_result = subprocess.run([
                'git', 'clone', '--recurse-submodules', info['install_url'], str(framework_dir)
            ], capture_output=True, text=True, timeout=600)
            
            if clone_result.returncode != 0:
                return False
            
            os.chdir(framework_dir)
            
            for command in info['build_commands']:
                self.logger.info(f"Running .NET build: {command}")
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True, timeout=1800
                )
                if result.returncode != 0:
                    self.logger.warning(f".NET build warning: {result.stderr}")
            
            return True
            
        except Exception as e:
            self.logger.error(f".NET installation error: {e}")
            return False
        finally:
            os.chdir(self.install_dir)
    
    async def _generate_installation_report(self):
        """Generate comprehensive installation report"""
        self.logger.info("📋 Generating installation report...")
        
        installed_count = len([s for s in self.installation_status.values() if s == 'installed'])
        failed_count = len(self.failed_installations)
        total_count = len(self.deadly_frameworks)
        
        report = {
            'installation_summary': {
                'total_frameworks': total_count,
                'successfully_installed': installed_count,
                'failed_installations': failed_count,
                'success_rate': f"{(installed_count/total_count)*100:.1f}%"
            },
            'installed_frameworks': {},
            'failed_frameworks': self.failed_installations,
            'lethality_analysis': {},
            'capabilities_summary': {},
            'timestamp': datetime.now().isoformat()
        }
        
        # Analyze installed frameworks
        total_lethality = 0
        all_capabilities = set()
        
        for name, status in self.installation_status.items():
            if status == 'installed':
                framework_info = self.deadly_frameworks[name]
                report['installed_frameworks'][name] = {
                    'name': framework_info['name'],
                    'category': framework_info['category'],
                    'tier': framework_info['tier'],
                    'lethality': framework_info['lethality'],
                    'used_by': framework_info['used_by'],
                    'stealth_level': framework_info['stealth_level']
                }
                
                total_lethality += framework_info['lethality']
                all_capabilities.update(framework_info['capabilities'])
        
        # Lethality analysis
        if installed_count > 0:
            avg_lethality = total_lethality / installed_count
            report['lethality_analysis'] = {
                'average_lethality': f"{avg_lethality:.1f}/10",
                'total_lethality_score': total_lethality,
                'lethality_rating': 'EXTREMELY DEADLY' if avg_lethality >= 8 else 'HIGHLY LETHAL' if avg_lethality >= 6 else 'MODERATE'
            }
        
        # Capabilities summary
        report['capabilities_summary'] = {
            'total_unique_capabilities': len(all_capabilities),
            'top_capabilities': list(all_capabilities)[:10]
        }
        
        # Save report
        report_file = self.install_dir / f"installation_report_{int(time.time())}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Display summary
        self.logger.info("="*60)
        self.logger.info("🔥 DEADLY FRAMEWORKS INSTALLATION REPORT")
        self.logger.info("="*60)
        self.logger.info(f"📊 Total Frameworks: {total_count}")
        self.logger.info(f"✅ Successfully Installed: {installed_count}")
        self.logger.info(f"❌ Failed Installations: {failed_count}")
        self.logger.info(f"📈 Success Rate: {report['installation_summary']['success_rate']}")
        
        if 'lethality_analysis' in report:
            self.logger.info(f"💀 Average Lethality: {report['lethality_analysis']['average_lethality']}")
            self.logger.info(f"🎯 Lethality Rating: {report['lethality_analysis']['lethality_rating']}")
        
        self.logger.info(f"🛠️ Total Capabilities: {report['capabilities_summary']['total_unique_capabilities']}")
        self.logger.info("="*60)
        
        return report
    
    def get_installation_status(self) -> Dict[str, Any]:
        """Get current installation status"""
        installed_count = len([s for s in self.installation_status.values() if s == 'installed'])
        
        return {
            'total_frameworks': len(self.deadly_frameworks),
            'installed_frameworks': installed_count,
            'failed_frameworks': len(self.failed_installations),
            'installation_status': self.installation_status,
            'frameworks': self.deadly_frameworks
        }
    
    def display_framework_arsenal(self):
        """Display the complete framework arsenal"""
        print("\n" + "="*80)
        print("⚔️ MAKV'S DEADLY FRAMEWORKS ARSENAL")
        print("="*80)
        
        frameworks_by_tier = {}
        for name, info in self.deadly_frameworks.items():
            tier = info['tier']
            if tier not in frameworks_by_tier:
                frameworks_by_tier[tier] = []
            frameworks_by_tier[tier].append((name, info))
        
        for tier in sorted(frameworks_by_tier.keys()):
            print(f"\n🎯 TIER {tier} - {'NATION-STATE' if tier <= 2 else 'ADVANCED' if tier <= 4 else 'PROFESSIONAL'}")
            print("-" * 60)
            
            for name, info in frameworks_by_tier[tier]:
                status = self.installation_status.get(name, 'not_installed')
                status_icon = "✅" if status == 'installed' else "❌" if status == 'failed' else "⏳"
                
                print(f"{status_icon} {info['name']}")
                print(f"   💀 Lethality: {info['lethality']}/10 | 👻 Stealth: {info['stealth_level']}/10")
                print(f"   🎭 Used by: {', '.join(info['used_by'])}")
                print(f"   📝 {info['description']}")
                print()
        
        print("="*80)

async def main():
    """Test the Deadly Frameworks Installer"""
    installer = DeadlyFrameworksInstaller()
    
    print("⚔️ Testing Deadly Frameworks Installer...")
    
    # Display arsenal
    installer.display_framework_arsenal()
    
    # Install all frameworks (commented out for testing)
    # await installer.install_all_frameworks()

if __name__ == "__main__":
    asyncio.run(main())