# Splat the moles

We're going to write a game in Python where the player has to splat
moles to score points.  But if they miss, they lose all their points!
(Don't worry, no real moles will be harmed in making this game.)

![screenshot](screenshot-w360.jpg#img-center)

---

TODO: Write tutorial

## Create a stage with backdrop

Our first job will be to set up the Stage for our game.  This tutorial
comes with a photo of a green field.  You can check what it looks like
in the "Images and sounds" tab — come back to this "Tutorial" tab when
you've done that.

In Pytch, to make our stage, we:

* give it a name (`Field`);

* say what its backdrops should be, using a Python _list_.  Even
  though there's only one backdrop, we still need to put it in a list,
  using square bracket `[]` characters.

To do these two things, we need this code:

{{< commit add-Field-as-stage >}}

If you run your program now, with the green flag, you should see the
photo appear as the backdrop.


## Add the mole's holes

{{< work-in-progress >}}

Our next job is to add the mole.  There are a few different ways we
could do this.  One way would be to have one Sprite per hole, with a
different costume for whether the mole is hiding in the hole or
popping its head up above ground.

But we'll do it a different way.  We'll have a sprite with a costume
showing a row of mole-less holes.  We'll add three more costumes, one
with the mole popping out of the left hole, one with the mole popping
out of the centre hole, and one with the mole popping out of the right
hole.  By choosing different costumes, we can make it look like the
mole is choosing different holes to pop out of.

So what we'll do first is add the three empty holes that the mole will
pop out of.

Add a Sprite for the mole, with a "three empty holes" costume.  You
can check the "Images and sounds" tab to see what it looks like.

{{< commit add-Mole-with-all-empty >}}

Run your program now — click the green flag.

This looks just about alright, although the holes are a bit high up.
Let's make it so they're a bit lower down the screen.  To do this, we
want to write some code that runs as soon as the green flag is
clicked.  In Scratch, we would do something like

``` scratch
when green flag clicked:
  go to x: (0) y: (-70)
```

and in Pytch we do something very similar.  We need a line of Python
code which works as the "hat block", and also a line of Python code
which does the same job as the "go to" block.  One new thing in Pytch
is that we need to give our script a _name_.  (If you want to know the
details, what we're doing is _defining_ a Python _function_.)

The code we need to add looks like this:

{{< commit init-Mole-position-and-costume >}}


## Add actual mole costumes

{{< commit add-Mole-other-costumes >}}


## Pop out of random holes

{{< commit import-random >}}

{{< commit Mole-loop-random-holes >}}

{{< commit hide-Mole-between-popping-up >}}


## Set up scoring

{{< commit add-Mallet-set-up-scoring >}}

{{< commit show-score >}}


## Let player hit left hole

{{< commit add-Mallet-hit-left-basic >}}

{{< commit lose-points-if-miss-left >}}

{{< commit add-Mole-return-underground >}}

{{< commit Mallet-broadcast-left >}}


## Add sound effects

{{< commit add-Mallet-sounds >}}

{{< commit play-splat-if-hit-left >}}

{{< commit play-thud-if-miss-left >}}


## Let player hit other holes

{{< commit copy-paste-edit-for-centre >}}

{{< commit copy-paste-edit-for-right >}}


## Credits

We have used various freely-available resources to create this
project:

{{< asset-credits >}}
