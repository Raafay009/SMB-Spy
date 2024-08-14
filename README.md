SMB Spy: A Simple SMB Scanner and Inspector

SMB Spy is a Python tool designed to scan, connect to, and inspect SMB (Server Message Block) services on a network. This tool helps security professionals and network administrators identify potential security issues related to SMB services. It scans for open SMB ports, connects to the SMB shares, and checks for files that might contain hard-coded credentials or other suspicious content.
Features

    Port Scanning: Detects if SMB services are running on the commonly used ports (139 and 445) of a given target.
    SMB Connection: Establishes a connection to SMB services using anonymous or specified credentials.
    Share Listing: Retrieves and lists available SMB shares on the target system.
    File Inspection: Downloads and inspects files within the shares for potential hard-coded credentials or sensitive information.

How It Works

    Scan for SMB Ports:
        The tool scans the target IP for open SMB ports (139 and 445) to identify if SMB services are available.

    Connect to SMB Services:
        If SMB services are found, it attempts to connect to them. Anonymous login is used by default, but you can specify credentials if needed.

    List and Access Shares:
        Once connected, it lists all accessible SMB shares on the target system.

    Inspect Files:
        For each share, it downloads and inspects files for keywords associated with hard-coded credentials (like 'username' and 'password').

Usage
Linux Version

    Requirements:
        Install the required Python libraries: nmap, impacket.
        Ensure you have permissions to run network scans and access SMB services.

    Running the Script:
        Edit the target_ip variable with the IP address you want to scan.
        Run the script using Python: python smbspy_linux.py.

    Output:
        The script logs its activities to smbspy.log and prints relevant information to the console.

Windows Version

    Requirements:
        Install the required Python library: impacket.
        Ensure you have network access and proper permissions.

    Running the Script:
        Update the target_ip, username, password, and domain variables with the appropriate values.
        Execute the script using Python: python smbspy_windows.py.

    Output:
        The script prints status messages and findings directly to the console.

Notes

    Security Warning: Use this tool responsibly and only on networks you have permission to scan. Unauthorized access to network services is illegal and unethical.
    Customization: Feel free to customize the scanning ports, file inspection criteria, and connection parameters according to your needs.

Contributing

Contributions are welcome! If you have improvements or additional features to suggest, please submit a pull request or open an issue on this repository.
