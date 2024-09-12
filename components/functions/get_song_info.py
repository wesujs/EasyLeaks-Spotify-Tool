import os
import re
import yt_dlp
import time

class GetSongInfo:
    def __init__(self, link):
        self.link = link
        self.original_title = ""
        self.title = ""
        self.artist = ""
        self.sanitized_title = ""
        self.downloaded_file = ""
        self.downloaded_path = ""

    def sanitize_filename(self, filename):
        sanitized = re.sub(r'[\\/*?:"<>|⧸]', "", filename)
        sanitized = re.sub(r'\s+', "_", sanitized)
        return sanitized

    def parse_title(self):
        # Split the title by hyphen or other special characters
        parts = re.split(r'[-–—_]', self.original_title, 1)
        if len(parts) > 1:
            self.artist = parts[0].strip()
            self.title = parts[1].strip()
        else:
            # If no separator found, use the whole string as the title
            self.artist = "Unknown Artist"
            self.title = self.original_title.strip()
        
        print(f"Parsed Artist: {self.artist}")
        print(f"Parsed Title: {self.title}")

    def find_downloaded_file(self, max_attempts=10, delay=1):
        for attempt in range(max_attempts):
            for file in os.listdir():
                if file.endswith('.mp3'):
                    self.downloaded_file = file
                    self.downloaded_path = os.path.abspath(file)
                    print(f"Found downloaded file: {self.downloaded_path}")
                    return True
            print(f"File not found, attempt {attempt + 1} of {max_attempts}")
            time.sleep(delay)
        return False

    def download_audio(self):
        initial_file_count = len([f for f in os.listdir() if f.endswith('.mp3')])
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
            'verbose': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print("Starting info extraction...")
                info = ydl.extract_info(self.link, download=False)
                
                self.original_title = info['title']
                self.parse_title()  # Parse the title to set artist and title
                self.sanitized_title = self.sanitize_filename(self.original_title)
                
                print(f"Original Title: {self.original_title}")
                print(f"Sanitized title: {self.sanitized_title}")
                
                print("Starting download...")
                ydl.download([self.link])
                
                if not self.find_downloaded_file():
                    print("File not found after multiple attempts. Checking for new files...")
                    current_file_count = len([f for f in os.listdir() if f.endswith('.mp3')])
                    if current_file_count > initial_file_count:
                        new_files = [f for f in os.listdir() if f.endswith('.mp3') and os.path.getmtime(f) > time.time() - 60]
                        if new_files:
                            self.downloaded_file = new_files[0]
                            self.downloaded_path = os.path.abspath(self.downloaded_file)
                            print(f"Found new file: {self.downloaded_path}")
                        else:
                            print("New file detected but not identified.")
                    else:
                        print("No new MP3 files detected.")
                
                if not self.downloaded_file:
                    print("Warning: No MP3 file found after download. Metadata changes may fail.")
                    
            except Exception as e:
                print(f"Error during download: {str(e)}")
                import traceback
                traceback.print_exc()