# platform: HackerRank
# kit: Interview Preparation Kit
# title: Jumping on the Clouds
# url: https://www.hackerrank.com/challenges/jumping-on-the-clouds/

# description:
# There is a new mobile game that starts with consecutively numbered clouds. 
# Some of the clouds are thunderheads and others are cumulus. 
# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
# The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
# It is always possible to win the game.
# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

def jumping_on_clouds(c):
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps