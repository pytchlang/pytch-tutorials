# Script-by-script Shoot the fruit

You're going to write a game in Python where the player has to click
on fruit to score points.  If you know some Scratch, you'll see that
in many ways Pytch is similar to Scratch.  But it's fine if you
haven't done any Scratch.

![screenshot](screenshot.png#img-center)

---

## Use a more interesting background

Run the empty game now, by clicking the green play button.  You'll see
that not much happens.  The _Stage_ has a _backdrop_, which is what
you're seeing, but the starting backdrop is just a white rectangle,
which is not very interesting.

{{< learner-task >}}

Add a more interesting background for your game.  There is one in
Pytch's media library with a pattern of green leaves which will work
well.  It's called `leafy-background.png`.

{{< learner-task-help >}}

{{< jr-commit add-leafy-Backdrop add-medialib-appearance ["leafy-background.png"] >}}

{{< /learner-task >}}

Try the game now.  You'll see that nothing has changed.  This is
because Pytch shows the Stage's _first_ backdrop, which is still the
solid white rectangle.

{{< learner-task >}}

Delete the `solid-white.png` backdrop from the Stage.

{{< learner-task-help >}}

{{< jr-commit remove-default-backdrop delete-appearance >}}

{{< /learner-task >}}

Now your game should use the new background.

{{< learner-task >}}

Try it!  Click the green play button to run your game.  You should see
the leafy green background.

{{< /learner-task >}}


## Create the fruit

Now you need a _sprite_, to be the fruit which the player has to shoot.

{{< learner-task >}}

Add a sprite called `Fruit` to your game.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-sprite add-sprite >}}

{{< /learner-task >}}

Next your sprite needs some _costumes_, to say what it should look
like.

{{< learner-task >}}

From the media library, add the "Cartoon fruit" bundle of images as
costumes for your sprite.  The first costume, which the sprite will
use by default, is a smiling apple.

{{< learner-task-help >}}

{{< jr-commit costumes-for-Fruit add-medialib-appearances-entry ["Cartoon fruit"] >}}

{{< /learner-task >}}

Now your game should include an apple.

{{< learner-task >}}

Try it!  Click the green play button to run your game.  You should see
the leafy green background with an apple in the middle.

**What is wrong?**

{{< learner-task-help >}}

The apple is much too big!

{{< /learner-task >}}

### Set the fruit's size

The game would be much too easy if the apple was this big.  You need
to write some code to make the apple smaller.

In Pytch (like in Scratch), your program is made up of _scripts_.  A
script runs when some event happens, like when the green flag is
clicked to start the game.  This is a good time to set the apple's
size.

{{< learner-task >}}

Add a _when green flag clicked_ script to your Fruit sprite.

{{< learner-task-help >}}

{{< jr-commit add-empty-Fruit-init-size-script add-script >}}

{{< /learner-task >}}

At the moment, this script is empty — it has no Python code in it.

{{< learner-task >}}

Add a line of Python code to your script which sets the Fruit's size
to something more sensible.

{{< learner-task-help >}}

Making the Fruit one-quarter of its default size is probably about
right.  If you know Scratch, you might know that

``` scratch
set size to (25) %
```

will do this.  Look in the help to find out how to do the same thing
in Pytch.

{{< learner-task-help >}}

The Pytch method you need is

``` python-expression
self.set_size()
```

with a number between the `()`s saying what size you want.

{{< learner-task-help >}}

To say "one quarter of its default size", you can use the value
`0.25`.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-init-size-script-body edit-script >}}

{{< /learner-task >}}

Now the Fruit should be a better size.

{{< learner-task >}}

Try it!  Click the green play button to run your game.  You should see
a more sensibly-sized apple on the leafy background.

{{< /learner-task >}}


## Let the player click the fruit

You need to make something happen when the player clicks on the Fruit
— it should disappear.  If you know Scratch, you might know to do
something like

```scratch
when this sprite clicked
hide
```

As you've just seen when you wrote code to set the Fruit's size,
things work in a very similar way in Pytch.

