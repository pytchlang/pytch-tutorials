# Catch the apple!

This tutorial will show you how to make a simple game in Pytch.  The
player will move a bowl to try to catch apples which fall down the
stage.

![Screenshot](screenshot-w240-darker-bg.png#img-center)

We’ll develop the game in stages, showing how knowledge of Scratch
helps with understanding how things work in Python.

---

## Add a _Sprite_ for the player's bowl

We’ll start with the bowl which the player controls.  Just like in
Scratch, we add a _Sprite_.

{{< learner-task >}}

Add a Sprite called `Bowl` to your project.

{{< learner-task-help >}}

{{< jr-commit add-empty-Bowl add-sprite >}}

{{< /learner-task >}}

If you run this now, you won’t see anything.  This is because we
haven’t given our Sprite any _costumes_.

### Add a costume for the Sprite

Pytch sprites have _costumes_ just like Scratch sprites do.

The costume we want to use is called `"bowl.png"`, and it is in the
Pytch media library.

{{< learner-task >}}

Add the costume `"bowl.png"` to your `Bowl` sprite from the media
library.

{{< learner-task-help >}}

{{< jr-commit add-Bowl-costume add-medialib-appearance bowl >}}

{{< /learner-task >}}

Now, if you click the green flag, you should see the player’s bowl
appear in the middle of the stage.  Test that now!


## Start the bowl in the right place

The player needs to be able to move the bowl.  We’ll let them do this
with the keyboard, using the `a` and `d` keys.  We do this, like in
Scratch, by adding a script to our Sprite.  The difference is that in
Pytch, we’ll type Python code into the script, instead of clicking
blocks together like we would do in Scratch.

We’ll start off by making a script which moves the bowl to a sensible
place at the bottom of the stage when the game starts.

{{< learner-task >}}

Add a new script to the `Bowl` sprite which will run when the player
clicks the green flag.

{{< learner-task-help >}}

{{< jr-commit add-empty-move-with-keys-handler add-script >}}

{{< /learner-task >}}

The code editing pane should now show the new (empty) script.

Now you need to add the code which moves the bowl to the right place
on the stage.  Pytch uses the same way of describing positions on the
stage as Scratch.  You can use the _Show coordinates_ tool to find
suitable coordinate values.  A `x`-coordinate of `0` puts the bowl in
the centre, left-to-right.  I picked `-145` for the `y`-coordinate, to
put the bowl almost at the bottom.

In Scratch, we would use a block like this:

``` scratch
go to x: [0] y: [-145]
```

In Python, you write code to do the same job.  You provide the extra
pieces of information (called “arguments”) in brackets “`()`” after
the method name.  This is the code we need:

``` python
self.go_to_xy(0, -145)
```

The “`self.`” part at the start means we want the Sprite itself to do
something.

{{< learner-task >}}

Add this code to the script you have just made.

{{< learner-task-help >}}

{{< jr-commit add-move-with-keys-initial-body edit-script >}}

{{< /learner-task >}}

Now, when you click the green flag, the bowl should move to its
starting position at the bottom of the stage.  Try it!


## Let the player move the bowl

Now we’re going to let the player move the bowl.  We’ll start by
letting them move it to the right.  We’ll keep checking whether the
player is pressing the `d` key, and if so, change the bowl’s
`x`-coordinate.  In Scratch we could do this with a _forever_ block:

``` scratch
forever:
  if <key [d v] pressed> then:
    change x by (2)
```

Python has the `while True:` statement to do the same job.  In
Scratch, the blocks we want to run forever are _inside_ the _forever_
block.  In Python, the code we want to run forever is _indented_ to
the right _under_ the `while True:`.

Python’s _if_ statement works in the same way.  The code you want to
run only if the condition is true is indented to the right.

{{< learner-task >}}

Add code which keeps checking whether the player is pressing the `d`
key, and, if so, changes the bowl’s `x`-coordinate by 2.

{{< learner-task-help >}}

Use the Scratch/Python help (click the circled `?` icon at top-left)
to learn how you can write '*key `d` pressed*' and '*change x by 2*'
in Python.  Then come back to this tutorial by clicking on the book
icon.

{{< learner-task-help >}}

{{< jr-commit move-bowl-right edit-script >}}

{{< /learner-task >}}

If you try this, it should let you move the bowl right by holding down
the `d` key.  But!  You can move the bowl all the way off the stage.
We’ll fix that next.

### Keep the bowl on the stage

If the player is pressing `d`, we then need to check whether it’s OK
to move the bowl rightwards.  We do this be checking the bowl’s
`x`-coordinate.  When the bowl is as far to the right as possible, the
`x`-coordinate is `190` — I found this value by trial and error in the
code below.  It’s OK to move right as long as the `x`-coordinate is
less than or equal to 190.  We can add another `if` statement to test
for this, and only do the `self.change_x(2)` if the test passes.

{{< learner-task >}}

Change your script so that it also checks whether the bowl’s
`x`-coordinate is less than 190, and only moves rightwards if it is.

{{< learner-task-help >}}

In scratch, we would move the block

``` scratch
change x by (2)
```

to be inside an 'if' block, like this:

``` scratch
if <(x position) < [190]> then:
  change x by (2)
```

In Python, we use another `if` statement and *indent* the code which
changes `x`.

{{< learner-task-help >}}

{{< jr-commit clamp-bowl-at-right edit-script >}}

{{< /learner-task >}}

Test this now — click the green flag, then check you can still move
rightwards, but only as far as the edge of the stage.

### Let the player move left too

The same idea will let the player move _left_ as well.  A natural
place for this new code is in the same `while True:` loop which
already lets the player move right.

{{< learner-task >}}

Add code to let the player move left.

Add code to the `while` loop inside the green-flag script, so the
player can move left using the `"a"` key.  Make sure that they can’t
move the bowl too far to the left.  They should still be able to move
right.

{{< learner-task-help >}}

Look at the existing code for moving _right_, which will be a useful
guide, because the task is very similar.  Think carefully about what
needs to change, about each part of the code, for moving _left_.

{{< learner-task-help >}}

The differences for moving left instead of right are:

* Check for the `"a"` key not the `"d"` key.
* Check that the bowl is not too far _left_ already, by checking that
  its `x`-coordinate is more than `-145`.  (This leaves a bit of room
  at the very left for a score-keeper to stand — we'll come to the
  score-keeper later in the tutorial.)
* Move by using a _negative_ value for the amount the bowl should
  change its `x`-coordinate by.

You can copy and paste the existing lines of code, and modify the copy
to make this list of changes.

{{< learner-task-help >}}

{{< jr-commit move-clamp-bowl-left edit-script >}}

{{< /learner-task >}}


## Add a Sprite for the apple

We now need something for the player to catch.  We’ll create another
Sprite for this.

{{< learner-task >}}

Make a new sprite called “Apple”.

{{< learner-task-help >}}

{{< jr-commit add-empty-Apple-class add-sprite >}}

{{< /learner-task >}}

Next is to give the apple a costume.

{{< learner-task >}}

Add the `"Apple.png"` costume from the media library to this new
sprite.

{{< learner-task-help >}}

{{< jr-commit give-Apple-costume add-medialib-appearance apple >}}

{{< /learner-task >}}

If you run the project now, an apple should appear in the middle of
the Stage.


## Make the apple fall down the stage

To give the apple its behaviour, we’ll add a script.  In more detail:

* We want this code to run when the green flag is clicked.
* Add a line of code to the script line which moves the apple to a
  good starting point on the stage — I chose just off the top of the
  stage, and off-centre to the right a bit, coordinates
  (100,&nbsp;200).

{{< learner-task >}}

Add a green-flag script with a line of code which does this.

{{< learner-task-help >}}

Add the script, and then think about what line of code you need.

{{< learner-task-help >}}

You need to work out what Python code will do the same job as this
Scratch block:

``` scratch
go to x: [100] y: [200]
```

Use the Scratch/Python help, or look back at how you got the bowl to
start at the right place.

{{< learner-task-help >}}

{{< jr-commit define-skeleton-apple-move-down-screen add-script >}}

{{< /learner-task >}}

If you try this now (click the green flag), you should just be able to
see the bottom of the apple at the top of the stage.

### Actually move down the stage

What we want the apple to do is keep moving down, as long as it is
above the bottom of the stage.  In Scratch we could use a `repeat
until` block.  Python has a `while` statement instead.  This is very
like Scratch’s `repeat until` block, but uses the test ‘the other way
round’ —

* Scratch’s `repeat until` block keeps running the contained blocks,
  and _stops when the test is true_.
* Python’s `while` statement checks the test, and _runs the contained
  code while the test is true_.

We want to test whether the apple’s `y`-coordinate is higher than some
value near the bottom of the stage.  By trial and error, I found that
`-140` worked well for this.  We want to add code which, in words, does

> while the `y`-coordinate is bigger than `-140`, move down by 3

{{< learner-task >}}

Add code to your script which does this.

{{< learner-task-help >}}

You need to add two lines of code to the end of your script.

{{< learner-task-help >}}

For ‘move down’, you can use `self.change_y()` with a negative value
for the argument.

{{< learner-task-help >}}

{{< jr-commit make-apple-fall-down-screen edit-script >}}

{{< /learner-task >}}

If you run this code, the apple should fall down the stage, and stop
at the bottom.

The `while` here might look different to when we used `while True:` to
mean “forever”, but it’s really just different ways of using the same
part of the Python language.  When we want something to happen
forever, the `True` in `while True:` acts as a test which always
passes, so the indented code keeps running again and again forever.


## Catch the apple in the bowl

Finally, we want to let the player catch the apple.  Each time the
apple moves, it can check whether it’s been caught.  This happens if
the apple is touching the bowl.  If it is, then we want to hide the
apple.  What we want to do is the Python equivalent of the Scratch
script

``` scratch
if < touching (Bowl v)?> then
hide
```

{{< learner-task >}}

Add code to your script which hides the apple if it touches the bowl.

{{< learner-task-help >}}

You can use the Scratch/Python help to find out what Pytch functions
work the same as the Scratch

``` scratch
touching (Bowl v)
```

and

``` scratch
hide
```

blocks.

{{< learner-task-help >}}

You will need an `if` statement at the end of the script, still
"inside" the `while` loop body.

{{< learner-task-help >}}

{{< jr-commit hide-Apple-when-caught edit-script >}}

{{< /learner-task >}}


## Add the score-keeper

The next piece we want to work on is a score-keeper, who will keep
track of how many apples the player has caught in their bowl.

By now, we know how the start of this job works:

{{< learner-task >}}

Add a Sprite called `ScoreKeeper`.

{{< learner-task-help >}}

{{< jr-commit define-skeleton-ScoreKeeper-sprite add-sprite >}}

{{< /learner-task >}}

{{< learner-task >}}

Give the score-keeper sprite a costume.  The `Dani` costume from the
media library works well, or you can choose a different one.

{{< learner-task-help >}}

{{< jr-commit give-ScoreKeeper-costume add-medialib-appearance Dani >}}

{{< /learner-task >}}

### Start the score-keeper in a sensible place

We want to move the score-keeper to a sensible place when the green
flag is clicked.  Using the _Show coordinates_ tool, the coordinates
(-215,&nbsp;115) seem about right, but you can adjust the values if
you prefer.

{{< learner-task >}}

Add a script which runs when the green flag is clicked, with code that
moves the score-keeper to a suitable place on the stage.

{{< learner-task-help >}}

Once you've added the script, you can refer to the other two Sprites
if you'd like to remind yourself what Python code to use to move a
Sprite to a particular place on the stage.

{{< learner-task-help >}}

{{< jr-commit move-ScoreKeeper-to-right-place add-script >}}

{{< /learner-task >}}


## Start off with zero points

When the player starts the game, they should have no points.  We want
to define a new _variable_ within the score-keeper.  This is just like
when you make a new _For this sprite only_ variable in Scratch.  In
Python, there is no separate step to create the variable.  You just
set your variable to a value, and this automatically creates the
variable.

For example, to create a variable, within a sprite, referring to a
string, we could use code like

``` python
self.my_name = "Arthur"
```

The “`self.`” is what makes this variable like Scratch’s _For this
sprite only_.

We want set the starting value of a new `score` variable in the
score-keeper to the number zero.

{{< learner-task >}}

Add code to the score-keeper's script which makes a new variable
`score` with value `0`.

{{< learner-task-help >}}

You can base your code on the example in the text above.  Your
variable should be called `score` (not `my_name`), and should be set
to the number `0` (not the string `"Arthur"`).

{{< learner-task-help >}}

{{< jr-commit add-ScoreKeeper-score-attribute edit-script >}}

{{< /learner-task >}}

The job of the score-keeper is to announce the score, so we want to
add a line to say the value of the `score` variable.  In Scratch we
would do this with a block

``` scratch
say (score)
```

You can use the Scratch/Python help content to find what Pytch
function does the same job as the “say” block.  Remember you’ll need
to say `self.score` to mean the score-keeper’s `score` variable.

{{< learner-task >}}

Add a line of code which makes the score-keeper say the starting
score.

{{< learner-task-help >}}

You'll need to add a line of code at the end of the script.

{{< learner-task-help >}}

{{< jr-commit announce-starting-score edit-script >}}

{{< /learner-task >}}

If you run this now, the score-keeper should say “`0`”.


## Give a point for catching an apple

The player can catch the apple in the bowl, but the score stays as
zero.  We will fix this next.

We’ll add another script to the score-keeper sprite.  The script’s
job will be to give the player a point, and announce the new score.

But first we need to think about when this code will run.  We want it
to run when the apple is caught by the bowl.  Like in Scratch, one
Sprite can _broadcast_ a message which other sprites can react to.
We’ll use a message `"award-point"` which the score-keeper will react
to.  Later, we’ll make the apple broadcast this message when the
player’s bowl catches it.

{{< learner-task >}}

Add a new empty script to the score-keeper which will run when it
receives the message `"award-point"`.

{{< learner-task-help >}}

{{< jr-commit add-empty-award-point-handler add-script >}}

{{< /learner-task >}}

Now we need to add code to this script which adds one to the
score-keeper’s `score` variable.  In Scratch you would say

``` scratch
change [score v] by (1)
```

Use the Scratch/Python help content to find the Python code which does
the same job.

{{< learner-task >}}

Add a line of code to the new script which increases the
score-keeper’s `score` variable by one.

{{< learner-task-help >}}

In the Scratch/Python help content, look in the “Working with
variables” section.

{{< learner-task-help >}}

{{< jr-commit increment-score edit-script >}}

{{< /learner-task >}}

We also need to make sure the score-keeper says the new score.

{{< learner-task >}}

Add a line of code which makes the score-keeper say the new value of
its `score` variable.

{{< learner-task-help >}}

The line will be the same as the line you added at the end of the last
chapter (to say the score after first setting it to zero).

{{< learner-task-help >}}

{{< jr-commit refresh-score-speech edit-script >}}

{{< /learner-task >}}

### Making the apple broadcast the message

This code is correct, but so far nobody is broadcasting the
`award-point` message, and so our code never runs.

As we said earlier, the apple needs to broadcast this message when
it’s caught by the bowl.

{{< learner-task >}}

Add some code to the right script **in your `Apple` sprite** which
broadcasts the `award-point` message when it’s caught.

{{< learner-task-help >}}

Make sure you choose the `Apple` sprite!

{{< learner-task-help >}}

Think carefully about what section of your code runs when the apple is
caught — remember that our code checks for this by asking whether the
apple is touching the bowl.

{{< learner-task-help >}}

{{< jr-commit broadcast-when-apple-caught edit-script >}}

{{< /learner-task >}}

If you try this now, you should be able to get your score from zero to
one by catching the apple.


## Drop the apple from a random place

So far the game drops the apple in the same place every time you play.
This makes the game far too easy.  We want to make the apple drop in a
random place each time.  We will use a _module_ which comes with
Python — a _module_ is some code, usually written by someone else,
which we can use in our program.

We will use a function in the `random` module which picks a random
whole number.  The function we want is called `randint` (for _random
integer_).  We need to say what the smallest and largest whole number
allowed are.  By trial and error, I worked out:

* The smallest (leftmost) `x`-coordinate which makes sure the apple
  doesn't hit the score-keeper is `-145`.
* The largest (rightmost) `x`-coordinate which makes sure the apple
  isn’t off the right edge of the stage is `190`.

So these are the arguments we want give to the `random.randint`
function, and we set a new variable `drop_x` to the result.  In
Scratch, this whole thing would look like

``` scratch
set [drop_x v] to (pick random [-145] to [190])
```

{{< learner-task >}}

Add a line at the start of the apple's script which creates a variable
`drop_x`, equal to the result of calling `random.randint()` with the
argument values just described.

{{< learner-task-help >}}

{{< jr-commit choose-random-drop-x edit-script >}}

{{< /learner-task >}}

Now we need to use the value of our `drop_x` variable instead of the
fixed `100` for the `x`-coordinate of where the apple falls from.

{{< learner-task >}}

_Change_ the code which calls the `go_to_xy()` function so that
instead of using `100` for the `x`-coordinate argument, it uses the
`drop_x` variable.

{{< learner-task-help >}}

{{< jr-commit drop-from-random-abscissa edit-script >}}

{{< /learner-task >}}

One thing you might notice is that we didn’t say `self.drop_x` here,
we just said `drop_x`.  By not saying `self`, Python makes the
`drop_x` variable only exist inside this script.  Since we won't need
`drop_x` anywhere else, this avoids cluttering up our project.

Now the game is better — each time we play the game, by clicking the
green flag, the apple falls from a different place.


## Make apples keep falling

We’re going to change the game so that the score-keeper is in charge
of making the apple fall from the sky.  It will do this by
broadcasting a message every time the apple should fall.

For the apple script, this means that the script should _not_ run when
the green flag is clicked.  Instead it should run when it receives a
message, let’s say `"drop-apple"`.

{{< learner-task >}}

Change the hat-block of the apple's script so that the script runs
when the apple receives the message `"drop-apple"` (instead of when
the green flag is clicked).

{{< learner-task-help >}}

Once you've found the right script, you can either double-click on the
hat-block, or choose _Change hat block_ from the hat-block's drop-down
menu.

{{< learner-task-help >}}

{{< jr-commit launch-apple-on-message-not-green-flag change-hat-block >}}

{{< /learner-task >}}

Right now, the game won’t work, because nothing is broadcasting the
`"drop-apple"` message.  We’ll give that job to the score-keeper now.

We’ll make a new script in the score-keeper sprite which will keep
sending the message telling the apples to drop.  This script should
run when the green flag is clicked.

{{< learner-task >}}

Add an empty script to the score-keeper which runs when the green flag
is clicked.

{{< learner-task-help >}}

{{< jr-commit add-empty-drop-apples-loop-script add-script >}}

{{< /learner-task >}}

We want our new script to keep making apples drop from the top of the
stage forever.  Just like in the code which lets the player move the
bowl, we do this with Python’s `while True:` loop.  Inside that loop,
we want to keep broadcasting the message `"drop-apple"`.  Here, we
will use the `broadcast_and_wait()` function, because we don't want to
drop the next apple until the current one has either been caught or
reached the bottom of the stage.  In Scratch, the code would be

``` scratch
forever
broadcast (drop-apple v) and wait
```

{{< learner-task >}}

Add the code to your new script which does the same job as these
Scratch blocks.

{{< learner-task-help >}}

You will need `while True:` followed by an _indented_ line of code.

{{< learner-task-help >}}

{{< jr-commit add-broadcast-drop-apple-loop edit-script >}}

{{< /learner-task >}}

If you try the game now, it doesn’t work!  What's happening is that
we’ve told the apple to `hide()` itself when it’s caught, but we
haven’t told it to `show()` itself when it starts dropping.

{{< learner-task >}}

Fix this!  Work out where, **in the `Apple`'s script**, you need to
add a line of code which makes the apple show itself.

{{< learner-task-help >}}

In the apple's script, there are two main sections.  The first section
chooses a random place to go to, and then goes to that place.  The
second section is the `while` loop which moves the apple down the
screen.  Just before the `while` loop (so at the end of the first,
"set-up" section) is a good place to put the `self.show()` we need.

{{< learner-task-help >}}

{{< jr-commit show-apple-when-fall-starts edit-script >}}

{{< /learner-task >}}

This is now a playable game written in Python — congratulations!

If you're using a shared computer, you can save your work using the
"Export to Google Drive" or "Download as zipfile" options from the
dropdown menu.


## Improve the game

{{< exclude-from-progress-trail >}}

Here are some ideas on how you could make this game more fun:

* Add a pause between one apple being caught / missed and the next one
  appearing.  Use the Scratch/Python help to find the Pytch version of
  Scratch’s `wait () seconds` block.  (Hint: just before doing
  `pytch.broadcast_and_wait("drop-apple")` is a good place to pause.)

* The `x`-coordinate where the apple starts is already random.  Make
  the starting `y`-coordinate be random too.  If an apple starts lower
  down the stage, the player has less time to get the bowl under the
  apple, making the game more challenging.

* Change how quickly the player can move the bowl.  A bit quicker
  would make the game easier; a bit slower would make the game harder.
  The speed appears in two places: for moving left and for moving
  right.  Investigate whether it’s worth setting a variable to hold
  the speed.  A variable makes it easier to experiment with the
  player’s speed, but it is a bit more work to write the code in the
  first place.

* Add another costume to the apple — you could use `orange.png` from
  the media library.  (Your code will be clearer if you then change
  the name of the sprite to `Fruit`!)  Each time the `Fruit` appears,
  choose randomly which costume to wear.  (Hint: a good place for this
  code is in the first part of the apple’s script, before the `while`
  loop.)  The Scratch/Python help will tell you the Pytch version of
  Scratch’s `switch costume` block.

* Make the score-keeper jump up and down in celebration when the
  player catches an apple.  In Scratch you might use the `repeat`
  block.  Use the Scratch/Python help to find how to do this in Pytch.

* Make there be a fixed number of apples — maybe 8.  Advanced: At the
  end of the game, make the score-keeper say something like “You got 5
  out of 8”.  You can use Python’s “f-strings” ([read about them in
  the Python
  documentation](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings))
  to get the score-keeper to say this.


## Credits

{{< exclude-from-progress-trail >}}

We have used various freely-available resources to make this project:

{{< asset-credits >}}
