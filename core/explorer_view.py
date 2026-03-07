import platform
import subprocess
import os

"""
    opens the file manager (Windows Explorer or Linux Nautilus) so the user
    immediately sees the iPhone
    folders when the device connects.
"""
def open_explorer():
    system = platform.system()
    
    if system == "Windows":
        try:
            #open files explorer at iphone mount point (simulated for now)
            
            #later replace with actual AFC path once implemented
            import os
            os.startfile(r"C:\Program Files\Common Files\Apple\Mobile Device Support")
            print(" File Explorer opened to iPhone support folder.")
            return True
        except Exception as e:
            print(f"Error opening Explorer: {e}")
            return False

    elif system == "Linux":
        try: 
            mount_point = "/mnt/iphone"
            if os.path.exists(mount_point):
                subprocess.run("xdg-open", mount_point)
                print(f"Nautilus open at {mount_point}")
                return True
            else:
                print("mount point not found.")
                return False
            
        except Exception as e:
            print(f"Error opening Natilus: {e}")
            return False
    else:
        print(f"Unsupported system: {system}")
        return False
    

if __name__ == "__main__":
    open_explorer()