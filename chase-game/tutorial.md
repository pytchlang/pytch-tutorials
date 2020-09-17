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

For this example I've chosen the name "Bird" but really you could name
it nearly anything you like. It has to be a single word, but Python
will count "_" as a letter so you can use a name like "Fancy_Bird" if
you like, and it can't be a name that Python or Pytch are already
using (so you can't call it "Sprite" for example, because Pytch
already uses that). Finally, Python treats capital letters and lower
case letters as different, so if you call it "bird" that's a different
name to "Bird" (this always trips people up at first).

Did you notice that the line ends with a ":" symbol? This signals to Python
that we will be adding more lines inside this class, which we will do
in a moment.

{{< commit create-bird-class >}}

Once we have created the new Sprite the next job is to say what it
looks like and how it behaves. In this tutorial we have already added
some graphics for the bird costume to the project, so let's connect
them to the sprite.

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

Usually sprites need a few instructions to set them up when the
project first loads. For example, Sprites in Pytch start out hidden
and we would like to see our bird!

In Python these instructions are organised together into functions,
which are like stacks of instructions. You use the functions
contained inside a Sprite to control it.

These lines add a new script called "start". The word "def" (short for
"define")begins it. Like the class there is a ":" at the end of the
line to say that there will be more lines after that will be part of
this function. Between the function's name and the ":" there is a list
of _variable_ names in brackets. Pytch needs at least one. The name
doesn't matter, but it's traditional to call it "self".

{{< commit add-start-def >}}

Now we can add the instructions that are part of the function. Each
line is indented so that it is inside the definition. To make the
sprite appear we use this line:

{{< commit show-bird >}}

There is still one thing missing, which is that we haven't told Pytch
_when_ this function should happen. The easiest thing is to have it
run when we click the green flag. To do that we need to put a "hat" on
the function, like this:

{{< commit green-flag-show >}}

Finally, we can see the results of our work! Press the Build button
(nothing seems to happen on the stage at first, because the Sprite
hasn't done the "start" function yet. But when you press the Green
flag you should see a giant bird appear!

The bird is very big because the image we are using is big. We can fix
that by setting the size of the Sprite. We can do this by adding
another line to the "start" function that sets the size to 30%. This line has to be indented
exactly as much as the other line that is _inside_ the function:

{{< commit set-bird-size >}}
