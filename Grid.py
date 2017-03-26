class Grid():
    def __init__(self, GAME_DISPLAY_WIDTH , GAME_DISPLAY_HEIGHT, GRID_DISTANCE):
        self._WIDTH = int(GAME_DISPLAY_WIDTH / GRID_DISTANCE )
        self._HEIGHT = int(GAME_DISPLAY_WIDTH / GRID_DISTANCE )

        self.grid = [[list() for i in range(self._WIDTH)] for i in range(self._HEIGHT)]
