# Catch the apple!

This tutorial will show you how to make a simple game in Pytch.  The
player will move a basket to try to catch apples which fall down the
stage.

**TODO: Animation of gameplay here?**

We'll develop the game in stages, showing how knowledge of Scratch
helps with understanding how things work in Python.


---

## Add a _Sprite_ for the player's bowl

We'll start with the Bowl which the player controls.  Just like in
Scratch, we make a _Sprite_.  In Pytch, we create a Sprite by adding
code to our program.

You need to make the following change to your program.  Clicking on
the blue "`i`" will show some help about understanding the changes
you need to make.

{{< commit add-empty-Bowl >}}

You will get an error if you try to run this now — then click back to
this _Tutorial_ tab.  The problem is that we haven't said anything at
all about the _Bowl_.  We'll do that now, by saying what the bowl
should look like.

### Add a costume for the Sprite

Pytch sprites have _costumes_ just like Scratch sprites do.  This
tutorial comes with the images you need — you can see them in the
_Images and sounds_ tab, then come back here by choosing the
_Tutorial_ tab.  To add a costume to our Pytch sprite, we just need to
write code saying which image to use.  A Sprite has a special variable
called `Costumes` which tells Pytch about that Sprite's costumes.

Because a Sprite can have more than one costume, we give Pytch a
_list_ of the costumes we want to use, even if there's only one
costume in that list.  Python writes lists with square brackets, like
this:

```
["red", "blue", "green"]
```

The costume we want to use is called `"bowl.png"`, so we make a list
with just that in it:

{{< commit add-Bowl-costume >}}

Now, if you click the green flag, you should see the player's bowl
appear in the middle of the stage.  Test that now!


## Start the bowl in the right place

The player needs to be able to move the bowl.  We'll let them do this
with the keyboard, using the `a` and `d` keys.  In Scratch, we would
do this by adding a script to our Sprite, clicking the blocks
together.  In Pytch, we write code to do the same job.

The Pytch equivalent of adding a script is _defining a method_ in our
Sprite.  Our method will start off by moving the bowl to the correct
place on the stage.  A Python method needs a name, which should
briefly describe what it does.  We'll use `move_with_keys` for our
method's name.

Pytch uses the same way of describing positions on the stage as
Scratch does, so we'll start off by making our method just move the
bowl to a sensible place at the bottom of the stage.

{{< commit define-skeleton-move-with-keys >}}

In Scratch, you give a block the information it needs by filling in
the ‘holes’ in the block:

![Scratch: go-to-xy](go-to-xy.png)

In Python, you provide these extra pieces of information (called
“arguments”) in brackets “`()`” after the function name:

```
self.go_to_xy(0, -145)
```

The ``self`` means we want to act on the Sprite.  The `x`-coordinate
of `0` puts the bowl in the middle, left-to-right.  I picked `-145`
for the `y`-coordinate by trial and error.

If you click the green flag now, our new code does not run.  This is because
what we've done so far is like making a script in Scratch with _no hat
block_ on top.  In Scratch we would attach a _when green flag clicked_
hat block on top of our script.  In Pytch, we do something very
similar, by attaching a special marker to the top of the method:

{{< commit trigger-move-with-keys-on-green-flag >}}

Now if you click the green flag, the bowl should
move to its starting position at the bottom of the stage.

## Let the player move the bowl

Now we're going to let the player move the bowl.  We'll start by
letting them move it to the right.  We'll keep checking whether the
player is pressing the `d` key, and if so, change the bowl's
`x`-coordinate.  In Scratch we would do this with a _forever_ block.
Python has the `while True` statement to do the same job.

In Scratch, the blocks we want to run forever are _inside_ the
_forever_ block.  In Python, the code we want to run forever is
_indented_ to the right.

Python's _if_ statements work in the same way.  The code you want to
run only if the condition is true is indented to the right.

Putting this all together, we get this new code:

{{< commit move-bowl-right >}}

If you try this, it should let you move the bowl right by holding down
the `d` key.  But!  You can move the bowl all the way off the stage.
We'll fix that next.

### Keep the bowl on the stage

If the player is pressing `d`, we then need to check whether it's OK
to move the bowl right.  We do this be checking the bowl's
`x`-coordinate.  When the bowl is as far to the right as possible, the
`x`-coordinate is `190` — I found this value by trial and error in the
code below.  It's OK to move right as long as the `x`-coordinate is
less than or equal to 190.  We add a test for this, and only do the
`self.change_x(2)` if the test passes.

