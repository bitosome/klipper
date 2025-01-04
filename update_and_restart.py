import subprocess
import sys

def git_pull():
    try:
        result = subprocess.run(
            ["git", "pull"],
            cwd="/home/pi/printer_data/config",  # Update to your specified directory
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error during git pull: {e.stderr}"

def restart_klipper():
    try:
        subprocess.run(["sudo", "systemctl", "restart", "klipper"], check=True)
        return "Klipper firmware restarted."
    except subprocess.CalledProcessError as e:
        return f"Error restarting Klipper: {e.stderr}"

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action == "pull":
        print(git_pull())
    elif action == "restart":
        print(restart_klipper())
    else:
        print("Usage: update_and_restart.py [pull|restart]")