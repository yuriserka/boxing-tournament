from src.core.utils.logger import Logger
from src.core.domain.stats.types import StatsTypes
from src.core.domain.participant import Participant

logger = Logger(__name__)

class Player(Participant):
    def __init__(self, participant: Participant):
        super().__init__(participant.name, participant.stats)
        self.last_selected_stat_index = None

    def select_stat(self, idx: int) -> None:
        if idx == self.last_selected_stat_index:
            raise Exception("You can't select the same stat twice in a row")

        self.last_selected_stat_index = idx
        

    def get_fight_attribute(self) -> StatsTypes:
        return list(StatsTypes)[self.last_selected_stat_index]

    def __dict__(self):
        return {
            **super().__dict__(),
            "last_selected_stat_index": self.last_selected_stat_index
        }
