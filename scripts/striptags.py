import re, os

directory = 'corpus/watch_raw'
for entry in os.scandir(directory):
	if entry.is_file():
		with open(entry.path, encoding="utf-8") as f:
			text = f.read()
			text = re.sub('\[.*\]', '', text)
		path = entry.path.replace( 'watch_raw', 'watch' )
		with open(path, "w", encoding="utf-8") as f:
			f.write(text)


