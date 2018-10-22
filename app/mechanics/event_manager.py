from mechanics.display_manager import DisplayManager
import sys


class EventManager:
    def __init__(self, game):
        self.game = game

    def listen(self):
        DisplayManager.initial_paint(self.game)

        for event in self.game.event.get():
            if event.type == self.game.QUIT:
                sys.exit()

        # probably extract to DisplayManager?
        self.game.display.flip()
