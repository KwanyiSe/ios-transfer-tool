import platform
import os
import subprocess
import ctypes


def detect_device():
    
    """currently
    -detect on windows if an iphone is connected or not 
    -detects on lunix if an iphone is connected or not 
    """
    system = platform.system()
    
    if system == "Windows":
        dll_path = r"C:\Program Files\Common Files\Apple\Mobile Device Support\MobileDevice.dll" #using r "raw string" since python \ as escap charaters
        if os.path.exists(dll_path):
            try:
                mobile_device = ctypes.CDLL(dll_path)
                print("apple mobile device dll loaded successfully")
                #todo: call funtion from dll to list connected devices
                
                return True
            
            except Exception as e:
                print(f" Error loading MobileDevice.dll: {e}")
                return False
        else:
            print("MobileDevice.dll not found. install apple mobile device support.")
            return False
    elif system == "Linux":
        try:
            output = subprocess.check_output(["idevice_id", "-l"]).decode().strip()
            if output:
                print(f"iPhone detected:{output}")
                return True
            else:
                print("No iphone detected. ")
                return False
        except Exception as e :
            print(f"Error detecting device: {e}")
            return False
    else:
        print(f"Unsupported system; {system}")
        return False


if __name__ == "__main__":
    detect_device()