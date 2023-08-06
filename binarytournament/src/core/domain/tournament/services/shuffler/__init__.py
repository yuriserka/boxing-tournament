import random
from typing import List


class Shuffler:
    @staticmethod
    def shuffle(items: List) -> List:
        shallow_copy = items.copy()
        return random.shuffle(shallow_copy) or shallow_copy