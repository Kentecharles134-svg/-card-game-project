class CmpPlayer:
    def __init__(self, name="Computer"):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        return None

    def add_point(self):
        self.score += 1


class HmnPlayer(CmpPlayer):
    def __init__(self, name):
        super().__init__(name)

    def play_card(self):
        input(f"{self.name}, press Enter to play your card...")
        return super().play_card()
