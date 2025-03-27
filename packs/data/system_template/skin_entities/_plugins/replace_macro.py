'''
This scripts implements a simple macro for text replacement to modify the
mod_tool.ts script. It replaces the specified key with a value defined in
scope.
'''
from typing import Any
import json
from pathlib import Path

def replace_macros(
        map_py_item: dict[str,Any],
        replacements: list[str, Any]) -> list[str, Any]:
    '''
    Replace the text read from the source file with the values in the
    replacements. The source is the _map.py item. The replacements is the
    list of key-value pairs to replace, where the key is a string and the
    value is a JSON serializable object.
    '''
    if 'source' not in map_py_item:
        return map_py_item
    source_path = Path(map_py_item['source'])
    if not source_path.exists():
        print(
            "The 'replace_macro.py' plugin couldn't identify the source file. "
            "of the _map.py item:\n"
            f"{json.dumps(map_py_item, indent=4)}\n"
            "The replace_macro function requires the source file to be an "
            "exact path. Using the glob patterns is not supported. If you "
            "used the glob pattern, this is the source of the error. It's "
            "also possible that the source file doesn't exist.\n"
        )
        return map_py_item
    with source_path.open('r', encoding='utf-8') as f:
        text = f.read()
    for key, value in replacements.items():
        text = text.replace(key, json.dumps(value))
    with source_path.open('w', encoding='utf-8') as f:
        f.write(text)

    # Pass throug the source _map.py item
    return map_py_item