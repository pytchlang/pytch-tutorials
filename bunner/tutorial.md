# Bunner: make a frogger-like game

In this tutorial we will make a complete [Frogger](https://en.wikipedia.org/wiki/Frogger)-style arcade game.

## Making the stage

Let's start by getting a nice backdrop up. I've drawn one already, so we can just load the image.

First, we make a Stage class. We can call it anything we want so long as it is declared as being a Stage. The second line of the class sets up a Python variable with the list of background images that we can use (there's only one for now but we will add more).

Each background has a name that we'll use in our code when we want to switch backgrounds. We also have to list the file name from the Pytch examples folder that we want to use. 

{{< commit background-hollow-class >}}

Every Python object has to have an initialisation function. Pytch will use this to create the Stage as soon as the program is loaded (even before the Green Flag is clicked).

{{< commit add-stage-initialisation >}}

I've added two steps in this initialisation: the first activates the _standard_ Stage setup which lets Pytch link in the stage object. If you forget this line then the Stage won't work properly.

The second step selects a backdrop to show so that the canvas has something in it right away.

If you build the project now you'll notice that the stage backdrop does not actually appear. That's because there is one more thing we need to do in order to have the Stage hooked up to our project. We need to _register_ it with Pytch. We will have to do this for each new Sprite class as well, so that the Pytch project knows about them.

{{< commit register-stage >}}

If you don't register the Stage (or any Sprites) with Pytch then they won't respond to any events (including the program starting), and they won't 

## Create our hero

There is not much to do in our game yet, so let's add something for the player to control. 

We want to talk about Sprites:

{{< commit import-Sprite >}}

The graphics are already there for the players sprite, all we have to do is create a class and set up the names of the costumes. Like the stage, the name of our new class is up to us, but we have to declare that it's a kind of ```Sprite```.

{{< commit simple-player-sprite >}}

Each costume has two numbers after it - these are the position of the _centre_ of the costume. The Bunny graphics are 60 pixels wide and 60 pixels tall, so that puts it right in the centre of the costume. When we issue a ```go_to_xy``` command it's that point on the costume that will be at exactly the ```x``` and ```y``` coordinates.

We select a costume and make sure that the Bunny actor is visible.

{{< commit register-player-sprite >}}

Like the stage, we have to connect up our Sprite to the rest of the Pytch system.

### Moving our hero

Now let's give the player a way to move the bunny around. We need to import the Pytch keyboard event.

{{< commit import-when-key-pressed >}}

Now we can create a function that will move the bunny up the screen, and tell Pytch to run that function whenever the up arrow key is pressed on the keyboard. We add a simple check of the bunny Y-coordinate to make sure that it is never moved off the top of the screen.

{{< commit move-bunny-up >}}

