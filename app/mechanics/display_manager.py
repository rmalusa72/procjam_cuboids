class DisplayManager:
    @classmethod
    def initial_paint(cls, game):
        screen = game.display.set_mode((300, 300))

        # Draw the ground
        game.draw.rect(screen, game.Color("#77AB59"), game.Rect(0, 290, 300, 10))
