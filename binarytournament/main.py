from src.ui.participant_selector import ParticipantSelectorUi
from src.core.domain.tournament.services.tournament_parser.csv_parser import CsvParser
from src.core.utils.logger import Logger

logger = Logger(__name__)


def main():
    parser = CsvParser("data/participants.csv")
    tournament = parser.parse()

    ParticipantSelectorUi(tournament).render()

    tournament.build_matchups()
    tournament.battle()

    logger.info(f"Tournament: {tournament}")


if __name__ == "__main__":
    main()
