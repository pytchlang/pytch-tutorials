# Blue Invaders

In this game we'll defend ourselves from dangerous blue invaders, by
clicking on them.  But don't destroy the friendly green aliens by
mistake!


---

## Set the backdrop

Our first job is to make the background for our game.  This tutorial
includes a starry sky image for us to use.  We create a sort of
`Stage`, calling it `Galaxy`, and say that it has one backdrop.  The
name in `""`s there — `"starry-sky.jpg"` — is the name of the image
file.  You can check this in the *Images and sounds* tab.

{{< commit create-stage-with-backdrop >}}

If you add this code to your project and click the green play button,
you should see the game's background.


## Create the aliens

For the aliens which will drop down the screen, we are going to use a
feature of Pytch called *clones*.  These work the same way as clones
in Scratch.  There will be an `Alien` Sprite which will have two
costumes.  When a clone is wearing one costume, it counts as an enemy
space invader, and when it's wearing the other costume, it's a
friendly visitor.

### Create Sprite with costumes

Our first job is to make the `Alien` Sprite, and say what images we
want to use for its two costumes:

{{< commit create-alien-with-costumes >}}

If you add this code to your project and run it, you should see a blue
enemy invader in the middle of the screen.  This is because Pytch
starts a Sprite off wearing the first costume in its list.

### Make the alien drift down the screen

Our next job is to make the alien move.  We'll make it glide from the
top to the bottom of the screen, then instantly go back to the top and
start gliding again.

This should all start happening as soon as the game starts, so we'll
use `@pytch.when_green_flag_clicked` at the top of our code.  For the
code itself, we want something which works the same as Scratch's
*forever* block.  In Python, we use `while True:`, and within that,
say what we want to keep happening.  We want the alien to go to the
top of the screen, then glide to the bottom.

{{< commit loop-drift-down-screen >}}

You'll see that the code uses `self.x_position` — this is the same as
the *(x&nbsp;position)* reporter block in Scratch.  For this original
alien, this might seem over-complicated, because we know its
*x*-position is zero.  But I'm looking ahead to when there will be
more than one alien, each with its own *x*-position.

### Randomly choose whether enemy or friendly

Some of the aliens that drift down the screen will be enemies, and
some will be friendly.  Remember that this is done by making the alien
wear a different costume.

We want the costume to be random each time.  Python can generate
random numbers, but we need to say we want to use that part of Python.
We do this by *importing* the `random` library:

{{< commit import-random >}}

This is very much like adding an extension in Scratch.

And now we can ask for a random costume.  Just like in Scratch, we can
switch costume either by the costume's position in the costumes list,
or by name.  We'll choose the costume by position.

In Python, things in a list are numbered from *zero*, so the first
thing in a list is at 'position&nbsp;0', the second thing is at
'position&nbsp;1', and so on.  So we want to randomly choose either
the costume at position&nbsp;0 or the one at position&nbsp;1.

The `random.choice()` function will do this for us.  We want to switch
to a random costume just before jumping back to the top of the screen:

{{< commit random-costume-per-descent >}}

There's quite a lot going on in this one line of new code.  Starting
from the inside:

* `[0, 1]` is a list with two things in it — the number zero and the
  number one.

* `random.choice([0, 1])` asks Python to choose randomly between the
  two things in that list.  So the result of this piece of code is
  either the number&nbsp;0 or the number&nbsp;1.

* `self.switch_costume(random.choice([0, 1]))` makes the Alien sprite
  switch to that randomly-chosen costume.

If you run the project now, you should see some blue enemy invaders
and some green friendly visitors gliding down the screen.

But only one alien is on screen at a time.  We'll fix that next.


## Make lots of aliens

To make more than one alien, we're going to use *clones*.  These work
the same as in Scratch — you get more than one copy of the same
sprite.  This is perfect for what we're trying to do.

To make sure that everything happens in the right order, we're going
to use another part of Pytch which might be familiar from Scratch —
*broadcasts*.  A sprite can 'shout' a message, and any sprite
(including the same sprite that shouted!) can be listening for that
message, and run some code whenever it hears it.

### Write code to create five clones

