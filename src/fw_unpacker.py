import os
import subprocess

def unpack_firmware(save_path):
    for root, _, files in os.walk(save_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                subprocess.run(['binwalk', '-Mre', '--directory', save_path, file_path], check=True) # Run binwalk for unpacking
                print(f"Unpacked file using binwalk: {file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to unpack file {file_path} using binwalk: {e}")


if __name__ == '__main__':
    save_path = "../fws"
    unpack_firmware(save_path)
