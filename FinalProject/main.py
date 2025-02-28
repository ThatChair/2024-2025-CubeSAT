import time
import board
from adafruit_lis3mdl import LIS3MDL
from FinalProject.utils.Gyro import Gyro
from FinalProject.utils.Integrator3d import Integrator3d
from FinalProject.utils.Pos import Pos
from FinalProject.utils.misc import *
from FinalProject.utils.ImageAnalyzer import *
from FinalProject.utils.BluetoothFileSender import BluetoothFileSender

#imu and camera initialization
i2c = board.I2C()
mag = LIS3MDL(i2c)
gyro = Gyro(i2c)
REPO_PATH = "/home/pi/Documents/Backbranch/2024-2025-CubeSAT"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "/FlatSat/Images"

#bluetooth receiving initialization
btserver = start_server_receiving_at("/home/pi/Documents/Backbranch/bluetooth_receivied")

def main():
    gyro.calibrate()
    gyro.reset()
    while True:
        gyro.update(time.time())

def img_gen(name):

    t = time.strftime("_%H%M%S")
    imgname = (f'{REPO_PATH}/{FOLDER_PATH}/{name}{t}.png')
    return imgname

sender = BluetoothFileSender("E8:BF:B8:A4:A1:F4")

time.sleep(5)
name = img_gen("TakenPhoto")
picam2.set_controls({"ExposureTime": 5, "AnalogueGain": 2.0})
picam2.start_and_capture_file(name, show_preview = False, )
image = Image.open(name)
edges = process_edges(find_edges(image.filter(ImageFilter.SHARPEN)).filter(ImageFilter.SMOOTH).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR))
out = Image.alpha_composite(after.convert("RGBA"), edges)
out.putalpha(255)
out.save("/home/pi/Documents/Backbranch/2024-2025-CubeSAT/FinalProject/Saved_Images")
sender.send_files("/home/pi/Documents/Backbranch/2024-2025-CubeSAT/FinalProject/Saved_Images/{name}")

if __name__ == '__main__':
    main()