We'll first write some code which clones the Alien five times.
Together with the original Alien, we'll have six aliens.  I worked out
what *x*-positions spread the aliens left to right across the screen:
-150, -90, -30, 30, 90, 150.  The idea now is to move the original
Alien to one of those places, make a clone, then move on to the next
place.  We'll make all of this happen when somebody broadcasts the
message `"make-clones"`.

This adds up to quite a lot of code:

{{< commit unrolled-make-clones >}}

### Broadcast the message to run that code

We'll put the *Galaxy* stage in charge of broadcasting the
`"make-clones"` message.  This next bit of code needs to be added to
the `Galaxy` not the `Alien`:

{{< commit broadcast-make-clones >}}

If you run the game now, it doesn't really work.  We do get some more
aliens at the top of the screen, but only one of them is gliding
down.  This is because the `drift_down_screen()` code starts running
before the `make_clones()` code has finished.  We need to make sure
things happen in the right order — we'll fix this next.

### Wait for all clones to exist before gliding

The code we just added uses `broadcast_and_wait()`.  Just like in
Scratch, your program doesn't go on to the next statement until
everybody listening for the `"make-clones"` message has finished doing
whatever it is they do when they hear it.  So if we add code after
`broadcast_and_wait()`, we know that all the clones will exist when
that code runs.

We'll use this to change when the aliens start gliding.  First, we'll
say that the `drift_down_screen()` code in the `Alien` sprite should
happen when an alien or clone hears a `"play-game"` message.  This is
like when, in Scratch, you get rid of a script's hat block and attach
a different one.

{{< commit descend-on-play-game-broadcast >}}

