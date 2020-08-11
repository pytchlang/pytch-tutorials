# Boing: Make a Pong-like game

In this tutorial we will make a version of the classic game
[Pong](https://en.wikipedia.org/wiki/Pong).  We are going to use the graphics,
and some of the ideas, kindly made available by the [Code the
Classics](https://wireframe.raspberrypi.org/books/code-the-classics1) book
published by the Raspberry Pi organisation.

{{< run-finished-project >}}

---

## Make the playing area

We first set up the _Stage_, which, like Scratch, is where the action takes
place.  We're going to use the same image as the version in _Code the Classics_.
We define a `class` which is based on the built-in `pytch.Stage`, and say what
_Backdrops_ we want it to have.  In Pytch we do this by giving a _list_ of
pairs.  The first thing in each pair is the name we want to be able to use to
talk about this backdrop in our code.  The second thing is where Pytch can find
the image file.

{{< commit add-stage-with-background >}}


## Add the player's bat

Now we have the background, we want to put the player's bat into the
game.  The first part of this is similar to how we introduced the
_BoingBackground_.  We define _PlayerBat_, which we say is a kind of
_Sprite_.  To say what _Costumes_ it has, we need to give more
information than for a _Backdrop_ for a _Stage_.  As well as the name
we want to call it in our code (here, ``normal``), and the image file
we want to use (here, ``images/bat00.png``), we need to say where the
_centre_ is.  When we tell a sprite to go to a particular place on the
stage, it's the Sprite's _centre_ which actually ends up exactly at
that point.  Our image is 60 pixels square (it has some clear
background), and we want its actual centre to be the 'centre' as Pytch
sees it.  So we need:

{{< commit add-Player-with-costume >}}

When the green flag is clicked, we want the player's bat to go to its
starting position, and become visible:

{{< commit init-Player-on-green-flag >}}

Once the game has started, the person playing the game needs to be
able to move the bat.  We do this by continually checking whether the
person is pressing the ``W`` key to move up, or the ``S`` key to move
down.  If they are, we change the bat's _y_ coordinate:

{{< commit move-Player-with-W-and-S >}}

If you play the game now, you'll see a problem.  You can move the bat
right off the top of the stage.  To stop this, we'll only move if
you're pressing ``W`` and you're low enough that moving up is allowed.
We'll make the same change to the 'move down' part of the code:

{{< commit limit-Player-y-coord >}}


## Add the ball

The next thing to add is the ball.  We do this in a very similar way
to how we added the player's bat.  The ball only has one costume, and
we tell Pytch what we want to call it (``ball``), the file to use, and
where the centre is:

{{< commit add-Ball-with-costume >}}

When the green flag is clicked, the ball should go to the very centre
of the screen and show itself:

{{< commit centre-Ball-on-green-flag >}}

Then it should straight away start moving away from the player, to
give them time to get ready.  We do this by continually changing the
ball's _x_ coordinate:

{{< commit move-Ball-across-screen >}}

The problem here is that the ball of course just keeps going right
off the edge of the screen.  We know we're going to need to keep track
of which direction the ball is going, so we bring in a variable
`x_speed` belonging just to the _Ball_:

{{< commit add-Ball-state-x-speed >}}

We'll leave the ball here until there is a robot bat for the player to
play against, which is what we'll do next.


## Add the robot opponent

This is familiar by now.  We add _RobotBat_, which is a sort of
_Sprite_, with a costume:

{{< commit add-Robot-with-costume >}}

When the green flag is clicked, the robot bat will go to the right
place on the screen, which is at the right, vertically centred:

{{< commit centre-Robot-on-green-flag >}}

Shortly we'll give the robot bat some intelligence, but next we'll
return to making the ball bounce.


## Bounce the ball off the bats: simple version

The ball can tell if it's moved far enough to the right that it should
bounce off the robot.  Straight after the ball has moved, we want
check if it's moved too far.  If it has, we want to move _back_ the
same amount we just moved, and then change our ``x_speed`` to be the
_opposite_ of what it just was:

{{< commit bounce-Ball-off-Robot >}}

We can do the same to make the ball check if it's bounced off the
player's bat:

{{< commit bounce-Ball-off-Player >}}

If you run this now, it looks good but boring.  The ball just bounces
backwards and forwards between the player and the robot.  But!  If you
move the player up or down, you'll see that the ball bounces even it
the player misses it.  We'll fix this next.


## Bounce properly off the player's bat

What we want to do is find where on the player's bat the ball has
hit.  We'll call the centre of the bat 'zero', and then positive
positions are towards the top of the bat, and negative positions are
towards the bottom.  We can work this out by finding the vertical
position — the _y_ coordinate — of the player's bat, and subtracting
that from the ball's _y_ coordinate:

{{< commit compute-position-on-Player >}}

By experimenting with the '45', we can see what a fair number to use
so the ball bounces when it looks like it should bounce, and misses
when it looks like it should miss.  The ball only bounces if the
position on the bat is 'higher than the bottom of the bat' and also
'lower than the top of the bat':

{{< commit check-Player-has-hit-Ball >}}

This is better.  The ball bounces when it should, but if the player is
too high or too low, the ball sails right past, off to the left.  But
this does not make for an interesting game.

We'll make the ball bounce off in different directions, depending
where on the bat the player hits it.  If the player hits the ball with
the top of their bat, the ball will bounce off upwards, and similarly
for the bottom of their bat.

To let us work with this, the ball needs to remember how quickly it's
moving _vertically_, i.e., in the _y_ direction.  So we add a local
variable ``y_speed``.  It starts off as zero, because the ball is
moving neither up nor down, just straight across:

{{< commit add-Ball-state-y-speed >}}

Every step, the ball should change its _y_ position by this amount:

{{< commit change-Ball-y >}}

At the moment this makes no difference, because changing something by
zero leaves it alone.

We can now make the ball fly off in different directions, depending on
where on the bat the player hit it.  We worked out that the 'position
on bat' goes from about ``-45`` at the bottom to ``45`` at the top.
We'll divide this by ten to get the ball's new _y_-speed, but ignoring
any remainder by telling Pytch to turn the answer of the division into
an _integer_ (whole number) using ``int()``:

{{< commit make-Ball-y-speed-depend-on-Player-position >}}

If you try this now, you can check that the ball bounces off the
player's bat as it should.  But the ball then just keeps flying off
the top or bottom of the screen.

## Bounce the ball off the top and bottom of the court

We can tell if the ball has gone too high or too low by comparing its
_y_ coordinate to numbers chosen by experiment.  If it has gone too
high or too low, we undo the last _y_ change, and make the _y_-speed
be the opposite of what it was:

{{< commit make-Ball-bounce-vertically >}}

If you play the game now, it sort of works, but there are two obvious
problems:

* The ball keeps going past the player's bat if you miss and then
  after a short while mysteriously re-appears.

* The robot player never moves but still the ball bounces off the
  right-hand edge of the screen.

We'll fix these things next.


## End the game if the player misses

The code we added to bounce the ball off the player's bat checked if
the _position on the bat_ was not too high or too low, and then
bounced the ball if it was OK.  But it did nothing if the ball _was_
too high or too low.  We need to add an ``else`` clause, saying that
if the player misses, that's the end of the game.  The ball should
hide, and we ``break`` out of the ``while True`` loop:

{{< commit hide-Ball-if-Player-misses >}}

This is better, but looks odd because the ball just vanishes.  We can
fix this by moving the ball for another few steps once we know the
player has missed it:

{{< commit continue-Ball-briefly-if-Player-misses >}}

(This still isn't quite right if the ball should bounce vertically,
but we'll ignore that.)


## Move the robot's bat automatically

Returning to the robot player, at the moment it just moves to the
centre at the start of the game and stays there.  We want it to then
keep its vertical position (_y_ coordinate) matching the ball's.  This
will make it follow the ball up and down:

**TODO: automatically provide a context in the "change the code"
header, like "change the code like this, in the BAR method of the FOO sprite"?**

{{< commit make-Robot-track-Ball >}}

This is much better, but still not quite right.  The robot can go off
the top of the court or off the bottom.  If moving to the ball's
position has taken the bat off the top of the court, we set the bat to
be at the top of the court instead.  And similary for the bottom:

{{< commit ensure-Robot-stays-in-court >}}


## Make some noise

{{< work-in-progress >}}

We want to bring in some sounds for the game:

* Different bounce noises for bouncing off a bat compared to the top
  or bottom of the court.

* Make a sound when the player loses.  (The robot never loses!)

We define these in a similar way to costumes.  We say what the
``Sounds`` for a sprite are.  Each sound needs a name we'll call it in
our code, and a filename for the sound file:

{{< commit define-Sounds-for-Ball >}}

To make the 'a bat hit the ball' sound, we start the `hit` sound just
after changing the ball's `x_speed`, which we do here for if it hits
the robot's bat:

{{< commit play-hit-sound-for-Robot-hit >}}

and here if the ball has bounced off the player's bat:

{{< commit play-hit-sound-for-Player-hit >}}

If the ball bounces off the top or bottom of the court, we start the
`bounce` sound straight after flipping the ball's `y_speed`:

{{< commit play-bounce-sound >}}

And we can start the `lost` sound once the ball has gone past the
player's bat and hidden itself:

{{< commit play-lost-sound >}}


## Add effects when a bat hits the ball

To make the game look better, we'll add a flash effect when either the
player or the robots hits the ball.  We'll need to add a costume to
the player bat Sprite:

{{< commit declare-Player-hit-flash-costume >}}

Next we say how we want the flash to happen.  We want to switch to the
`hit-flash` costume, wait a short time, then switch back to `normal`.
We'll do this when the player's bat sprite receives a message
`player-hit`:

{{< commit define-Player-hit-handler >}}

To make this actually happen, we want to broadcast that message when
the ball bounces off the  player's bat:

{{< commit trigger-Player-flash-on-hit >}}

**TODO: Move the broadcast to just before the start-sound?  That keeps
'effects' together, after the state changes to make the game actually work.**

Now we do something very similar for the robot.  First add a costume:

{{< commit declare-Robot-hit-flash-costume >}}

Define what needs to happen to make the robot bat flash:

{{< commit define-Robot-hit-handler >}}

And then trigger it when the ball bounces off the robot's bat:

{{< commit trigger-Robot-flash-on-hit >}}


## Avoid a stalemate

{{< work-in-progress >}}

The game can get 'stuck' with the ball bouncing just straight left and
right between the bats.  This is boring.  We'll make it so that if the
ball bounces off the robot bat and is going horizontally, we'll change
it to go either gently up or gently down at random.

To do this, we need to use the random number part of Pytch, by
bringing in the `random` module:

{{< commit import-random-module >}}

Now we have this, we can test if the ball's `y_speed` is zero, and if
so, use the `random.choice()` function to make Pytch randomly choose
between the two `y_speed` values we want:

{{< commit ensure-nonzero-y-speed-on-Robot-hit >}}