Maybe you can guess what the red line, marked with “⊖”, means — if
not, you can click on the blue “``i``” to get an explanation.

{{< commit clamp-bowl-at-right >}}

Test this now — click the green flag, then check you
can still move right, but only as far as the edge of the stage.

### Let the player move left too

The same idea will let the player move _left_ as well.  We'll add code
to the same `while True` loop.  The differences for moving left
instead of right are:

* We check for the `"a"` key not the `"d"` key.
* We check that the bowl is not too far left already, by checking that
  its `x`-coordinate is at least `-145`.  (I've left a bit of room at
  the very left for a score-keeper to stand — we'll come to the
  score-keeper later in the tutorial.)
* We move by using a negative value for the amount the bowl should
  change its `x`-coordinate by.

{{< commit move-clamp-bowl-left >}}


## Add a Sprite for the apple

We now need something for the player to catch.  We'll create another
Sprite for this, and we'll start by adding a line of code to define
our new _Apple_ Sprite:

{{< commit add-empty-Apple-class >}}

Before we can run this code, we need to put some code into the Apple
Sprite — we'll say what costume we want the Apple to have.  We're
taking the same steps here as what we did when we made the player's
bowl sprite.

{{< commit give-Apple-costume >}}

If you run the project now, an apple should appear in the middle of
the Stage.


## Make the apple fall down the stage

To give the Apple its behaviour, we define a method — remember this is
like making a script in Scratch.  Because this is very similar to what
we did with the Bowl, we'll add this code all in one go.  We will:

* Say that we want this code to run when the green flag is clicked —
  this is like the 'hat block' in Scratch.
* Give the method a short name to say what it does — we're using
  `move_down_stage`.  The code doesn't yet move the apple down the
  stage but it will!
* Start the code off with a line which moves the Apple to a good
  starting point on the stage — I chose just off the top of the
  stage, and off-centre to the right a bit.

{{< commit define-skeleton-apple-move-down-screen >}}

If you try this now (click green flag), you should just be able
to see the bottom of the apple at the top of the stage.

### Actually move down the stage

What we want the apple to do is keep moving down, as long as it is
above the bottom of the stage.  In Scratch we could use a `repeat
until` block.  Python has a `while` statement instead.  This is very
like Scratch's `repeat until` block, but uses the test 'the other way
round' —

* Scratch's `repeat until` block keeps running the contained blocks,
  and _stops when the test is true_.
* Python's `while` statement checks the test, and _runs the contained
  code while the test is true_.

We want to test whether the apple's `y`-coordinate is higher than some
value near the bottom of the stage.  By trial and error, I found that
`-140` worked well for this.  We'll add this `while` loop to our
method:

{{< commit make-apple-fall-down-screen >}}

We're changing the `y`-coordinate by the negative number `-3` to make
the apple move _down_ the stage a small amount each time round the
`while` loop.

If you run this code, the apple should fall down the stage, and stop
at the bottom.

## Catch the apple in the bowl

Finally, we want to let the player catch the apple.  Each time the
apple moves, it can check whether it's been caught.  This happens if
the apple is touching the player's bowl.  If it is, then we want to
_return_ from the method, which means that Python immediately stops
running that method.  This is like Scratch's `stop this script` block,
so what we're doing is the Pytch equivalent of the Scratch script

![Scratch: if-touching-Bowl stop-this-script](if-touching-Bowl-stop-this-script.png)

In Pytch, the code we need is:

{{< commit stop-falling-if-caught-in-bowl >}}

The apple now stops, but it stays on the stage, which looks very odd.
We want to make the Apple _hide_ when it's caught:

{{< commit hide-Apple-when-caught >}}

If we had put the `self.hide()` _after_ the `return`, our code would
not have worked.  Scratch stops you connecting blocks underneath the
`stop this script` block, but in Python you're responsible for not having
code which will never be run.


## Add the score-keeper

The next piece we want to work on is a score-keeper.  By now we know
how this works.  We define a new Sprite:

{{< commit define-skeleton-ScoreKeeper-sprite >}}

Give it a costume:

{{< commit give-ScoreKeeper-costume >}}

And make it move to a sensible place when the green flag is clicked.
I found these coordinates by trial and error, to put the score-keeper
in the bottom left corner of the stage.

