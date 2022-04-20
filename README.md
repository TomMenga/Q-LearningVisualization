# Q-LearningVisualization

Hey there :wave:,  
this is a simple application of the [Q-learning](https://en.wikipedia.org/wiki/Q-learning) algorithm in a "Find the exit from the maze" game.  
It is part of my bachelor-degree thesis project where I explored the use of AI algorithms in video games. 

The entities modelled are:
* The escapee (as the Red dot)
* The escapee skills (a set _K_ of movement actions)
* The maze (an _NxM_ matrix of walls, trap-pits, neutral tiles and finally, the __exit__)

The final goal is to find the shortest path to the exit using only the available movement skills (for example, you can only move like the knight in chess).

<img src="https://user-images.githubusercontent.com/12052575/164197844-51c12101-80e6-41c7-8207-d1f54174e065.png" height="300">

There are some hard-to-watch violations of the SOLID principles, but I prefer to freeze the project as it was, as a memento of a long-gone past 😢
