# Q*bert: Recreate the cube-hopping action

As Mark Vanstone explains in [Issue 42 of Wireframe
magazine](https://wireframe.raspberrypi.org/issues/42):

> Late in 1982, a funny little orange character with a big nose landed
> in arcades.  The titular Q*bert’s task was to jump around a network of
> cubes arranged in a pyramid formation, changing the colours of each as
> they went.  Once the cubes were all the same colour, it was on to the
> next level.

In this tutorial we'll follow Mark's example and create the basics of
this classic arcade game.

{{< run-finished-project >}}


## Credits

Many thanks to the Raspberry Pi Press for making the contents of their
*Wireframe* magazine available under a Creative Commons licence.  We
have used their code for inspiration, and also the images.

Many thanks to Freesound users *greenvwbeetle*, *Robinhood76*, and
*InspectorJ* for making their sound effects available under friendly
licences.

### Detailed credits

{{< asset-credits >}}



---

## Set up the background

Our first job is to set up the playing background.  We'll use the
image from Wireframe, modified slightly to fit the size of the Pytch
stage.  The image is bundled with this tutorial, so we just need to
define the sort of *Stage* we will be using in this game:

{{< commit add-Stage-with-backdrop >}}

If you build the project now, you'll see the background.

## Define the blocks for making the pyramid

The game world is a pyramid of blocks.  We'll make this in Pytch by
having a `Block` sprite, and create a *clone* of it for every block in
the pyramid.  First we'll define the `Block` sprite, and say what
costumes we'll use with it.  The two costumes have different coloured
tops, one for the starting state, and one which is lit up once Qbert
has landed on that cube.

{{< commit add-Block-with-costumes >}}

If you try the project now, you can see a single block appear in the
middle of the stage.  We won't want this to happen once we're using
clones, so we'll tell Pytch not to show this sprite on start-up:

{{< commit start-original-Block-not-shown >}}

The block is also a bit big for the size of the Pytch stage.  We'll
fix that when we come to making the pyramid.

## Make the pyramid

Getting this right is going to require some maths!  The pyramid has
seven *rows*, and each row has a different number of *blocks* in it.
Each block will be a clone of the original *Block* sprite.

We'll give each row and block a number.  The bottom row will be *row
zero*, and within each row, the block at the far left will be *block
zero* of that row.

The bottom row (row 0, remember) has seven blocks in it.  The next row
up (row 1) has six blocks, and so on.  We can see that row number *r*
has (7&nbsp;−&nbsp;*r*) blocks in it.

To work out where to put each block, we need to work out its *x* and
*y* coordinates.

**
TODO: Finish this explanation, possibly with the aid of a picture.
**

Putting this altogether, we can create our clones with this code:

{{< commit create-block-pyramid >}}

If you try the project now, by building it and then clicking the green
flag, nothing happens.  This is because all the clones we've made are
still not shown.  We can fix this by giving *Block* a
`when_I_start_as_a_clone` handler, which will shrink the clone
slightly and then show itself:

{{< commit block-clone-set-size-show >}}

If you build and green-flag the project now, you'll see the pyramid
appear block by block.

## Introduce the Q*bert character

Now let's bring in our hero!  We'll define a *Sprite* for Q\*bert:

{{< commit add-Qbert-with-costumes >}}

Q\*bert has four costumes, one for each direction they might face.

If you build now, you'll see Q\*bert appear in the middle of the
stage.  We don't want this to happen in the real game, so we'll tell
Pytch to start Q\*bert off not shown:

{{< commit start-Qbert-not-shown >}}

We'll want Q\*bert to set themselves up once the pyramid is complete,
so we'll define a method which will listen out for a `"set-up-qbert"`
message.  This method will make Q\*bert move to the top block, face
downhill, and show themselves:

**
TODO: Explain extra offset of 28.
**

{{< commit initialise-Qbert-position >}}

This should happen once the pyramid is ready for Q\*bert, so we'll go
back to the *Block* sprite and send the `"set-up-qbert"` message once
we've created all the clones:

{{< commit tell-Qbert-to-set-up >}}

If you try this, it doesn't look right.  Q\*bert is behind the pyramid
of blocks.  We need to tell Pytch to bring Q\*bert to the *front* of
the drawing:

{{< commit move-Qbert-to-front >}}

## Let the player move Q\*bert

The player will control Q\*bert with the arrow keys.  We'll start with
the *down* arrow key, which will move Q\*bert 'southwest' on the
screen.

We want Q\*bert to face in the correct direction.  We can check in the
*Images and sounds* tab to see which image this is — it's `"qbert2"`.
We want Q\*bert to move 28 pixels to the left and 42 pixels down, which
we'll do in 14 steps of "2 left, 3 down" to make the movement smoother.

{{< commit move-down-on-arrow >}}

And moving Q\*bert up is very similar:

{{< commit move-up-on-arrow >}}

If you try this now, it mostly works.  Q\*bert can move up and down
(northeast and southwest on the screen), but there are two problems:

- Q\*bert can go off the top or the bottom of the pyramid.
- If you press the up-arrow key twice quickly, Q\*bert moves at twice
  the speed.

Because these problems affect moving up and moving down, it will make
sense to fix them just in once place in the code.  Our first step is
to *refactor* the code so the jumping logic only appears once.  That's
what we'll do next.

## Refactor the jumping code

If you compare the `jump_down()` and `jump_up()` methods, you'll
notice they are very similar.  The differences are:

- the costume is different
- the amount we change *x* by is different
- the amount we change *y* by is different

We'll create a `jump()` method which can work with different values
for these three things.  This is very much like a custom block in
Scratch.

{{< commit define-jump-method >}}

And now we can simplify the original `jump_up()` method, by calling
our new method with the right values for the *x*-speed, *y*-speed, and
costume name:

{{< commit simplify-jump-up-method >}}

We can simplify the `jump_down()` method in the same way:

{{< commit simplify-jump-down-method >}}

## Fix the 'double speed jump' problem

Now there's only one place we'll need to look at to fix the first of
our problems, which was that quickly pressing an arrow key twice makes
Q\*bert move at double speed.  We only need to look at the `jump()`
method.

The problem is that the player might press an arrow key while we're in
the middle of doing the jump.  We'll fix this by recording whether
we're in the middle of a jump, and ignoring arrow key presses if we
are.

The first step is to create an *instance variable*, which is very much
like a 'for this sprite only' variable in Scratch.  When we're setting
Q\*bert up (in response to the `"set-up-qbert"` message), we'll set
this variable to say we are *not* currently jumping:

{{< commit initialise-jumping-slot >}}

Then the first thing we'll do when jumping is to record that we are
jumping, and then record that we're *not* jumping once we've finished
that jump:

{{< commit note-when-jumping >}}

Now we can just leave the `jump()` method early, without doing
anything, if we're already mid-jump:

{{< commit do-not-jump-if-already-jumping >}}

(There's still the problem of being able to go off the top or bottom
of the pyramid.  We'll get to that later.)

## Finish the movement controls: left and right

With this done, it's now quite easy to let the player move in the
other two directions.

We handle the `ArrowLeft` keypress to let the player move Q\*bert
left, which is northwest on the screen:

{{< commit move-left-on-arrow >}}

and the `ArrowRight` keypress to let the player move Q\*bert right,
which is southeast on the screen:

{{< commit move-right-on-arrow >}}

## Add a little bounce to the jump

To make the game look better, we'll add a bounce to Q\*bert's
movement.  We want a bit of extra upwards speed in the *y* direction
at the start of a jump, and a bit of extra downwards speed at the end
of a jump.  Each jump is 14 frames long, so we'll define a *list* of
the extra *y* speeds:

{{< commit define-bounce-list-of-y-speeds >}}

Those extra bits of speed all add up to zero, so Q\*bert will still
end up in the right place at the end of their jump.

Again, we'll now see that it was worth our time to not have the
jumping code copied out four times, because we only need to change the
`jump()` method.  We include the right bounce amount when changing
*y*, depending on what frame we're on:

{{< commit bounce-when-moving >}}

With this, the movement looks a lot better.

## Work out where on the pyramid we are

We'll now work on the second problem we noticed, which was that
Q\*bert can jump right off the top, bottom, or sides of the pyramid.
We'll make a method which works out which row we're on, and which
block within that row.  There's more maths here, to 'undo' the
calculation we did to find where to place each Block clone.

**TODO: Do we need to explain that?**

{{< commit method-to-compute-pyramid-coords >}}

This method *returns a value*, like blocks such as *(mouse&nbsp;x)* in
Scratch.  The value here is a pair of numbers.  The first one is the
row, and the second the block within that row.

Nothing is using this method yet, though, so it's hard to tell if it's
working correctly.  We'll make it so pressing `"w"` (for 'where') will
print out where on the pyramid this code thinks we are:

{{< commit add-diagnostics-for-coordinates >}}

Try this:

- Switch to the *Output* tab.
- Build and green-flag the project.
- Move Q\*bert around, and press the `"w"` key to check the code is
  working out Q\*bert's position correctly.

Remember, row zero is the bottom row, and block zero is the far-left
block on each row.

You can come back to the tutorial by clicking on the *Tutorial* tab
header.  Once you're happy that the calculations are correct, you can
remove the temporary code:

{{< commit remove-pyramid-coords-diagnostics >}}

## Make Q\*bert fall off the pyramid

Now we know what row and block Q\*bert is on, it's easy to tell
whether they are actually on the pyramid or not.  If the row number is
smaller than zero then Q\*bert has fallen off the bottom.  If the row
number is seven or more, then Q\*bert has fallen off the top.  If
the block number is less than zero, then Q\*bert has fallen off to the
left.  The only slightly tricky one is telling whether Q\*bert has
fallen off to the right — this happens if the block number is equal to
or greater than the number of blocks in the row, which, as we worked
out above, is (7&nbsp;−&nbsp;*r*).  We'll broadcast a message if
Q\*bert falls off the pyramid at the end of their jump:

{{< commit check-for-falling-off >}}

If Q\*bert falls off, we'll make it so they disappear into the
distance, by shrinking and then hiding altogether.  Here we're using a
version of the Python `range()` function where we give the starting
value as a percentage (here, 100), the stopping value as a percentage
(here, 10), and the 'step', which here has to be negative to work down
from 100 to 10 in steps of 5.  (In fact, Python stops just *before*
the 'stop' value, but this will look fine for our use.)  In the loop,
we'll turn the percentage into a value by dividing by 100.

{{< commit define-disappear-method >}}

If you try this now, you'll see that you can still jump around in a
strange way while falling off.  We'll fix this by keeping track of
whether Q\*bert is in the middle of falling off the pyramid, with
another 'instance variable' which we'll initialise in the green-flag
method:

{{< commit initialise-fallen-off >}}

Then we set the variable to `True` if we work out that Q\*bert has
fallen off the pyramid:

{{< commit record-when-falling-off >}}

And finally, we abandon the `jump()` method early if we've fallen off,
by extending the *am I already jumping?* test to *am I already
jumping, or falling off?*, like this:

{{< commit forbid-movement-when-falling-off >}}

If you play the game, fall off, then click green-flag to try again,
you'll see that Q\*bert is the wrong size.  We need to set their size
correctly in the green-flag method `go_to_starting_position()`:

{{< commit set-Qbert-full-size-when-starting >}}

## Lighting up the blocks Q\*bert lands on

Since the block is the actor which is going to need to do something
when it's landed on, we'll do this work in the *Block* class.  We're
going to define a method which checks whether the clone's position is
equal to Q\*bert's.  If it is, that block has been landed on and
should switch to the lit-up costume.

But first, we need to make each *Block* clone know its own position.
We'll set new instance variables in the original *Block* just before
making the clone:

{{< commit record-row-block-for-clone >}}

Now each *Block* clone has this information, we can define a method
which tests whether that *Block* is the one Q\*bert is on.  We'll find
the original (in fact, only) Q\*bert instance, and ask it for its
coordinates in pyramid row/block terms, then check whether the Block's
row-number and block-number match.  If so, light up!

{{< commit define-Block-check-landed-on-method >}}

All we need to do now is launch this method by making Q\*bert
broadcast the message:

{{< commit check-block-if-not-fallen-off >}}

We use `broadcast_and_wait()` to make sure the block checking has
happened before allowing Q\*bert to move again.

If you try this now, it seems to work OK, but if you fall off then try
again with green-flag, all the blocks are lit up already!  We need to
make sure each blocks starts off in its un-lit-up costume:

{{< commit start-Block-with-unjumped-costume >}}

## Checking Q\*bert's progress

This is now working quite well, but we need a way to tell whether
Q\*bert has cleared the level.  We'll track the number of un-lit-up
blocks Q\*bert still has left to jump on.  We'll store this number in
a *global variable*, which is one that all sprites have access to.  We
define it at the start of the code, outside any `class`:

{{< commit initialise-blocks-left-counter >}}

This might look strange, since at the start of the game there are
definitely *not* zero un-lit-up blocks.  What we'll do is make Q\*bert
count the blocks as soon as the pyramid has been made:

{{< commit count-initial-number-blocks-left >}}

There are a couple of things to notice here:

- We need to tell Python that it's the global variable `blocks_left`
  we want to set the value of, not make a new local variable.
- We use the `all_clones()` method on the `Block` *class*, which is a
  Pytch built-in giving us a list of all the live clones of that
  class.  We're only interested in how many clones there are, so we
  find the length of that list with the Python built-in `len()`.

We're now going to make each block clone keep track of whether it's
lit up.  We'll set the value of a new instance variable `is_lit_up`
when the clone starts up:

{{< commit record-whether-block-lit-up >}}

Now, when a block works out that it's the one Q\*bert has landed on,
we'll first check whether we're already lit up, and only if *not*, do
we switch costume to the lit-up one.  We also then record the fact
that this clone has lit up.

{{< commit only-light-up-if-not-already >}}

When lighting up a block, we can decrease by one the number of blocks
left to light up.  Again, we have to tell Python that it's the global
`blocks_left` variable we want to work with:

{{< commit decrement-blocks-left-when-newly-lit-up >}}

To check this is working, we'll make Q\*bert say the number of blocks
which are left to light up:

{{< commit temporarily-say-blocks-left-count >}}

If you run this now, it mostly works, except that when you land on the
very top block, the count drops by *two* instead of one.  What's
happening is that the *original* instance of *Block* is updating the
count, as well as the clone which was created there.  We'll fix this
by making the original *Block* think it's in a nonsense position.
This isn't a very elegant way of solving this problem, but it will
work:

{{< commit set-original-Block-coords-to-invalid-values >}}

Once you're happy this is working, you can remove the diagnostic
speech bubble:

{{< commit remove-blocks-left-diagnostic >}}

## Winning the game!

When Q\*bert has lit up all the blocks, we want to congratulate the
player.  We'll do this with a sprite with a message as its costume:

{{< commit add-LevelClearedText-with-costume >}}

This Sprite should start off not shown:

{{< commit start-LevelClearedText-not-shown >}}

And we'll define a simple method which puts the sprite in a useful
place and shows it when a message is broadcast:

{{< commit define-show-LevelClearedText-method >}}

The only time the level might have been cleared is just after a new
block has been lit up, so at that point we'll check whether there are
zero blocks left, and send the `"level-cleared"` message if so:

{{< commit check-for-level-cleared-then-announce >}}


## Making some noise

The game is now playable, but to make it more interesting we'll
include some sounds.  We'll start with a victory sound, which will be
a trumpet fanfare.  The 'level cleared' announcement sprite is a
reasonable one for this sound to belong to:

{{< commit define-LevelClearedText-fanfare-sound >}}

And we want to play this sound at the same time as showing the
message:

{{< commit play-fanfare-when-level-cleared >}}

The other sounds will belong to the *Block* sprite, and will play when
a block is landed on by Q\*bert.  We'll make different noises
depending on whether the block was already lit up, so we declare two
sounds for the *Block* sprite:

{{< commit define-pop-ping-sounds >}}

If a block is lighting up, then we'll play the bell:

{{< commit play-ping-for-newly-lit-up >}}

and if a block is already lit up, we'll play the pop.  We do this by
adding an `else` clause to the `if` test for whether the block is
newly lit:

{{< commit play-pop-for-already-lit-up >}}

## Challenges

This is now a playable game, although quite easy once you get the hang
of it!  There's lots more you could do with it:

- The player can keep making Q\*bert jump around the pyramid after
  clearing the level, which looks odd.  What's the best way to handle
  this?
- When Q\*bert falls off the pyramid, they just get smaller.  It would
  look better if they looked like they carried on falling, at an
  increasing speed.
- Add challenges like were in the original, such as bouncy balls which
  you have to avoid.
- Make there be more than one level.  Different levels could have
  different colour schemes.
- Add the safety discs of the original, which transport Q\*bert back
  to the top of the pyramid.

