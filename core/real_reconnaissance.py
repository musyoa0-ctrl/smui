#!/usr/bin/env python3
"""
REAL RECONNAISSANCE ENGINE
Advanced Network Discovery and Vulnerability Assessment

This module implements ACTUAL reconnaissance capabilities:
- Real network scanning with Nmap integration
- Service enumeration and version detection
- Subdomain discovery using multiple techniques
- Technology stack fingerprinting
- Vulnerability identification with CVE mapping
- SSL/TLS analysis and certificate inspection

CLASSIFICATION: AUTHORIZED USE ONLY
"""

import asyncio
import subprocess
import json
import socket
import ssl
import dns.resolver
import whois
import requests
import nmap
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import concurrent.futures
import ipaddress
from urllib.parse import urlparse
import re
import hashlib
import base64
from pathlib import Path

class RealReconnaissanceEngine:
    """
    Real Reconnaissance Engine for actual network discovery and vulnerability assessment
    
    This engine performs REAL reconnaissance operations:
    1. Network scanning and port discovery
    2. Service enumeration and version detection
    3. Subdomain discovery and DNS analysis
    4. Technology stack fingerprinting
    5. Vulnerability identification and CVE mapping
    6. SSL/TLS security assessment
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nm = nmap.PortScanner()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Reconnaissance results storage
        self.target_info = {}
        self.discovered_hosts = []
        self.open_ports = {}
        self.services = {}
        self.vulnerabilities = []
        self.subdomains = []
        
        # Wordlists and payloads
        self.subdomain_wordlist = self._load_subdomain_wordlist()
        self.common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080, 8443]
        
    def _load_subdomain_wordlist(self) -> List[str]:
        """Load subdomain wordlist for discovery"""
        common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2',
            'cpanel', 'whm', 'autodiscover', 'autoconfig', 'ns3', 'm', 'imap', 'test', 'ns', 'blog',
            'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns4', 'mail2', 'new', 'mysql',
            'old', 'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql',
            'secure', 'demo', 'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img',
            'www1', 'intranet', 'portal', 'video', 'sip', 'dns2', 'api', 'cdn', 'stats', 'dns1',
            'ns5', 'upload', 'client', 'forum', 'bb', 'chat', 'irc', 'live', 'search', 'ftp2'
        ]
        return common_subdomains
    
    async def full_reconnaissance(self, target: str) -> Dict[str, Any]:
        """
        Perform comprehensive reconnaissance on target
        
        Args:
            target: Target domain or IP address
            
        Returns:
            Complete reconnaissance results
        """
        self.logger.info(f"🔍 Starting REAL reconnaissance on {target}")
        
        results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'host_discovery': {},
            'port_scan': {},
            'service_enumeration': {},
            'subdomain_discovery': {},
            'dns_analysis': {},
            'ssl_analysis': {},
            'technology_detection': {},
            'vulnerability_assessment': {},
            'whois_information': {}
        }
        
        try:
            # Phase 1: Host Discovery and Network Mapping
            self.logger.info("🌐 Phase 1: Host Discovery")
            results['host_discovery'] = await self._host_discovery(target)
            
            # Phase 2: Port Scanning and Service Detection
            self.logger.info("🔍 Phase 2: Port Scanning")
            results['port_scan'] = await self._port_scanning(target)
            
            # Phase 3: Service Enumeration
            self.logger.info("🔧 Phase 3: Service Enumeration")
            results['service_enumeration'] = await self._service_enumeration(target, results['port_scan'])
            
            # Phase 4: Subdomain Discovery
            self.logger.info("🌍 Phase 4: Subdomain Discovery")
            results['subdomain_discovery'] = await self._subdomain_discovery(target)
            
            # Phase 5: DNS Analysis
            self.logger.info("🔍 Phase 5: DNS Analysis")
            results['dns_analysis'] = await self._dns_analysis(target)
            
            # Phase 6: SSL/TLS Analysis
            self.logger.info("🔒 Phase 6: SSL/TLS Analysis")
            results['ssl_analysis'] = await self._ssl_analysis(target)
            
            # Phase 7: Technology Detection
            self.logger.info("🔧 Phase 7: Technology Detection")
            results['technology_detection'] = await self._technology_detection(target)
            
            # Phase 8: Vulnerability Assessment
            self.logger.info("⚠️ Phase 8: Vulnerability Assessment")
            results['vulnerability_assessment'] = await self._vulnerability_assessment(target, results)
            
            # Phase 9: WHOIS Information
            self.logger.info("📋 Phase 9: WHOIS Analysis")
            results['whois_information'] = await self._whois_analysis(target)
            
            self.logger.info("✅ REAL reconnaissance completed successfully")
            
        except Exception as e:
            self.logger.error(f"❌ Reconnaissance failed: {e}")
            results['error'] = str(e)
        
        return results
    
    async def _host_discovery(self, target: str) -> Dict[str, Any]:
        """Discover live hosts in target network"""
        try:
            # Resolve target to IP
            target_ip = socket.gethostbyname(target)
            
            # Ping sweep for network discovery
            network = ipaddress.IPv4Network(f"{target_ip}/24", strict=False)
            live_hosts = []
            
            # Use concurrent ping to discover live hosts
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                futures = []
                for ip in list(network.hosts())[:50]:  # Limit to first 50 IPs
                    futures.append(executor.submit(self._ping_host, str(ip)))
                
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result['alive']:
                        live_hosts.append(result)
            
            return {
                'target_ip': target_ip,
                'network_range': str(network),
                'live_hosts': live_hosts,
                'total_discovered': len(live_hosts)
            }
            
        except Exception as e:
            self.logger.error(f"Host discovery failed: {e}")
            return {'error': str(e)}
    
    def _ping_host(self, ip: str) -> Dict[str, Any]:
        """Ping individual host to check if alive"""
        try:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                  capture_output=True, text=True, timeout=5)
            alive = result.returncode == 0
            
            return {
                'ip': ip,
                'alive': alive,
                'response_time': self._extract_ping_time(result.stdout) if alive else None
            }
        except:
            return {'ip': ip, 'alive': False}
    
    def _extract_ping_time(self, ping_output: str) -> Optional[float]:
        """Extract ping response time from ping output"""
        try:
            match = re.search(r'time=(\d+\.?\d*)', ping_output)
            return float(match.group(1)) if match else None
        except:
            return None
    
    async def _port_scanning(self, target: str) -> Dict[str, Any]:
        """Perform comprehensive port scanning"""
        try:
            self.logger.info(f"🔍 Scanning ports on {target}")
            
            # Nmap TCP SYN scan
            self.nm.scan(target, '1-65535', '-sS -sV -O --script=default')
            
            scan_results = {}
            for host in self.nm.all_hosts():
                host_info = {
                    'state': self.nm[host].state(),
                    'protocols': {},
                    'os_detection': {},
                    'open_ports': []
                }
                
                # Process each protocol
                for protocol in self.nm[host].all_protocols():
                    ports = self.nm[host][protocol].keys()
                    host_info['protocols'][protocol] = {}
                    
                    for port in ports:
                        port_info = self.nm[host][protocol][port]
                        if port_info['state'] == 'open':
                            host_info['open_ports'].append({
                                'port': port,
                                'protocol': protocol,
                                'service': port_info.get('name', 'unknown'),
                                'version': port_info.get('version', ''),
                                'product': port_info.get('product', ''),
                                'extrainfo': port_info.get('extrainfo', '')
                            })
                        
                        host_info['protocols'][protocol][port] = port_info
                
                # OS Detection
                if 'osmatch' in self.nm[host]:
                    host_info['os_detection'] = self.nm[host]['osmatch']
                
                scan_results[host] = host_info
            
            return scan_results
            
        except Exception as e:
            self.logger.error(f"Port scanning failed: {e}")
            return {'error': str(e)}
    
    async def _service_enumeration(self, target: str, port_scan_results: Dict) -> Dict[str, Any]:
        """Enumerate services running on discovered ports"""
        try:
            service_info = {}
            
            for host, host_data in port_scan_results.items():
                if 'error' in host_data:
                    continue
                    
                service_info[host] = {}
                
                for port_info in host_data.get('open_ports', []):
                    port = port_info['port']
                    service = port_info['service']
                    
                    # Detailed service enumeration
                    service_details = await self._enumerate_specific_service(host, port, service)
                    service_info[host][port] = service_details
            
            return service_info
            
        except Exception as e:
            self.logger.error(f"Service enumeration failed: {e}")
            return {'error': str(e)}
    
    async def _enumerate_specific_service(self, host: str, port: int, service: str) -> Dict[str, Any]:
        """Enumerate specific service for detailed information"""
        service_details = {
            'service': service,
            'port': port,
            'banner': '',
            'version_info': {},
            'vulnerabilities': [],
            'configuration': {}
        }
        
        try:
            # Banner grabbing
            banner = await self._grab_banner(host, port)
            service_details['banner'] = banner
            
            # Service-specific enumeration
            if service.lower() in ['http', 'https']:
                service_details.update(await self._enumerate_web_service(host, port))
            elif service.lower() == 'ssh':
                service_details.update(await self._enumerate_ssh_service(host, port))
            elif service.lower() == 'ftp':
                service_details.update(await self._enumerate_ftp_service(host, port))
            elif service.lower() in ['mysql', 'postgresql']:
                service_details.update(await self._enumerate_database_service(host, port, service))
            
        except Exception as e:
            service_details['error'] = str(e)
        
        return service_details
    
    async def _grab_banner(self, host: str, port: int) -> str:
        """Grab service banner"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            
            # Send HTTP request for web services
            if port in [80, 443, 8080, 8443]:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            else:
                sock.send(b"\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            sock.close()
            return banner.strip()
            
        except Exception as e:
            return f"Banner grab failed: {str(e)}"
    
    async def _enumerate_web_service(self, host: str, port: int) -> Dict[str, Any]:
        """Enumerate web service details"""
        web_info = {
            'server_header': '',
            'technologies': [],
            'directories': [],
            'forms': [],
            'cookies': [],
            'security_headers': {}
        }
        
        try:
            protocol = 'https' if port in [443, 8443] else 'http'
            url = f"{protocol}://{host}:{port}"
            
            response = self.session.get(url, timeout=10, verify=False)
            
            # Server information
            web_info['server_header'] = response.headers.get('Server', '')
            web_info['status_code'] = response.status_code
            
            # Security headers analysis
            security_headers = [
                'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options',
                'Strict-Transport-Security', 'Content-Security-Policy',
                'X-Permitted-Cross-Domain-Policies', 'Referrer-Policy'
            ]
            
            for header in security_headers:
                web_info['security_headers'][header] = response.headers.get(header, 'Missing')
            
            # Technology detection from headers and content
            web_info['technologies'] = self._detect_web_technologies(response)
            
            # Directory enumeration (basic)
            web_info['directories'] = await self._enumerate_directories(url)
            
        except Exception as e:
            web_info['error'] = str(e)
        
        return web_info
    
    def _detect_web_technologies(self, response) -> List[str]:
        """Detect web technologies from response"""
        technologies = []
        
        # Check headers
        server = response.headers.get('Server', '').lower()
        if 'apache' in server:
            technologies.append('Apache')
        if 'nginx' in server:
            technologies.append('Nginx')
        if 'iis' in server:
            technologies.append('IIS')
        
        # Check X-Powered-By header
        powered_by = response.headers.get('X-Powered-By', '').lower()
        if 'php' in powered_by:
            technologies.append('PHP')
        if 'asp.net' in powered_by:
            technologies.append('ASP.NET')
        
        # Check content for framework signatures
        content = response.text.lower()
        if 'wordpress' in content:
            technologies.append('WordPress')
        if 'drupal' in content:
            technologies.append('Drupal')
        if 'joomla' in content:
            technologies.append('Joomla')
        
        return technologies
    
    async def _enumerate_directories(self, base_url: str) -> List[str]:
        """Enumerate common directories"""
        common_dirs = [
            'admin', 'administrator', 'wp-admin', 'login', 'dashboard',
            'panel', 'cpanel', 'phpmyadmin', 'backup', 'config',
            'api', 'test', 'dev', 'staging', 'uploads', 'files'
        ]
        
        found_dirs = []
        
        for directory in common_dirs:
            try:
                url = f"{base_url}/{directory}"
                response = self.session.get(url, timeout=5, verify=False)
                if response.status_code in [200, 301, 302, 403]:
                    found_dirs.append({
                        'directory': directory,
                        'status_code': response.status_code,
                        'url': url
                    })
            except:
                continue
        
        return found_dirs
    
    async def _enumerate_ssh_service(self, host: str, port: int) -> Dict[str, Any]:
        """Enumerate SSH service"""
        ssh_info = {'version': '', 'algorithms': [], 'auth_methods': []}
        
        try:
            import paramiko
            
            # Get SSH version and algorithms
            transport = paramiko.Transport((host, port))
            transport.start_client()
            
            ssh_info['version'] = transport.remote_version
            ssh_info['server_key_algorithm'] = transport.get_server_key().get_name()
            
            transport.close()
            
        except Exception as e:
            ssh_info['error'] = str(e)
        
        return ssh_info
    
    async def _enumerate_ftp_service(self, host: str, port: int) -> Dict[str, Any]:
        """Enumerate FTP service"""
        ftp_info = {'banner': '', 'anonymous_login': False, 'features': []}
        
        try:
            import ftplib
            
            ftp = ftplib.FTP()
            ftp.connect(host, port, timeout=10)
            ftp_info['banner'] = ftp.getwelcome()
            
            # Test anonymous login
            try:
                ftp.login('anonymous', 'anonymous@example.com')
                ftp_info['anonymous_login'] = True
                ftp_info['directory_listing'] = ftp.nlst()
            except:
                ftp_info['anonymous_login'] = False
            
            ftp.quit()
            
        except Exception as e:
            ftp_info['error'] = str(e)
        
        return ftp_info
    
    async def _enumerate_database_service(self, host: str, port: int, service: str) -> Dict[str, Any]:
        """Enumerate database service"""
        db_info = {'version': '', 'databases': [], 'users': []}
        
        # Database enumeration would require credentials
        # This is a placeholder for actual database enumeration
        db_info['note'] = 'Database enumeration requires valid credentials'
        
        return db_info
    
    async def _subdomain_discovery(self, target: str) -> Dict[str, Any]:
        """Discover subdomains using multiple techniques"""
        subdomains = {
            'discovered_subdomains': [],
            'methods_used': ['dns_bruteforce', 'certificate_transparency', 'search_engines'],
            'total_found': 0
        }
        
        try:
            # Method 1: DNS Brute Force
            dns_subdomains = await self._dns_bruteforce_subdomains(target)
            subdomains['discovered_subdomains'].extend(dns_subdomains)
            
            # Method 2: Certificate Transparency Logs
            ct_subdomains = await self._certificate_transparency_subdomains(target)
            subdomains['discovered_subdomains'].extend(ct_subdomains)
            
            # Remove duplicates
            subdomains['discovered_subdomains'] = list(set(subdomains['discovered_subdomains']))
            subdomains['total_found'] = len(subdomains['discovered_subdomains'])
            
        except Exception as e:
            subdomains['error'] = str(e)
        
        return subdomains
    
    async def _dns_bruteforce_subdomains(self, target: str) -> List[str]:
        """Brute force subdomains using DNS queries"""
        found_subdomains = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for subdomain in self.subdomain_wordlist:
                full_domain = f"{subdomain}.{target}"
                futures.append(executor.submit(self._resolve_domain, full_domain))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found_subdomains.append(result)
        
        return found_subdomains
    
    def _resolve_domain(self, domain: str) -> Optional[str]:
        """Resolve domain to check if it exists"""
        try:
            socket.gethostbyname(domain)
            return domain
        except:
            return None
    
    async def _certificate_transparency_subdomains(self, target: str) -> List[str]:
        """Find subdomains from Certificate Transparency logs"""
        subdomains = []
        
        try:
            # Query crt.sh for certificate transparency logs
            url = f"https://crt.sh/?q=%.{target}&output=json"
            response = self.session.get(url, timeout=15)
            
            if response.status_code == 200:
                certificates = response.json()
                for cert in certificates:
                    name_value = cert.get('name_value', '')
                    for domain in name_value.split('\n'):
                        domain = domain.strip()
                        if domain.endswith(f'.{target}') and domain not in subdomains:
                            subdomains.append(domain)
            
        except Exception as e:
            self.logger.error(f"Certificate transparency lookup failed: {e}")
        
        return subdomains
    
    async def _dns_analysis(self, target: str) -> Dict[str, Any]:
        """Perform comprehensive DNS analysis"""
        dns_info = {
            'a_records': [],
            'aaaa_records': [],
            'mx_records': [],
            'ns_records': [],
            'txt_records': [],
            'cname_records': [],
            'soa_record': {},
            'dns_servers': []
        }
        
        try:
            resolver = dns.resolver.Resolver()
            
            # A Records
            try:
                answers = resolver.resolve(target, 'A')
                dns_info['a_records'] = [str(rdata) for rdata in answers]
            except:
                pass
            
            # AAAA Records (IPv6)
            try:
                answers = resolver.resolve(target, 'AAAA')
                dns_info['aaaa_records'] = [str(rdata) for rdata in answers]
            except:
                pass
            
            # MX Records
            try:
                answers = resolver.resolve(target, 'MX')
                dns_info['mx_records'] = [{'priority': rdata.preference, 'exchange': str(rdata.exchange)} for rdata in answers]
            except:
                pass
            
            # NS Records
            try:
                answers = resolver.resolve(target, 'NS')
                dns_info['ns_records'] = [str(rdata) for rdata in answers]
            except:
                pass
            
            # TXT Records
            try:
                answers = resolver.resolve(target, 'TXT')
                dns_info['txt_records'] = [str(rdata) for rdata in answers]
            except:
                pass
            
            # SOA Record
            try:
                answers = resolver.resolve(target, 'SOA')
                soa = answers[0]
                dns_info['soa_record'] = {
                    'mname': str(soa.mname),
                    'rname': str(soa.rname),
                    'serial': soa.serial,
                    'refresh': soa.refresh,
                    'retry': soa.retry,
                    'expire': soa.expire,
                    'minimum': soa.minimum
                }
            except:
                pass
            
        except Exception as e:
            dns_info['error'] = str(e)
        
        return dns_info
    
    async def _ssl_analysis(self, target: str) -> Dict[str, Any]:
        """Analyze SSL/TLS configuration"""
        ssl_info = {
            'certificate_info': {},
            'cipher_suites': [],
            'protocol_versions': [],
            'vulnerabilities': [],
            'grade': 'Unknown'
        }
        
        try:
            # Get SSL certificate information
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            with socket.create_connection((target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=target) as ssock:
                    cert = ssock.getpeercert()
                    
                    ssl_info['certificate_info'] = {
                        'subject': dict(x[0] for x in cert['subject']),
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'version': cert['version'],
                        'serial_number': cert['serialNumber'],
                        'not_before': cert['notBefore'],
                        'not_after': cert['notAfter'],
                        'signature_algorithm': cert.get('signatureAlgorithm', 'Unknown')
                    }
                    
                    # Check for Subject Alternative Names
                    if 'subjectAltName' in cert:
                        ssl_info['certificate_info']['subject_alt_names'] = [name[1] for name in cert['subjectAltName']]
                    
                    # Basic SSL grade assessment
                    ssl_info['grade'] = self._assess_ssl_grade(cert, ssock.cipher())
            
        except Exception as e:
            ssl_info['error'] = str(e)
        
        return ssl_info
    
    def _assess_ssl_grade(self, cert: Dict, cipher: Tuple) -> str:
        """Assess SSL configuration grade"""
        grade = 'A'  # Start with A grade
        
        # Check certificate validity
        try:
            not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            if not_after < datetime.now():
                grade = 'F'  # Expired certificate
        except:
            pass
        
        # Check cipher strength
        if cipher and len(cipher) >= 3:
            cipher_name = cipher[0]
            if 'RC4' in cipher_name or 'DES' in cipher_name:
                grade = 'C'  # Weak ciphers
            elif 'AES128' in cipher_name:
                grade = 'B'  # Medium strength
        
        return grade
    
    async def _technology_detection(self, target: str) -> Dict[str, Any]:
        """Detect technologies used by target"""
        tech_info = {
            'web_technologies': [],
            'cms': [],
            'frameworks': [],
            'programming_languages': [],
            'databases': [],
            'web_servers': []
        }
        
        try:
            # Web technology detection
            response = self.session.get(f"http://{target}", timeout=10, verify=False)
            
            # Analyze headers
            headers = response.headers
            content = response.text.lower()
            
            # Web server detection
            server = headers.get('Server', '').lower()
            if 'apache' in server:
                tech_info['web_servers'].append('Apache')
            if 'nginx' in server:
                tech_info['web_servers'].append('Nginx')
            if 'iis' in server:
                tech_info['web_servers'].append('Microsoft IIS')
            
            # Programming language detection
            powered_by = headers.get('X-Powered-By', '').lower()
            if 'php' in powered_by:
                tech_info['programming_languages'].append('PHP')
            if 'asp.net' in powered_by:
                tech_info['programming_languages'].append('ASP.NET')
            
            # CMS detection
            if 'wp-content' in content or 'wordpress' in content:
                tech_info['cms'].append('WordPress')
            if '/sites/default/' in content or 'drupal' in content:
                tech_info['cms'].append('Drupal')
            if 'joomla' in content:
                tech_info['cms'].append('Joomla')
            
            # Framework detection
            if 'laravel' in content:
                tech_info['frameworks'].append('Laravel')
            if 'django' in content:
                tech_info['frameworks'].append('Django')
            if 'react' in content:
                tech_info['frameworks'].append('React')
            if 'angular' in content:
                tech_info['frameworks'].append('Angular')
            
        except Exception as e:
            tech_info['error'] = str(e)
        
        return tech_info
    
    async def _vulnerability_assessment(self, target: str, recon_results: Dict) -> Dict[str, Any]:
        """Assess vulnerabilities based on reconnaissance results"""
        vuln_info = {
            'critical_vulnerabilities': [],
            'high_vulnerabilities': [],
            'medium_vulnerabilities': [],
            'low_vulnerabilities': [],
            'total_vulnerabilities': 0,
            'risk_score': 0
        }
        
        try:
            # Analyze open ports for known vulnerabilities
            for host, host_data in recon_results.get('port_scan', {}).items():
                if 'open_ports' in host_data:
                    for port_info in host_data['open_ports']:
                        vulns = self._check_port_vulnerabilities(port_info)
                        for vuln in vulns:
                            if vuln['severity'] == 'critical':
                                vuln_info['critical_vulnerabilities'].append(vuln)
                            elif vuln['severity'] == 'high':
                                vuln_info['high_vulnerabilities'].append(vuln)
                            elif vuln['severity'] == 'medium':
                                vuln_info['medium_vulnerabilities'].append(vuln)
                            else:
                                vuln_info['low_vulnerabilities'].append(vuln)
            
            # Check SSL vulnerabilities
            ssl_results = recon_results.get('ssl_analysis', {})
            if ssl_results.get('grade') in ['C', 'D', 'F']:
                vuln_info['high_vulnerabilities'].append({
                    'name': 'Weak SSL/TLS Configuration',
                    'severity': 'high',
                    'description': f"SSL grade: {ssl_results.get('grade')}",
                    'cve': 'N/A',
                    'solution': 'Update SSL/TLS configuration and certificates'
                })
            
            # Check for missing security headers
            for host, host_data in recon_results.get('service_enumeration', {}).items():
                for port, service_data in host_data.items():
                    if 'security_headers' in service_data:
                        missing_headers = [h for h, v in service_data['security_headers'].items() if v == 'Missing']
                        if missing_headers:
                            vuln_info['medium_vulnerabilities'].append({
                                'name': 'Missing Security Headers',
                                'severity': 'medium',
                                'description': f"Missing headers: {', '.join(missing_headers)}",
                                'cve': 'N/A',
                                'solution': 'Implement proper security headers'
                            })
            
            # Calculate total vulnerabilities and risk score
            vuln_info['total_vulnerabilities'] = (
                len(vuln_info['critical_vulnerabilities']) +
                len(vuln_info['high_vulnerabilities']) +
                len(vuln_info['medium_vulnerabilities']) +
                len(vuln_info['low_vulnerabilities'])
            )
            
            # Risk score calculation
            risk_score = (
                len(vuln_info['critical_vulnerabilities']) * 10 +
                len(vuln_info['high_vulnerabilities']) * 7 +
                len(vuln_info['medium_vulnerabilities']) * 4 +
                len(vuln_info['low_vulnerabilities']) * 1
            )
            vuln_info['risk_score'] = min(risk_score, 100)  # Cap at 100
            
        except Exception as e:
            vuln_info['error'] = str(e)
        
        return vuln_info
    
    def _check_port_vulnerabilities(self, port_info: Dict) -> List[Dict]:
        """Check for known vulnerabilities on specific ports/services"""
        vulnerabilities = []
        port = port_info['port']
        service = port_info['service'].lower()
        version = port_info.get('version', '').lower()
        
        # Common vulnerability checks
        if port == 21 and 'ftp' in service:
            vulnerabilities.append({
                'name': 'FTP Anonymous Access',
                'severity': 'medium',
                'description': 'FTP server may allow anonymous access',
                'cve': 'N/A',
                'solution': 'Disable anonymous FTP access'
            })
        
        if port == 22 and 'ssh' in service:
            if 'openssh' in version and any(v in version for v in ['7.4', '7.5', '7.6']):
                vulnerabilities.append({
                    'name': 'OpenSSH User Enumeration',
                    'severity': 'medium',
                    'description': 'OpenSSH version vulnerable to user enumeration',
                    'cve': 'CVE-2018-15473',
                    'solution': 'Update OpenSSH to latest version'
                })
        
        if port == 23 and 'telnet' in service:
            vulnerabilities.append({
                'name': 'Telnet Unencrypted Protocol',
                'severity': 'high',
                'description': 'Telnet transmits data in plaintext',
                'cve': 'N/A',
                'solution': 'Replace Telnet with SSH'
            })
        
        if port in [80, 443, 8080, 8443] and 'http' in service:
            vulnerabilities.append({
                'name': 'Web Application Present',
                'severity': 'low',
                'description': 'Web application requires security assessment',
                'cve': 'N/A',
                'solution': 'Perform web application security testing'
            })
        
        if port == 3389 and 'rdp' in service:
            vulnerabilities.append({
                'name': 'RDP Service Exposed',
                'severity': 'high',
                'description': 'Remote Desktop Protocol exposed to internet',
                'cve': 'N/A',
                'solution': 'Restrict RDP access or use VPN'
            })
        
        return vulnerabilities
    
    async def _whois_analysis(self, target: str) -> Dict[str, Any]:
        """Perform WHOIS analysis"""
        whois_info = {}
        
        try:
            w = whois.whois(target)
            whois_info = {
                'domain_name': w.domain_name,
                'registrar': w.registrar,
                'creation_date': str(w.creation_date) if w.creation_date else None,
                'expiration_date': str(w.expiration_date) if w.expiration_date else None,
                'name_servers': w.name_servers,
                'status': w.status,
                'emails': w.emails,
                'country': w.country
            }
        except Exception as e:
            whois_info['error'] = str(e)
        
        return whois_info