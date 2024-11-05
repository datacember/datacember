## Quereying the server

usage:

from datacember import antartica

```
with antartica("username", "password") as db:
	content = db("SELECT * FROM davis"_)
	print(content)
```