{{< commit move-ScoreKeeper-to-right-place >}}


## Start off with zero points

When the player starts the game, they have no points.  We define a new
_variable_ within the score-keeper.  This is just like when you make a
new _For this sprite only_ variable in Scratch.  In Python, you can
just set a variable to a value, and this creates the variable.  We set
the starting value of a new `score` variable to zero:

{{< commit add-ScoreKeeper-score-attribute >}}

The “`self.`” is what makes this variable like Scratch’s _For this
sprite only_.

The job of the score-keeper is to announce the score, so we add a line
to say the value of the `score` variable:

{{< commit announce-starting-score >}}

If you run this now, the score-keeper should say "`0`".


## Give a point for catching an apple

The player can catch the apple in the bowl, but the score stays as
zero.  We will fix this next.

We'll define another method in the `ScoreKeeper` sprite.  That
method's job is to give the player a point and announce the new score.
A good short name for this job is `award_point`, so we define a method
with this name.  The first piece of code in our new method will
increase the `score` variable by `1`:

{{< commit define-skeleton-award-point >}}

The `+=` is like Scratch’s `change (score) by (1)`.

And then we need to change what the score-keeper is saying to be the
new value of the `score` variable:

{{< commit announce-updated-score >}}

Our code is correct, but we haven't said when to run it.  We want to
run this method whenever the apple lands in the bowl.  In our code,
it's the Apple's job to check whether it's landed in the bowl.  So,
just like in Scratch, we're going to make the Apple _broadcast a
message_ when it knows that it's landed in the bowl.  We'll tell Pytch
to run our score-keeper's `award_point` method when it *receives* that
message.

Just like in Scratch, we have to choose a good message.  In Pytch, a
message can be any string — we'll use `"award-point"`.

This is just like in Scratch, where we would use a `broadcast` block
and a `when I receive` hat-block:

![Scratch: broadcast and receive](broadcast-and-receive.png)

And just like in Scratch, we have to choose a
good message.  In Pytch, a message can be any string — we'll use
`"award-point"`.

First we tell Pytch to run `award_point` whenever the score-keeper
receives the message `"award-point"`:

{{< commit trigger-award-point-on-message >}}

And then we make the apple broadcast this message when it's caught.

This change needs to be made inside your `Apple` sprite:

{{< commit broadcast-when-apple-caught >}}

If you try this now, you should be able to get your score from zero to
one by catching the apple.

## Drop the apple from a random place

So far the game drops the apple in the same place every time you play.
This makes the game far too easy.  We want to make the apple drop in a
random place each time.

To do this, we will use some code which other people have already
written.  The name for a collection of Python code ready for use in
other programs is _module_.  A module for making random choices comes
with Python — this module is called `random`.  We say we want to use
the `random` module in our program by _importing_ it:

{{< commit import-random >}}

(This is how we’ve been using the `pytch` functions like
`pytch.broadcast()` already.)

Now we can use the function in the `random` module which picks a
random whole number.  This is called `randint` (for _random integer_).
We need to say what the smallest and largest whole number allowed are.
By trial and error, I worked out:

* The smallest (leftmost) `x`-coordinate which makes sure the apple
  doesn't hit the score-keeper is `-145`.
* The largest (rightmost) `x`-coordinate which makes sure the apple
  isn't off the right edge of the stage is `190`.

So these are the values we give to the `random.randint` function, and
we set a new variable `drop_x` to the result.  In Scratch, this whole
thing would look like

![Scratch: set-drop-x-to-random](set-drop-x-to-random.png)

and in Python it looks like this:

{{< commit choose-random-drop-x >}}

Now we need to use the value of our `drop_x` variable instead of the
fixed `100` for the `x`-coordinate of where the apple falls from:

We’re changing a line of code here — the “i” button will help explain
the ⊖ and ⊕ lines.

{{< commit drop-from-random-abscissa >}}

One thing you might notice is that we didn't say `self.drop_x` here,
we just said `drop_x`.  By not saying `self`, Python makes the
`drop_x` variable only exist inside the `move_down_stage` method.
Since we won't need `drop_x` anywhere else, this way avoids cluttering
up our code with variables.

Now the game is better — each time click the green flag, the
apple falls from a different place.

## Make apples keep falling

