games = {
    "Halo": {
        "console" : "Xbox",
        "genre" : "fps",
        "year" : 2001,
    },
    "Metal Gear Solid" : {
        "console" : "Playstation",
        "genre" : "stealth",
        "year" : 1998,
    },
    "Super Mario Bros" : {
        "console" : "Nintendo Entertainment System",
        "genre" : "platform",
        "year" : 1985,
    },
}
print("----- Games -----")
for game, info in games.items():
    print(game)
    for g in info:
        print("\t",g,":",info[g])