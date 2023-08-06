from src.core.domain.participant import Participant
from src.core.domain.stats import Stats
from src.core.domain.tournament import Tournament
from src.core.domain.tournament.services.tournament_parser import TournamentParser

import json


class JsonParser(TournamentParser):
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self) -> Tournament:
        with open(self.file_path) as json_file:
            data = json.load(json_file)
            return Tournament(
                participants=[
                    Participant(
                        name=participant["name"],
                        stats=Stats(
                            strength=participant["stats"]["strength"],
                            intelligence=participant["stats"]["intelligence"],
                            dexterity=participant["stats"]["dexterity"],
                            constitution=participant["stats"]["constitution"],
                        ),
                    )
                    for participant in data
                ]
            )
