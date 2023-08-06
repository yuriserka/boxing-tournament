from src.core.domain.stats.services.stat_selector import StatSelectorService
from src.core.domain.player import Player
from src.ui import Ui
from src.core.utils.logger import Logger

logger = Logger(__name__)


class StatSelectorUi(Ui):
    def __init__(self, player: Player):
        self.player = player
        self.stat_selector_service = StatSelectorService(player)

    def render(self) -> None:
        logger.info("Select your stat to fight: ")
        stats_items = self.player.stats.__dict__().items()

        for idx, stat in enumerate(stats_items):
            stat_value = stat[1] if idx != self.player.last_selected_stat_index else '---'
            logger.info(f"{idx}: {stat[0]} -> {stat_value}")

        self.stat_selector_service.execute()
