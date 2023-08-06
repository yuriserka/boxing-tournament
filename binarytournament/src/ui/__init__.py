from abc import ABC, abstractmethod


class Ui(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError()
