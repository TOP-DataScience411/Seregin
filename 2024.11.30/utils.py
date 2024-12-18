from textwrap import wrap
import shutil

def important_message(text: str) -> str:

    terminal_width = shutil.get_terminal_size().columns - 1  

    wrapped_text = wrap(text, width=(terminal_width - 4)) 

    result = '=' * terminal_width + '\n'
    
    result += '#' + ' ' * (terminal_width - 2) + '#\n'

    for line in wrapped_text:
        result += f"#  {line.center(terminal_width - 4)}  #\n"

    result += '#' + ' ' * (terminal_width - 2) + '#\n'
   
    result += '=' * terminal_width

    return result
