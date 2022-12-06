# Wave Function Collapse

My own interpretation of the Wave Function Collapse program.

---
## What is that?
The wave function collapse program is designed to create variations of tile based images.
The program is divided into two parts, the rule maker, and the board generator.

#### 1. The Rule Maker
The rule maker takes an example 2d array of integer values, each value represents a tile type.
Here's an example:
```
0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 1 0 0 0 0
```
The rule maker then creates rules based on this image. For example `1 cannot be to the right/left of 1` or `1 can be on top/bottom of 1`.
After the rules have been generated, it passes them to the board generator.

#### 2. The Board Generator
The generator starts with a blank grid of variable size, each square in the grid is in a "superposition" of all possible values, this means that it is all possible tiles types at the same time. The generator starts by "collapsing" a random square, it does this by checking the available values (all values in superposition) and choosing one at random to assign to that square. After the first collapse, the generator updates all of the other tiles according to the rules. For example, if the first tile is collapsed to `1`, then the tiles to the left and right must be `0` according to the rules (using the example image above). The generator then collapses another square at random and this process continues until all squares have been collapsed. Then you are left with an image similar but not identical to the starting one.

## My interpretation
If you would like to try it for yourself you can either
1. Download the code and run it yourself
2. Go see the [repl.it page](https://replit.com/@Eclipz/Wavefunction-Collapse?v=1) and run it there
<br>
My interpretation was created based only on an explanation from an article I read, meaning I at no point in its development looked at anyone else's code. This is important to know because my project most likely isn't exactly as preformant or accurate as some other models, and that is why. 

## More info
For more information regarding the wave function collapse program, check out [mxgmn's github page](https://github.com/mxgmn/WaveFunctionCollapse) on the topic.

