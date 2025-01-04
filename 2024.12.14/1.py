from pathlib import Path

def files(absolutepath: str) -> tuple[str, str] | None:

	pathdate = Path(absolutepath)
	return tuple([file.name for file in pathdate.iterdir() if file.is_file()]) if pathdate.is_dir() else None
 
 
 
 # 15:35:08 > python -i 1.py
# >>> files(r'C:\Users\dense\Data Science\Seregin\2024.12.14\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>>