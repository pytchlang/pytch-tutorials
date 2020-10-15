# Q*bert: Recreate the cube-hopping action

As Mark Vanstone explains in issue 42 of Wireframe:

> Late in 1982, a funny little orange character with a big nose landed
> in arcades.  The titular Q*bert’s task was to jump around a network of
> cubes arranged in a pyramid formation, changing the colours of each as
> they went.  Once the cubes were all the same colour, it was on to the
> next level.

In this tutorial we'll follow Mark's example and create the basics of
this classic arcade game.

## Credits

Many thanks to the Raspberry Pi Press for making the contents of their
*Wireframe* magazine available under a Creative Commons licence.  We
have used their code for inspiration, and also the images.

TODO: asset-credits shortcode

{{< run-finished-project >}}


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

TODO: Finish this explanation, possibly with the aid of a picture.

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
We want Q\*bert to move 28 pixels to the left and 42 pixels up, which
we'll do in 14 steps of "2 left, 3 up" to make the movement smoother.

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

## Refactor

If you compare the `jump_down()` and `jump_up()` methods, you'll
notice they are very similar.  The differences are:

- the costume is different
- the amount we change *x* by is different
- the amount we change *y* by is different


{{< commit define-jump-method >}}

{{< work-in-progress >}}

Note that if you go down then back up, it says "25 left" which is
wrong.  Double-count the original block.
