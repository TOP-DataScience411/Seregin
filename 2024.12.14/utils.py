from shutil import copy2
from pathlib import Path
import string


def files(path: Path) -> Path:

	return copy2(path, Path.cwd()/ path.name)
 
def remove_punctuation(text: str) -> str:

	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator)