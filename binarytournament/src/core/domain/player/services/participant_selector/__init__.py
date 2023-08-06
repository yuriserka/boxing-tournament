from src.core.domain.tournament import Tournament
from src.core.utils.logger import Logger


logger = Logger(__name__)


class ParticipantSelectorService:
    def __init__(self, tournament: Tournament):
        self.tournament = tournament

    def execute(self):
        total_participants = len(self.tournament.participants)
        idx = self._get_input()
        while idx < 0 or idx >= total_participants:
            logger.info(
                f"Invalid selection. Please select a number between 0 and {total_participants - 1}"
            )
            idx = self._get_input()

        self.tournament.select_player_participant(idx)

    def _get_input(self) -> int:
        return int(input("Select a champion: "))
