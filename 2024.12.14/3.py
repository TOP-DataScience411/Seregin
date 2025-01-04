from pathlib import Path
from utils import load_file
from importlib.util import spec_from_file_location, module_from_spec

def ask_for_file():
    while True:
        path_for_file = Path(input('Введите путь к файлу:'))
        
        if path_for_file.is_file():
            copy_file = load_file(path_for_file)
            spec = spec_from_file_location("conf", str(copy_file))
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module 
        else:
            print('По указанному пути файла не существует. Попробуйте еще раз.')