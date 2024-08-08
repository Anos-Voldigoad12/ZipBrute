import zipfile
import sys

def check_password(zip_ref, password):
    try:
        zip_ref.setpassword(pwd=bytes(password,'utf-8'))
        zip_ref.testzip()
        return True
    except RuntimeError:
        return False
    except Exception:
        return False

if len(sys.argv)!=3:
    print("Usage: zipbrute.py <zip> <wordlist>")
    sys.exit()
try:
    zip_ref = zipfile.ZipFile(sys.argv[1],'r')
    with open(sys.argv[2],'r') as passwords:
        for password in passwords.readlines():            
            if check_password(zip_ref,password.strip()):
                print()
                print("\033[33mFound the Correct Password: ",password.strip(),"\033[m")
                print()
                break
            else:
                print("Skipping: ",password.strip())
except zipfile.BadZipfile:
    print("Invalid zip file")
    
