import pathlib
from typing import Optional, List


__all__ = [
    'iterate_dict_files',
    'load_dict_files',
]


DEFAULT_DICTS_PATH = '../data/dictionaries/'
DEFAULT_DICT_EXTENSIONS = {'dic', 'txt'}


def iterate_dict_files(
    dicts_path: Optional[str] = None, *,
    extensions: Optional[str] = None,
) -> List[str]:
    if dicts_path is None:
        dicts_path = DEFAULT_DICTS_PATH

    if extensions is None:
        extensions = DEFAULT_DICT_EXTENSIONS

    for path in pathlib.Path(dicts_path).iterdir():
        if any(path.name.endswith(ext) for ext in extensions):
            yield path


def load_dict_files(
    dicts_path: Optional[str] = None, *,
    extensions: Optional[str] = None,
    min_word_length: int = 3,
):
    words: List[str] = []

    for path in iterate_dict_files(dicts_path, extensions=extensions):
        data = pathlib.Path(path).read_text(encoding='utf-8')
        new_words: List[str] = [
            word.strip().lower() for word in data.split('\n')
            if ' ' not in word and '-' not in word and word.strip() and
            len(word.strip()) > min_word_length
        ]
        words.extend(new_words)

    return words
