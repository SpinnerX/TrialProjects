![Screenshot 2023-09-26 at 8 43 38 PM](https://github.com/SpinnerX/TrialProjects/assets/56617292/de5f892a-c994-475c-998f-6f138c2ead69)


## Overview
For the SJSU Robotics Intelligent Systems trial project, I implemented the pathfinder Dijkstra's algorithm to help solve a maze. Which allows users to drag the mouse to see the different kinds of ways the maze could be solved.

## Resourceful Links
`https://www.youtube.com/watch?v=KiCBXu4P-2Y&t=286s&ab_channel=WilliamFiset` - useful idea from this YouTube to help with maze generator. \
 `https://youtu.be/sVcB8vUFlmU?si=_65d2dp7PNN2aAZb` - video used as part of the journey in looking into maze generation  \
 `https://www.youtube.com/watch?v=jZQ31-4_8KM&ab_channel=RocketsandRobotics` - video that discusses visually on how maze generation works.

## Design
For this trial project the design was to easily simulate how a maze solver would initially solve a maze, in real-time. So, a creative way that I wanted to look into was animating how thhe lines would adjust when the user is allowed to change the ending point.

So, I designed the project in two parts

## Issues Occurred
The issues that I came across was generating and ranomizing how mazes would be generated

First part - Maze generation
- If you look at how the maze is generated, is we simply create a tile grid based on the maze dimensions. Where we use DFS to visually chhange thhe tile grid and filter out thhe lines of each tile, generating the maze.
- Hence creating an offset of based on the amount of tiles a and then grabbing the starting and ending of vertical lines. As handling the offsets. As we have offsets for both the horizontal lines, top-left, top-right corners of a tile.
-  Including offsets representing as the lines diagonaly that help generate and connect bottom left and right corners of tiles.

## Implementation
- Using Dijkstra's Algorithm, for the maze solver
- Simulating how to demonstrate how Dijkstra's work when given a different ending points, simulating how this can work in various environments

## UI Features
### Mouse Clicks
`Right-click` - To stop from tracking thhe mouse to leave the algorithm in place \
`Left-click`  - To start the algorithm and drag your mouse to see the different possibilities this algorithm may use \
`Middle-click` - To clear the maze, and re-generate a new maze. \
`Click Escape` - To exit the window

### Buttons
`Generate New` - Click on this button to generate a new randomized maze \
`Clear` - Clears and resets the maze