We're going to change the game so that the score-keeper is in charge
of making the apple fall from the sky.  We're going to take away the
'hat block' `@pytch.when_green_flag_clicked` on the Apple's
`move_down_stage` method, and replace it with a hat block listening
for the broadcast of the message `"launch-apple"`:

{{< commit launch-apple-on-message-not-green-flag >}}

Right now, the game won't work, because nothing is broadcasting the
`"launch-apple"` message.  We'll give that job to the score-keeper
now.

We'll make a new method in the ScoreKeeper sprite which will keep
launching apples.  A good name for this is `launch_apples`, so we
start defining that method:

{{< commit define-launch-apples-method >}}

We want to keep making apples drop from the top of the stage forever.
Just like in the code which lets the player move the bowl, we do this
with a `while True:` loop in Python.  Inside that loop, we want to
keep broadcasting `"launch-apple"`.  But here, we will use the
`broadcast_and_wait` function, because we don't want to drop the next
Apple until the current one has either been caught or reached the
bottom of the stage.  In Scratch, the code would be

![Scratch: forever-launch-apple](forever-launch-apple.png)

and in Pytch it's

{{< commit bcast/wait-launch-apples-in-loop >}}

Finally, we need to say that we want this to start happening when the
green flag is clicked:

{{< commit start-launching-apples-on-green-flag >}}

If you try the game now, it doesn't work!  What's happening is that
we've told the Apple to `hide` itself when it's caught, but we haven't
told it to `show` itself when it starts dropping.  We can fix that:

{{< commit show-apple-when-fall-starts >}}

and this is now a playable game written in Python — congratulations!

## Improve the game

Here are some ideas on how you could make this game more fun:

* The `x`-coordinate where the apple starts is already random.  Make
  the starting `y`-coordinate be random too.  If an apple starts lower
  down the stage, the player has less time to get the bowl under the
  apple, making the game more challenging.

* Play a sound when the player catches an apple.  There is an
  apple-crunching sound as part of this tutorial.  Make this sound
  part of the `Apple` sprite, by setting a `Sounds` variable just
  under the `Costumes` variable: `Sounds = ["apple-crunch.wav"]`.  Use
  the slide-out help panel to find the Pytch function for playing the
  sound.

* Make the referee jump up and down in celebration when the player
  catches an apple.  In Scratch you might use the `repeat` block.  Use
  the slide-out help panel to find how to do this in Pytch.

* Add the provided `orange.png` costume to the Apple.  Its `Costumes`
  list will then have two things in it.  (Your code will be clearer if
  you also change the name of the sprite to `Fruit`!)  Each time the
  `Fruit` appears, choose randomly which costume to wear.  (Hint: a
  good place for this code is in the first part of the
  `move_down_stage()` method, before the `while` loop.)  The slide-out
  help panel will tell you the Pytch version of Scratch’s `switch
  costume` block.

* Make there be a fixed number of apples — maybe 8.  Advanced: At the
  end of the game, make the referee say something like "You got 5 out
  of 8".  You can use "f-strings" ([read about them in the Python
  documentation](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings))
  to get the scorekeeper to say this.

* Change the speed of the bowl.  A bit quicker would make the game
  easier; a bit slower would make the game harder.  The speed appears
  in two places: for moving left and for moving right.  Investigate
  whether it’s worth setting a variable to hold the speed.  A variable
  makes it easier to experiment with the player's speed, but it is a
  bit more work to write the code in the first place.

* Add a pause between one apple being caught / missed and the next one
  appearing.  Use the help sidebar to find the Pytch version of
  Scratch’s `wait () seconds` block.


## TODOs for tutorial author

Some scattered throughout, but also:

* Do we need something less "babyish" for the graphics?  But avoid
  being "stereotypically boyish", which, e.g., spaceships catching
  asteroids might be seen as.

* Where to talk about SELF. in front of built-ins?

* Do we need more explanation over `forever` vs `while True:`, or can
  WHILE TRUE be a magic spell for now?

* Say how params in ()s are like putting values/variables into
  the 'holes' in Scratch blocks.

* Change transitive verb "launch" to "drop" throughout.

* Any more "now you try this" ideas?  Add hints?  Put them in sensible
  order?  Add something say how hard each challenge is?

* The collision detection is generous to the player because it's based
  on bounding boxes.  Do we need to explain that?  (Don't think so.)

* Any terms-of-art we need to introduce?  "Function"?
