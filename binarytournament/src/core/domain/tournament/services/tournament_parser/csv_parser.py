from src.core.domain.participant import Participant
from src.core.domain.stats import Stats
from src.core.domain.tournament import Tournament
from src.core.domain.tournament.services.tournament_parser import TournamentParser

import csv


class CsvParser(TournamentParser):
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self) -> Tournament:
        with open(self.file_path) as csv_file:
            participants = list(csv.DictReader(csv_file))
            return Tournament(
                participants=[
                    Participant(
                        name=participant["name"],
                        stats=Stats(
                            strength=int(participant["strength"]),
                            intelligence=int(participant["intelligence"]),
                            dexterity=int(participant["dexterity"]),
                            constitution=int(participant["constitution"]),
                        ),
                    )
                    for participant in participants
                ]
            )
