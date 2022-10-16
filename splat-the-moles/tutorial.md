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

    TODO: Explain why list laid out like that.

Run your program now — click the green flag.

This looks just about alright, although the holes are a bit high up.
Let's make it so they're a bit lower down the screen.  To do this, we
want to write some code that runs as soon as the green flag is
clicked.  In Scratch, we would do something like

``` scratch
when green flag clicked:
  go to x: (0) y: (-70)
```

where the `x: 0` means we want the sprite centred left-to-right, and
the `y: -70` means we want the sprite a bit lower than the centre
top-to-bottom.

In Pytch we do something very similar.  We need a line of Python code
which works as the "hat block", and also a line of Python code which
does the same job as the "go to" block.  One new thing in Pytch is
that we need to give our script a _name_.  (If you want to know the
details, what we're doing is _defining_ a Python _function_.)

We'll use the name `pop_up_and_down`, because in a minute, this script
will also make the mole pop up from a random hole and then back down
underground.

The code we need to add looks like this:

{{< commit init-Mole-position-and-costume >}}

Check you understand what each of these three lines of code is doing,
and then try running your program again.  The row of mole holes should
be nearer the bottom of the stage now.  You can adjust the `-70` if
you think it would look better a bit higher or lower.


## Add actual mole costumes

Our Mole sprite now needs the rest of its costumes, to show it popping
up out of each of the holes.  We add more costumes to the `Costumes`
list:

{{< commit add-Mole-other-costumes >}}

This won't make any difference to what the game does, because we
haven't yet told the mole to switch to any of these costumes.  We'll
do that next.

    TODO: This is why we laid out the Costumes list like that.


## Pop out of random holes

To make the mole pop up out of random holes, we're going to need to
ask Python for some random numbers.  In Scratch, we would use the
random number block

``` scratch
pick random (2) to (4)
```

### Saying we want to use random-number functions

The Scratch `pick random` block is always available, but in Python we
have to say we want to use the Python equivalent.  This is a bit like
how in Scratch we need to turn on extensions like the _Music_ or _Pen_
blocks.

In Python, we _import_ the functions that let us choose different
sorts of random numbers by adding this line just underneath the
`import pytch` that's already there at the top of our program:

{{< commit import-random >}}

This lets us use Python's random-number functions.

### Choosing a random hole to pop out of

And now we can write some code to get the mole to keep popping up in
different holes.  In Scratch, we might do something like

``` scratch
forever
  wait (pick random (0.5) to (1)) seconds
  switch costume to (pick random (2) to (4))
```

In Python we do something very similar.  The Python equivalent of
Scratch's `forever` is `while True:`.  The Pytch functions we need for
the 'body' of the `while` loop are `pytch.wait_seconds()` and
`self.switch_costume()`, and then also the functions to get a random
number.  There are some important differences:

* Scratch guesses (usually correctly!) whether you want whole-number
  random numbers or numbers which can have a fractional part.  Python
  has separate functions for the two jobs:

    * `random.randint(lowest, highest)` chooses a random whole number
      from `lowest` to `highest` inclusive.

    * `random.uniform(lowest, highest)` chooses a random number
      anywhere between `lowest` and `highest`, not necessarily a whole
      number.

* In Scratch, you give the position of a thing in a list by calling
  the first one _position 1_, the second one _position 2_, and so on.
  Python _counts from zero in this situation_, so in Python, the first
  thing in a list is at _position 0_.

Just like Scratch, you can say which costume you want to switch to
either by name, or by number.  We want to choose between the costumes
at positions `1`, `2`, and `3` (remember Python counts from `0`).

Putting this all together, we want to add this code to our
`pop_up_and_down()` method in the `Mole` sprite:

{{< commit Mole-loop-random-holes >}}

There's quite a lot going on in just the two lines inside the `while
True:`, so take some time to make sure you're happy with what we're
doing.

### Waiting underground

The final piece to make the mole hide underground in between popping
out of random holes is to add something like the Scratch blocks

``` scratch
wait (pick random (0.5) to (1)) seconds
switch costume to (all-empty v)
```

inside the `forever` block.

We'll add two lines of Python code which match these two Scratch
blocks to the end of the code inside our `while True:` loop:

{{< commit hide-Mole-between-popping-up >}}

Try this!  The mole should go round and round spending a random time
underground and then popping out of a random hole for a random time.

Adjust the numbers used with `random.uniform()` if you think the mole
should spend more or less time popped up or underground.

### Experiment with a deliberate bug (optional)

If you're curious to see what happens, make a deliberate mistake by
changing the `3` in the line

``` python
self.switch_costume(random.randint(1, 3))
```

to `10`, to give

``` python
self.switch_costume(random.randint(1, 10))
```

and running your program.  If the random number Python comes up with
is bigger than 3, you'll get an error like

``` text
ValueError: could not switch to Costume number 8 in class "Mole": it only has 4 Costumes
```

After you've fixed the deliberate mistake, come back to this
"Tutorial" tab.


## Set up scoring

Now let's start making the code which lets the player try to splat the
mole.  The Mole will keep score of how many times the player has
managed to splat it.

To keep track of something, our program will use a _variable_.  It
will be like a "this sprite only" variable in Scratch.  In Python, to
create a variable, you just set it to a value.  There's no separate
step to create it.

At the very start of the game, we want to set the score to zero,
because the player hasn't splatted any moles yet.  So we'll add a
when-green-flag script which sets the score to zero:

{{< commit set-up-scoring >}}

If you run the game, nothing will happen yet, because we're not doing
anything with the `score` variable.  In Scratch we could display the
score by checking the check-box next to the variable, or by using this
block:

``` scratch
show variable [score v]
```

Pytch does have a command like that block, but we have to give a bit
more information.  We have to say who owns the variable, and we can
also, if we want, say where on the stage the variable display should
appear.  The `score` variable belongs to the Mole, which is called
`self` inside a script.  And we want to put the score display just a
bit in from the top-right of the stage.

Putting this together, we want to add this line underneath the code we
just wrote:

{{< commit show-score >}}

Try this now — you should see a `score 0` display on the stage.


## Let player hit left hole

Now let's make it so the player can try to splat the mole!

We'll make the game be controlled by the keyboard.  The player will:

* press `j` to aim at the left hole;

* press `k` to aim at the centre hole;

* press `l` to aim at the right hole.

We'll get the code right for `j` (the left hole) first, and then see
what changes are needed for the other two.

### Running a script when a key is pressed

In Scratch we would use the hat block

``` scratch
when [j v] key pressed
```

and we can do the same thing in Pytch, remembering that we have to
give a name to the script.  We'll add the start of a new script to our
Mole sprite:

{{< commit add-hit-left-hat-block >}}

If you try to run this now, you'll get a _Syntax Error_ saying _There
is a body or indentation missing_.  Python needs a script (_function_)
to have a _body_, and we haven't written it yet.

### Knowing if the mole is popped out of the left hole

There are a couple of things we need to know next:

* How do we know which costume the mole is wearing?  Remember that
  there is one costume for each hole the mole might pop out of, as
  well as a costume for when the mole is hiding underground.

* How do we do different things depending on whether the mole is
  popped out of the left hole?

For the first question, we can get Pytch to tell us what costume the
mole is wearing.  In Scratch, we could use this reporter block:

``` scratch
(costume [number v])
```

We can do something similar in Pytch, by using `self.costume_number`
inside a Mole script.

If the mole is popped out of the left hole, this will be `1`.  If the
mole is popped out of another hole, it will be `2` or `3` (depending
which hole), and if the mole is hiding underground, it will be `0`
(the "all-empty" costume is the first one, which is at _position 0_).

So we want to ask

> Is the mole's costume number equal to 1?

and then only give the player a point if the answer is 'yes'.  Scratch
has an `if` block for this, which we would use something like

``` scratch
if <(costume [number v]) = (1)> then
  change [score v] by (1)
```

One thing to watch out for is that in Python, we ask whether two
things are equal by writing `==`, which has _two_ equals signs.
Remembering this, the code looks like:

{{< commit add-hit-left-basic-body >}}

### What if the player misses?

But this is now too easy.  The player can just keep pressing `j` and
whenever the mole pops out of the left hole, the player scores a
point.  There needs to be a way to discourage the player from doing
this.

Let's be harsh — if the player misses, they lose all their points.
This should happen if the player presses `j` but the mole is _not_ in
costume number `1`.  We need something like Scratch's

``` scratch
if <> then
else
end
```

block.  In Python, it's very similar — we add an `else` to the `if` we
already have:

{{< commit lose-points-if-miss-left >}}

You might think this is a bit _too_ harsh!  Have a look at the
_Challenges_ at the end of this tutorial for some other ideas.

### Make a splatted mole go back underground

There's still a small way the player can get more points.  If they
keep hitting `j` while the mole is popped up out of the left hole,
they can rack up points.

Let's make the mole go back underground if the player has splatted it.
We can do this just by making it switch back to the `"all-empty"`
costume:

{{< commit left-hit-return-underground >}}

Try it now!


## Add sound effects

Let's add some sounds to the game.  This tutorial comes with some
examples, or you can use your own.

Just as we need to list the image files we want a sprite to be able to
use for its costumes, we need to list the sound files we want a sprite
to be able to use.

Add a variable `Sounds` near the top of the Mole sprite, just after
the `Costumes`:

{{< commit add-sounds >}}

Now we just need to start the right sound playing depending on whether
the player has hit the mole or missed it.  To play the "splat"
sound if they hit it, add this code:

{{< commit play-splat-if-hit-left >}}

And to play a "thud" sound if they miss, add:

{{< commit play-thud-if-miss-left >}}


## Let player hit other holes

We've done all the work now.  We can finish the game by copying  the
code for the left hole, and pasting it twice — once for the centre
hole and once for the right — with small changes.

We need to be very careful that we make the changes we need when
copy/pasting.  To change the left-hole code into code for the
centre-hole, we need to:

* React to the `k` key (instead of the `j` key).

* Give the function a different name: `hit_centre` (instead of
  `hit_left`).

* In the `if` statement, ask whether `self.costume_number` is equal to
  `2` (instead of `1`).

Making these changes, we get this new code for the centre hole:

{{< commit copy-paste-edit-for-centre >}}

And along the same lines, we get this for the right hole:

{{< commit copy-paste-edit-for-right >}}

(If you're wondering whether there's a better way, have a look at the
advanced challenges in the next chapter.)

### Game complete!

Try the finished game!


## Challenges

Maybe you can think of ways to make this game better.  Here are some
ideas:

* Find a different backdrop.

* Perhaps it's a bit harsh for the player to lose all their points
  when they miss.  Maybe they should lose some fixed number of points
  instead.  Change the code (in three places!) so that the player
  loses five points if they miss.  You can use the Python operator
  `-=` to subtract points.  What happens if they only have three
  points when they miss?

* Adjust the difficulty of the game by making the mole stay out of its
  hole for a longer or shorter time.

* Add some more backdrops, and change between them as the player gets
  more points.

* Make the game get more difficult as the player gets more points.


### Advanced challenges

* Refactor to remove dup'd code.

* Try implementing the "one sprite per hole" approach.

## Credits

We have used various freely-available resources to create this
project:

{{< asset-credits >}}
