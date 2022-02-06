def make_album(artist,title,songs=0):
    album = {
        "artist":artist,
        "title":title,
        "songs":songs,
    }
    return album

# 8-7 Examples
# print(make_album("Pink Floyd","The Dark Side of the Moon"))
# print(make_album("Pink Floyd","Wish You Were Here"))
# print(make_album("Pink Floyd","Animals"))
# print(make_album("Pink Floyd","The Wall",23))

sentinel = True
while sentinel:
    albumArtist = input("Enter album artist: ")
    albumTitle = input("Enter album title: ")
    print("Added: ",make_album(albumArtist,albumTitle))
    if (input("Add another? Type y to continue: ") != "y"):
        sentinel = False    