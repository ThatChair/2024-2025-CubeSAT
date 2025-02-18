import subprocess

def calculate_average(previous_average, new_value, size):
    if size <= 1:
        return new_value
    else:
        return previous_average + (1 / size) * (new_value - previous_average)

def start_server_receiving_at(directorypath:str):
    cmd = ["/usr/libexec/bluetooth/obexd","-r", directorypath, "-a"]

    process = subprocess.Popen(cmd, capture_output=True, text=True)

    if process.returncode != 0:
        raise RuntimeError(f"Failed to start obexd: {process.stderr.strip()}")
    
    return process

def restart_bluetooth():
    cmd = ["sudo", "systemctl","restart","bluetooth"]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Failed to restart Bluetooth: {result.stderr.strip()}")

def stop_server_receiving(process):
    process.terminate()
    process.wait()