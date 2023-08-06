import random
from src.core.domain.player.services.participant_selector import ParticipantSelectorService
from src.core.utils.logger import Logger
from src.ui import Ui
from src.core.domain.tournament import Tournament

logger = Logger(__name__)


class ParticipantSelectorUi(Ui):
    def __init__(self, tournament: Tournament):
        self.tournament = tournament
        self.participant_selector_service = ParticipantSelectorService(tournament)

    def render(self) -> None:
        logger.info(f"Select your champion to fight: ")

        for idx, participant in enumerate(self.tournament.participants):
            stats_items = participant.stats.__dict__().items()
            stat_to_show_idx = random.randint(0, len(stats_items) - 1)
            hidden_stats = {
                stat[0]: stat[1] if idx == stat_to_show_idx else '???' for idx, stat in enumerate(stats_items)
            }
            logger.info(f"{idx}: {participant.name} -> {hidden_stats}")

        self.participant_selector_service.execute()
