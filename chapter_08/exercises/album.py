def make_album(artist_name, title):
    """ Describe a music album """
    album = {
        "artist": artist_name.title(),
        "album": title.title()
    }

    return album


album = make_album("KANYE WEST", "808S & HEARTBREAK")
print(album)
album = make_album("RADIOHEAD", "IN RAINBOWS")
print(album)
album = make_album("MARY J. BLIGE", "WHAT'S THE 411?")
print(album)
