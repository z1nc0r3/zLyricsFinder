import lyricsgenius as lg
import pyperclip as pc

genius = lg.Genius("CmK8zyrlpjTMptRr9Jh2HVnOsUh7Bj8SCNmkvKlzWSk8P7_L4ZdCtalbR_cyxzQ8", skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

song = input("Enter the song : ")
artist = input("Enter the artist name : ")

try: 
    pc.copy(genius.search_song(song, artist).lyrics)
except:
    print("No Lyrics found !")
