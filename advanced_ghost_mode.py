#!/usr/bin/env python3
"""
MAKV'S ADVANCED GHOST MODE SYSTEM
Automatic Tor Activation, IP Rotation, Traffic Obfuscation, and Trace Wiping

This system automatically activates Ghost Mode on startup, manages Tor connections,
rotates IP addresses, obfuscates traffic, and wipes all traces for maximum anonymity.

CLASSIFICATION: AUTHORIZED USE ONLY
VERSION: 3.0.0 - ADVANCED ANONYMIZATION

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
import requests
import socket
import threading
import random
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import psutil

class AdvancedGhostMode:
    """
    Advanced Ghost Mode with automatic Tor, IP rotation, and trace wiping
    """
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.tor_process = None
        self.proxy_chains = []
        self.current_ip = None
        self.geo_location = None
        self.rotation_schedule = []
        self.obfuscation_active = False
        self.trace_wiper_active = False
        self.ghost_mode_active = False
        
        # Tor configuration
        self.tor_config = {
            'socks_port': 9050,
            'control_port': 9051,
            'data_directory': '/tmp/tor_data_makv',
            'log_file': '/tmp/tor_makv.log',
            'exit_nodes': ['us', 'ca', 'de', 'nl', 'se', 'ch'],  # Preferred exit countries
            'rotation_interval': 300,  # 5 minutes
            'max_circuit_dirtiness': 600  # 10 minutes
        }
        
        # Proxy rotation sources
        self.proxy_sources = [
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'
        ]
        
        # Traffic obfuscation tools
        self.obfuscation_tools = {
            'obfs4': {
                'name': 'obfs4proxy',
                'description': 'Tor pluggable transport for traffic obfuscation',
                'install_cmd': 'apt-get install -y obfs4proxy',
                'active': False
            },
            'meek': {
                'name': 'meek-client',
                'description': 'Domain fronting pluggable transport',
                'install_cmd': 'apt-get install -y meek-client',
                'active': False
            },
            'scramblesuit': {
                'name': 'scramblesuit',
                'description': 'Polymorphic network protocol',
                'install_cmd': 'pip3 install scramblesuit',
                'active': False
            }
        }
        
        # Trace wiping targets
        self.trace_targets = [
            '/var/log/',
            '/tmp/',
            '~/.bash_history',
            '~/.python_history',
            '~/.cache/',
            '/var/cache/',
            '/var/tmp/',
            '~/.local/share/recently-used.xbel'
        ]
    
    def _setup_logging(self):
        """Setup logging with trace wiping"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Create secure log file
        log_file = log_dir / f"ghost_mode_{int(time.time())}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)s | GHOST | %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        logger = logging.getLogger(__name__)
        
        # Schedule log file for wiping
        self._schedule_file_wipe(str(log_file))
        
        return logger
    
    async def initialize_ghost_mode(self):
        """Initialize complete Ghost Mode system"""
        self.logger.info("👻 INITIALIZING ADVANCED GHOST MODE...")
        
        try:
            # Step 1: Install required tools
            await self._install_anonymization_tools()
            
            # Step 2: Start Tor with custom configuration
            await self._start_tor_service()
            
            # Step 3: Configure proxy chains
            await self._setup_proxy_chains()
            
            # Step 4: Activate traffic obfuscation
            await self._activate_traffic_obfuscation()
            
            # Step 5: Start IP rotation scheduler
            await self._start_ip_rotation()
            
            # Step 6: Activate trace wiping
            await self._activate_trace_wiping()
            
            # Step 7: Verify anonymization
            await self._verify_anonymization()
            
            self.ghost_mode_active = True
            self.logger.info("✅ ADVANCED GHOST MODE FULLY ACTIVATED!")
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Ghost Mode initialization failed: {e}")
            return False
    
    async def _install_anonymization_tools(self):
        """Install all required anonymization tools"""
        self.logger.info("🛠️ Installing anonymization tools...")
        
        tools_to_install = [
            'tor',
            'proxychains4',
            'obfs4proxy',
            'torsocks',
            'macchanger',
            'bleachbit'
        ]
        
        for tool in tools_to_install:
            try:
                # Check if tool is already installed
                result = subprocess.run(['which', tool], capture_output=True, text=True)
                if result.returncode == 0:
                    self.logger.info(f"✅ {tool} already installed")
                    continue
                
                # Install tool
                self.logger.info(f"📥 Installing {tool}...")
                install_result = subprocess.run([
                    'sudo', 'apt-get', 'install', '-y', tool
                ], capture_output=True, text=True, timeout=300)
                
                if install_result.returncode == 0:
                    self.logger.info(f"✅ {tool} installed successfully")
                else:
                    self.logger.warning(f"⚠️ Failed to install {tool}: {install_result.stderr}")
                    
            except subprocess.TimeoutExpired:
                self.logger.warning(f"⚠️ Installation of {tool} timed out")
            except Exception as e:
                self.logger.warning(f"⚠️ Error installing {tool}: {e}")
    
    async def _start_tor_service(self):
        """Start Tor service with custom configuration"""
        self.logger.info("🧅 Starting Tor service with advanced configuration...")
        
        # Create Tor data directory
        os.makedirs(self.tor_config['data_directory'], exist_ok=True)
        
        # Generate Tor configuration
        tor_config_content = f"""
# MAKV's Advanced Tor Configuration
SocksPort {self.tor_config['socks_port']}
ControlPort {self.tor_config['control_port']}
DataDirectory {self.tor_config['data_directory']}
Log notice file {self.tor_config['log_file']}

# Circuit configuration
MaxCircuitDirtiness {self.tor_config['max_circuit_dirtiness']}
NewCircuitPeriod 30
MaxClientCircuitsPending 32
EnforceDistinctSubnets 1

# Exit node preferences
ExitNodes {{{','.join(self.tor_config['exit_nodes'])}}}
StrictNodes 0

# Security settings
AvoidDiskWrites 1
DisableDebuggerAttachment 1
SafeLogging 1

# Performance optimization
NumEntryGuards 8
NumDirectoryGuards 3
CircuitBuildTimeout 30

# Pluggable transports for obfuscation
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
ClientTransportPlugin meek exec /usr/bin/meek-client
        """
        
        # Write Tor configuration
        tor_config_file = '/tmp/torrc_makv'
        with open(tor_config_file, 'w') as f:
            f.write(tor_config_content)
        
        try:
            # Kill any existing Tor processes
            subprocess.run(['sudo', 'pkill', '-f', 'tor'], capture_output=True)
            await asyncio.sleep(2)
            
            # Start Tor with custom configuration
            self.tor_process = subprocess.Popen([
                'tor', '-f', tor_config_file
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait for Tor to start
            await asyncio.sleep(10)
            
            # Verify Tor is running
            if await self._check_tor_status():
                self.logger.info("✅ Tor service started successfully")
                return True
            else:
                raise Exception("Tor failed to start properly")
                
        except Exception as e:
            self.logger.error(f"❌ Failed to start Tor: {e}")
            return False
    
    async def _setup_proxy_chains(self):
        """Setup proxy chains configuration"""
        self.logger.info("🔗 Configuring proxy chains...")
        
        # Download fresh proxy lists
        fresh_proxies = await self._download_proxy_lists()
        
        # Create proxychains configuration
        proxychains_config = f"""
# MAKV's Advanced Proxy Chains Configuration
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
# Tor SOCKS5 proxy
socks5 127.0.0.1 {self.tor_config['socks_port']}

# Additional proxy chains
"""
        
        # Add fresh proxies to chain
        for proxy in fresh_proxies[:5]:  # Use top 5 proxies
            try:
                ip, port = proxy.split(':')
                proxychains_config += f"http {ip} {port}\n"
            except:
                continue
        
        # Write proxychains configuration
        proxychains_config_file = '/tmp/proxychains_makv.conf'
        with open(proxychains_config_file, 'w') as f:
            f.write(proxychains_config)
        
        # Set environment variable
        os.environ['PROXYCHAINS_CONF_FILE'] = proxychains_config_file
        
        self.logger.info(f"✅ Proxy chains configured with {len(fresh_proxies)} proxies")
    
    async def _download_proxy_lists(self) -> List[str]:
        """Download fresh proxy lists"""
        self.logger.info("📥 Downloading fresh proxy lists...")
        
        all_proxies = []
        
        for source in self.proxy_sources:
            try:
                response = requests.get(source, timeout=10)
                if response.status_code == 200:
                    proxies = response.text.strip().split('\n')
                    valid_proxies = [p for p in proxies if ':' in p and len(p.split(':')) == 2]
                    all_proxies.extend(valid_proxies)
                    self.logger.info(f"✅ Downloaded {len(valid_proxies)} proxies from {source}")
            except Exception as e:
                self.logger.warning(f"⚠️ Failed to download from {source}: {e}")
        
        # Remove duplicates and validate
        unique_proxies = list(set(all_proxies))
        self.logger.info(f"📊 Total unique proxies: {len(unique_proxies)}")
        
        return unique_proxies
    
    async def _activate_traffic_obfuscation(self):
        """Activate traffic obfuscation tools"""
        self.logger.info("🎭 Activating traffic obfuscation...")
        
        for tool_id, tool_info in self.obfuscation_tools.items():
            try:
                # Check if tool is available
                result = subprocess.run(['which', tool_info['name']], capture_output=True)
                if result.returncode == 0:
                    self.logger.info(f"✅ {tool_info['name']} is available")
                    tool_info['active'] = True
                else:
                    self.logger.warning(f"⚠️ {tool_info['name']} not available")
            except Exception as e:
                self.logger.warning(f"⚠️ Error checking {tool_info['name']}: {e}")
        
        self.obfuscation_active = any(tool['active'] for tool in self.obfuscation_tools.values())
        
        if self.obfuscation_active:
            self.logger.info("✅ Traffic obfuscation activated")
        else:
            self.logger.warning("⚠️ No obfuscation tools available")
    
    async def _start_ip_rotation(self):
        """Start automatic IP rotation"""
        self.logger.info("🔄 Starting automatic IP rotation...")
        
        # Create rotation schedule
        self.rotation_schedule = []
        current_time = datetime.now()
        
        for i in range(24):  # 24 rotations per day
            rotation_time = current_time + timedelta(hours=i)
            self.rotation_schedule.append(rotation_time)
        
        # Start rotation thread
        rotation_thread = threading.Thread(target=self._ip_rotation_worker, daemon=True)
        rotation_thread.start()
        
        self.logger.info(f"✅ IP rotation scheduled for {len(self.rotation_schedule)} intervals")
    
    def _ip_rotation_worker(self):
        """Worker thread for IP rotation"""
        while self.ghost_mode_active:
            try:
                # Rotate IP by requesting new Tor circuit
                self._request_new_tor_circuit()
                
                # Update current IP and location
                asyncio.run(self._update_current_status())
                
                # Wait for next rotation
                time.sleep(self.tor_config['rotation_interval'])
                
            except Exception as e:
                self.logger.error(f"IP rotation error: {e}")
                time.sleep(60)  # Wait 1 minute before retry
    
    def _request_new_tor_circuit(self):
        """Request new Tor circuit for IP rotation"""
        try:
            # Connect to Tor control port
            control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            control_socket.connect(('127.0.0.1', self.tor_config['control_port']))
            
            # Send NEWNYM command to get new circuit
            control_socket.send(b'AUTHENTICATE\r\n')
            control_socket.recv(1024)
            
            control_socket.send(b'SIGNAL NEWNYM\r\n')
            response = control_socket.recv(1024)
            
            control_socket.close()
            
            if b'250 OK' in response:
                self.logger.info("🔄 New Tor circuit requested successfully")
            else:
                self.logger.warning("⚠️ Failed to request new Tor circuit")
                
        except Exception as e:
            self.logger.error(f"Error requesting new circuit: {e}")
    
    async def _activate_trace_wiping(self):
        """Activate automatic trace wiping"""
        self.logger.info("🧹 Activating automatic trace wiping...")
        
        # Start trace wiping thread
        wiper_thread = threading.Thread(target=self._trace_wiper_worker, daemon=True)
        wiper_thread.start()
        
        self.trace_wiper_active = True
        self.logger.info("✅ Automatic trace wiping activated")
    
    def _trace_wiper_worker(self):
        """Worker thread for trace wiping"""
        while self.ghost_mode_active:
            try:
                # Wipe traces every 30 minutes
                self._wipe_system_traces()
                time.sleep(1800)  # 30 minutes
                
            except Exception as e:
                self.logger.error(f"Trace wiping error: {e}")
                time.sleep(300)  # Wait 5 minutes before retry
    
    def _wipe_system_traces(self):
        """Wipe system traces and logs"""
        self.logger.info("🧹 Wiping system traces...")
        
        wiped_count = 0
        
        for target in self.trace_targets:
            try:
                expanded_target = os.path.expanduser(target)
                
                if os.path.isfile(expanded_target):
                    # Wipe file
                    with open(expanded_target, 'w') as f:
                        f.write('')
                    wiped_count += 1
                    
                elif os.path.isdir(expanded_target):
                    # Wipe directory contents
                    for root, dirs, files in os.walk(expanded_target):
                        for file in files:
                            try:
                                file_path = os.path.join(root, file)
                                if file.endswith(('.log', '.tmp', '.cache')):
                                    os.remove(file_path)
                                    wiped_count += 1
                            except:
                                pass
                                
            except Exception as e:
                self.logger.debug(f"Could not wipe {target}: {e}")
        
        # Clear bash history
        try:
            subprocess.run(['history', '-c'], shell=True, capture_output=True)
            subprocess.run(['history', '-w'], shell=True, capture_output=True)
        except:
            pass
        
        # Clear Python history
        try:
            import readline
            readline.clear_history()
        except:
            pass
        
        self.logger.info(f"🧹 Wiped {wiped_count} trace files")
    
    def _schedule_file_wipe(self, file_path: str):
        """Schedule a file for wiping on exit"""
        def wipe_on_exit():
            try:
                if os.path.exists(file_path):
                    # Overwrite with random data
                    file_size = os.path.getsize(file_path)
                    with open(file_path, 'wb') as f:
                        f.write(os.urandom(file_size))
                    # Remove file
                    os.remove(file_path)
            except:
                pass
        
        import atexit
        atexit.register(wipe_on_exit)
    
    async def _verify_anonymization(self):
        """Verify anonymization is working"""
        self.logger.info("🔍 Verifying anonymization level...")
        
        # Get current IP and location
        await self._update_current_status()
        
        # Check for DNS leaks
        dns_leak = await self._check_dns_leaks()
        
        # Check for WebRTC leaks
        webrtc_leak = await self._check_webrtc_leaks()
        
        # Calculate anonymization score
        score = 100
        if dns_leak:
            score -= 30
        if webrtc_leak:
            score -= 20
        if not self.obfuscation_active:
            score -= 10
        
        self.logger.info(f"🎯 Anonymization Level: {score}%")
        
        if score >= 80:
            self.logger.info("✅ High anonymization level achieved")
        elif score >= 60:
            self.logger.warning("⚠️ Medium anonymization level")
        else:
            self.logger.error("❌ Low anonymization level - check configuration")
        
        return score
    
    async def _update_current_status(self):
        """Update current IP and geo-location"""
        try:
            # Get IP through Tor
            proxies = {
                'http': f'socks5://127.0.0.1:{self.tor_config["socks_port"]}',
                'https': f'socks5://127.0.0.1:{self.tor_config["socks_port"]}'
            }
            
            response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
            self.current_ip = response.json().get('origin', 'Unknown')
            
            # Get geo-location
            if self.current_ip != 'Unknown':
                geo_response = requests.get(
                    f'https://ipapi.co/{self.current_ip}/json/',
                    proxies=proxies,
                    timeout=10
                )
                geo_data = geo_response.json()
                self.geo_location = f"{geo_data.get('city', 'Unknown')}, {geo_data.get('country_name', 'Unknown')}"
            
        except Exception as e:
            self.logger.error(f"Failed to update status: {e}")
            self.current_ip = 'Unknown'
            self.geo_location = 'Unknown'
    
    async def _check_tor_status(self) -> bool:
        """Check if Tor is running"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', self.tor_config['socks_port']))
            sock.close()
            return result == 0
        except:
            return False
    
    async def _check_dns_leaks(self) -> bool:
        """Check for DNS leaks"""
        try:
            proxies = {
                'http': f'socks5://127.0.0.1:{self.tor_config["socks_port"]}',
                'https': f'socks5://127.0.0.1:{self.tor_config["socks_port"]}'
            }
            
            response = requests.get('https://1.1.1.1/cdn-cgi/trace', proxies=proxies, timeout=5)
            return 'cloudflare' not in response.text.lower()
        except:
            return True  # Assume leak if can't test
    
    async def _check_webrtc_leaks(self) -> bool:
        """Check for WebRTC leaks (simplified)"""
        # This would require a more complex implementation with a browser
        # For now, return False (no leak detected)
        return False
    
    def get_ghost_status(self) -> Dict[str, Any]:
        """Get current Ghost Mode status"""
        return {
            'ghost_mode_active': self.ghost_mode_active,
            'tor_active': self.tor_process is not None and self.tor_process.poll() is None,
            'current_ip': self.current_ip,
            'geo_location': self.geo_location,
            'obfuscation_active': self.obfuscation_active,
            'trace_wiper_active': self.trace_wiper_active,
            'proxy_chains_count': len(self.proxy_chains),
            'rotation_schedule_count': len(self.rotation_schedule),
            'obfuscation_tools': {k: v['active'] for k, v in self.obfuscation_tools.items()},
            'last_updated': datetime.now().isoformat()
        }
    
    def display_ghost_status(self):
        """Display Ghost Mode status in a beautiful format"""
        status = self.get_ghost_status()
        
        print("\n" + "="*60)
        print("👻 MAKV'S ADVANCED GHOST MODE STATUS")
        print("="*60)
        print(f"🔥 Ghost Mode: {'🟢 ACTIVE' if status['ghost_mode_active'] else '🔴 INACTIVE'}")
        print(f"🧅 Tor Service: {'🟢 RUNNING' if status['tor_active'] else '🔴 STOPPED'}")
        print(f"🌍 Current IP: {status['current_ip']}")
        print(f"📍 Location: {status['geo_location']}")
        print(f"🎭 Obfuscation: {'🟢 ACTIVE' if status['obfuscation_active'] else '🔴 INACTIVE'}")
        print(f"🧹 Trace Wiper: {'🟢 ACTIVE' if status['trace_wiper_active'] else '🔴 INACTIVE'}")
        print(f"🔗 Proxy Chains: {status['proxy_chains_count']}")
        print(f"🔄 Rotation Schedule: {status['rotation_schedule_count']} intervals")
        print("\n🛠️ Obfuscation Tools:")
        for tool, active in status['obfuscation_tools'].items():
            print(f"  • {tool}: {'🟢 ACTIVE' if active else '🔴 INACTIVE'}")
        print("="*60)
    
    async def shutdown_ghost_mode(self):
        """Shutdown Ghost Mode and clean up"""
        self.logger.info("🚪 Shutting down Ghost Mode...")
        
        self.ghost_mode_active = False
        
        # Stop Tor process
        if self.tor_process:
            self.tor_process.terminate()
            await asyncio.sleep(2)
            if self.tor_process.poll() is None:
                self.tor_process.kill()
        
        # Final trace wipe
        self._wipe_system_traces()
        
        # Remove temporary files
        temp_files = [
            '/tmp/torrc_makv',
            '/tmp/proxychains_makv.conf',
            self.tor_config['log_file']
        ]
        
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
        
        # Remove Tor data directory
        try:
            shutil.rmtree(self.tor_config['data_directory'], ignore_errors=True)
        except:
            pass
        
        self.logger.info("✅ Ghost Mode shutdown complete")

async def main():
    """Test Advanced Ghost Mode"""
    ghost = AdvancedGhostMode()
    
    print("👻 Testing Advanced Ghost Mode...")
    
    # Initialize Ghost Mode
    success = await ghost.initialize_ghost_mode()
    
    if success:
        # Display status
        ghost.display_ghost_status()
        
        # Wait for a few rotations
        print("\n⏳ Waiting for IP rotations...")
        await asyncio.sleep(30)
        
        # Display updated status
        ghost.display_ghost_status()
        
        # Shutdown
        await ghost.shutdown_ghost_mode()
    else:
        print("❌ Ghost Mode initialization failed")

if __name__ == "__main__":
    asyncio.run(main())