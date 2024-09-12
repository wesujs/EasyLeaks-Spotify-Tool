import logging
import sys
import subprocess
import os
import traceback
import re
import time
import tkinter as tk
from tkinter import font as tkfont
import customtkinter as ctk
from tkinter import filedialog
import yt_dlp
import threading
import pyglet
from PIL import Image, ImageTk

from components.functions.properties import Properties
from components.functions.get_song_info import GetSongInfo

# Setup the logger to write to error.txt
logging.basicConfig(filename='error.txt', 
                    filemode='a',  # 'a' will append to the file, 'w' will overwrite it
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)

def log_error(e):
    """Logs the exception to error.txt and prints the stack trace."""
    logging.error("Unhandled Exception: ", exc_info=True)  # Logs error with traceback
    print(f"An error occurred: {str(e)}")
    traceback.print_exc()  # For console output (optional)


def main():
    # App Custom Settings
    app = ctk.CTk()
    app.configure(fg_color="#000")

    # App Title
    app.title("Easy Leaks")

    # Logo/Icon Change
    absolute_path = os.path.abspath("app_icon.ico")
    app.iconbitmap(absolute_path)
    print(absolute_path)

    #lock screen size settings
    app.geometry("500x500")
    app.resizable(False, False)

    global folder_path
    folder_path = None

    def get_link_value():
        link_value = link_entry.get()
        return link_value

    # Input user's Local Files Locations
    def get_local_folder():
        global folder_path
        folder_path = filedialog.askdirectory()
        if folder_path:
            label.configure(text=f"Selected Folder: {folder_path}")
        else:
            label.configure(text="No folder selected")


    def download_process():
        link_value = get_link_value()
        song_info = GetSongInfo(link_value)

        # Update the progress bar on the main thread
        def update_progress_bar():
            progress_bar.pack(pady=10)
            progress_bar.start()

        app.after(0, update_progress_bar)

        def download_audio(song_info):
            try:
                song_info.download_audio()

                if song_info.downloaded_path:
                    print(f"File downloaded: {song_info.downloaded_path}")
                else:
                    print("File not detected, but proceeding with metadata changes and move attempt.")
                    if song_info.find_downloaded_file(max_attempts=5, delay=2):
                        print(f"File found on retry: {song_info.downloaded_path}")
                    else:
                        print("File still not found. Proceeding with best guess.")
                        song_info.downloaded_file = f"{song_info.sanitized_title}.mp3"
                        song_info.downloaded_path = os.path.abspath(song_info.downloaded_file)

                if os.path.exists(song_info.downloaded_path):
                    properties = Properties(song_info.downloaded_path, song_info.title, song_info.artist)
                    properties.change_mp3_metadata()
                    print(f"Updated metadata for: {song_info.downloaded_file}")

                    # Verify metadata before moving
                    properties.verify_metadata()

                    if folder_path:
                        target_file_path = os.path.join(folder_path, song_info.downloaded_file)
                        print(f"Attempting to move file to: {target_file_path}")
                        try:
                            os.rename(song_info.downloaded_path, target_file_path)
                            print(f"Successfully moved {song_info.downloaded_file} to: {folder_path}")
                            
                            # Verify metadata after moving
                            moved_properties = Properties(target_file_path, song_info.title, song_info.artist)
                            moved_properties.verify_metadata()
                        except Exception as move_error:
                            print(f"Error moving file: {str(move_error)}")
                            print(f"File remains in: {os.path.dirname(song_info.downloaded_path)}")
                    else:
                        print(f"No folder selected, file saved in: {os.path.dirname(song_info.downloaded_path)}")
                else:
                    print(f"File not found at {song_info.downloaded_path}. Unable to update metadata or move file.")

            except Exception as e:
                print(f"Error in download_audio: {str(e)}")
                import traceback
                traceback.print_exc()
            finally:
                # Stop and hide the progress bar on the main thread
                def stop_progress_bar():
                    progress_bar.stop()
                    progress_bar.pack_forget()

                app.after(0, stop_progress_bar)

        # Create and start the download thread, passing song_info as an argument
        download_thread = threading.Thread(target=download_audio, args=(song_info,))
        download_thread.start()

    # Load Custom Font
    def load_custom_font(font_path, size, weight="normal"):
        current_dir = os.getcwd()
        abs_font_path = os.path.abspath(os.path.join(current_dir, font_path))
        print(f"Attempting to load font from: {abs_font_path}")
        
        if not os.path.exists(abs_font_path):
            raise FileNotFoundError(f"Font file not found: {abs_font_path}")
        
        # Load the font using pyglet
        pyglet.font.add_file(abs_font_path)
        font_name = pyglet.font.load(os.path.splitext(os.path.basename(abs_font_path))[0]).name
        
        # Create and return a CTkFont object
        return ctk.CTkFont(family=font_name, size=size, weight=weight)

    # Load your custom font
    try:
        custom_font = load_custom_font("KGHAPPY.ttf", 24)
        print("Custom font loaded successfully!")
    except Exception as e:
        print(f"Error loading font: {e}")
        # Fallback to a system font if custom font fails to load
        custom_font = ctk.CTkFont(family="Helvetica", size=24)
        print("Fallback font loaded.")

    # Create a frame to hold all the widgets
    content_frame = ctk.CTkFrame(app, fg_color="transparent")
    content_frame.pack(expand=True)

    # Title for App
    title = ctk.CTkLabel(content_frame, text="Easy Leaks", font=custom_font, height=30, text_color="#1DB954")
    title.pack(pady=10, padx=20)

    # Button to find spotify Local file location
    file_button = ctk.CTkButton(content_frame, text="Open Folder",fg_color="#1DB954", command=get_local_folder)
    file_button.pack(pady=(0, 10), padx=20, fill='x')

    # Label to display the selected folder path
    label = ctk.CTkLabel(content_frame, text="No folder selected", text_color="#1DB954")
    label.pack(pady=10, padx=20)

    # Entry for youtube link
    link_entry = ctk.CTkEntry(content_frame, placeholder_text="Enter Link", justify="center", placeholder_text_color="#2dc962", fg_color="#000", text_color="#1DB954")
    link_entry.pack(pady=10, padx=20, fill='x')

    # Download, Change Properties, Then Add To spotify library
    download_button = ctk.CTkButton(content_frame, text="Add to Spotify",fg_color="#1DB954", command=download_process)
    download_button.pack(pady=10, padx=20, fill='x')

    # Create the progress bar
    progress_bar = ctk.CTkProgressBar(content_frame, progress_color="#1DB954")

    app.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(e)  # Call the log_error function to handle the error