import collections
from typing import List, Optional, Dict, Set, Tuple


__all__ = [
    'RecursiveDict',
]

Point = Tuple[int, int]


DIAGONAL_DIRECTIONS: List[Point] = []
for dy in range(-1, 2):
    for dx in range(-1, 2):
        if dx != 0 or dy != 0:
            DIAGONAL_DIRECTIONS.append((dy, dx))


SQUARE_DIRECTIONS: List[Point] = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


class RecursiveDict(object):
    def __init__(self):
        self._root = {}

    @property
    def root(self):
        return self._root

    @classmethod
    def build_word_index(cls, words: List[str]) -> 'RecursiveDict':
        word_index = RecursiveDict()
        for word in words:
            node = word_index
            for letter in word:
                node = node[letter]
            node[None]  # marker for word end
        return word_index

    def search_words(
        self,
        input_matrix: List[str], *,
        directions: Optional[List[Point]] = None,
    ) -> Dict[str, List[List[Point]]]:
        if directions is None:
            directions = SQUARE_DIRECTIONS

        paths: Dict[str, List[List[Point]]] = collections.defaultdict(list)

        for y, row in enumerate(input_matrix):
            for x, letter in enumerate(row):
                self._recursive_search(
                    input_matrix,
                    x=x, y=y,
                    paths=paths,
                    directions=directions,
                )

        return paths

    def _recursive_search(
        self,
        input_matrix: List[str], *,
        x: int, y: int,
        paths: Dict[str, List[List[Point]]],  # result paths
        prefix: str = '',
        used_points: Optional[Set[Tuple[int, int]]] = None,
        path: Optional[List[Tuple[int, int]]] = None,
        directions: List[Point],
    ) -> None:
        rows = len(input_matrix)
        cols = len(input_matrix[0])

        if used_points is None:
            used_points = set()
        else:
            used_points = set(used_points)
        used_points.add((y, x))

        if path is None:
            path = list()
        else:
            path = list(path)
        path.append((y, x))

        letter = input_matrix[y][x]

        if letter == 'е' and letter not in self and 'ё' in self:
            letter = 'ё'

        if letter in self:
            if None in self[letter]:
                word = prefix + letter
                paths[word].append(path)

            for dy, dx in directions:
                new_y = y + dy
                new_x = x + dx
                if (
                    0 <= new_y < rows and
                    0 <= new_x < cols and
                    (new_y, new_x) not in used_points
                ):
                    if letter in self:
                        self[letter]._recursive_search(
                            input_matrix,
                            x=new_x, y=new_y,
                            paths=paths,
                            prefix=prefix + letter,
                            used_points=used_points,
                            path=path,
                            directions=directions,
                        )

    def __getitem__(self, k) -> 'RecursiveDict':
        if k not in self._root:
            self._root[k] = type(self)()
        return self._root[k]

    def __contains__(self, k) -> bool:
        return k in self._root

    def __len__(self) -> int:
        return len(self._root)

    def __repr__(self) -> str:
        return '<{} size={}>'.format(type(self).__name__, len(self))
