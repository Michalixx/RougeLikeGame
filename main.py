from Game import Game
import settings as stt
import GUI
import stats

# Load settings and stats
stt.load_settings()
stats.load_stats()
while True:
    # GUI
    val = GUI.display_gui()
    if val == 1: break
    # Game
    g = Game()
    g.run_game()
    # Save settings and stats
    stt.save_settings()
    stats.save_stats()


