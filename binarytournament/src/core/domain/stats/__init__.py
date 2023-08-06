from src.core.domain.base_entity import BaseEntity
from src.core.domain.stats.types import StatsTypes
import random


class Stats(BaseEntity):
    def __init__(
        self,
        strength: int,
        intelligence: int,
        dexterity: int,
        constitution: int
    ):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.constitution = constitution

    @staticmethod
    def from_random():
        return Stats(
            strength=random.randint(1, 100),
            intelligence=random.randint(1, 100),
            dexterity=random.randint(1, 100),
            constitution=random.randint(1, 100)
        )

    def __dict__(self):
        return {
            StatsTypes.STRENGTH.value: self.strength,
            StatsTypes.INTELLIGENCE.value: self.intelligence,
            StatsTypes.DEXTERITY.value: self.dexterity,
            StatsTypes.CONSTITUTION.value: self.constitution
        }
