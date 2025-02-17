import subprocess

def start_receiving(directorypath:str):
    cmd = ["obexpushd","-B","-o", directorypath]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to run obexpushd: {result.stderr.strip()}")

def restart_bluetooth():
    cmd = ["sudo", "systemctl","restart","bluetooth"]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to restart Bluetooth: {result.stderr.strip()}")