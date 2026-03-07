
""" 
Why Folder Manager Matters:
- By default, iOS only exposes certain  folders like DICM.
- With AFC (Windows) or ifuse (Linux), we can create new directories inside the accessible space.
- These folders will then show up in the Files app on iOS, so user can drop files there and later copy them to your PC
"""

import os
import platform
import subprocess

def create_custom_folders():
    system = platform.system()
    
    folders = ["DownloadDocs", "WhatsAppDocs", "TelegramDocs", "GeneralDocs"]
    
    if system == "Windows":
        try:
            #for now, we simulate folder creation since AFC calls are complex
            
            #later: use AFC funtion from mobileDevice.dll
            
            for folder in folders:
                print(f"simulating creation of {folder} on iphone (Windows AFc)")
            return True
        except Exception as e:
            print(f"Error creating folders on windows: {e}")
            return False
        
    elif system == "Linux":
        try:
            mount_point = "/mnt/iphone"
            for folder in folders:
                path = os.path.join(mount_point, folder)
                os.makedirs(path, exist_ok=True)
                print(f"created {folder} at {path}")
                return True
            
        except Exception as e:
            print(f"Error creating folders on linuc: {e}")
            return False
    
    else:
        print(f"Usupported system: {system}")
        return False
    

if __name__ == "__main__":
    create_custom_folders()
    

