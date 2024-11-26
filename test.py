from datacember import antartica

with antartica(username="default", password="demo", url="http://192.168.1.109:8997") as db:
    content = db("SELECT * FROM mawson LIMIT 2;")
    for row in content:
        print(row)
