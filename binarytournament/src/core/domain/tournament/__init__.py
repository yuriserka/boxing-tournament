import math

from typing import List, Optional
from src.ui.stat_selector import StatSelectorUi

from src.core.domain.player import Player
from src.core.domain.tournament.services.shuffler import Shuffler

from src.core.utils.logger import Logger
from src.core.datastructures.binarytree import BinaryTree
from src.core.datastructures.binarytree.node import TreeNode
from src.core.domain.battle import Battle
from src.core.domain.base_entity import BaseEntity
from src.core.domain.participant import Participant

logger = Logger(__name__)


class Tournament(BaseEntity):
    def __init__(
        self,
        participants: List[Participant],
    ):
        self.participants: List[Participant] = Shuffler.shuffle(participants)
        self.tournament = BinaryTree.of_height(
            math.ceil(math.log2(len(self.participants)))
        )
        self.match_history = []
        self.player: Optional[Player] = None

    def select_player_participant(self, participant_index) -> Player:
        self.player = Player(self.participants[participant_index])
        return self.player

    def build_matchups(self):
        shuffled_participants = Shuffler.shuffle(self.participants)
        self.tournament.fill_leaves(shuffled_participants)

    def battle(self):
        def _battle(node: TreeNode):
            if node.is_leaf:
                return
            
            battle_args = [*node.children_values]
            if self.player in node.children_values:
                StatSelectorUi(self.player).render()
                battle_args.append(self.player.get_fight_attribute())

            batlle = Battle(*battle_args)
            winner, battle_report = batlle.run()
            self.match_history.append(battle_report)

            node.reset_with(winner)

        self.tournament.traverse(_battle)

    def __dict__(self):
        return {
            "participants": [p.__dict__() for p in self.participants],
            "tournament": self.tournament.__dict__(),
            "match_history": self.match_history
        }
