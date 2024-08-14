
## SMB Spy: A SMB Scanner and Inspector

SMB Spy is a Python tool designed to scan, connect to, and inspect SMB (Server Message Block) services on a network. This tool will help security professionals and network administrators identify potential security issues related to SMB services. It scans for open SMB ports, connects to the SMB shares, and checks for files that might contain hard-coded credentials or other suspicious content.
## Authors

- [@raafay009](https://github.com/Raafay009)


## Features

- Scans for SMB services on ports 139 and 445.
- Connects to discovered SMB shares.
- Checks for suspicious files and text files.
- Inspects files for hard-coded credentials.


## Documentation

𝗙𝗶𝗹𝗲 𝘀𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲:

1. smbspy.exe (windows) & smbspy.exe (Linux) are download and ready to run tools.

2. SMB Spy (Linux) & SMB Spy (Windows) folders contain actual source code & build, open sourced for further collaborative developments and improvements.

𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀

1. Port Scanning: Detects if SMB services are running on the commonly used ports (139 and 445) of a given target.
2. SMB Connection: Establishes a connection to SMB services using anonymous or specified credentials.
3. Share Listing: Retrieves and lists available SMB shares on the target system.
4. File Inspection: Downloads and inspects files within the shares for potential hard-coded credentials or sensitive information.

𝗪𝗼𝗿𝗸𝗶𝗻𝗴

- Scan for SMB Ports: The tool scans the target IP for open SMB ports (139 and 445) to identify if SMB services are available.

- Connect to SMB Services: If SMB services are found, it attempts to connect to them. Anonymous login is used by default, but you can specify credentials if needed.

- List and Access Shares: Once connected, it lists all accessible SMB shares on the target system.

- Inspect Files: For each share, it downloads and inspects files for keywords associated with hard-coded credentials (like 'username' and 'password').

𝗟𝗶𝗻𝘂𝘅 𝗩𝗲𝗿𝘀𝗶𝗼𝗻:

- Requirements: Install the required Python libraries: nmap, impacket. Ensure you have permissions to run network scans and access SMB services.

- Running the Script: Edit the target_ip variable with the IP address you want to scan. Run the script using Python: python smbspy_linux.py.

- Output: The script logs its activities to smbspy.log and prints relevant information to the console.

𝗪𝗶𝗻𝗱𝗼𝘄𝘀 𝗩𝗲𝗿𝘀𝗶𝗼𝗻:

- Requirements: Install the required Python library: impacket. Ensure you have network access and proper permissions.

- Running the Script: Update the target_ip, username, password, and domain variables with the appropriate values. Execute the script using Python: python smbspy_windows.py.

- Output: The script prints status messages and findings directly to the console.

𝗡𝗼𝘁𝗲𝘀:

- Security Warning: Use this tool responsibly and only on networks you have permission to scan. Unauthorized access to network services is illegal and unethical.

- Customization: Feel free to customize the scanning ports, file inspection criteria, and connection parameters according to your needs.

𝗖𝗼𝗻𝘁𝗿𝗶𝗯𝘂𝘁𝗶𝗼𝗻𝘀:

Contributions are welcome! If you have improvements or additional features to suggest, please submit a pull request or open an issue on this repository.

