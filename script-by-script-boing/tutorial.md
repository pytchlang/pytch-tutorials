# Boing: Make a Pong-like game

In this tutorial we will make a version of the classic game
[Pong](https://en.wikipedia.org/wiki/Pong).


---

## Set up the playing area

The game needs a better backdrop than the plain one it has by default.
Pytch’s media library has one we can use.

{{< learner-task >}}

Add the “court” image as a new Backdrop for the stage.  You can find
it in the media library.

{{< learner-task-help >}}

{{< jr-commit add-table-backdrop add-medialib-appearance ["court.png"] >}}

{{< /learner-task >}}

You don’t need the default plain backdrop any more.

{{< learner-task >}}

Delete the plain white backdrop from the stage.

{{< learner-task-help >}}

{{< jr-commit remove-default-backdrop delete-appearance >}}

{{< /learner-task >}}


## Add the player’s bat

Next, the game needs a bat for the player to control.

{{< learner-task >}}

Add a sprite called `PlayerBat` to your game.

{{< learner-task-help >}}

{{< jr-commit add-PlayerBat-sprite add-sprite >}}

{{< /learner-task >}}

The sprite needs a costume.  There is a bundle of two costumes in
Pytch’s media library with — one “smiling” and one “wincing”.  We will
use the “smiling” one now, and the “wincing” one later on in this
tutorial.

{{< learner-task >}}

Add the “Boing player bats” bundle of images as Costumes for the
`PlayerBat` sprite.

{{< learner-task-help >}}

{{< jr-commit add-PlayerBat-costumes add-medialib-appearances-entry ["Boing player bats"] >}}

{{< /learner-task >}}


{{< learner-task >}}

Test your game!  You should see the player’s bat in the middle of the
court background.

{{< /learner-task >}}


## Let the player control their bat

The player bat needs some scripts to control its behaviour.

When the green flag is clicked, the player’s bat needs to go to its
starting position at the left of the stage.

{{< learner-task >}}

Add a “when green flag clicked” script to the `PlayerBat` sprite.

{{< learner-task-help >}}

{{< jr-commit add-empty-PlayerBat-play-script add-script >}}

{{< /learner-task >}}

You can use the “Show coordinates” helper to check that `(-212, 0)` is
a reasonable choice for the player’s bat’s starting position.

{{< learner-task >}}

Add a line of code to the script which moves the player’s bat to the
position with coordinates `(-212, 0)`.

{{< learner-task-help >}}

{{< jr-commit centre-PlayerBat-on-start edit-script >}}

{{< /learner-task >}}

Once the game has started, the player needs to be able to move the
bat, either up or down.

### Moving up

The program should continually check whether the person is
pressing the `w` key to move up.  If they are, your code needs to
change the bat’s `y` coordinate.

In Scratch, this would look like:

``` scratch
forever
  if <key (w v) pressed> then
    change y by (3)
```

{{< learner-task >}}

Work out the Python code which does this job.  You can use the help
`(?)` to find how to do “forever”, “if”, “key pressed”, and “change y”
in Pytch.

You’ll also need to know how to put Python code “inside” things like
“forever” and “if”.  There are examples in the help.

{{< learner-task-help >}}

{{< learner-task-help >}}

{{< jr-commit move-PlayerBat-up-with-W edit-script >}}

{{< /learner-task >}}

### Moving down

This is similar.

{{< learner-task >}}

Add similar lines of code, to make the player’s bat move down when the
`s` key is pressed.

{{< learner-task-help >}}

**Important:** You do **not** want another `while True` loop.  The new
code can go “inside” the same `while True` loop you already have.

{{< learner-task-help >}}

You can copy and paste the two lines of code you already have, then
change the copy, if you think that will save time.

{{< learner-task-help >}}

{{< jr-commit move-PlayerBat-down-with-S edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  Hold down the `w` key and check the bat moves up.
Hold down the `s` key and check it moves down.

**There is a bug — what is it?**

{{< learner-task-help >}}

The player can move the bat right off the top or bottom of the court.

{{< /learner-task >}}

### Staying on the court

If you play the game now, you’ll see a bug.  You can move the bat
right off the top or bottom of the court.  To stop this, you need to
add checks to your code.

At the moment, the code only checks whether the player is pressing `w`
before deciding it should move the bat up.  But there are *two* things
that *both* must be true for the bat to move up:

* The `w` key must be pressed.
* The bat must be low enough that moving up is allowed.

{{< learner-task >}}

Extend the

``` python-expression
pytch.key_pressed("w")
```

test in your code to *also* test whether the bat is low enough.

{{< learner-task-help >}}

To test whether the bat is low enough, you can ask whether its _y_
coordinate is less than some fixed value: you can experiment to check
that `112` works for this.

{{< learner-task-help >}}

The expression

``` python-expression
self.y_position < 112
```

will test whether the bat is low enough.

{{< learner-task-help >}}

You can join these tests together with Python’s `and` operator.  This
works the same as Scratch’s

``` scratch
< <> and <> >
```

block.

{{< learner-task-help >}}

The new test expression for your `if` statement is

``` python-expression
pytch.key_pressed("w") and self.y_position < 112
```

{{< learner-task-help >}}

{{< jr-commit clamp-PlayerBat-y-high edit-script >}}

{{< /learner-task >}}

The same problem happens for moving down.  The player bat can go right
off the bottom of the court.

{{< learner-task >}}

Make a similar change to the “move down” code.

{{< learner-task-help >}}

The extra part of the test in the `if` statement this time will be to
test whether the _y_ coordinate is _greater than_ some fixed value.
Everything is symmetrical up/down, so -112 will do the job.

{{< learner-task-help >}}

{{< jr-commit clamp-PlayerBat-y-low edit-script >}}

{{< /learner-task >}}


## Add the ball

The next thing to add is the ball.  You do this in a very similar way
to how you added the player’s bat.

{{< learner-task >}}

Add a `Ball` sprite to your project.

{{< learner-task-help >}}

{{< jr-commit add-Ball-sprite add-sprite >}}

{{< /learner-task >}}

And it needs a costume.

TODO: There are two balls; distinguish them by filename?  "yellow-ball.png"?

{{< learner-task >}}

Add the `ball.png` costume from Pytch’s media library to your sprite.

{{< learner-task-help >}}

{{< jr-commit add-Ball-costume add-medialib-appearance ["ball.png"] >}}

{{< /learner-task >}}

When the green flag is clicked, the ball should go to the very centre
of the screen.

{{< learner-task >}}

Add a “when green flag clicked” script to your `Ball` sprite, with
code to move it to the centre of the screen.

{{< learner-task-help >}}

The centre of the screen is at coordinates `(0, 0)`.  You can check
this with the “Show coordinates” tool.

{{< learner-task-help >}}

{{< jr-commit centre-Ball-on-green-flag add-script >}}

{{< /learner-task >}}

Then it should straight away start moving away from the player, to
give them time to get ready.  This means moving to the right.

It’s useful to think ahead a bit here.  The ball won’t always be
moving to the right.  Once the robot has hit the ball, the ball will
move to the left.  To remember the direction the ball is travelling
in, you can use a _variable_.  Choosing a good name for variables is
important.  This variable will remember the *velocity* of the ball in
the *x* direction, so `x_velocity` is a good name.

(You might have thought of “speed” — the difference is that “velocity”
includes information about direction but “speed” doesn’t.)

{{< learner-task >}}

Add code which sets the variable `x_velocity` to the value `3`.  This
value was chosen by experiments to make the ball move at a good speed.

{{< learner-task-help >}}

{{< jr-commit define-Ball-x-velocity edit-script >}}

{{< /learner-task >}}

Now you can write code to move the ball.

{{< learner-task >}}

Add a `while True` loop which moves the ball horizontally with the
correct velocity.

{{< learner-task-help >}}

Moving the ball horizontally is done by changing its _x_ coordinate by
the value of the `x_velocity` variable.

{{< learner-task-help >}}

You will need the code

``` python
self.change_x(x_velocity)
```

inside a `while True` loop.

{{< learner-task-help >}}

{{< jr-commit move-Ball-with-x-velocity edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  You should still be able to move the player bat up and
down (`w` and `s` keys) while the ball moves to the right.

**There is a bug — what is it?**

{{< learner-task-help >}}

The ball just keeps going off the right of the stage.

TODO: Pick consistent word for stage / court / screen.

{{< /learner-task >}}

The problem here is that the ball of course just keeps going right,
off the edge of the screen.

The next chapter will add the robot bat for the player to play
against.  This will give the ball something to bounce off.


## Add the robot opponent

This should be familiar by now!

{{< learner-task >}}

Add a _RobotBat_ sprite to your program.

{{< learner-task-help >}}

{{< jr-commit add-RobotBat-sprite add-sprite >}}

{{< /learner-task >}}

There are some “robot bat” costumes in the media library.

{{< learner-task >}}

Add the right costumes to this new sprite.

{{< learner-task-help >}}

{{< jr-commit add-RobotBat-costumes add-medialib-appearances-entry ["Boing robot bats"] >}}

{{< /learner-task >}}

At the start of the game, the robot bat needs to go to the right
place on the screen.

{{< learner-task >}}

Add a “when green flag script” to your `RobotBat` sprite, with code
which moves it to the correct starting point — at the right,
vertically centred.

{{< learner-task-help >}}

The coordinates `(212, 0)` are a reasonable guess for this.

{{< learner-task-help >}}

{{< jr-commit centre-RobotBat-on-green-flag add-script >}}

{{< /learner-task >}}

The robot bat needs some intelligence, but next you’ll go back to the
`Ball` sprite, and make it bounce.


## Bounce the ball off the bats: simple version

You’ll develop the “bounce off bats” code in stages.  To start with,
the ball will always bounce off the left and right edges, taking no
notice of where the bats are.

The ball can tell if it’s moved far enough to the right that it should
bounce off the robot.  It does this by looking at its *x* coordinate.
If it has moved too far, it needs to move _back_ the same amount it just
moved, and then change its `x_velocity` to be the _opposite_ of what
it just was.

{{< learner-task >}}

Add code to the `Ball` which:

* Checks whether its *x* coordinate is greater than some fixed value;
  you can check that `200` is a reasonable guess for this.
* If so, you need to do two things:
    * Change the ball’s *x* coordinate by the opposite (i.e., negative)
      of the `x_velocity`.  This puts the ball back where it was before
      it moved.
    * Set the `x_velocity` to the opposite of what it currently is.

{{< learner-task-help >}}

You will need an `if` statement.  The test will be

``` python-expression
self.x_position > 200
```

{{< learner-task-help >}}

To find the negative of the value in the variable `x_velocity`, you
can use the Python expression

``` python-expression
-x_velocity
```

{{< learner-task-help >}}

{{< jr-commit bounce-Ball-off-RobotBat edit-script >}}

{{< /learner-task >}}

You can do something very similar to make the ball bounce when it’s at
the left edge of the screen — remember for this first stage, it
doesn’t matter where the bat is.

{{< learner-task >}}

Add code to the `Ball` which makes it bounce at the left edge.  The
code will be very similar to the three lines you just added.

{{< learner-task-help >}}

The test in the `if` statement needs to check whether the ball is ‘too
far’ left, using the Python expression

``` python-expression
self.x_position < -200
```

{{< learner-task-help >}}

But the code “inside the `if`” to actually make the bounce happen is
exactly the same.

TODO: Should we combine those `if` statements then?

{{< learner-task-help >}}

{{< jr-commit bounce-Ball-off-PlayerBat edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  You should still be able to move the player bat up and
down (`w` and `s` keys).  The ball should bounce back and forth.

**There is a bug (which we were expecting) — what is it?**

{{< learner-task-help >}}

The ball bounces even if the player misses it.

{{< /learner-task >}}

The next chapter will fix this.


## Bounce properly off the player’s bat

Once the code knows the ball is far enough left that it might bounce
off the player’s bat, it should then also check whether the ball is
touching the bat.

{{< learner-task >}}

Move the “bounce at left” lines of code inside another `if` statement,
inside the

``` python
if self.x_position < -200:
```

one.  The new `if` statement should test whether the ball is touching
the player bat.

**Why not use `and` like before?**  Looking ahead, we want to do
something different if the ball is far enough left but the player
misses it.

{{< learner-task-help >}}

The help bar will show you some examples of testing for one sprite
touching another.  Look for the Python equivalent of the Scratch

``` scratch
< touching [PlayerBat v] >
```

{{< learner-task-help >}}

{{< jr-commit check-hit-PlayerBat edit-script >}}

{{< /learner-task >}}

Now the ball bounces when it should.  If the player is too high or too
low, the ball sails right past, off to the left.

But it’s not an interesting game because the ball only moves exactly
left and right.  The ball needs to bounce off in different directions.

The ball _also_ needs to remember how quickly it’s moving
_vertically_, i.e., in the _y_ direction.

{{< learner-task >}}

Add a variable `y_velocity` which will store how quickly (and in which
direction) the ball is moving in the *y* direction.  Think about what
its starting value should be.

{{< learner-task-help >}}

The ball starts off moving exactly horizontally, so its *y*-velocity
should start at zero.

{{< learner-task-help >}}

{{< jr-commit add-Ball-state-y-velocity edit-script >}}

{{< /learner-task >}}

Now the code needs to *use* this variable.

{{< learner-task >}}

Add code at the end of the “body” of the `while True` loop which
changes the ball’s *y* coordinate by its `y_velocity`.

{{< learner-task-help >}}

{{< jr-commit change-Ball-y edit-script >}}

{{< /learner-task >}}

At the moment this makes no difference, because changing something by
zero leaves it alone.

{{< learner-task >}}

Give the ball a random `y_velocity` when it bounces off the player’s
bat.

{{< learner-task-help >}}

Good values for `y_velocity` are whole numbers from `-4` to `4`
(inclusive).  Look in the help to find out how to choose a random
number in this range.

{{< learner-task-help >}}

The Python expression

``` python-expression
random.randint(-4, 4)
```

will do this.

{{< learner-task-help >}}

{{< jr-commit random-Ball-y-velocity-PlayerBat-bounce edit-script >}}

{{< /learner-task >}}

The ball needs to do the same when it bounces off the robot bat.

{{< learner-task >}}

Give the ball a random `y_velocity` when it bounces off the robot
bat.

{{< learner-task-help >}}

{{< jr-commit random-Ball-y-velocity-RobotBat-bounce edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.  You should still be able to move the player bat up and
down (`w` and `s` keys).  The ball should bounce back and forth, and
when the player hits it, it should go in a random direction.

**There is a bug — what is it?**

{{< learner-task-help >}}

The ball goes off the top or bottom of the table.

{{< /learner-task >}}

The next chapter will fix this.


## Bounce the ball off the top and bottom of the table

This is a similar problem to bouncing the ball off a bat, except the
code needs to check the *y* coordinate, and work with `y_velocity`.

{{< learner-task >}}

Add code after the `change_y()` code which makes the ball check if it
has gone too high or too low, and react correctly if so.

{{< learner-task-help >}}

You can use an `if` statement with a test which asks whether either of
the following is true:

TODO: Think the 158 values need to be smaller in magnitude.  The ball
enters the top/bottom boundaries of the court with 158.

* the *y* coordinate is “too big” (meaning the ball is about to go off
  the top of the stage); greater than `158` counts as too big
* the *y* coordinate is “too small” (meaning the ball is about to go off
  the bottom of the stage); smaller than `-158` counts as too small.

You can join these individual tests with Python’s `or` operator.

{{< learner-task-help >}}

If the ball is too high or too low, you need code which:

* changes the ball’s *y* coordinate by the opposite of the change it
  just made;
* makes the `y_velocity` be the opposite of what it currently is.

{{< learner-task-help >}}

{{< jr-commit make-Ball-bounce-vertically edit-script >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Try your game.

**There are some bugs left — what are they?**

{{< learner-task-help >}}

* The game is too generous about letting the player hit the ball — the
  player can “hit” the ball after it’s gone past the bat.

* The ball can “get stuck” in the player’s bat.

* The robot player never moves, but the ball bounces off the
  right-hand edge of the screen anyway.

{{< /learner-task >}}

The next chapters will fix these.


## End the game if the player misses

The code to bounce the ball off the player’s bat checked if the ball
was touching the bat, and bounced the ball if so.  But it does nothing
if the ball is _not_ touching the bat.

{{< learner-task >}}

Add an `else` clause to the

``` python
if self.touching(PlayerBat):
    # [code to bounce ball]
```

statement, so that if the player misses, that's the end of the
game.

{{< learner-task-help >}}

You can use the help to see how `if`/`else` statements work in Python.

{{< learner-task-help >}}

The `else` code should make the ball hide, and use the Python `break`
statement to jump out of the `while True` loop and finish the game.

{{< learner-task-help >}}

{{< jr-commit hide-Ball-if-PlayerBat-misses edit-script >}}

{{< /learner-task >}}

**TODO: Can we do without this next bit?  Make it a challenge**

This is better, but looks odd because the ball just vanishes.  We can
fix this by moving the ball for another few steps once we know the
player has missed it:

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit continue-Ball-briefly-if-Player-misses edit-script >}}

{{< /learner-task >}}

(This still isn’t quite right if the ball should bounce vertically.
Fix this if you like!)


## Move the robot’s bat automatically

Returning to the robot player, at the moment it just moves to the
centre at the start of the game and stays there.  It needs to
keep its vertical position (_y_ coordinate) matching the ball’s.  This
will make it follow the ball up and down.

{{< learner-task >}}

Add code to the `RobotBat` sprite which makes it forever make its *y*
coordinate match the Ball’s.

{{< learner-task-help >}}

**TODO: This might need breaking down.  Students might wonder why
we’re bothering with a variable.  And the “get the original ball
instance” has quite a lot going on behind the scenes.**

{{< learner-task-help >}}

{{< jr-commit make-RobotBat-track-Ball edit-script >}}

{{< /learner-task >}}

This is much better, but still not quite right.  The robot can go off
the top of the court or off the bottom.

The problem is that `target_y` can be too big or too small.

{{< learner-task >}}

Add code just before the `set_y()` call which tests whether `target_y`
is too big, and if so, sets it to the maximum allowed value.  “Too
big” means greater than `120`.

**TODO: Check that 120 for new assets.  Where does player bat hit its stops?**

{{< learner-task-help >}}

{{< jr-commit clamp-RobotBat-y-high edit-script >}}

{{< /learner-task >}}

Now if you test this, you should see that the robot bat stops at the
top of the table.

{{< learner-task >}}

Add code just before the `set_y()` call which tests whether the
`target_y` is too small, and if so, sets it to the minimum allowed
value.  “Too big” means less than `-120`.

**TODO: Or should we use `tgt = min(tgt, 120)` etc.?**

{{< learner-task-help >}}

{{< jr-commit clamp-RobotBat-y-low edit-script >}}

{{< /learner-task >}}


## Add effects when a bat hits the ball

The game would look better with animation effects when the player or the
robots hits the ball.  This is what the costumes with “wince” in their
name are for.

**TODO: Explain coordination between ball and bats via bcast/recv.**

{{< learner-task >}}

Add a script **to the `PlayerBat` sprite** which runs when the sprite
receives a `"player-hit"` message, with code which:

* switches to the `"player-bat-wince.png"` costume;
* waits a short time;
* switches back to the `"player-bat-smile.png"` costume.

{{< learner-task-help >}}

To switch costume, you can either explicitly say

``` python
self.switch_costume("player-bat-wince.png")
```

or, because there are only two costumes, you can say


``` python
self.next_costume()
```

both times.  This works because if a Sprite is wearing its last
costume, `self.next_costume()` moves back to the first costume.

Which way do you prefer?

{{< learner-task-help >}}

{{< jr-commit define-PlayerBat-hit-handler add-script >}}

{{< /learner-task >}}

To make this actually happen, the ball needs to broadcast that message
when it bounces off the player’s bat.

{{< learner-task >}}

Add code **to the `Ball` sprite** which broadcasts the message as part
of the “bounce off player’s bat” section.

{{< learner-task-help >}}

{{< jr-commit trigger-PlayerBat-flash-on-hit edit-script >}}

{{< /learner-task >}}

Now do something very similar for the robot.

**TODO: Costume names need fixing in code.**

{{< learner-task >}}

Add a script **to the `RobotBat` sprite** which runs when the sprite
receives a `"robot-hit"` message, and which switches briefly to its
`"robot-bat-wince.png"` costume.

{{< learner-task-help >}}

{{< jr-commit define-RobotBat-hit-handler add-script >}}

{{< /learner-task >}}

To make this actually happen, the ball must broadcast `"robot-hit"` at
the right time.

{{< learner-task >}}

Add code **to the `Ball` sprite** which broadcasts the message as part
of the “bounce off robot’s bat” section.

{{< learner-task-help >}}

{{< jr-commit trigger-RobotBat-flash-on-hit edit-script >}}

{{< /learner-task >}}


## Make fine adjustments to positions

Some of the numbers the code uses for things like the *x* positions of
the bats and the bounce positions of the balls are not *quite* right.
If you experiment carefully, you’ll see that they need adjusting.

The player’s bat needs to move left a tiny amount:

{{< learner-task >}}

Move the player’s bat so that its *x* coordinate is `-219`.

{{< learner-task-help >}}

{{< jr-commit adjust-PlayerBat-position edit-script >}}

{{< /learner-task >}}

The robot bat needs to move right a tiny amount:

{{< learner-task >}}

Move the robot bat so that its *x* coordinate is `217`.

{{< learner-task-help >}}

{{< jr-commit adjust-RobotBat-position edit-script >}}

{{< /learner-task >}}

And the values the ball compares its *x* position to need to be
changed to match.

{{< learner-task >}}

Make the ball use `202` as the value to know when it’s too far to the
right, and `-203` for testing whether it’s too far to the left.

{{< learner-task-help >}}

{{< jr-commit adjust-Ball-thresholds edit-script >}}

{{< /learner-task >}}


## Challenges

Here are some ways you could make the game better.  Both of these
tasks are quite advanced, so your first step should be to think about
how to break the job down into manageable pieces.

* At the moment, the human player has no chance against the computer.
  Can you make it so the computer does *not* always win?

* At the moment, the game stops once the player misses the ball.  Can
  you instead keep score, and make it so the winner is the first to
  get ten points?  This only makes sense if you’ve already made it so
  the computer sometimes misses!

You could also experiment with changing the physics of the game, for
example:

* Add gravity, so the ball falls towards the bottom of the screen.
  Think about how the `y_velocity` of the `Ball` sprite needs to
  change to give the right effect.  You might then also want to change
  the random velocity the ball gets when it bounces off a bat.

Can you think of other changes or improvements?

**TODO FOR TUTORIAL AUTHOR: Use underscores or asterisks consistently
for italics.  Check all numbers (eg thresholds for “off the edge”)
match text/code.  Use “table” or “court” or “stage” or “screen”
consistently; maybe even say at start what term we’ll use.  Review
other TODOs in text.**


### Credits

**TODO: Take fresh screenshot.**

**TODO: Check progress trail doesn’t make the colun too wide on narrow
viewports.  What about “hidden from progress” chapters?  How are we
meant to navigate to them?**

### Detailed credits

{{< asset-credits >}}
