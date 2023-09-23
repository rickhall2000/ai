# Pick and drop example
from Reinforcement Learning and Deep RL Python (Theory and Projects)

## Environment
The board is 10 x 10
player can move up, down, left, right, or can pick up or drop off
In the exmaple the player starts at 0,9, the item is at 0,0 and the finish is at 9,9

## Rewards
* try to go off the field = -10
* legal move = -1
* pick up when the item is not there (or already picked up) -10
* agent picks up the item +20
* drop off in the wrong place -10
* drop off in the correct place +20