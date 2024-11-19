# Script-by-script splat the moles

We're going to write a game in Python where the player has to splat
moles to score points.  But if they miss, they lose all their points!
(Don't worry, no real moles will be harmed in making this game.)

![screenshot](screenshot-w360.jpg#img-center)

---

## Give the stage a backdrop

When you create a project, the stage has a plain backdrop.  This game
needs a better backdrop.

{{< learner-task >}}

Add the “cartoon field” backdrop to the stage.

{{< learner-task-help >}}

{{< jr-commit add-field-backdrop add-medialib-appearance ["cartoon-field.png"] >}}

{{< /learner-task >}}

We don’t need the plain backdrop any more.

{{< learner-task >}}

Delete the “solid white” backdrop from the stage.

{{< learner-task-help >}}

{{< jr-commit remove-default-backdrop delete-appearance >}}

{{< /learner-task >}}

It’s a good idea to test your project as you go along.

{{< learner-task >}}

Run your project using the green button above the stage.  Check that
the backdrop is the “cartoon fields” one.

{{< /learner-task >}}


## Add a sprite for the mole

There are a few different ways the moles could work.  For this
tutorial, you’ll have one sprite with four different costumes
depending on whether the mole is completely underground, or poking up
from one of the three holes.  By making the sprite wear different
costumes, you can make it look like the mole is choosing different
holes to pop out of.

First we need a Sprite for the mole and its holes.

{{< learner-task >}}

Create a new sprite, and call it “Mole”.

{{< learner-task-help >}}

{{< jr-commit create-Mole-sprite add-sprite >}}

{{< /learner-task >}}

The Mole sprite needs its four costumes.  These are in Pytch’s media
library.

{{< learner-task >}}

Add the “cartoon moles” image bundle as costumes of your new Mole
sprite.

{{< learner-task-help >}}

{{< jr-commit add-Mole-costumes add-medialib-appearances-entry ["cartoon moles"] >}}

{{< /learner-task >}}

Remeber to test your game as you go along!

{{< learner-task >}}

Run your project using the green button above the stage.  Check that
a row of empty mole-holes appears in the field.

{{< /learner-task >}}

### Put the mole-holes in a better position

This looks alright, but the holes are a bit high.  To move them lower,
you need to write some code that runs as soon as the green flag is
clicked.  In Scratch, you might do something like

``` scratch
when green flag clicked:
  go to x: (0) y: (-100)
```

where the `x: 0` means the sprite should be centred left-to-right, and
the `y: -100` means sprite should be a bit lower than the centre
top-to-bottom.

In Pytch it’s very similar.

{{< learner-task >}}

Add a “when green flag clicked” script to your Mole sprite.

{{< learner-task-help >}}

{{< jr-commit add-Mole-green-flag-script add-script >}}

{{< /learner-task >}}

Now you can write the code to move the mole-holes.

{{< learner-task >}}

Add code to this script to move the Mole to `(0, -100)`.

{{< learner-task-help >}}

{{< jr-commit init-Mole-position edit-script >}}

{{< /learner-task >}}


## Pop out of random holes

Now you need to make the mole appear out of one of the holes.  If you
look in the “Costumes” tab, you’ll see which costumes have the mole
popping out of a hole.

Pytch stores a sprite’s costumes in a *list*, and describes the
position of an entry of a list using numbers *starting from zero*.  A
number used to point at an entry of a list is often called an *index*.
So you need to choose a “costume index” randomly between `1` and `3`
(inclusive).

One good use of *variables* is to give things names so that your
program is easier to understand when a human is reading it.

{{< learner-task >}}

Add code which chooses a random whole number between `1` and `3`
(inclusive), and stores it in a variable `costume_index`.

{{< learner-task-help >}}

In Scratch you might use

``` scratch
(pick random (1) to (3))
```

to get a random number from `1` to `3`.  You can use the help to find
out how to do this in Python.

{{< learner-task-help >}}

To create a variable in Python, you use `=`.  For example, here’s how
to make the variable `health` have the value `150`:

``` python
health = 150
```

{{< learner-task-help >}}

{{< jr-commit choose-random-hole-costume edit-script >}}

{{< /learner-task >}}

Now your program has chosen a costume, you can switch to it.

{{< learner-task >}}

Add a line of code which makes the Mole switch to the costume you have
chosen.

{{< learner-task-help >}}

You have just made the variable `costume_index` hold the number of the
costume the Mole should switch to.

{{< learner-task-help >}}

{{< jr-commit switch-to-chosen-costume edit-script >}}

{{< /learner-task >}}

Time to test again!

{{< learner-task >}}

Run your program a few times.  Check the mole pops out of random
holes.

{{< /learner-task >}}


## Keep popping out of holes

The mole should *repeatedly* pop out of a random hole, not just once.
In scratch you might put the blocks

``` scratch
set [costume_index v] to (pick random (1) to (3))
switch costume to (costume_index)
```

“inside a forever”, like this:

``` scratch
forever
  set [costume_index v] to (pick random (1) to (3))
  switch costume to (costume_index)
```

In Python, you can use `while True:` to do the same job.  Putting code
“inside” means *indenting* it four spaces.

{{< learner-task >}}

Move the two lines of code which choose and switch to a random costume
inside a `while True:` loop.

{{< learner-task-help >}}

There is an example of what this looks like in the help.

{{< learner-task-help >}}

{{< jr-commit iterate-switching-costume edit-script >}}

{{< /learner-task >}}

Test it!

It *sort of* works.  The problem is that it’s switching costume so
quickly, the player would have no chance.

### Make the mole wait when it’s popped up

The mole should wait a random amount of time after switching to the
chosen costume.  The code will be quite similar to the code for
choosing and switching to a random costume.

{{< learner-task >}}

Add code, just below where you switch costume, which chooses a random
number between `0.5` and `1.0` (inclusive), and stores it in a
variable `above_ground_time`.

Instead of `random.randint(⋯)`, you can use `random.uniform(⋯)` to
allow Python to randomly choose a number with a fractional part.

{{< learner-task-help >}}

To choose a random number between `0.5` and `1.0`, you can use the
Python expression

``` python
random.uniform(0.5, 1.0)
```

{{< learner-task-help >}}

{{< jr-commit choose-wait-time edit-script >}}

{{< /learner-task >}}

Now you can make the program wait before going round the loop and
choosing another costume.

{{< learner-task >}}

Add another line which makes the mole wait for the number of seconds
in the `above_ground_time` variable.

{{< learner-task-help >}}

You can use the help to find what to say in Python to match Scratch’s

``` scratch
wait () seconds
```

block.

{{< learner-task-help >}}

{{< jr-commit wait-for-chosen-time edit-script >}}

{{< /learner-task >}}


## Hide underground before popping back up

The game is better if the mole hides underground for a bit in between
popping up from random holes.  You can do this by making it switch to
the `"no-moles.png"` costume and then waiting for a short random
amount of time.

{{< learner-task >}}

Add three lines of code which:

* Switch to the `"no-moles.png"` costume.
* Choose a random number from `0.5` to `1.0` and store it in a
  variable `under_ground_time`.
* Wait for the amount of time in the `under_ground_time` variable.

{{< learner-task-help >}}

The code will be similar to the lines we just wrote which switch to a
costume, choose a random over-ground time, and wait for that time.

{{< learner-task-help >}}

{{< jr-commit hide-underground-for-random-time edit-script >}}

{{< /learner-task >}}

Test it!


## Scoring

Now you’ll start making the code which lets the player try to splat the
mole.  The `Mole` sprite will keep score — how many times the player
has managed to splat it.

To keep track of something, your program will use a *variable*.  It
will be like a “For this sprite only” variable in Scratch.  Remember,
in Python, to create a variable, you just set it to a value.  There’s
no separate step to create it.

At the very start of the game, the score should be set to zero,
because the player hasn’t splatted any moles yet.

You could put this code in the same green-flag script which already
exists, but it’s a good idea to keep the different parts of your
program separate, so it’s easier to understand.

{{< learner-task >}}

Add a new green-flag script to your Mole.

{{< learner-task-help >}}

{{< jr-commit add-init-score-script add-script >}}

{{< /learner-task >}}

Now you can write the code to *initialise* the score.

{{< learner-task >}}

Assign the value `0` to a variable `self.score`.  The `self.` at the
start of `self.score` is what makes it a “For this sprite only”
variable.

{{< learner-task-help >}}

{{< jr-commit init-score-to-zero edit-script >}}

{{< /learner-task >}}

If you run the game, you won’t see anything different happen, because
the program doesn’t do anything with the `Mole` sprite’s `score`
variable.  In Scratch, you could display the score by checking the
check-box next to the variable, or by using this block:

``` scratch
show variable [score v]
```

Pytch does have a command like that block, but it needs a bit more
information: You have to say who owns the variable.  The `score`
variable belongs to the `Mole` sprite, which as you’ve seen, is called
`self` inside its scripts.

{{< learner-task >}}

Add a line of code which uses Pytch’s `pytch.show_variable(⋯)` to
display the score.

{{< learner-task-help >}}

The help gives an example.  Try to adapt it to what you’re trying to
do here.

{{< learner-task-help >}}

{{< jr-commit show-score edit-script >}}

{{< /learner-task >}}

Test it!

{{< learner-task >}}

Run your program.  You should see the score displayed on the stage.

{{< /learner-task >}}


## Let the player splat the moles

The game will be controlled by the keyboard.  The player will:

* press `j` to hit the left hole;

* press `k` to hit the centre hole;

* press `l` to hit the right hole.

You’ll write code for `j` (the left hole) first, and then adapt it for
the other two keys.

{{< learner-task >}}

Add a script to the Mole which runs when the player presses the `j`
key.

{{< learner-task-help >}}

{{< jr-commit add-left-mole-click-script add-script >}}

{{< /learner-task >}}

When the player presses `j`, if the mole is popped out of the left
hole, the score should go up by `1`.  Remember that “popped out of the
left hole” is the same as “wearing costume number 1”.

In Scratch, you might write code like this:

``` scratch
if <(costume [number v]) = (1)> then
  change [score v] by (1)
```

{{< learner-task >}}

Write Python code in your new script which does the same job.  Use the
help to look up the Python version of the two Scratch blocks above.

{{< learner-task-help >}}

In Python, you need *two* equals signs to test whether two things are
the same.  So to ask whether the Mole’s costume-number is `1`, you can
use the Python expression

``` python
self.costume_number == 1
```

{{< learner-task-help >}}

To add one to a variable, you can use Python’s `+=` operator.  For
example, to add one to a sprite’s `health` variable, you could do

``` python
self.health += 1
```

{{< learner-task-help >}}

{{< jr-commit point-for-left-hit edit-script >}}

{{< /learner-task >}}

Test it!

{{< learner-task >}}

Run your program.  You should see the score go up if you press `j`
while the mole is popped out of the left hole.

{{< /learner-task >}}

### What if the player misses?

But this is now too easy.  The player can just keep pressing `j` and
whenever the mole pops out of the left hole, the player scores a
point.  There needs to be a way to discourage the player from doing
this.

Let’s be harsh — if the player misses, they lose all their points.
This should happen if the player presses `j` but the `Mole` sprite is
_not_ wearing costume number `1`.  You need something like Scratch’s

``` scratch
if <> then
else
end
```

block.

{{< learner-task >}}

Add an *else* clause to your `if` statement which sets the score to
zero if the Mole is not popped out of the left hole when the player
presses `j`.

{{< learner-task-help >}}

You can find an example in the help.

{{< learner-task-help >}}

{{< jr-commit lose-points-left-miss edit-script >}}

{{< /learner-task >}}

You might think this is a bit _too_ harsh!  Have a look at the
_Challenges_ at the end of this tutorial for some other ideas.

### Make a splatted mole go back underground

There’s still a small way the player can unfairly get more points.  If
they keep hitting `j` while the mole is popped up out of the left
hole, they can rack up points.

Let’s make the mole go back underground when the player splats it.  We
can do this just by making it switch back to the `"no-moles.png"`
costume.

{{< learner-task >}}

Add a line of code (after the line which gives the player a point)
which switches the Mole’s costume to the `"no-moles.png"` one.

{{< learner-task-help >}}

{{< jr-commit hide-after-left-hit edit-script >}}

{{< /learner-task >}}

## Let the player splat the centre and right holes

To finish the game, you just need to make two more scripts, very
similar to the one you’ve just made.

### Splat the centre hole

First handle the centre hole.

{{< learner-task >}}

Make a script which:

* runs when the player presses the `k` key;
* has code which is almost the same as the `j` key script, but checks
  that the mole is popped up in the centre hole.

{{< learner-task-help >}}

To check whether the mole is popped up in the centre hole, check
whether its costume number is `2`.

{{< learner-task-help >}}

{{< jr-commit copy-paste-for-centre add-script >}}

{{< /learner-task >}}

### Splat the right hole

And finally handle the right-hand hole.

{{< learner-task >}}

Make a script which:

* runs when the player presses the `l` key;
* has code which is almost the same as the `j` key script, but checks
  that the mole is popped up in the right-hand hole.

{{< learner-task-help >}}

To check whether the mole is popped up in the centre hole, check
whether its costume number is `3`.

{{< learner-task-help >}}

{{< jr-commit copy-paste-for-right add-script >}}

{{< /learner-task >}}

### Try the finished game!

How many points can you get?


## Challenges and questions

{{< exclude-from-progress-trail >}}

Maybe you can think of ways to make this game better.  Here are some
ideas:

* Find and use a different backdrop.  Add more than one backdrop, and
  change between them randomly, or as the player gets more points.

* Perhaps it’s a bit harsh for the player to lose all their points
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

### Other ways of doing things

There is often more than one way to write a program.  Here are some
ways you could investigate writing the program differently.

* The `Mole` sprite has two green-flag scripts.  Can you combine them
  into one script?  Do you think the program is easier to understand
  with two green-flag scripts or one?

* **Advanced:** Instead of one `Mole` sprite with four costumes, we
  could have made three sprites: `LeftMole`, `CentreMole`, and
  `RightMole`, each with two costumes: an “empty hole” one and a “mole
  popping out of hole” one.  This tutorial comes with suitable
  graphics files.  **TODO: It does not yet!**  See if you can re-write
  the game this way.  Some questions you might want to think about:

    * Should it be possible for more than one mole to be out of its
      hole at the same time?

    * How will you keep track of the score?  One way would be to use a
      variable which belongs to the stage.

    * With one sprite per mole/hole, you could let the player click or
      tap to hit a hole, instead of using the keyboard.  Do you think
      that would be better?  Can you change the code so it reacts to
      the sprite being clicked?
