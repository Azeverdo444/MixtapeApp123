from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for tracks
tracks = [
    {"title": "Track 1", "artist": "Head Over Heels  - Tears for fears", "duration": "4:16", "file": "Head_Over_Heels.mp3"},
    {"title": "Track 2", "artist": "Heaven Or Las Vegas - Cocteau Twins", "duration": "3:50", "file": "Cocteau Twins - Heaven Or Las Vegas (Official Video).mp3"},
    {"title": "Track 3", "artist": "A Lovely Night - La La Land", "duration": "3:57", "file": "A Lovely Night (Lyrics) - Ryan Gosling ft Emma Stone.mp3"},
    {"title": "Track 4", "artist": "City Of Stars - La La Land", "duration": "2:26", "file": "'City of Stars' (Duet ft. Ryan Gosling, Emma Stone) - La La Land Original Motion Picture Soundtrack.mp3"},
    {"title": "Track 5", "artist": "Girls - The Dare", "duration": "2:06", "file": "The Dare - Girls.mp3"},
    {"title": "Track 6", "artist": "Charli xcx - 360", "duration": "2:13", "file": "Charli xcx - 360 (official lyric video).mp3"},
    {"title": "Track 7", "artist": "Chappell Roan - After Midnight", "duration": "3:25", "file": "Chappell Roan - After Midnight (Official Audio).mp3"},
    {"title": "Track 8", "artist": "Chappell Roan - Subway", "duration": "4:07", "file": "the subway lyrics  ｜｜ chappell roan unreleased ♡.mp3"},
    {"title": "Track 9", "artist": "Fleetwood Mac - Silver Springs", "duration": "4:49", "file": "Silver Springs (2004 Remaster).mp3"},
    {"title": "Track 10", "artist": "Glee Cast - Creep", "duration": "3:58", "file": "Creep (Glee Cast Version).mp3"},
    {"title": "Track 11", "artist": "Soundgarden - Black Hole Sun", "duration": "5:21", "file": "Soundgarden - Black Hole Sun.mp3"},
    {"title": "Track 12", "artist": "Foo Fighters - Everlong", "duration": "4:11", "file": "Foo Fighters - Everlong.mp3"},
    {"title": "Track 13", "artist": "Lego Batman - Who's the (Bat)man", "duration": "3:04", "file": "Whos the (Bat) Man.mp3"},
    {"title": "Track 14", "artist": "Hole - Celebrity Skin", "duration": "2:44", "file": "Hole - Celebrity Skin (Official Music Video).mp3"},
    {"title": "Track 15", "artist": "Hole - Doll Parts", "duration": "3:35", "file": "Hole - Doll Parts.mp3"},
    {"title": "Track 16", "artist": "Jeff Buckley - So Real", "duration": "4:39", "file": "Jeff Buckley - So Real.mp3"},
    {"title": "Track 17", "artist": "I Know Its Over - The smiths", "duration": "5:49", "file": "The Smiths - I Know It's Over (Official Audio).mp3"},
    {"title": "Track 18", "artist": "Something - The Beatles", "duration": "3:08", "file": "The Beatles - Something.mp3"},
    {"title": "Track 19", "artist": "Hey Jude - The Beatles", "duration": "3:59", "file": "Hey Jude (Remastered 2015).mp3"},
    {"title": "Track 20", "artist": "The girl from impanema", "duration": "2:55", "file": "The Girl From Ipanema.mp3"},
    {"title": "Track 21", "artist": "Copacabana -  Barry Manilow", "duration": "3:57", "file": "Copacabana (At the Copa).mp3"},
    {"title": "Track 22", "artist": "Succsession - Main theme", "duration": "1:41", "file": "Succession (Main Title Theme) - Nicholas Britell ｜ Succession (HBO Original Series Soundtrack).mp3"},
    {"title": "Track 23", "artist": "Dress to impress theme", "duration": "5:33", "file": "＂Dress Up Theme＂ from Dress To Impress.mp3"},
    {"title": "Track 24", "artist": "Disco - Surf Curse", "duration": "3:58", "file": "Surf Curse - Disco.mp3"},

]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mixtape_name = request.form.get("mixtape_name", "My Mixtape")
        message = request.form.get("message", "It's so Julia")
        color = request.form.get("color", "#f0f0f0")
        return render_template("index.html", tracks=tracks, mixtape_name=mixtape_name, message=message, color=color)

    return render_template("index.html", tracks=tracks)

if __name__ == "__main__":
    app.run(debug=True)