(The red and green lines here mean that you delete the old code (red
background, with `-` at the left), and add in its place the new code
(green background, with `+` at the left).  Quite a lot of the old line
is still in the new line, so you can just delete `green_flag_clicked`
and replace it with `I_receive("play-game")` if you're careful!)

And then we'll make the `run()` code in `Galaxy` broadcast that
message, after the clones have all been created:

{{< commit broadcast-play-game >}}

If you run the code now, you should see waves of aliens gliding down
the screen, with a mixture of blue and green.

This is OK, but it would be better if some aliens went faster than
others.

### Randomise the glide time

At the moment, every alien clone takes exactly 3&nbsp;seconds to glide
down the screen.  We want to add a bit of variation, by making each
alien clone take a random time to glide down the screen.  This will
make some aliens move faster than others and make it more interesting.

The `drift_down_screen()` code is where we'll need to make the change.

We have already done `import random`, so we can use the
`random.uniform()` function to get a random number anywhere from 3.0
up to 5.0 (including fractions).  We'll store the randomly-chosen
number in a variable:

{{< commit define-glide-time >}}

And then use this variable instead of the fixed number `3.0` in the
`glide_to_xy()` function call:

{{< commit use-glide-time >}}

Just like when we change `when_green_flag_clicked` into
`when_I_receive("play-game")` earlier, the red and green lines here
mean that you delete the old code (red background, with `-` at the
left), and add in its place the new code (green background, with `+`
at the left).  Since most of the line is the same, you can just delete
`3.0` and type in `glide_time` if you like.

Now if you run the game, som aliens should be faster than others, and
after little while it looks almost like aliens are appearing at
random.


## Click on the aliens!

So far our project is quite nice to look at, but it isn't a *game*
because there's nothing for the player to do.  We'll fix that now.

### Add sound effects

We want there to be sound effects when the player clicks on the alien.
We'll have one sound effect when they click on an enemy alien, and a
different one when they click on a friendly one.  This tutorial comes
with an explosion and a scream, and we tell the `Alien` sprite that we
want to use these sounds in a similar way to how we say what images we
want to use for costumes:

{{< commit add-alien-sounds >}}

### React when hit

We want the Aliens (original and clones) to react when they're clicked
on by the player.  We'll write some `when_this_sprite_clicked` code
which plays the right sound, depending on whether that clone is being
an enemy or a friendly alien.

Remember that an alien is an enemy when wearing the blue costume
(number&nbsp;0) and a friendly visitor when wearing the green costume
(number&nbsp;1).  So we can use an `if` statement to test which
costume the alien is wearing, and play the right sound:

{{< commit start-appropriate-sound-when-hit >}}

If you try now, you should hear the sounds when you click on the
aliens — check you get the right sound for the right costume!

But the player can keep clicking on the same alien.  We need the alien
to hide itself once its been clicked on.  We can add a line to our
`handle_hit()` code to make this happen:

{{< commit hide-when-hit >}}

Now each alien should disappear (with a sound) when the player clicks
on it.  Try this!

But now we have a different problem — once the player has clicked on
all six aliens, no more aliens appear.

We need to make sure each alien is visible just before it starts
gliding down the screen.  Add a line to the `drift_down_screen()` code
to make this happen:

{{< commit show-when-starting-descent >}}

Try your game!  It should be quite noisy now.

### Make a sound if the player misses

For extra noise, we'll make it so that a sound effect happens if the
player misses all the aliens when they click.  We can tell this
happens by making the *stage* react when it's clicked.

First we need to say that the `Galaxy` stage will use the 'fizz' sound
effect (which comes with this tutorial):

{{< commit add-sound-to-stage >}}

And then we'll add some code to the `Galaxy` so it plays this sound
when the player clicks on the stage:

{{< commit make-miss-sound-when-stage-clicked >}}

Try your game!  It should be even more noisy.


## Keep score

To let the player know how they're doing, we'll add score-keeping to
the game.  Just like in Scratch, your program remembers numbers (or
strings, or lists, or anything else) using a *variable*.  In Python,
you don't have to explicitly make a variable.  Setting a new variable
to a value creates that variable for you.

### Initialise score to zero

The player's score starts off at zero, so near the top of the program,
we'll create the `score` variable with a value of `0`:

{{< commit define-global-score >}}

### Show score

In Scratch, you tick a box to say that you want the variable to be
shown.  In Pytch you do this by writing some code.  We want the
`score` variable to be shown as soon as the game starts, so the
`run()` code inside `Galaxy` is a good place to put this.

We won't go into the details of what `None` is doing there in this
tutorial, but you can see that we give the *name* of the variable that
we want to show:

{{< commit show-score >}}

### Give points for hitting an enemy

Let's give the player 10&nbsp;points when they click on an enemy
invader.  We already have some code which makes a sound when the alien
is clicked, so this is a good place to add the code which updates the
score.

We need to tell Python that it's the *global* variable `score` we want
to change.  Without this, Python thinks you mean a *local* variable
which exists just inside your `handle_hit()` code.  Once we've said
which `score` we're talking about, we add 10 to it.

{{< commit award-score-when-hit-enemy >}}

Try this — you should get 10 points for every blue enemy you click on.

## Avoid repetitive code

The changes we'll make in this chapter aren't essential for the game
to work.  But they do tidy up your code and make it easier to change
and work with.

You might have thought that the code we added, quite early on, to make
the five Alien clones was very repetitive:

    self.go_to_xy(-150, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-90, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-30, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(30, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(90, 180)
    pytch.create_clone_of(self)

There is a pattern to these pairs of lines of code, which we can make
clearer by writing out exactly where those `-90`, `-30`, `30`,
and `90` number come from.  The pattern is that we're adding an extra
`60` each time, starting from `-150`.  We can change the code to show
this clearly:

{{< commit explicit-clone-start-locations >}}

and then we can even make the `-150` and `-90` values fit the exact
pattern, by changing:

{{< commit explicit-0-and-1-clone-start-locations >}}

Now your code should look like

    self.go_to_xy(-150 + 0 * 60, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-150 + 1 * 60, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-150 + 2 * 60, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-150 + 3 * 60, 180)
    pytch.create_clone_of(self)
    self.go_to_xy(-150 + 4 * 60, 180)
    pytch.create_clone_of(self)

and you can see that this is just five copies of

    self.go_to_xy(-150 + SOME_NUMBER * 60, 180)
    pytch.create_clone_of(self)

with a different number in place of `SOME_NUMBER` each time, starting
at&nbsp;0 and going up to&nbsp;4.

We can use a *loop* to avoid all this copied code.  The *loop
variable* `i` will take on values starting at&nbsp;0, and stopping
just before it gets to&nbsp;5.  This "stop just before 5" way of
saying when to stop is how Python does things — it seems strange at
first but does make sense once you get used to it!

Then inside the *loop body* we have the two lines, and use the
variable `i` where the repeated code has `0`, `1`, `2`, `3`, or `4`:

{{< commit replace-repetition-with-loop >}}


## Count lives

The game is quite good now, but there's nothing to discourage the
player from just clicking everywhere.  There's no penalty for hitting
a friendly alien.

We'll fix that by giving the player three lives, and making it so
destroying a friendly alien costs a life.

### A 'custom block'

In Scratch, you can create *custom blocks* to:

* give a name to a particular bit of behaviour

* let you re-use that behaviour without duplicating large stacks of
  blocks.

In Python, you can do the same thing.  You *define* a function, and can
*call* it from elsewhere in your code.  We'll do that to gather
together the "lose a life" behaviour.

We'll copy the existing behaviour of making the *scream* sound,
defining a function `lose_life()`.  To define a function in Python, we
use `def` — we've been using this already in fact, to define the code
which happens when, say, the sprite is clicked on.

Here's the start of our new `lose_life()` function:

{{< commit extract-lose-life-method >}}

Now we have the function, but nobody is using it.  This is like the
situation in Scratch where you have made a custom block, but not used
it anywhere.

We'll change the `handle_hit()` function to use our new function:

{{< commit call-lose-life-method >}}

Test this now — the game should work exactly as before.  (So you might
wonder why we're making these changes.  As your projects get bigger,
it becomes more important that a human can read and understand the
program, and one way to make this easier is by giving names to parts
of the behaviour.)

### Keeping track of lives

We need a variable to store how many lives the player has.  The
changes are very similar to when we brought in the `score` variable.
First we create the variable near the top of our program:

{{< commit define-global-lives >}}

Then we want the variable to be shown on the stage.  We don't want the
display to be right on top of where the score is, so we provide extra
information saying that we want the right-hand edge of the display to
be a little bit in from the right-hand edge of the stage.  This is
what the `right=236` code is doing here:

{{< commit show-lives >}}

And finally we then want to take one life away whenever the player
clicks on a friendly alien.  We say we want to work with the *global*
`lives` variable, and then subtract one from it:

{{< commit decrement-lives >}}

Try this now — you should see the `lives` display go down each time
you click on a green alien.  But the game doesn't stop when you run
out of lives.  We'll fix this next.


## End game when no lives left

Our last piece of work is to make the game stop when the player has
used all their lives.  We *could* just ask 'is `lives` zero?' at
different places in the code, but it will be clearer to give a name to
this idea, with a `game_over` variable.  This will be either `True` or
`False`, and when the game starts up, the game is *not* over, so we want:

{{< commit define-global-game-over >}}

### All lives gone means game is over

The only time that `game_over` might change is when the player has
lost a life.  So, inside `lose_life()`, we'll ask whether subtracting
a life has left `lives` equal to zero.  If so, we update the global
`game_over` variable to be `True`:

{{< commit set-game-over-when-no-lives >}}

### Stop the aliens when game is over

We now have to make sure no more aliens glide down the screen once the
game is over.  We'll change the `forever`-like loop inside
`drift_down_screen()` so that each alien (clone or original) keeps
going as long as the game is not over:

{{< commit stop-descent-loop-when-game-over >}}

Try this now — deliberately click on three green aliens.  You should
see that no more aliens appear, but any aliens which are part-way down
the screen keep going until they reach the bottom.  We'll tidy this
last part up now.

We want all aliens to disappear immediately the game is over.  We'll
make this happen with a message which `lose_life()` will broadcast
after setting `game_over` to `True`:

{{< commit broadcast-game-over >}}

If you try this now, nothing will happen because nobody is *listening*
to this message.  We'll add a last piece of code to the `Alien` so
that all aliens (clones or the original) hide when they hear that
message:

{{< commit hide-when-receive-game-over >}}

### Game complete!

Test your game now and make sure it works properly.


## Challenges

Here are some ways you could make the game even better:

* Once the game is over, the player still hears the *fizz* noise if
  they click on the stage.  Stop this from happening.

* Make the aliens move more quickly as the player's score goes up.

* Add a rare red alien which is worth 50 points.

* Add some left-to-right randomness to where the aliens start.


## Credits

This project was loosely inspired by the *Red Alert* game in the DK
book [*Coding Games in
Python*](https://www.dk.com/us/book/9781465473615-coding-games-in-python/).

### Detailed credits

{{< asset-credits >}}
