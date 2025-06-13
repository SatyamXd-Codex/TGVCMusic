import yt_dlp

def get_audio(query):
    try:
        ydl_opts = {
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "quiet": True,
            "outtmpl": "downloads/%(title)s.%(ext)s",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)["entries"][0]
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print("YT ERROR:", e)
        return None
