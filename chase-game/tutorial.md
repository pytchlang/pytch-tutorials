#Chase game

In this tutorial we will make a game where you control a bird that
chases a star around the stage.

---

Pytch programs are written in a programming language called Python, to
which we have added extra commands for Sprites, sounds, and other
things. You make a Pytch project by writing a Python program using the
special Pytch system.

The first line tells Python that we will be using the Pytch
add-ons. If you leave this out then you can only write ordinary Python
programs without Sprites, so the Pytch web site puts that line in for
you when you make a new project.


Next we will tell Python that we want _all_ the pytch features (later on we'll see why it's useful to sometimes only include some features).

When you see a block of code like this, with some lines of text shown
in green with "+" symbols in front of them, it's telling you to change
your project so that it has the new lines in green added to it. Add
them in exactly the places where they are shown.

{{< commit import specifics >}}

---

## Creating the first Sprite

We'll start with the sprite that the player will control.

To create a new sprite we need to say three things: that we are
creating a new "thing" in the project, give the thing a name, and say
that it is a Sprite (rather than a Background or some other sort of
thing). In Pytch we can do that by making a new "class" and giving it a name.

For this example I've chosen the name "Bird" but really you could name it
nearly anything you like.

{{< commit create-bird-class >}}

Once we have created the new Sprite the next job is to say what it
looks like and how it behaves. In this tutorial we have already added some graphics for the bird costume to the project, so let's connect them to the sprite.

We need to write a line that set up a _variable_
in the new Sprite that will hold a list of the costumes.

Pytch needs to find the list in a variable named ```Costumes``` (with
a capital ```C```). If we call it anything else then Pytch won't be
looking in the right place when it goes to find the costumes.

We have to list four things for each costume: the costume name (so
that we can select it for the sprite to wear), the _file_ that has the
image for the costume, and two numbers saying where the centre of the
costume is.

Finally, so that the instruction is contained _within_ the Sprite - that
is, it's pushed in from the left of the program a bit. This is how
Python knows that this variable is part of the Sprite. Everything
that's part of the Sprite has to be "indented" (pushed in) the same
amount.

We put this together with a line like this:

{{< commit bird-costume >}}

In Pytch Sprites start out invisible, so we need to add some
instructions to select the costume and show the sprite.

These lines add a new script (Python calls these "functions" instead
of scripts) to the Sprite. The word "def" followed by the name of the
function makes it, and the lines that are indented more than the first
line are the instructions that are contained within the script.

The name "__init__" is special -- that function is started
automatically when the project loads, so we can use it to set some
things up.

{{< commit init-bird-1 >}}

Finally, we can press the "Build" button and see the results of this work!
