import platform
import subprocess
import ctypes
import os

def mount_device():
    """ this actually open the iphone filesystem so we can browse and later create folders """
    
    system = platform.system()
    
    if system == "Windows":
        try:
            #psth to MobileDevice.dll
            
            dll_path = r"C:\Program Files\Common Files\Apple\Mobile Device Support\MobileDevice.dll"
            if not os.path.exists(dll_path):
                print("MobileDevice.dll not found.")
                return False
            
            #load DLL
            
            mobile_device = ctypes.CDLL(dll_path)
            print("MobileDevice.dll loaded.")
            
            #todo: call AFC funtion here
            
            print("simulating afc mount: iphone filesystem accessible.")
            return True
        except Exception as e:
            print(f"Error mounting device on windows: {e}")
            return False
    
    elif system == "Linux":
        try:
            mount_point = "/mnt/iphone"
            os.makedirs(mount_point, exist_ok=True)
            
            #run ifuse to mount iphone
            
            subprocess.run(["ifuse", mount_point], check=True)
            print(f"iphone mounted at {mount_point}")
            return True
        
        except Exception as e:
            print(f"Error mounting device on linux: {e}")
            return False
    else:
        print(f"Unsurpported system: {system}")
        

if __name__ == "__main__":
    mount_device()