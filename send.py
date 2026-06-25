import paramiko
from scp import SCPClient

# -------------------------
# PI CONNECTION INFO
# -------------------------
pi_ip = "10.145.245.95"   # Pi IP
pi_user = "pi"
pi_password = "pi"

# -------------------------
# FILE PATHS
# -------------------------
local_file = r"U:\project\test.jpg"  # Laptop image
remote_dir = "/home/pi/images/"
remote_file = remote_dir + "test.jpg"

# -------------------------
# CONNECT VIA SSH
# -------------------------
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(pi_ip, username=pi_user, password=pi_password)

# -------------------------
# CREATE REMOTE FOLDER
# -------------------------
ssh.exec_command(f"mkdir -p {remote_dir}")

# -------------------------
# COPY FILE TO PI
# -------------------------
from scp import SCPClient
with SCPClient(ssh.get_transport()) as scp:
    scp.put(local_file, remote_file)

print(f"File sent to Pi: {remote_file}")
ssh.close()
