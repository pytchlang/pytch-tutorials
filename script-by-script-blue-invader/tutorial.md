# Blue Invaders

In this game, the player will defend earth from dangerous blue
invaders, by clicking on them.  But they must not destroy the friendly
green aliens by mistake!


---

## Set the backdrop

The first job is to make the background for our game.  Pytch’s media
library includes a galaxy image for us to use.

{{< learner-task >}}

Add the “starry sky” backdrop to the Stage from the media library.

{{< learner-task-help >}}

{{< jr-commit add-starry-backdrop add-medialib-appearance ["starry-sky.jpg"] >}}

{{< /learner-task >}}

If you run your game now, you won’t see your new background.  This is
because the Stage still has the default solid white background, and
that background is the first one, so it is the one that gets shown.

{{< learner-task >}}

Delete the `solid-white.png` backdrop from the stage.

{{< learner-task-help >}}

{{< jr-commit remove-white-backdrop delete-appearance >}}

{{< /learner-task >}}

Click on the green play button now — you should see the game’s
new background.


## Create the first alien

When it’s finished, the game will have lots of aliens, but to start
with, there will just be one.

There will be an `Alien` Sprite which will have different costumes.
When this sprite is wearing one costume (a blue one), it counts as an
enemy space invader, and when it’s wearing another costume (a green
one), it’s a friendly visitor.

### Create _Alien_ Sprite

The project needs a new sprite to be the Alien.

{{< learner-task >}}

Add a Sprite called `Alien` to your project.

{{< learner-task-help >}}

{{< jr-commit create-alien-sprite add-sprite >}}

{{< /learner-task >}}

### Give the _Alien_ some costumes

The new sprite then needs costumes.  There is a bundle of three
suitable costumes in Pytch’s media library.

**TODO: Remove duplicate "space invaders" group in media lib.**

{{< learner-task >}}

Add the ‘space invaders’ bundle of images from the media library as
costumes to the `Alien` sprite.

{{< learner-task-help >}}

{{< jr-commit add-alien-costumes add-medialib-appearances-entry ["space invaders"] >}}

{{< /learner-task >}}

If you run your project now, you should see a blue enemy invader in
the middle of the screen.  This is because Pytch starts a Sprite off
wearing its first costume.

### Make the alien drift down the screen

The Alien should glide from the top to the bottom of the screen, then
instantly go back to the top and start gliding again.

This should all start happening as soon as the game starts.

{{< learner-task >}}

Add a new empty script to the `Alien` with a “when green flag clicked”
hat-block.

{{< learner-task-help >}}

{{< jr-commit add-drift-down-skeleton add-script >}}

{{< /learner-task >}}

The code of this script should work the same as Scratch’s *forever*
block.  In Python, you can say `while True:`, and underneath put
*indented* lines to say what should keep happening.

For example, here’s code which moves a sprite slowly across the screen:

``` python
while True:
    self.change_x(1)
```

{{< learner-task >}}

Write the code in your new script which makes the alien repeatedly go
to the top of the screen then glide to the bottom.

{{< learner-task-help >}}

To tell the alien to go to a particular vertical place on the screen,
you can use something like

``` python
self.set_y(50)
```

The number `50` here is the *y* coordinate the alien should go to.
Its *x* coordinate is not changed.  The alien will move purely up or
down.

{{< learner-task-help >}}

To tell the alien to move smoothly to a different place on the screen, you can
use something like

``` python
self.glide_to_xy(0, -50, 2.5)
```

The numbers are the *x* and *y* coordinates of the point the alien
should go to, and how long to take (the number of seconds) to move
there.  You might find it useful to use

``` python-expression
self.x_position
```

instead of an actual *x* number, looking ahead to when there are lots
of aliens, each with its own *x* position.

{{< learner-task-help >}}

{{< jr-commit add-drift-down-body edit-script >}}

{{< /learner-task >}}


## Mixture of enemy and friendly aliens

Some of the aliens that drift down the screen need to be enemies, and
some friendly.  Remember that this is done by making the alien wear a
different costume.

Just like in Scratch, you can switch costume either by giving the new
costume’s position in the costumes list, or by giving its name.  In
this case it will be slightly easier to choose the costume by
position.  You can look in the “Costumes” tab to see what costumes are
available and what their positions are.

In Python, things in a list are numbered from *zero*, so the first
thing in a list is at ‘position&nbsp;0’, the second thing is at
‘position&nbsp;1’, and so on.  So the code should randomly choose
either the costume at position&nbsp;0 or the one at position&nbsp;1.

