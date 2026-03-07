import platform
import logging

# Configure logging
logging.basicConfig(
    filename="iphone_tool.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def notify(message, level="info"):
    system = platform.system()

    # Log the message
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.debug(message)

    # Show notification
    if system == "Windows":
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("iPhone Tool", message, duration=5)
        except Exception as e:
            logging.error(f"Notification error: {e}")
            print(f" Notification error: {e}")

    elif system == "Linux":
        try:
            import subprocess
            subprocess.run(["notify-send", "iPhone Tool", message])
        except Exception as e:
            logging.error(f"Notification error: {e}")
            print(f"Notification error: {e}")

    else:
        print(f"Unsupported system: {system}")