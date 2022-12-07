# Splat the moles

We're going to write a game in Python where the player has to splat
moles to score points.  But if they miss, they lose all their points!
(Don't worry, no real moles will be harmed in making this game.)

![screenshot](screenshot-w360.jpg#img-center)

---

## Create a stage with backdrop

Our first job will be to set up the Stage for our game.  This tutorial
comes with a photo of a green field, `green-field.jpg`.  You can check
what it looks like in the "Images and sounds" tab — come back to this
"Tutorial" tab when you've done that.

In Pytch, to make our stage, we:

* give it a name (`Field`);

* say what its backdrops should be, using a Python _list_.  Even
  though there's only one backdrop, we still put it in a list, using
  square bracket `[]` characters.

To do these two things, we need to add this code:

{{< commit add-Field-as-stage >}}

If you run your program now, with the green flag, you should see the
photo appear as the backdrop.


## Add the mole's holes

Our next job is to add the mole.  There are a few different ways we
could do this.  For this tutorial, we'll have one sprite with a costume
showing a row of mole-less holes.  We'll add three more costumes, one
with the mole popping out of the left hole, one with the mole popping
out of the centre hole, and one with the mole popping out of the right
hole.  By making the sprite wear different costumes, we can make it
look like the mole is choosing different holes to pop out of.

(If you're wondering what other ways we could do this, have a look at
the "Challenges" chapter at the end of this tutorial.)

So we'll start off by adding the three empty holes that the mole will
pop out of.

Add a Sprite for the mole, with a "three empty holes" costume.  You
can check the "Images and sounds" tab to see what it looks like.

{{< commit add-Mole-with-all-empty >}}

(Python lets you write lists on more than one line like this.  We're
doing this because in a minute we'll need to add some more costumes,
and the code will be easier for us to read if the `Costumes` list
isn't on one big long line.)

Run your program now — click the green flag.

This looks alright, but the holes are a bit high up.  Let's make it so
they're a bit lower down the screen.  To do this, we want to write
some code that runs as soon as the green flag is clicked.  In Scratch,
we would do something like

``` scratch
when green flag clicked:
  go to x: (0) y: (-70)
```

where the `x: 0` means we want the sprite centred left-to-right, and
the `y: -70` means we want the sprite a bit lower than the centre
top-to-bottom.

In Pytch we do something very similar.  We need a line of Python code
which works as the "hat block", and a line of Python code which does
the same job as the "go to" block.  One new thing in Pytch is that we
need to give our script a _name_.  (If you want to know the details,
what we're doing is _defining_ a Python _function_.)

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

Our `Mole` sprite now needs the rest of its costumes, to show it
popping up out of each of the holes.  We can add more costumes to the
`Mole`'s `Costumes` list like this:

{{< commit add-Mole-other-costumes >}}

This won't make any difference to what the game does, because we
haven't yet told our `Mole` to switch to any of these costumes.  We'll
do that next.


## Pop out of random holes

To make the mole pop up out of random holes, we're going to need to
ask Python for some random numbers.  In Scratch, we would use the
random number block

``` scratch
pick random (2) to (4)
```

### Saying we want to use random-number functions

The Scratch `pick random` block is always available, but in Python we
have to say we want to use the Python equivalent.  This is like how in
Scratch we need to turn on extensions like the _Music_ or _Pen_
blocks.

In Python, we _import_ the functions that let us choose different
sorts of random numbers by adding this line just underneath the
`import pytch` that's already there at the top of our program:

{{< commit import-random >}}

This lets us use Python's random-number functions.

### Choosing a random hole to pop out of

And now we can write some code to get the mole to keep popping up out
of different holes.  In Scratch, we might do something like

``` scratch
forever
  switch costume to (pick random (2) to (4))
  wait (pick random (0.5) to (1)) seconds
```

In Python we do something very similar.  The Python equivalent of
Scratch's `forever` is `while True:`.  The Pytch functions we need for
the 'body' of the `while` loop are `pytch.wait_seconds()` and
`self.switch_costume()`, and then also the functions to get a random
number.

There are some important differences:

* Scratch works out whether you want whole-number random numbers, or
  numbers which can have a fractional part.  Python has separate
  functions for the two jobs:

    * `random.randint(lowest, highest)` chooses a random whole number
      ('integer') from `lowest` to `highest` inclusive.

    * `random.uniform(lowest, highest)` chooses a random number
      anywhere between `lowest` and `highest`, not necessarily a whole
      number.

* In Scratch, you give the position of an item in a list by saying the
  first item is at _position 1_, the second one is at _position 2_,
  and so on.  _Python counts from zero in this situation_, so in
  Python, the first item in a list is at _position 0_.

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
switch costume to (all-empty v)
wait (pick random (0.5) to (1)) seconds
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

and running your program.  If Python comes up with a random number
bigger than 3, you'll get an error like

``` text
ValueError: could not switch to Costume number 8 in class "Mole": it only has 4 Costumes
```

After you've fixed the deliberate mistake, come back to this
"Tutorial" tab.


## Set up scoring

Now let's start making the code which lets the player try to splat the
mole.  The `Mole` sprite will keep score of how many times the player
has managed to splat it.

To keep track of something, our program will use a _variable_.  It
will be like a "For this sprite only" variable in Scratch.  In Python,
to create a variable, you just set it to a value.  There's no separate
step to create it.

At the very start of the game, we want to set the score to zero,
because the player hasn't splatted any moles yet.  So we'll add a
when-green-flag script which sets the score to zero:

{{< commit set-up-scoring >}}

The `self.` at the start of `self.score` is what makes it a "For this
sprite only" variable.

If you run the game, you won't see anything different happen, because
we're not doing anything with the `Mole` sprite's `score` variable.
In Scratch, we could display the score by checking the check-box next
to the variable, or by using this block:

``` scratch
show variable [score v]
```

Pytch does have a command like that block, but we have to give a bit
more information: We have to say who owns the variable.  Our `score`
variable belongs to the `Mole` sprite, which as we've seen, is called
`self` inside its scripts.

Putting this together, we want to add this line underneath the code we
just wrote:

{{< commit show-score >}}

Unusually, we give the _name_ of the `score` variable as a _string_
here, so make sure you include the `""` characters.

Try this now — you should see a `score 0` display on the stage.


## Hit the left hole

Now let's make it so the player can try to splat the mole!

The game will be controlled by the keyboard.  The player will:

* press `j` to hit the left hole;

* press `k` to hit the centre hole;

* press `l` to hit the right hole.

We'll get the code right for `j` (the left hole) first, and then see
what changes are needed for the other two.

### Running a script when a key is pressed

In Scratch we would use the hat block

``` scratch
when [j v] key pressed
```

and we can do the same thing in Pytch, remembering that we have to
give a name to the script.  We'll add the start of a new script to our
`Mole` sprite:

{{< commit add-hit-left-hat-block >}}

If you try to run this now, you'll get a _Syntax Error_ saying _There
is a body or indentation missing_.  Python needs a script (_function_)
to have a _body_, and we haven't written it yet.

### Knowing if the mole is popped out of the left hole

There are a couple of things we need to know next:

* How do we know which costume the `Mole` sprite is wearing?  Remember
  that there is one costume for each hole the mole might pop out of,
  as well as a costume for when the mole is hiding underground.

* How do we do different things depending on whether the mole is
  popped out of the left hole?

For the first question, we can get Pytch to tell us what costume the
`Mole` sprite is wearing.  In Scratch, we could use this reporter
block:

``` scratch
(costume [number v])
```

We can do something similar in Pytch, by using `self.costume_number`
inside a `Mole` script.

If the mole is popped out of the left hole, this will be `1`.  If the
mole is popped out of another hole, it will be `2` or `3` (depending
which hole), and if the mole is hiding underground, it will be `0`
(the "all-empty" costume is the first one, which is at _position 0_).

So we want to ask

> Is the `Mole` sprite's costume number equal to 1?

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

Try it!


### What if the player misses?

But this is now too easy.  The player can just keep pressing `j` and
whenever the mole pops out of the left hole, the player scores a
point.  There needs to be a way to discourage the player from doing
this.

Let's be harsh — if the player misses, they lose all their points.
This should happen if the player presses `j` but the `Mole` sprite is
_not_ wearing costume number `1`.  We need something like Scratch's

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

There's still a small way the player can unfairly get more points.  If
they keep hitting `j` while the mole is popped up out of the left
hole, they can rack up points.

Let's make the mole go back underground when the player splats it.  We
can do this just by making it switch back to the `"all-empty"`
costume:

{{< commit left-hit-return-underground >}}

Try it now!


## Add sound effects

Let's add some sounds to the game.  This tutorial comes with some
examples, or you can find and use your own.  Just as we need to list
the image files we want a sprite to be able to use for its costumes,
we need to list the sound files we want a sprite to be able to use.

Add a variable `Sounds` near the top of the `Mole` sprite, just after
the `Costumes`:

{{< commit add-sounds >}}

Now we just need to start the right sound playing depending on whether
the player has hit the mole or missed it.  To play the "splat"
sound if they hit it, add this code:

{{< commit play-splat-if-hit-left >}}

And to play a "thud" sound if they miss, add:

{{< commit play-thud-if-miss-left >}}


## Hit the other holes

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

(If you're wondering whether there's a better way then copying and
pasting, there is, but it's outside the scope of this tutorial.)

### Game complete!

Try the finished game!


## Using real arcade buttons

We now want to be able to control our game using the real physical
buttons, and light the real physical lights.  A lot of our program
will stay the same.

### Splatting moles using the buttons

At the moment, the player controls the game using the "`j`", "`k`",
and "`l`" keys.  To change it so that the player uses the physical
arcade buttons, we only need to change the "hat blocks".

Each switch is wired up so that it connects one of the Raspberry Pi's
"GPIO" pins to "low" (also known as "ground" or "0V") when it's
pressed.  We can use a hat block to say we want to run our code when
this happens.

The three switches are connected as follows:

* Left switch to pin 16.
* Centre switch to pin 20.
* Right switch to pin 21.

So we can change the hat block of the `hit_left()` method like this:

{{< commit control-left-with-gpio >}}

And change the hat block of the `hit_centre()` method like this:

{{< commit control-centre-with-gpio >}}

And change the hat block of the `hit_right()` method like this:

{{< commit control-right-with-gpio >}}

### Lighting an LED for the mole

At the moment, a mole pops up out of one of the holes, on the screen.
We'll give the player an extra clue by lighting the matching LED.

We already have some code to switch to a randomly-chosen costume:

``` python
self.switch_costume(random.randint(1, 3))
```

We now need to use that random number for *two* things:

* To know what costume to switch to.
* To know which LED to light up.

So we will use a variable to store the random number, and then use it
straight away in the ``switch_costume()`` call:

{{< commit introduce-chosen-costume-number-variable >}}

The LEDs are wired up like this:

* The left LED is wired to pin 22.
* The centre LED is wired to pin 23.
* The right LED is wired to pin 24.

And we know that the chosen costume number variable will have one of
these values:

* `chosen_costume_number` = 1, to make the mole appear in the left
  hole.
* `chosen_costume_number` = 2, to make the mole appear in the centre
  hole.
* `chosen_costume_number` = 3, to make the mole appear in the right
  hole.

So to know which LED to light up, we can put these together to see:

* If `chosen_costume_number` is 1, light up the LED on pin 22.
* If `chosen_costume_number` is 2, light up the LED on pin 23.
* If `chosen_costume_number` is 3, light up the LED on pin 24.

We *could* write some `if`/`else` statements, but we can also notice
that the pin number is always 21 plus the costume number.  We'll use
this to work out the required pin number with arithmetic:

{{< commit compute-gpio-pin-number >}}

And now we can turn that LED on with the `set_gpio_output()`
function.  This needs two pieces of information: what pin to control,
and whether to turn it on (`1`) or off (`0`).

{{< commit turn-on-LED >}}

When the mole goes back underground, we want to turn all LEDs off:

{{< commit turn-off-all-LEDs >}}

(We could instead do this with a `for` loop, but for just three lines,
it's not clear that it's worth it.)

But if you try this now, you'll see that the LED stays on after you've
hit the right button.  The three 'hit' methods all switch to the 'all
empty' costume, but don't turn the LEDs off.

We could just copy and paste the three `pytch.set_gpio_output()` lines
into each of those functions, but we'll do it a more tidy way.

### Defining a function to hide the mole

Perhaps you've used the Scratch feature which lets you define your own
custom blocks.  We'll do something very similar here, to define a
function which does both parts of hiding the mole underground:

* Switch to the 'all holes empty' costume on the screen.
* Turn all the LEDs off.

We use `def` in the same way as always, but we do not add a "hat
block".  The code here is copied from our existing code in
`pop_up_and_down()`:

{{< commit define-hide-underground-method >}}

And now, in `pop_up_and_down()` we can just use our new "custom
block":

{{< commit use-hide-underground-method >}}

The point of doing this is that it's now very easy to use this same
behaviour in the other three places we need to make the mole hide
underground, which are:

When the player successfully hits the mole in the left hole:

{{< commit use-hide-underground-when-left-hit >}}

When the player successfully hits the mole in the centre hole:

{{< commit use-hide-underground-when-centre-hit >}}

And when the player successfully hits the mole in the right hole:

{{< commit use-hide-underground-when-right-hit >}}


## Challenges and questions

Maybe you can think of ways to make this game better.  Here are some
ideas:

* Find and use a different backdrop.  Add more than one backdrop, and
  change between them randomly, or as the player gets more points.

* Find and use different sound effects.  Maybe choose randomly between
  different effects to make the game more interesting.  The site
  `freesound.org` has lots of good sound effects.

* Perhaps it's a bit harsh for the player to lose all their points
  when they miss.  Maybe they should lose some fixed number of points
  instead.  Change the code (in three places!) so that the player
  loses five points if they miss.  You can use the Python operator
  `-=` to subtract points.  What happens if they only have three
  points when they miss?

* Instead of losing points, the player could start with three lives,
  and they lose a life every time they miss.  Hint: You can show a
  variable at the _right_ of the screen with the code
  `pytch.show_variable(self, "lives", right=236)`.

* Adjust the difficulty of the game by making the mole stay out of its
  hole for a longer or shorter time.  You could even make the game get
  more difficult as the player gets more points.

* In the hardware version, make all the LEDs be *on* when the mole is
  hiding underground, with one LED turning *off* to show which hole
  the mole has popped out of.

### Other ways of doing things

There is often more than one way to write a program.  Here are some
ways you could investigate writing the program differently to how this
tutorial did it:

* The `Mole` sprite has two green-flag scripts.  Can you combine them
  into one script?  Do you think the program is easier to understand
  with two green-flag scripts or one?

* **Advanced:** Instead of one `Mole` sprite with four costumes, we
  could have made three sprites: `LeftMole`, `CentreMole`, and
  `RightMole`, each with two costumes: an "empty hole" one and a "mole
  popping out of hole" one.  This tutorial comes with suitable
  graphics files.  See if you can re-write the game this way.  Some
  questions you might want to think about:

    * Should it be possible for more than one mole to be out of its
      hole at the same time?

    * How will you keep track of the score?  One way would be to use a
      _global variable_.

    * With one sprite per mole/hole, you could let the player click or
      tap to hit a hole, instead of using the keyboard.  Do you think
      that would be better?  Can you change the code so it reacts to
      the sprite being clicked?


## Credits

We have used various freely-available resources to create this
tutorial:

{{< asset-credits >}}
