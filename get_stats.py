import re
import numpy as np

player_win_count = 0
opponent_win_count = 0
player_turns = []
opponent_turns = []
fh = open("tests/logs.log")
for line in fh:
    if 'Player' in line:
        player_win_count += 1
        match = re.search('([0-9]{1,})', line)
        player_turn_count = int(match.group(0))
        player_turns.append(player_turn_count)
    else:
        opponent_win_count += 1
        match = re.search('([0-9]{1,})', line)
        opponent_turn_count = int(match.group(0))
        opponent_turns.append(opponent_turn_count)
fh.close()

player_avg_turns = np.average(player_turns)
opponent_avg_turns = np.average(opponent_turns)

print("Player Win Count: {}".format(player_win_count))
# print("Player Turns: {}".format(player_turns))
print("Player Avg Turns: {}".format(player_avg_turns))


print("Opponent Win Count: {}".format(opponent_win_count))
# print("Opponent Turns: {}".format(opponent_turns))
print("Opponent Avg Turns: {}".format(opponent_avg_turns))
