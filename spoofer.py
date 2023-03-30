import random
import os

def generate_serial():
    serial = ""
    for i in range(8):
        serial += str(random.randint(0,9))
    return serial

os.system("wmic path win32_desktopmonitor get serialnumber > monitor_serial.txt")
with open("monitor_serial.txt", "r") as f:
    lines = f.readlines()
    with open("monitor_serial.txt", "w") as f1:
        for line in lines:
            if "SerialNumber" in line:
                f1.write("SerialNumber\t" + generate_serial() + "\n")
            else:
                f1.write(line)

os.system("wmic path win32_physicalmedia get serialnumber > disk_serial.txt")
with open("disk_serial.txt", "r") as f:
    lines = f.readlines()
    with open("disk_serial.txt", "w") as f1:
        for line in lines:
            if "SerialNumber" in line:
                f1.write("SerialNumber\t" + generate_serial() + "\n")
            else:
                f1.write(line)

os.system("wmic path win32_videocontroller get serialnumber > gpu_serial.txt")
with open("gpu_serial.txt", "r") as f:
    lines = f.readlines()
    with open("gpu_serial.txt", "w") as f1:
        for line in lines:
            if "SerialNumber" in line:
                f1.write("SerialNumber\t" + generate_serial() + "\n")
            else:
                f1.write(line)

os.system("wmic path win32_processor get processorid > cpu_serial.txt")
with open("cpu_serial.txt", "r") as f:
    lines = f.readlines()
    with open("cpu_serial.txt", "w") as f1:
        for line in lines:
            if "ProcessorId" in line:
                f1.write("ProcessorId\t" + generate_serial() + "\n")
            else:
                f1.write(line)

os.system("wmic path win32_computersystemproduct get uuid > hwid_serial.txt")
with open("hwid_serial.txt", "r") as f:
    lines = f.readlines()
    with open("hwid_serial.txt", "w") as f1:
        for line in lines:
            if "UUID" in line:
                f1.write("UUID\t" + generate_serial() + "\n")
            else:
                f1.write(line)

print("Your monitor serial number is: " + generate_serial())
print("Your disk serial number is: " + generate_serial())
print("Your GPU serial number is: " + generate_serial())
print("Your CPU serial number is: " + generate_serial())
print("Your HWID serial number is: " + generate_serial())
