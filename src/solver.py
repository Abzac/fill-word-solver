import logging
import sys
from typing import List, Union

import resources
from recursive_dict import RecursiveDict


LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

MatrixType = List[Union[str, List[str]]]


INPUT_MATRIX: MatrixType = [
    'междас',
    'огоугм',
    'сорбро',
    'кдтуон',
    'вйфашд',
    'аефлан',
]


def print_word_matrix(matrix, path):
    for y, row in enumerate(matrix):
        print_row = '\t'.join(
            letter if (y, x) in path else '#' for x, letter in enumerate(row)
        )
        print(print_row)


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    logger = logging.getLogger()

    words = resources.load_dict_files()
    logger.info(f'Loaded %d words', len(words))
    if len(words) == 0:
        raise Exception('No words found in dictionaries')

    matrix = INPUT_MATRIX

    logger.info('Building word index...')
    word_index = RecursiveDict.build_word_index(words)

    logger.info('Searching...')

    paths = word_index.search_words(matrix)

    logger.info(f'Found %d words', len(paths))

    sys.stdout.flush()
    print()
    for word in sorted(paths, key=lambda word: (-len(word), word)):
        word_paths = paths.get(word)

        print(f'==== {word} ({len(word_paths)}) ====')
        for path in word_paths:
            print_word_matrix(matrix, path)
            print()

    logger.info('Found words: %d', len(paths))


if __name__ == '__main__':
    main()
