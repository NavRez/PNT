# PNT
The Pick-Numbered-Token game is a technical game played between two players : MAX and MIN. The game starts with N tokens and MAX always goes first with his first move being an odd number strictly inferior to N/2. The next chosen token needs to be a multiple or factor of the previous token. The game ends when a player has no more moves. (Ex: say N = 5, max plays 1 then min plays 3, that means max has no more moves and will lose).

The goal of this project was to explore how many nodes can be explored using an Alpha-Beta prunning tree. a txt input is given with the first value being the number of tokens and the last being the depth at which the tree needs to be explored (with 0 being to leaf nodes and N being the orignal node). There's a heuristic property that was used to define the associated heuristic values for alpha and beta. More information can be found in the PDF.

## How to run

import all of the pre-requisites and enter the desired values in your txt file. Run the code and await for the results.
