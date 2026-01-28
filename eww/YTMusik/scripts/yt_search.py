#!/usr/bin/env python3
import sys
import subprocess
import os

def play_yt(input_data):
    MPV = "/usr/bin/mpv"
    YTDLP = "/usr/bin/yt-dlp"
    
    # --- LA SOLUCIÓN ANTI-LOCURA ---
    # Mata cualquier mpv anterior antes de empezar el nuevo
    subprocess.run(["pkill", "mpv"], stderr=subprocess.DEVNULL)
    
    if input_data.startswith("http"):
        url = input_data
    else:
        try:
            # Buscamos el ID
            search_cmd = [YTDLP, "--get-id", f"ytsearch1:{input_data}"]
            video_id = subprocess.check_output(search_cmd).decode('utf-8').strip()
            url = f"https://www.youtube.com/watch?v={video_id}"
        except:
            return

    # Lanzamos el nuevo audio
    cmd = [
        MPV,
        "--no-video",
        "--ytdl-raw-options=yes-playlist=",
        url
    ]
    
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        play_yt(sys.argv[1])
