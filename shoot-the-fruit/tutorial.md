# Shoot the fruit

We're going to write a game in Python where the player has to click on
fruit to score points.  We'll write the game in a very similar way to
how we'd create it in Scratch.

![screenshot](screenshot.png#img-center)


### Acknowledgements for images

{{< asset-credits >}}

---

## Create a stage with backdrop

The first thing we'll do is to create a *Stage* for the game.  To keep
things simple, we'll use a solid dark green background.

In Scratch, there is automatically a Stage for your project.  In
Pytch, we have to create it.  We're going to call it `GameBackground`,
and we need to say that it's the `Stage` for our game.

In this tutorial, we'll show the code we need in boxes like this — the
blue `?` will show help on what to do:

{{< commit empty-GameBackground >}}

Here, we need to add two blank lines under the `import pytch` line
which is already there, and then the line starting `class
GameBackground`.

Python ignores the blank lines, but they keep our code tidy and easy
to read.

This code does not yet make sense, so if you click the green flag you
will get an error!  Come back to this *Tutorial* tab if that happens.

In Pytch, the stage has *backdrops*, like in Scratch.  To say what
backdrops we want, we set a variable called `Backdrops` for the
stage.  If you look in the *Images and sounds* tab, you'll see an
image called `"solid-green.png"`.  We'll use this by adding a line of
code to our program:

{{< commit Backdrop-for-GameBackground >}}

The square brackets `[` and `]` mean that this is a *list* of
backdrops.  Our stage here only has one backdrop, but we still
need to write `Backdrops` as a list.

Try your program now — click the green flag.  You should see the dark
green backdrop appear.


## Create the fruit

Now we'll add a *Sprite* for the fruit which the player has to shoot.
In Scratch you would click on the "add Sprite" button.  In Python we
add some code to our program.  We'll call our new Sprite `Fruit`, and
we need to say that it's a Sprite.  This is the code we need:

{{< commit empty-Fruit >}}

Just like in Scratch, Sprites in Pytch have *costumes*.  We set a
variable to the list of costumes we want our Sprite to have.  For now,
we only have one costume, `"apple.png"`.

{{< commit Costume-for-Fruit >}}

Try your program — if you click on the green flag, you should see an
apple in the middle of the stage.


## Let the player click the fruit

We need to make something happen when the player clicks on the apple —
we'll make the fruit disappear.  In Scratch you would do something
like

![Scratch: when-sprite-clicked-hide](when-sprite-clicked-hide.png#img-center)

This has two parts:

* We say *when* we want something to happen using a "hat block" — when
  this sprite clicked.

* We say *what* we want to happen by connecting other blocks
  underneath the hat block — the *hide* block.

Things work nearly the same in Pytch.  To say *when* we want something
to happen, we use a special marker in the code:

{{< commit Fruit-when-clicked-decorator >}}

In Python, we need to give a name to the section of code we want to
run.  This piece of code will run when the fruit is hit, so we'll call
it `hit_fruit`.

{{< commit hit-fruit-method-def >}}

(The `def` is short for *define* — we're about to define the section
of code called `hit_fruit`.  The `self` is like a variable which will
refer to the Sprite being clicked.)

Finally, we say what we want to happen when the Sprite is clicked — we
want it to *hide*:

{{< commit hide-when-hit >}}

The `self` means that we want *this* Sprite to hide.

When you have added the code to your program, test it!  Click the
green flag and check that:

* the apple disappears when you click on it;
* the apple does *not* disappear when you click somewhere random on
  the green background.


## Make the apple reappear after being hit

The game is not very exciting yet.  Once the player clicks on the
apple, it disappears, and that's it.  We need to make the apple
reappear so the player can keep playing.

After the fruit has hidden itself, we want it to wait for a short
time, and then show itself again.  In Scratch, we would add these
blocks to the bottom of the 'when this sprite clicked' script:

![Scratch: wait-1-second-then-show](wait-1-second-then-show.png#img-center)

In Python, we add two lines to our code:

{{< commit wait-then-show >}}

Try the program now!  The apple should disappear when you click it,
then reappear one second later.


## Make the apple reappear somewhere else

The game is better now, but still not very exciting.  The player knows
where the apple is going to appear.  We want the apple to reappear at
a random place on on the stage.

### Saying where to go on the stage

Like in Scratch, positions on the Pytch stage are described by two
numbers, `x` and `y`:

* The `x` number says how far right of the centre we are (and so `x`
  is negative if we are *left* of the centre).
* The left-right centre of the stage is `x = 0`, far left is `x =
  -240`, and far right is `x = 240`.
* The `y` number says how far above the centre we are (and so `y` is
  negative if we are *below* the centre).
* The up-down centre of the stage is `y = 0`, the very bottom is `y =
  -180`, and the very top is `y = 180`.

### Picking a random number

We'll need to randomly pick `x` and `y` numbers for where the apple
reappears.

To do this, we will use some code that the Python team have written
which picks random numbers.  We first need to say that we want to use
this code:

{{< commit import-random >}}

(You might notice that our program starts off with `import pytch` —
this is what tells Python that we want to be able to use things like
`pytch.wait_seconds`.)

We will use the `randint` 'function' of this `random` code, to pick
random numbers for us, and choose where the apple will reappear.  We
will need to tell `randint` the smallest and biggest possible numbers
we want.

In Scratch you would put this information into the 'holes' of
the block.  For example, to roll a dice you might say:

![Scratch: pick-random-1-to-6](pick-random-minus-1-to-6.png#img-center)

In Python, we put the pieces of information between brackets `(` and
`)`.  This Scratch block would look like this in Python:

```
random.randint(1, 6)
```

### Picking a random place to appear

We want to pick a random `x` number and a random `y` number to say
where the apple should reappear.  We will store these values in
*variables*.  These work very much like Scratch variables.  In Python,
you don't need to explicitly 'make a variable' — you just set a
variable to something and it is created for you.

We will make a variable to hold the `x` number for where we want the
apple to reappear:

{{< commit assign-new-x >}}

The `-200` and `200` don't go all the way to the edges of the stage,
because we want the apple to always definitely be completely on the
stage — it's the centre of the apple which we are picking a location
for.

We will set another variable to hold the `y` number:

{{< commit assign-new-y >}}

We use `-140` and `140` rather than `-180` and `180` to make sure the
apple doesn't go off the top or off the bottom of the stage.

### Appear at the random location

Now we know where we want the apple to randomly reappear, we can make
it go there just before showing itself.

In Scratch, we can use variables to 'fill in holes' in blocks, like:

![Scratch: go-to-appear-x-appear-y](go-to-appear-x-appear-y.png#img-center)

In Python, we put the variables in `()`s:

{{< commit go-to-random-x-y >}}

### Try it!

Run your program with the green flag.  The apple should reappear in a
random place every time you click it.


## Show the player's score

It would be good if the player knew how well they were doing.  We want
to keep a *score*, and give the player a point every time they shoot
the fruit.

We will set this variable at the top of our program.  When the game
starts, the player has no points, so we set our new `score` variable
to zero.  In Scratch we would say

![Scratch: set-score-to-zero](set-score-to-zero.png#img-center)

and in Python, we use this code, which creates the variable and sets
it to zero:

{{< commit define-score-global >}}

### Showing the score

In Scratch you can just tick a box to show a variable on the stage.
In Pytch we write code to do this.  We want to do this as soon as the
green flag is clicked, so we'll need code to act like Scratch's "when
green flag clicked" hat block.  We'll put this in the `GameBackground`
(our stage), because it's part of the overall game.

{{< commit GameBackground-when-green-flag-decorator >}}

The code to display the variable is a bit complicated, so for this
tutorial, we won't go into details.  The code we need is:

{{< commit show-score >}}

So far our program has no way for the player to get points, so the
score will be stuck at zero.  We will fix this next.


## Give the player points

To increase the player's score, in Scratch we would do

![Scratch: change-score-by-1](change-score-by-1.png#img-center)

Python has `+=` ('change by adding'), which works very much the same.
The code we want is

```
score += 1
```

and it needs to go in our code which runs when the `Fruit` is clicked.
There is a detail we need to deal with first, which is to tell Python
that we want to change the *global* variable `score`.  A 'global'
variable is very like a "for all sprites" variable in Scratch.  Add
these lines to the `hit_fruit` code:

{{< commit award-point-when-hit >}}

Try it!  The score should now count how many times the player has
hit the fruit.


## Knock off points if player misses

To make the game more challenging, we'll make it so if the player
misses the fruit, they lose points.

We can tell if the player misses by making our stage run some code
when *it* is clicked.  We'll start by adding code to act like
Scratch's "when stage clicked" hat block:

{{< commit when-stage-clicked-decorator >}}

We need a name for the chunk of code we're about to write.  The code
will run when the player misses the fruit, so `missed_fruit` is a good
name:

{{< commit missed-fruit-def >}}

And now we can knock off points if a click gets through to the stage.
Just as when we gave the player points, we need to tell Python that we
want to change the global `score` variable.  And this time, instead of
*adding* to `score` by using `+=`, we want to *subtract* from `score`,
so we use `-=` ('change by subtracting').  This code knocks off five
points when the player misses:

{{< commit lose-points-on-miss >}}

### Stopping the score going negative

There is a problem with this: What happens if the player misses when
their score is less than five?  Try it — run your game and
deliberately miss with your first click.  You'll see that the game
says your score is `-5`.  This is not very sensible.

After knocking off five points with `score -= 5`, we want to test
whether the score has become negative.  If so, we want to set `score`
to zero.  Python has an `if` statement which works the same as
Scratch's *if* block.  This is the code we need:

{{< commit clamp-score-at-zero >}}

The `score < 0` part is the test — it asks whether the `score`
variable is less than zero.  If it is, the *indented* (pushed to the
right) code runs.  Here, there is only one indented line, which sets
`score` to zero.


## Game complete!

This is now a playable game written in Python — congratulations!

Play a few games and see how quickly you can score points.


## Extra: Add another fruit

To make the game look more interesting, we can add another fruit.

### Add a costume

At the moment, the `Fruit` sprite only has one costume.  We want to
add another one.  There is an image `"orange.png"` included with this
tutorial, so we just need to tell Pytch about it.  In Python, the
different things in a list are written with commas between them.  So
we need to change the line which sets the Fruit's costumes:

{{< commit add-orange-costume >}}

The box explains this change as deleting the `Costumes` line and
adding a replacement, but you can just type in the new part —

```
, "orange.png"
```

— if that's easier for you.

### Choose a random costume

We have already used the Python function `random.randint` to pick
random numbers for where to appear on the screen.  There is another
function — `random.choice` — which chooses a random thing from a
list.  We'll use this to set a variable to the name of the costume we
want the Fruit to wear when it reappears.

Find the right place in `hit_fruit` to add this code:

{{< commit choose-random-new-costume >}}

### Switch to the chosen costume

And just like Scratch has a *switch costume to* block, Pytch has a way
to get a Sprite to wear a different costume.  We'll use this to switch
to the costume we just randomly picked:

{{< commit switch-to-random-costume >}}


## Challenges

Can you:

* Give the player 10 points for every fruit they hit instead of 1?

* Make the fruit smaller, so it's harder to hit?  (*Hint:* You can use
  `self.set_size(0.5)` to shrink a Sprite to half its normal size.)

* Harder challenge: Make the fruit smaller if the player has more
  points?  This makes the game get more difficult as the player gets
  better at it.
