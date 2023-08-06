from src.core.domain.player import Player
from src.core.utils.logger import Logger


logger = Logger(__name__)


class StatSelectorService:
    def __init__(self, player: Player):
        self.player = player

    def execute(self):
        stats_items = self.player.stats.__dict__().items()

        while True:
            idx = self.get_input()
            while idx < 0 or idx >= len(stats_items):
                logger.info(f"Invalid selection. Please select a number between 0 and {len(stats_items) - 1}")
                idx = self.get_input()    

            try:
                self.player.select_stat(idx)
                break
            except Exception as e:
                logger.info(f"{e}. Please select a different stat.")
    
    def get_input(self) -> int:
        return int(input("Select a stat: "))