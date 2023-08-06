from typing import Optional, Self
from src.core.domain.stats.types import StatsTypes
from src.core.domain.stats import Stats
from src.core.domain.base_entity import BaseEntity


class Participant(BaseEntity):
    def __init__(self, name: str, stats: Optional[Stats] = None):
        self.name = name
        self.stats = stats or Stats.from_random()

    def fight(self, other: Self, stat: StatsTypes) -> Self:
        self_stat = getattr(self.stats, stat.value)
        other_stat = getattr(other.stats, stat.value)

        return self if self_stat >= other_stat else other

    def __eq__(self, other: Self) -> bool:
        return self.name == other.name or super().__eq__(other)

    def __dict__(self):
        return {
            "name": self.name,
            "stats": self.stats.__dict__()
        }