This *could* be done all in one line of code, but breaking the job
into two steps will make it easier to understand:

* Randomly choose a costume position (0 or 1).
* Switch to the chosen costume.

### Randomly choose which costume

The `random.choice(list_of_choices)` function will do this job.

The `random.choice()` function needs a *list* of the options it should
choose from.  Here, the choices are `0` and `1`.  In Python, the list
containing `0` and `1` is written `[0, 1]`.

{{< learner-task >}}

Add a line of code which randomly chooses `0` or `1` to be the
position of the new costume, and stores the choice in a variable
called `costume_position`.

**TODO: Is “position” a helpful word?  Might people think we’re
talking about position on the stage, i.e., coordinates?  Could we
introduce the word “index”?**

{{< learner-task-help >}}

The new code should go at the top of the indented body of the `while
True` loop.

{{< learner-task-help >}}

{{< jr-commit choose-random-costume edit-script >}}

{{< /learner-task >}}

Once the chosen number is in a variable, the alien can switch to that
costume.

{{< learner-task >}}

Add a line of code which switches to the costume whose position is in
the variable `costume_position`.

{{< learner-task-help >}}

{{< jr-commit switch-to-chosen-costume edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  If you run the project, you should see aliens gliding
down the screen.  There should be a random mixture of blue ones and
green ones.

{{< /learner-task >}}


## Make lots of aliens

To make more than one alien, the program will use *clones*.  These
work the same as in Scratch — you get more than one copy of the same
sprite.

The program will clone the Alien five times.  Together with the
original Alien, this makes six aliens altogether.

Using the *x*-positions

> -150, -90, -30, 30, 90, and 150

will spread the aliens left to right across the screen.

The idea is:

* Move the original Alien to the first place (*x*-position of `-150`).
* Make a clone at that position, then move the original to the next
  place (`x = -90`).
* Make another clone, and move the original to `x = -30`.
* And so on.

{{< learner-task >}}

Add an empty *green-flag* script to the Alien.

{{< learner-task-help >}}

{{< jr-commit add-make-clones-script add-script >}}

{{< /learner-task >}}

This script now needs code to make and move the clones.

{{< learner-task >}}

Add a line of code to this script which moves the alien to the place
on the stage with *x*-position `-150` and *y*-position `180`.

{{< learner-task-help >}}

{{< jr-commit move-first-alien-to-position edit-script >}}

{{< /learner-task >}}

{{< learner-task >}}

Add two lines of code to this script.  The first line should make a
clone of the Alien.  The second line should move the original Alien to
the place on the stage with *x*-position `-90` and *y*-position `180`.

{{< learner-task-help >}}

{{< jr-commit make-first-clone edit-script >}}

{{< /learner-task >}}

{{< learner-task >}}

Add the rest of the required code, which will be very similar to
copies of the lines you’ve just added.  You should end up with clones
at *x*-positions

> -150, -90, -30, 30, and 90

and the original Alien at *x*-position 150.

{{< learner-task-help >}}

{{< jr-commit make-rest-of-clones edit-script >}}

{{< /learner-task >}}

(You might be thinking that there must be a better way to do this than
by copy and pasting nearly identical code.  You’re right, but that’s
outside the scope of this tutorial!)

### Test it!

{{< learner-task >}}

Try your game.  What happens?

{{< learner-task-help >}}

More aliens do appear, but only one of them moves.

{{< /learner-task >}}

### It doesn’t work properly!

If you run the game now, it doesn’t really work.  There are more
aliens at the top of the screen, but only one of them is gliding down.
This is because Pytch doesn’t make any guarantees about which order
the two *green-flag* scripts run, and the glide script is happening
before all the clones are made.

The next chapter explains how to fix this.


## Using broadcasts to control when scripts run

To make sure that everything happens in the right order, the program
will use another part of Pytch which might be familiar from Scratch —
*broadcasts*.  A sprite can ‘shout’ a message, and any sprite
(including the same sprite that shouted!) can be listening for that
message, and run some code whenever the sprite hears the message.

The program needs to make sure that all the clones are made before the
gliding starts.  The Stage will be in charge of making this happen.

Because the program will use broadcasts to coordinate things, the
script you just wrote, which makes all the clones, needs to run when
it receives an appropriate broadcast message.

{{< learner-task >}}

Make the script which creates all the clones run when the Alien
receives the `"make-clones"` message (not when green flag is clicked).

{{< learner-task-help >}}

The code stays the same.  You just need to change the script’s hat
block.  This is like when, in Scratch, you get rid of a script’s hat
block and attach a different one.

{{< learner-task-help >}}

{{< jr-commit make-clones-when-receive change-hat-block >}}

{{< /learner-task >}}

{{< learner-task >}}

Add a *green-flag* script **to the stage** which broadcasts this
`"make-clones"` message, and waits for the listening scripts to finish
running.

**TODO: It doesn’t actually have to be the stage.  Motivation is to
keep all the “control” stuff in the stage.  Is that enough
justification?  Should we add some explanation?**

{{< learner-task-help >}}

{{< jr-commit broadcast-make-clones add-script >}}

{{< /learner-task >}}


### Wait for all clones to exist before gliding

The code you just added uses `broadcast_and_wait()`.  Just like in
Scratch, your program doesn’t go on to the next statement until
everybody listening for the `"make-clones"` message has finished doing
whatever it is they do when they hear it.  So any code after
`broadcast_and_wait()` won’t run until all the clones exist.

This is how the program can control when the aliens start gliding.

{{< learner-task >}}

Change your program so the gliding code in the `Alien` sprite runs
when an alien or clone hears a `"play-game"` message (and not when the
green flag is clicked).

{{< learner-task-help >}}

Just like a minute ago, the code stays the same.  You just need to
change the script’s hat block.

{{< learner-task-help >}}

{{< jr-commit descend-on-play-game-broadcast change-hat-block >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  What happens?  Why?

{{< learner-task-help >}}

_All_ the aliens just stay at the top of the screen.  The gliding code
only runs when somebody broadcasts the `"play-game"` message, and
nobody is doing that.

{{< /learner-task >}}

Now you can add code to the correct place which broadcasts the message
the aliens are waiting for.

{{< learner-task >}}

Make the Stage broadcast that `"play-game"` message, once the clones
have all been created.

{{< learner-task-help >}}

{{< jr-commit broadcast-play-game edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project.  You should see waves of aliens gliding down the
screen, a mixture of blue and green each time.  (Sometimes, just by
chance, you’ll get an all-blue wave or an all-green one.)

{{< /learner-task >}}

This is OK, but it would be better if some aliens went faster than
others.


## Randomise the glide time

At the moment, every alien clone takes exactly 3&nbsp;seconds to glide
down the screen.  The game would be better with a bit of variation, by
making each alien clone take a random time to glide down the screen.
This will make some aliens move faster than others and make it more
interesting.

The Alien’s `"play-game"` code needs changing so that each alien takes
a random time between, say, 3 and 5 seconds.

Your program already uses `random.choice()`.  Python also provides the
`random.uniform()` function, which picks a random number anywhere
between two limits.  Your program can use this to get a random number
anywhere between 3.0 and 5.0 (including fractions).

{{< learner-task >}}

In the Alien’s `"play-game"` script, add a line of code just before
the `self.glide_to_xy()` which uses `random.uniform()` to get a random
number anywhere between 3 and 5 and assigns the result to a variable
called `glide_time`.

{{< learner-task-help >}}

The Python expression

``` python-expression
random.uniform(3.0, 5.0)
```

will generate the random number you want.

{{< learner-task-help >}}

Remember you used the code

``` python
costume_position = random.choice([0, 1])
```

to make a random choice from the list `[0, 1]`, and assigns the result
to the variable `costume_position`.  You want to do something similar.

{{< learner-task-help >}}

Here you want a random number anywhere between 3 and 5, including
fractional part.  The

``` python-expression
random.uniform()
```

function will do this for you.  Look in the help to see how to use it.

{{< learner-task-help >}}

{{< jr-commit define-glide-time edit-script >}}

{{< /learner-task >}}

Now you can use this variable to say how long the gliding motion
should take.

{{< learner-task >}}

Change the existing code to use this new `glide_time` variable instead
of the fixed number `3.0` in the `glide_to_xy()` function call.

{{< learner-task-help >}}

{{< jr-commit use-glide-time edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project.  You should see some aliens falling faster than
others, and after little while it looks almost like aliens are
appearing at random.

{{< /learner-task >}}


## Click on the aliens!

Now your project is quite nice to look at, but it isn’t a *game*
because there’s nothing for the player to do.  That’s the next job.

### React when hit

The Aliens (original and clones) should react when they’re clicked on
by the player.

{{< learner-task >}}

Add a *when-this-sprite-clicked* script to your Alien.

{{< learner-task-help >}}

{{< jr-commit add-when-hit-skeleton add-script >}}

{{< /learner-task >}}

Now you have the script, you need to write its code.

{{< learner-task >}}

Add code to your new script which makes the Alien hide itself.

{{< learner-task-help >}}

{{< jr-commit hide-when-hit edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  Check you can click on the aliens to make them
disappear.

{{< /learner-task >}}

But now there’s a different problem — once the player has clicked on
an alien, that alien doesn’t appear again.

### Re-appear at the top of the screen

Each alien must make sure it’s visible just before it starts
gliding down the screen.

{{< learner-task >}}

Think about where in your Alien’s code you need to make sure each
Alien is visible, and add code to do this.

{{< learner-task-help >}}

Remember that the Aliens’ movement is controlled by code in the
`"play-game"` script.

{{< learner-task-help >}}

A good place to make the Alien show itself is after it has chosen a
random costume and moved to the top of the screen, but before the code
which makes the Alien glide down the screen.

{{< learner-task-help >}}

{{< jr-commit show-when-starting-descent edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  Aliens should constantly reappear after you click on
them.

{{< /learner-task >}}


## Keep score

To let the player know how they’re doing, the game should keep score.
Just like in Scratch, your program remembers numbers (or strings, or
lists, or anything else) using a *variable*.  In Python, you don’t
have to explicitly make a variable.  Setting a new variable to a value
creates that variable for you.

### Initialise score to zero

The Stage will keep track of the player’s score, in a variable which
belongs to the Stage.

For example, to create a variable `time` belonging to the Stage,
setting it to the value `60`, the code would be

``` python
Stage.time = 60
```

{{< learner-task >}}

Use this example to write code which sets a Stage variable `score` to
the value `0`.  This variable should be created when your program
starts running, so think about where your code should be added.

{{< learner-task-help >}}

To make sure the new code runs at the start of the game, it should go
at the top of the Stage’s *green-flag* script.

{{< learner-task-help >}}

{{< jr-commit define-global-score edit-script >}}

{{< /learner-task >}}

### Show score

In Scratch, you tick a box to say that you want the variable to be
shown.  In Pytch you do this by writing some code.  The Stage’s
`score` variable should be shown as soon as the game starts, just
after the variable is created.

For example, to show a variable `time` belonging to the Stage, the
code would be

``` python
pytch.show_variable(Stage, "time")
```

The way this works is unusual — you use the *name* of the variable,
written as a *string*.  The reason for this is outside the scope of
this tutorial!

{{< learner-task >}}

Add code which shows the Stage’s `score` variable.  Think about where
that code should go.

{{< learner-task-help >}}

The code should go straight after the code which creates the
`Stage.score` variable.

{{< learner-task-help >}}

{{< jr-commit show-score edit-script >}}

{{< /learner-task >}}

### Give points for hitting an enemy

Let’s give the player 10&nbsp;points when they click on an enemy
invader.  There is already some code which makes the Aliens hide
themselves when it’s clicked, so this is a good place to add the code
which updates the score.

{{< learner-task >}}

Add code which gives the player ten points whenever they click on
*any* alien.  (In a minute you’ll change this code so only enemy
aliens give you points.)

{{< learner-task-help >}}

In Scratch, the code

``` scratch
change [score v] by (10)
```

adds `10` to a variable called `score`.  Look in the help (use the
‘question mark in circle’ icon at the top of the activity bar to show it)
to find how to do the same thing in Python.  Remember the variable you
want to change is `Stage.score`.

{{< learner-task-help >}}

The Python code to do this job is

``` python
Stage.score += 10
```

Think about where to add this code.

{{< learner-task-help >}}

{{< jr-commit award-score-on-any-hit edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  Check you get 10 points for every alien you click.

{{< /learner-task >}}

### Only get points for enemy aliens

{{< learner-task >}}

Move this code so it is ‘inside an `if` test’ — only give the player
points if it’s an enemy alien.

{{< learner-task-help >}}

You can test whether it’s an enemy alien by checking whether the
costume number is zero.

{{< learner-task-help >}}

In Scratch, you would write code like

``` scratch
if <(costume_number) = (0)> then
  change [score v] by (10)
```

Look in the help to find how to do the same thing in Python.

{{< learner-task-help >}}

{{< jr-commit award-score-just-for-enemy edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  You should get 10 points for every blue enemy you
click on, and nothing for clicking on a green alien.

{{< /learner-task >}}


## Count lives

The game is quite good now, but there’s nothing to discourage the
player from just clicking everywhere.  There’s no penalty for hitting
a friendly alien.

The player will have three lives.  Destroying a friendly alien will
cost a life.

### Keeping track of lives

A variable will store how many lives the player has.  The code will be
very similar to the code you wrote to make and show the `score`
variable.

{{< learner-task >}}

Using the `Stage.score` variable as an example, create a variable
`Stage.lives` which has the value `3` at the start of the game.

{{< learner-task-help >}}

{{< jr-commit define-global-lives edit-script >}}

{{< /learner-task >}}

The player needs to be able to see how many lives they have.  The
‘lives’ display must not be on top of where the ‘score’ display is,
though.  The `pytch.show_variable()` function can be told where to put
the display.

For example, to show a variable `Stage.time` at the top right of the
stage, the code would be

``` python
pytch.show_variable(Stage, "time", right=236)
```

{{< learner-task >}}

Show the `Stage.lives` variable at the top right of the stage.

{{< learner-task-help >}}

{{< jr-commit show-lives edit-script >}}

{{< /learner-task >}}

And finally your program should take one life away whenever the player
clicks on a friendly alien.

{{< learner-task >}}

In its *when clicked* script, your Alien already has code which gives
the player points but only if that Alien is wearing the ‘enemy’
costume (i.e., costume number `0`).

Add similar code which subtracts one life but only if that Alien is
wearing the ‘friendly’ costume (i.e., costume number `1`).

{{< learner-task-help >}}

{{< jr-commit decrement-lives-if-friendly edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  You should see the `lives` display go down each time
you click on a green alien.

**There’s a bug — what is it?**

{{< learner-task-help >}}

The game doesn’t stop when you run out of lives.

{{< /learner-task >}}

Although the player loses a life when they click a friendly alien, the
game keeps going even once the player has lost all their lives.  You
will fix this in the next chapter.


## End game when no lives left

The last piece of work is to make the game stop when the player has
used all their lives.  Your program can tell when this has happened
because the `Stage.lives` variable will be zero.

### Stop aliens gliding when game is over

First, aliens should stop gliding down the screen once the game is
over.  At the moment, they glide forever, because of the `while True`.
Instead, they should only glide while the player has some lives left.

{{< learner-task >}}

The ‘condition’ of the `while` loop is currently just the constant
`True`, which means the `while` loop runs forever.

Replace `True` with a comparison which tests whether the player has
more than zero lives left.

{{< learner-task-help >}}

You can find out whether the number of lives is greater than zero with
the Python expression

``` python-expression
Stage.lives > 0
```

{{< learner-task-help >}}

{{< jr-commit stop-descent-loop-when-game-over edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  Deliberately click on three green aliens.  You should
see that no more aliens appear.  Instead, aliens stop at the bottom of
the screen.

{{< /learner-task >}}

But any aliens which are part-way down the screen keep going until
they reach the bottom.  This needs fixing too.

All aliens should disappear immediately when the player’s lives goes
to zero.  Broadcasting a message when all the player’s lives are gone
will achieve this.

{{< learner-task >}}

After subtracting one from `Stage.lives`, check whether `Stage.lives`
is zero.  If it is, broadcast the message `"game-over"`.

{{< learner-task-help >}}

You will need an `if` statement.  For the “condition”, you can ask
whether the player’s lives are all gone with the test

``` python-expression
Stage.lives == 0
```

Notice there are two equals signs there!

{{< learner-task-help >}}

{{< jr-commit broadcast-game-over edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your game.  Deliberately click on three green aliens.  What happens?

{{< learner-task-help >}}

Nothing really!

{{< /learner-task >}}

Nothing really happens when this code runs, because nobody is
*listening* for this message.

{{< learner-task >}}

Add a script to the Alien which runs when the message `"game-over"` is
broadcast.  Inside that script, write a line of code to hide the
alien.

{{< learner-task-help >}}

{{< jr-commit hide-when-receive-game-over add-script >}}

{{< /learner-task >}}

### Game complete!

Test your game now and make sure it works properly.


## Challenges

Here are some ways you could make the game even better:

* Make the aliens move more quickly as the player’s score goes up.

* Add a rare red alien which is worth 50 points.  The “space invaders”
  bundle of images, which you added to the project, includes a red
  alien.

* Add some left-to-right randomness to where the aliens start.

### Credits

This project was loosely inspired by the *Red Alert* game in the DK
book [*Coding Games in
Python*](https://www.dk.com/us/book/9781465473615-coding-games-in-python/).

### Detailed credits

{{< asset-credits >}}
