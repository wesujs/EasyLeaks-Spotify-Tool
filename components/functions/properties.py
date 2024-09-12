from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB
import os

class Properties:
    def __init__(self, file_path, title, artist):
        self.file_path = file_path
        self.title = title
        self.artist = artist

    def change_mp3_metadata(self):
        try:
            # Load the MP3 file
            audio = MP3(self.file_path, ID3=ID3)

            # If there's no ID3 tag, add one
            if audio.tags is None:
                print("No ID3 tag found. Adding a new one.")
                audio.add_tags()

            # Set the title
            audio.tags['TIT2'] = TIT2(encoding=3, text=self.title)
            
            # Set the artist
            audio.tags['TPE1'] = TPE1(encoding=3, text=self.artist)

            # Save the changes
            audio.save()

            print(f"Updated metadata for {self.file_path}")
            print(f"Title set to: {self.title}")
            print(f"Artist set to: {self.artist}")

            # Double-check that the tags were set correctly
            audio = MP3(self.file_path, ID3=ID3)
            print("Actual metadata after update:")
            print(f"Title: {audio.tags.get('TIT2').text[0] if 'TIT2' in audio.tags else 'Not set'}")
            print(f"Artist: {audio.tags.get('TPE1').text[0] if 'TPE1' in audio.tags else 'Not set'}")

        except Exception as e:
            print(f"Error updating metadata: {str(e)}")
            import traceback
            traceback.print_exc()

    def verify_metadata(self):
        try:
            audio = MP3(self.file_path, ID3=ID3)
            print(f"Verifying metadata for {self.file_path}")
            print(f"Title: {audio.tags.get('TIT2').text[0] if 'TIT2' in audio.tags else 'Not set'}")
            print(f"Artist: {audio.tags.get('TPE1').text[0] if 'TPE1' in audio.tags else 'Not set'}")
        except Exception as e:
            print(f"Error verifying metadata: {str(e)}")