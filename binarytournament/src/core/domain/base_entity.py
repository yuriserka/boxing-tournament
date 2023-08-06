from abc import ABC, abstractmethod
import json


class BaseEntity(ABC):
    def __str__(self) -> str:
        return json.dumps(self.__dict__(), indent=2)

    @abstractmethod
    def __dict__(self) -> dict:
        raise NotImplementedError("This method must be implemented")
