import os
import subprocess
import tempfile
import streamlit as st

st.set_page_config(page_title="YouTube Video Downloader", page_icon="??")

if "downloaded_files" not in st.session_state:
    st.session_state.downloaded_files = []

def fetch_video(url):
    temp_dir = tempfile.mkdtemp()
    try:
        command = [
            "yt-dlp",
            "-f", "18/22/best[ext=mp4]",
            "-o", f"{temp_dir}/%(title)s.%(ext)s",
            url
        ]
        subprocess.run(command, check=True, text=True, capture_output=True)
        
        files = os.listdir(temp_dir)
        if files:
            file_name = files[0]
            file_path = os.path.join(temp_dir, file_name)
            return True, file_path, file_name
    except subprocess.CalledProcessError as e:
        return False, f"Error: {e.stderr}", None
    return False, "Not found", None

st.title("YouTube Video Downloader ??")
st.markdown("Download videos directly to your device.")

url_input = st.text_input("Paste YouTube URL here:")

if st.button("Prepare Download"):
    if url_input.strip():
        with st.spinner("Fetching video..."):
            success, path, name = fetch_video(url_input.strip())
        if success:
            st.session_state.downloaded_files.append((name, path))
            st.success("Ready! Click below to download.")
        else:
             st.error(path)

if st.session_state.downloaded_files:
    st.divider()
    st.subheader("Your Downloads")
    for name, path in st.session_state.downloaded_files:
        if os.path.exists(path):
            with open(path, "rb") as f:
                st.download_button(label=f"?? {name}", data=f, file_name=name, mime="video/mp4", key=path)