{{< learner-task >}}

Add a script to the Fruit sprite which runs when the player clicks on
it.

{{< learner-task-help >}}

{{< jr-commit add-Fruit-when-clicked-script add-script >}}

{{< /learner-task >}}

Again, you only need one line of code in the new script.

{{< learner-task >}}

Add code to this script which makes the Fruit hide.

{{< learner-task-help >}}

You can check the help to see what Pytch method will make the Fruit
hide.

{{< learner-task-help >}}

The method you want is

``` python-expression
self.hide()
```

There is no more information you need to give, but you do still need
the `()`s.

{{< learner-task-help >}}

{{< jr-commit hide-when-hit edit-script >}}

{{< /learner-task >}}

It's a good idea to test your game after making each change.

{{< learner-task >}}

Try it!  Click the green play button to run your game, then:

* On purpose, miss the apple by clicking on the background.  The apple
  should _not_ disappear.
* Click on the apple.  It should disappear.

{{< /learner-task >}}


## Make the apple reappear after being hit

The game is not very exciting yet.  Once the player clicks on the
apple, it disappears, and that's it.  You need to make the apple
reappear so the player can keep playing.

After the Fruit has hidden itself, it should wait for a short time,
and then show itself again.  If you know Scratch, you might add these
blocks to the bottom of the 'when this sprite clicked' script:

```scratch
wait [1] seconds
show
```

In Python, you add two lines of code to your script.

{{< learner-task >}}

Use the help to find what Pytch statements will:

* Make the script wait for one second.
* Make the apple show itself.

{{< learner-task-help >}}

To wait for some amount of time, you can use the

``` python-expression
self.wait_seconds()
```

method, and put the number of seconds you want to wait between the
`()`s.

{{< learner-task-help >}}

To make a sprite show itself, you can use the

``` python-expression
self.show()
```

method.  You don't need anything between the `()`s, but the `()`s do
need to be there.

{{< learner-task-help >}}

{{< jr-commit wait-then-show edit-script >}}

{{< /learner-task >}}

Again, it's a good idea to test your game as you go along.

{{< learner-task >}}

Try it!  Click the green play button to run your game, then:

* Click on the apple.  It should disappear, then after a second,
  re-appear.  Click it a few more times to make sure.

{{< /learner-task >}}


## Make the apple reappear somewhere else

The game is better now, but still not very exciting.  The player knows
where the apple is going to appear.  We want the apple to reappear at
a random place on on the Stage.

Scratch has the block

``` scratch
go to (random position v)
```

and Pytch has something similar.  You can say

``` python
self.go_to_random_position()
```

to make your sprite move to a random position on the stage.

{{< learner-task >}}

Add this line of code to your Fruit's _when this Sprite clicked_
script.  Think about where the new line of code should go into the
sequence of lines of code that are already there.

{{< learner-task-help >}}

A sensible place is after the `self.wait_seconds(1)` line but before
the `self.show()` line.

{{< learner-task-help >}}

