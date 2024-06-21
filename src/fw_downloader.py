import requests
import os

def download_firmware(url_list, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)  # Create the folder if it doesn't exist

    for url in url_list:
        try:
            # Extract the original file name from the URL
            original_filename = os.path.basename(url)
            full_save_path = os.path.join(save_path, original_filename)
            
            # Make the request to download the file
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Check for HTTP errors

            with open(full_save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive new chunks
                        file.write(chunk)
            print(f"Firmware downloaded successfully and saved to {full_save_path}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download the firmware from {url}: {e}")


if __name__ == '__main__':
    firmware_urls = [
        "https://static.tp-link.com/TL-WR940N(US)_V4_160617_1476690524248q.zip",
        "https://static.tp-link.com/resources/software/TL-WR1043ND_V1_140319.zip",
        "https://static.tp-link.com/resources/software/TL-WA801ND_V1_130131_beta.zip"
    ]
    save_path = "../fws"
    download_firmware(firmware_urls, save_path)
