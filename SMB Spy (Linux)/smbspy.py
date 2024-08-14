import os
import re
import nmap
import logging
from impacket.smbconnection import SMBConnection

# Constants
SMB_PORTS = [139, 445]
SUSPICIOUS_EXTENSIONS = ['.ps1', '.bat', '.sh', '.txt']
CREDENTIAL_PATTERN = re.compile(r'(password|pwd|pass|passwd|user|username):\s*["\']?([^\s"\'<>]+)["\']?', re.IGNORECASE)

# Configure logging
logging.basicConfig(filename='smb_spy.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_smb(ip):
    """Scan for SMB services on ports 139 and 445 on a given IP using nmap."""
    nm = nmap.PortScanner()
    open_ports = []
    try:
        logging.info(f"Scanning SMB ports 139 and 445 on {ip}...")
        nm.scan(ip, '139,445')
        for port in SMB_PORTS:
            if nm[ip].has_tcp(port) and nm[ip]['tcp'][port]['state'] == 'open':
                logging.info(f"SMB service found at {ip}:{port}")
                open_ports.append(port)
    except Exception as e:
        logging.error(f"Error scanning SMB ports on {ip}: {e}")
    return open_ports

def connect_to_smb(ip, ports, username, password, domain):
    """Connect to SMB shares on a given IP using the open ports."""
    for port in ports:
        try:
            conn = SMBConnection(ip, ip, sess_port=port)
            conn.login(username, password, domain)
            logging.info(f"Connected to SMB service on {ip}:{port}")

            shares = conn.listShares()
            for share in shares:
                share_name = share['shi1_netname'].decode('utf-8').rstrip('\x00')
                if share_name not in ['IPC$', 'ADMIN$', 'C$']:
                    logging.info(f"Checking share: {share_name}")
                    list_files(conn, share_name)

            conn.close()
        except Exception as e:
            logging.error(f"Error connecting to SMB service on {ip}:{port} - {e}")

def list_files(conn, share_name):
    """List files in a given SMB share."""
    try:
        files = conn.listPath(share_name, '*')
        for file in files:
            file_name = file.get_longname()
            if file.is_directory() or file_name in ['.', '..']:
                continue

            if any(file_name.endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
                logging.info(f"Found suspicious file: {file_name}")
                inspect_file(conn, share_name, file_name)
    except Exception as e:
        logging.error(f"Error listing files in share {share_name}: {e}")

def inspect_file(conn, share_name, file_name):
    """Inspect a file for hard-coded credentials."""
    try:
        local_path = f"/tmp/{file_name}"
        with open(local_path, 'wb') as f:
            conn.retrieveFile(share_name, file_name, f)
        
        with open(local_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = CREDENTIAL_PATTERN.findall(content)
            if matches:
                logging.warning(f"Potential credentials found in {file_name}: {matches}")
        
        # Clean up the local file after inspection
        os.remove(local_path)
    except Exception as e:
        logging.error(f"Error inspecting file {file_name}: {e}")

def main():
    # Prompt user for IP address or URL
    target_ip = input("Enter the IP address or URL to scan: ")

    # Prompt user for SMB credentials
    username = input("Enter the SMB username (leave blank if not required): ")
    password = input("Enter the SMB password (leave blank if not required): ")
    domain = input("Enter the SMB domain (leave blank if not required): ")

    # Step 1: Scan for SMB Services
    open_ports = scan_smb(target_ip)
    
    if open_ports:
        # Step 2: Connect to SMB Shares
        connect_to_smb(target_ip, open_ports, username, password, domain)
    else:
        logging.info("No open SMB ports found.")

if __name__ == "__main__":
    main()
