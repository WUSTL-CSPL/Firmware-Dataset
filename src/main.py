from fw_downloader import download_firmware
from fw_unpacker import unpack_firmware

def main(firmware_urls, save_path):
    download_firmware(firmware_urls, save_path)
    unpack_firmware(save_path)

if __name__ == '__main__':
    # Three firmware samples
    firmware_urls = [
        "https://static.tp-link.com/TL-WR940N(US)_V4_160617_1476690524248q.zip",
        "https://static.tp-link.com/resources/software/TL-WR1043ND_V1_140319.zip",
        "https://static.tp-link.com/resources/software/TL-WA801ND_V1_130131_beta.zip"
    ]
    save_path = "../fws"
    main(firmware_urls, save_path)
    