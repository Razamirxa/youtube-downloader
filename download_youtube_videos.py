import os
import sys
import subprocess

def download_video(url, save_path):
    try:
        command = [
            "yt-dlp",
            "-f", "18/22/best[ext=mp4]",
            "-o", f"{save_path}/%(title)s.%(ext)s",
            url
        ]
        subprocess.run(command, check=True)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def bulk_download(file_path, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            download_video(url, save_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_txt_file> <download_folder>")
        sys.exit(1)

    file_path = sys.argv[1]
    save_path = sys.argv[2]
    bulk_download(file_path, save_path)
