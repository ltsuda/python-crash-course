def make_album(artist_name, title):
    """ Describe a music album """
    album = {
        "artist": artist_name.title(),
        "album_title": title.title()
    }

    return album


while True:
    artist = input(f"\nEnter an artist."
                   "(Enter 'quit' to finish the program): ")
    if artist == 'quit':
        break

    album_name = input(f"Enter the name of a music album."
                       "(Enter 'quit' to finish the program): ")
    if album_name == 'quit':
        break

    album = make_album(artist, album_name)
    print(
        f"---\nThe music album {album['album_title']} is from {album['artist']}\n---")
