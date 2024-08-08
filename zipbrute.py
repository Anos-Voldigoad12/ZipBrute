import zipfile
import sys
from tqdm import tqdm

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
        passwords = passwords.readlines()
        found = False
        print()
        for i in tqdm(range(len(passwords)),desc="Bruteforcing...",ascii=False,ncols=75):            
            if check_password(zip_ref,passwords[i].strip()):
                found = True
                break
        if found:
            print()
            print("\033[33mFound the Correct Password: ",passwords[i].strip(),"\033[m")
            print()
        else:
            print()
            print("\033[31mNo Suitable Password Found\033[m")
            print()
except zipfile.BadZipfile:
    print("Invalid zip file")
