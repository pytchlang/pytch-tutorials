# Bunner: make a frogger-like game

In this tutorial we will make a complete [Frogger](https://en.wikipedia.org/wiki/Frogger)-style arcade game.

## Making the stage

Let's start by getting a nice backdrop up. I've drawn one already, so we can just load the image.

First, we make a Stage class. We can call it anything we want so long as it is declared as being a Stage. The second line of the class sets up a Python variable with the list of background images that we can use (there's only one for now but we will add more).

Each background has a name that we'll use in our code when we want to switch backgrounds. We also have to list the file name from the Pytch examples folder that we want to use. 

{{< commit background-hollow-class >}}

Every Python object has to have an initialisation function. Pytch will use this to create the Stage as soon as the program is loaded (even before the Green Flag is clicked).

{{< commit Add Stage initialisation >}}

I've added two steps in this initialisation: the first activates the _standard_ Stage setup which lets Pytch link in the stage object. If you forget this line then the Stage won't work properly.

The second step selects a backdrop to show so that the canvas has something in it right away.
