from typing import Optional
from src.core.domain.base_entity import BaseEntity
from src.core.domain.participant import Participant
from src.core.domain.stats.types import StatsTypes
from src.core.utils.logger import Logger
import random

logger = Logger(__name__)


class Battle(BaseEntity):
    def __init__(
        self,
        attacker: Participant,
        defender: Participant,
        stat: Optional[StatsTypes] = None
    ):
        self.attacker = attacker
        self.defender = defender
        self.stat = stat or random.choice(list(StatsTypes))
        self.winner: Optional[Participant] = None

    def run(self) -> (Participant, dict):
        self.winner = self.attacker.fight(self.defender, self.stat)
        report = self._get_report()

        return self.winner, report

    def _get_report(self):
        return self.__dict__()

    def __dict__(self):
        return {
            "attacker": self.attacker.name,
            "defender": self.defender.name,
            "stat": self.stat.value if self.stat else None,
            "winner": self.winner.name if self.winner else None
        }