{{< jr-commit go-to-random-position edit-script >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Run your program with the green flag.  Every time you click on the
Fruit, it should disappear, then after a second, reappear in a random
place.

{{< /learner-task >}}


## Show the player's score

It would be good if the player knew how well they were doing.  The
game should keep a *score*, and give the player a point every time
they shoot a Fruit.

### Create a **variable** to hold the score

Your code will remember the score in a *variable*.  These work very
much like Scratch variables.  In Python, you don't need to explicitly
'make a variable' — you just set a variable to a value, and the
variable is created for you.

In Python, it's more common to use variables which 'belong to' the
Stage or to a particular sprite.

The score is something which the Fruit and the Stage both need to work
with.  There's not a very strong reason to set up the score in one or
the other.  We'll give the job to the Stage.

The game should set the score to zero at the start of the game, so
your program needs a script which runs when the game starts.

{{< learner-task >}}

Make sure you're working with **the Stage** — click on the Stage in
the Stage and Sprites pane, and make sure the coding area has tabs
"Code", "Backdrops", and "Sounds".

{{< /learner-task >}}

{{< learner-task >}}

Add a script **to the Stage** which runs when the game starts.

{{< learner-task-help >}}

{{< jr-commit add-Stage-setup-script add-script >}}

{{< /learner-task >}}

The score variable needs to exist across all scripts, so we'll use a
variable which 'belongs to' the Stage.  The full details of how all
this works are beyond the scope of this tutorial, but for now you just
need to know that you talk about a variable called `score` belonging
to the Stage with the Python expression

``` python-expression
Stage.score
```

{{< learner-task >}}

Add a line of code to the Stage's new script which sets the
`Stage.score` variable to the number zero.

{{< learner-task-help >}}

{{< jr-commit init-Stage-score edit-script >}}

{{< /learner-task >}}

### Showing the score

In Scratch you tick a box to show a variable on the Stage.  In Pytch,
you write code to do this.  The code will go just after the code to
start the score off at zero.

{{< learner-task >}}

Add a line of code to show the `Stage.score` variable.

{{< learner-task-help >}}

Look in the help to see what Pytch method does this.

{{< learner-task-help >}}

Here, the variable's name is `"score"`.

{{< learner-task-help >}}

{{< jr-commit show-score edit-script >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Run your program with the green flag.  Check you see the score
displayed at the top-left.  Click on the Fruit a few times.

**What's wrong?**

{{< learner-task-help >}}

The score doesn't change!

{{< /learner-task >}}

So far your program has no way for the player to get points, so the
score will be stuck at zero.  The next chapter will fix this.


## Give the player points

To increase the player's score, in Scratch you might do

``` scratch
change [score v] by [1]
```

Python has the `+=` operator ('change by adding'), which works the
same.  For example, if your code had a variable `Stage.health`, the
code to add five to it would be

``` python
Stage.health += 5
```

{{< learner-task >}}

Make sure you're working with **the Fruit sprite** — click on the
Fruit sprite in the Stage and Sprites pane, and make sure the coding
area has tabs "Code", "Costumes", and "Sounds".

{{< /learner-task >}}

{{< learner-task >}}

**In the Fruit sprite**, add a line of code to the script which runs
when the Fruit is clicked, making it so the player gets one point.

Think about where in the script the new line of code should go.

{{< learner-task-help >}}

To get a point, you need to add one to the `Stage.score` variable.

{{< learner-task-help >}}

{{< jr-commit award-point-when-hit edit-script >}}

{{< /learner-task >}}

You might have noticed that the code in this tutorial sometimes has
blank lines.  Blank lines are ignored by Python, but they make the
code easier for a human to read.

### Try it!

{{< learner-task >}}

Run your program with the green flag.  Check the score goes up when
you click on the Fruit.

{{< /learner-task >}}


## Lose points if player misses

The game would be more challenging if the player loses points when
they miss the Fruit.

Your program can react if the player misses by making the Stage run
some code when *it* is clicked.

{{< learner-task >}}

Make sure you're working with **the Stage** — click on the Stage in
the Stage and Sprites pane, and make sure the coding area has tabs
"Code", "Backdrops", and "Sounds".

{{< /learner-task >}}

{{< learner-task >}}

Add a _when stage clicked_ script **to the Stage**.

{{< learner-task-help >}}

{{< jr-commit add-stage-clicked-script add-script >}}

{{< /learner-task >}}

The code in this script should make the player lose some points.
Python has `-=` ('change by subtracting') for this.  For example, if
your program had a variable `Stage.health`, the code

``` python-expression
Stage.health -= 10
```

would subtract ten from it.

{{< learner-task >}}

Add a line of code to your script which subtracts five from the
`Stage.score` variable.

{{< learner-task-help >}}

{{< jr-commit lose-points-on-miss edit-script >}}

{{< /learner-task >}}

By now you should know what to do next!

{{< learner-task >}}

Try it!  Run your program with the green flag.  Check the score goes
up when you click on the Fruit.  Check the score goes down when you
click on the Stage on purpose.

**What's the problem?**

{{< learner-task-help >}}

If the score is less than five when the player misses, the score
becomes negative.

{{< /learner-task >}}

### Stop the score becoming negative

If the first thing the player does is miss the Fruit, their score will
be `-5`.  This is not very sensible.

After subtracting five points, the code needs to test whether the
score has become negative.  If so, the score should be set to zero
instead.

To only run some code if some condition is met, Python has the `if`
statement.  If you know Scratch, it works the same as Scratch's `if`
block.

{{< learner-task >}}

Add an `if` statement under the `Stage.score -= 5` line.  The `if`
statement should test whether `Stage.score` is negative, and, if so,
set `Stage.score` to zero.

{{< learner-task-help >}}

The help gives some examples of how this works.  Look for _If/then_ in
the _Control_ section.  Notice how in Python, the _body_ of the `if`
statement is _indented_ — moved across from the left margin by four
spaces.

You need to work out what Python expression to use for the _test_, and
work out what code goes in the _body_ of the `if` statement.

{{< learner-task-help >}}

The test you want is

* _Is the `Stage.score` variable less than zero?_

The Python expression for this is

``` python-expression
Stage.score < 0
```

{{< learner-task-help >}}

{{< jr-commit clamp-score-at-zero edit-script >}}

{{< /learner-task >}}


## Game complete!

This is now a playable game written in Python — congratulations!

{{< learner-task >}}

Play a few games and see how quickly you can score points.

{{< /learner-task >}}


## Extra: Add another fruit

To make the game look more interesting, you can add another kind of
fruit.

### Choose a random costume

You have already used the Python function `random.randint()` to pick
random numbers for where the Fruit should appear on the screen.

The function

``` python-expression
random.choice()
```

chooses a random thing from a list.  You can use this to set a
variable to the name of a random costume for the Fruit to wear when it
reappears.

{{< learner-task >}}

Add code to the Fruit sprite's _when this sprite clicked_ script.  The
code should:

* Choose a random costume, with the options being `"Apple-1.png"` and
  `"Orange-1.png"`.  You can check the _Costumes_ tab to see what
  other costumes there are, if you prefer.
* Set a variable `new_costume` to the chosen costume name.

{{< learner-task-help >}}

The help has an example for choosing from a list.  Look in the
_Operators_ section for `random.choice()`.

{{< learner-task-help >}}

You need to give `random.choice()` a _list_ of options.  The Python
expression

``` python-expression
["Apple-1.png", "Orange-1.png"]
```

means a list with two things in it — the name `"Apple-1.png"` and the
name `"Orange-1.png"`.

{{< learner-task-help >}}

{{< jr-commit choose-random-new-costume edit-script >}}

**Note on layout:** Here, the new code is shown split into three
physical lines.  If you prefer, you can type it all as one line.

{{< /learner-task >}}

### Switch to the chosen costume

If you know Scratch, you might have used the

``` scratch
switch costume to [Apple-1 v]
```

block to tell a sprite to use a different costume.  Pytch can do
the same.

{{< learner-task >}}

After the `random.choice()` line, add a line of code which switches to
the chosen costume.

{{< learner-task-help >}}

{{< jr-commit switch-to-random-costume edit-script >}}

{{< /learner-task >}}

And finally:

{{< learner-task >}}

Try it!  Run your program.  Check you get a mixture of kinds of fruit.

{{< /learner-task >}}


## Challenges

Can you change your program to solve these challenges?

* Choose from more costumes, not just an apple or an orange.
* Give the player 10 points for every fruit they hit instead of 1.
* Give the player 5 points for an apple and 10 points for an orange.
  (_Hint:_ You can use the expression `self.costume_name` to find the
  name of the costume the sprite is currently wearing.)
* Make the Fruit smaller, so it's harder to hit.
* _Harder challenge:_ Make the Fruit smaller if the player has more
  points.  This makes the game get more difficult as the player gets
  better at it.
