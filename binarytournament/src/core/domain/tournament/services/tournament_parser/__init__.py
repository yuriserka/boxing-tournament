from abc import ABC, abstractmethod

from src.core.domain.tournament import Tournament


class TournamentParser(ABC):
    @abstractmethod
    def parse(self) -> Tournament:
        raise NotImplementedError("This method must be implemented")
