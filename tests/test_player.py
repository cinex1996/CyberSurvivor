from player.player import Player
class TestPlayerPosition:

    def test_player_starts_in_screen_center(self):
        play = Player(1280,720)
        assert play.x == 640 and play.y == 360

    def test_player_starts_in_center_for_different_screen_size(self):
        play = Player(1000,500)
        assert play.x == 500 and play.y == 250