# Hello there!

In this tutorial we will learn about how to create and run a Pytch project with a Sprite.

---

## Writing a Pytch program

Pytch programs are written in a programming language called Python, to
which we have added extra commands for Sprites, sounds, and other
things. You make a Pytch project by writing a Python program using the
special Pytch system.

The first line tells Python that we will be using the Pytch
add-ons. If you leave this out then you can only write ordinary Python
programs without Sprites, so the Pytch web site puts that line in for
you when you make a new project.


Next we will tell Python that we want _all_ the pytch features (later
on we'll see why it's useful to sometimes only include some features).

When you see a block of code like this, with some lines of text shown
in green with "+" symbols in front of them, it's telling you to change
your project so that it has the new lines in green added to it. Add
them in exactly the places where they are shown.

{{< commit import-specifics >}}

---

## Creating the Sprite

We'll start with the sprite that the player will control.

To create a new sprite we need to say three things: that we are
creating a new "thing" in the project, give the thing a name, and say
that it is a Sprite (rather than a Background or some other sort of
thing). In Pytch we can do that by making a new "class" and giving it a name.

For this example I've chosen the name "Snake" but really you could name it
nearly anything you like.

Notice that the line ends with a ":" marker. There is more to come in the definition of Snake, and this symbol is how we tell Pytch that there will be more to the Snake class.

{{< commit create-snake-class >}}

## Adding a costume

Once we have created the new Sprite the next job is to say what it
looks like and how it behaves. In this tutorial we have already added
a picture for the snake costume to the project, so let's connect
them to the sprite.

We need to write a line that set up a _variable_ in the new Sprite
that will hold a list of the costumes.

Pytch needs to find the list in a variable named ```Costumes``` (with
a capital ```C```). If we call it anything else then Pytch won't be
looking in the right place when it goes to find the costumes.

This variable contains a list of the images in the project that will
be used by this Sprite as costumes. In Python we create lists by
writing things between square brackets ([ and ] characters). When we
mention the file name we need to put it between double-quote
characters (these: "). 

Finally, so that the instruction is contained _within_ the Sprite - that
is, it's pushed in from the left of the program a bit. This is how
Python knows that this variable is part of the Sprite. Everything
that's part of the Sprite has to be "indented" (pushed in) the same
amount.

So, to create our Costumes variable we need a line like this.

{{< commit snake-costume >}}

## Adding a script

These lines add a new script (Python programmers sometimes calls these
"functions" or "methods" instead of scripts) to the Sprite. The word
"def" followed by the name of the function creates it, and the lines
that are indented more than the first line are the instructions that
are contained within the script.

{{< commit snake-speak-1 >}}

Now, we haven't yet told Pytch when it should run this script. We need
to attach a "hat" block to it, something that tells Pytch to run the
script at the right time. We can set this script to run when the Snake
sprite is clicked on.

{{< commit when-clicked >}}

## Running the Project

Finally, we can press the "Build" button and see the results of this
work! When You press Build the Snake should appear on the stage, and
when you click on it a speech balloon will appear. 

Congratulations on your first Pytch project!

