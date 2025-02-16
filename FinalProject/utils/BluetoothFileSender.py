import subprocess
import re
import shlex

class BluetoothFileSender:

    def __init__(self, device_address: str, channel:int = None):
        self.address = device_address
        self.channel = channel

        if self.channel is None:
            self.channel = self.discover_obex_channel()
            if self.channel is None:
                raise RuntimeError("No OBEX Object Push service found. Please open \"Recieve A File\" menu on reciving windows device and try finding channel again")
        
    def discover_obex_channel(self):

        cmd = ["sdptool", "browse", self.device_address]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to run sdptool: {result.stderr.strip()}")
        
        output = result.stdout

        found_push_service = False
        channel_pattern = re.compile(r"Channel:\s+(\d+)")

        for line in output.splitlines():
            line = line.strip()
            if "Service Name: OBEX Object Push" in line:
                found_push_service = True
                continue
            
            if found_push_service:
                match = channel_pattern.search(line)
                if match:
                    return match.group(1)
        return None

    def send_files(self, file_paths):
        """
        :param file_paths: List of absolute paths to send.
        """
        cmd = [
            "obexftp"
            "--bluetooth", self.device_adress,
            "--channel", str(self.channel),
            "--uuid none",
            "--nopath",
            "--put"
        ]
        cmd.extend(file_paths)

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"obexftp failed. Return code {result.returncode}. "
                               f"Stderr: {result.stderr.strip()}")
        
        else:
            print("Successfully sent files")