# Trimon

We’ll make a memory game where the player has to remember longer and
longer patterns of flashing lights.  Don’t get one wrong!


---

## Creating the backdrop

We’ll start by adding a Stage with a simple blue gradient backdrop:

{{< commit add-background-and-backdrop >}}

If you run your program after adding these lines, you should see the
background.


## Making the first light

Our game will have three lights.  We’ll start by adding just one of
them.  Once we have that working, we’ll copy and paste the code, with
small changes, to make the other lights.  (This isn’t usually the best
way to make a set of similar things, but the other ways are more
advanced than we can cover in this tutorial.)

The light is called an ‘LED’ in the code, because that’s the sort of
light the image looks most like.  It needs two costumes, one for when
it’s just sitting there, and another for when it’s lit up:

{{< commit add-LED1-and-costumes >}}

We want to arrange the LEDs in a line across the screen, so at the
start of the game, this LED should move to a position a bit to the
left of centre, and a bit above centre:

{{< commit init-LED1-position >}}

The light should be able to make a noise, so we’ll add a sound:

{{< commit add-LED1-sound >}}

And finally (for now), we’ll make the light flash and make its sound
when we click on it:

{{< commit flash-LED1-on-click >}}

I’m saying which costume to switch to based on position in the list,
where the first thing in the list is position zero.  You could use the
costume names (`"light-off"` and `"light-on"`) if you prefer.

### Try this now!

In the final game, it won’t be clicking that sets off the flash and
sound, but by writing this code, we can test what we’ve done so far.
We’ll change the code later.


## Making the other lights

The other lights are fairly similar, so we’ll go through this more
quickly.  For now we’ll just add the basics of these two.

First the middle light.  Its costumes and sounds are very similar to
the left-hand light, except this light will make a different sound:

{{< commit add-LED2-and-costumes-sounds >}}

The right-hand light is also similar:

{{< commit add-LED3-and-costumes-sounds >}}

At the start of the game, the middle light should move to its
position:

{{< commit init-LED2-position >}}

And the right-hand light to _its_ position:

{{< commit init-LED3-position >}}

We won’t bother with the testing ‘click to flash and make a noise’
code for these two.  We’ll put the proper code in later.


## Storing the pattern in a variable

Now we’ll think about how to keep track of the pattern which the
player has to repeat.  We’ll give each light a number:

* `1` — left-hand light
* `2` — middle light
* `3` — right-hand light

and store the pattern in a variable holding a Python _list_, which is
perfect for this job.

Soon we’ll write the code which shows the pattern, and we want to be
able to test that code without having to write all the rest of the
game.  So we’ll cheat, and start off with a short pattern.  At the top
of the program, we’ll define a variable holding a pattern we can test
with:

{{< commit define-pattern-global-test-value >}}

When we’ve written the code, this list should play the pattern

* left, middle, right, left.


## Playing the pattern on the lights

We need to think about whose job it is to control the showing of the
pattern.  It involves more than one light, so we’ll put the code in
our `Background`.

The `Background` will tell a particular light to flash by broadcasting
a message:

* To tell the **left-hand** light to flash, it’ll broadcast **`"flash-1"`**.
* To tell the **middle** light to flash, it’ll broadcast **`"flash-2"`**.
* To tell the **right-hand** light to flash, it’ll broadcast **`"flash-3"`**.

We’ll use `broadcast_and_wait()` to make sure each light finishes its
flash before we tell the next light to do its flash.

We want to be able to test this code, so for now we’ll make it happen
when we press a key.  In the full game, this will be different.

Our code should go through each number in the `pattern` list in turn,
and broadcast the correct message.  The message should be the string
`"flash-"` joined on to the light number.  Suppose we have a variable
`led` which is the number `1`, `2`, or `3`.  Then we can turn that
number into a string by saying `str(led)`.  We can glue the two
strings together with `+`, and give a name to the string we get, by
saying

``` python
message = "flash-" + str(led)
```

To go through the numbers in the `pattern` list one by one, we can use
a useful feature of Python made for exactly this job, the

``` python
for thing in list_of_things:
    # Do something with thing
```

loop.

Putting this all together, we get:

{{< commit play-pattern-on-keypress >}}

But if you run this and try pressing `p`, nothing will happen, because
we haven’t told the lights to react to those messages yet.


## Making the lights flash via messages

We already have working code to make the left-hand light flash and
make its sound.  We just need to use a different ‘hat block’, to tell
Pytch to run this code when the message `"flash-1"` is received.  So
delete the `when_this_sprite_clicked` line and replace it with a
`when_I_receive` line:

{{< commit flash-LED1-on-message >}}

Now this block of code is ready to copy and paste into the code for
the other two lights.  First we’ll copy it into `LED2`.  There are two
changes:

* The message it reacts to is **`"flash-2"`** (not `"flash-1"`).
* The sound it plays is **`"note-2"`** (not `"note-1"`).

{{< commit flash-LED2-on-message >}}

And for `LED3`, we copy, paste, and change:

* React to message **`"flash-3"`**.
* Play sound **`"note-3"`**.

{{< commit flash-LED3-on-message >}}

If you try the program now, our test pattern (left, middle, right,
left) should play when you press the `p` key.

It would look better with a small pause between each flash, so we’ll
add a line to the loop in `Background`:

{{< commit small-delay-between-pattern-flashes >}}


## Adding the buttons

Next, the game needs three buttons, so the player can try to repeat
the patterns.

### Left-hand button

We’ll add a sprite for each button, starting with the left-hand one:

{{< commit add-Button1-and-costume >}}

It should start the game by moving to a position underneath the
left-hand light:

{{< commit init-Button1-position >}}

And when it’s clicked, it should make the left-hand light flash and
make a sound.  We can do this by broadcasting the correct message:

{{< commit handle-Button1-click-v1 >}}

### Middle button

This is very similar.  The `Button2` sprite has the same costume:

{{< commit add-Button2-and-costume >}}

but moves to a different position at the start of the game:

{{< commit init-Button2-position >}}

and broadcasts the right message to make the middle light flash and
make its sound:

{{< commit handle-Button2-click-v1 >}}

### Right-hand button

We can now copy and paste and make small changes to get the code for
the right-hand button, `Button3`.  Watch out for the coordinates given
to `self.go_to_xy()`, and the message given to
`pytch.broadcast_and_wait()`.

{{< commit add-Button3-all-v1 >}}


## Stopping the player from mashing buttons

If you try the game now and are quick enough, you can click the
buttons quickly and make more than one light flash at once.  This
shouldn’t happen.

The program needs to be able to tell when a light is in the middle of
flashing, and not flash another light until that flash has finished.

We’ll keep track of that in a variable which stores the true/false
information

> is a light in the middle of flashing?

Several places in the program need to use this variable, so we’ll make
it _global_ by defining it outside any sprites.  At the start of the
game, no light is flashing, so the variable holds `False`:

{{< commit define-global-light-flashing >}}

Starting with the when-clicked script for `Button1`, we’ll set the
variable to `True` just before the broadcast of `"flash-1"`, and
`False` again afterwards.  We need to tell Python that we’re talking
about the _global_ `light_flashing` variable:

{{< commit maintain-light-flashing-in-Button1 >}}

And then, `return` early if a light is already flashing:

{{< commit return-if-light-flashing-Button1 >}}

We do the same thing in `Button2`:

{{< commit guard-Button2-press >}}

and `Button3`:

{{< commit guard-Button3-press >}}

(If you’re thinking ‘surely there’s a better way to write this program
than copying and pasting everything’, you’re right, but the techniques
you need are more advanced than this tutorial covers.)


## Recording the player’s attempt

As the player clicks the buttons to try to repeat the pattern, our
program needs to remember the sequence of buttons in the player’s
attempt.

A global variable holding a list will do this for us.  At the start of
the game, the player has not pressed any buttons, so the list is
empty:

{{< commit define-global-user-attempt >}}

When each button is pressed, we want to add an element to this list,
to build up a history of the player’s attempt to repeat the pattern.
Inside `Button1`, we tell Python we’ll be talking about the _global_
`user_attempt` variable as well as the global `light_flashing`
variable:

{{< commit resolve-user-attempt-as-global >}}

and then once the `"flash-1"` message has been responded to, we
_append_ the value `1` to the list:

{{< commit append-1-to-user-attempt >}}

We do something very similar in `Button2`:

{{< commit append-2-to-user-attempt >}}

and in `Button3`:

{{< commit append-3-to-user-attempt >}}


## Checking whether the player is getting it right

Each time the player adds to the pattern, we need to check if they’re
right so far.  We also need to check whether they’ve now done the
whole pattern correctly.

This is quite a fiddly piece of code, so we’ll print some messages to
the `Output` tab, to check the code is behaving as we want.

We’ll start by defining a function which will run in response to a
message `"check-user-attempt"`:

{{< commit define-check-user-attempt-function >}}

In the body of this function, want to ask the question

> Is what the user has done so far correct?

Suppose the user has pressed four buttons so far.  Then we want to
compare the `user_attempt` list to a list containing the first four
items in the `pattern` list.  We’ll use Python _slicing_ to extract a
section of a list.  We find out how many items are in the
`user_attempt` list, and then copy that many items from the start of
`pattern` into a local list variable `pattern_start`:

{{< commit compute-pattern-start >}}

So we can check we’re doing this right, we’ll print the lists we’re
interested in:

{{< commit print-pattern-user-attempt-pattern-start >}}

We can now ask whether the player’s attempt matches the first part of
the pattern they’re meant to be copying.  For now, we’ll print a
message saying whether they’re right or wrong:

{{< commit print-fail-or-ok-so-far >}}

If they’re right so far, we can go on to check whether they’ve in fact
got the whole pattern right.  We can test this by comparing the length
of the user pattern to the length of the original pattern — if they’re
the same, the player has got the whole pattern right.  Again, for now
we just print a message if the player has got everything right:

{{< commit maybe-print-whole-pattern-OK >}}

### Checking after each button click

But our program is not yet _running_ this code, because nothing is
broadcasting the `"check-user-attempt"` message.

Each button needs to broadcast this message after adding its number to
the `user_attempt` list.  We add code to `Button1`:

{{< commit check-after-Button1 >}}

and `Button2`:

{{< commit check-after-Button2 >}}

and `Button3`:

{{< commit check-after-Button3 >}}

### Test the code

You can try this now — press `p` and check what’s printed in the
`Output` tab as you click on the buttons.


## Running the game

We can now start to replace some of our ‘just for now’ code with real
code.

The code which plays the pattern is currently launched by pressing
`p`.  Instead, it should run when it receives a `"play-pattern"`
message:

{{< commit play-pattern-on-message-not-keypress >}}

At the start of the game, there are no lights in the pattern, so
`pattern` should start off as the empty list:

{{< commit init-pattern-to-empty-list >}}

### Building up a random pattern

To be able to choose random numbers, we need to `import` Python’s
library for working with random numbers.  This is like adding an
extension in Scratch.  We want to use the code provided in the
`random` library:

{{< commit import-random >}}

Now we’ll put together a function which adds a new random light to the
pattern, then makes the new pattern play.  In the next block of code,
you should be able to find a line which:

* makes sure Python knows we’re talking about the _global_ `pattern`
  variable
* uses the `randint()` function in the `random` library to choose a
  random whole number between 1 and 3
* adds that number to the end of the `pattern` list
* broadcasts the right message to make the pattern play.

{{< commit add-flash-and-play-v1 >}}

### Extending the pattern when the player gets the old pattern right

Jumping back to the code which tests whether the player has got the
pattern completely right, this is exactly when we should add a new
light-flash to the end of the pattern.  We also need to set
`user_attempt` to the empty list, ready to build up the player’s
attempt at the new, longer pattern.  The `clear()` method does this.

{{< commit next-pattern-when-success-so-far >}}

### Starting the whole game off

Finally, we start the game by broadcasting the message to add a
light-flash and let the player try to copy it.

{{< commit start-game-by-adding >}}

Try this now!


## Only allowing button pressing at right times

You might notice that the player can click the buttons at any time,
even when the game is showing the player the pattern.  We’ll fix that
now.

There are some times in the game when pressing the buttons is allowed,
and some times when it is not allowed.  We’ll make a global variable
to keep track of the true/false information

> is the player allowed to press a button right now?

This starts off `False`, because the
player isn’t allowed to press a button until the first pattern has
been played.

{{< commit define-global-pressing-allowed >}}

Once the pattern has been played, the player is allowed to press
buttons to try to copy the pattern (we tell Python we’re talking about
the _global_ `pressing_allowed` variable):

{{< commit set-pressing-allowed-after-play-pattern >}}

In the `check_user_attempt()` function, if the user gets the whole
pattern right, they’re then _not_ allowed to press any buttons just
yet.  There are two changes needed in this function:

{{< commit clear-pressing-allowed-when-player-repeats-ok >}}

If the user fails, by getting a light wrong, they’re not allowed to
press buttons:

{{< commit clear-pressing-allowed-when-player-fails >}}

So far we’re just setting this variable to different values.  We now
make the `Button1`, `Button2`, and `Button3` sprites abandon their
when-clicked script early if pressing is not allowed.

For `Button1`:

{{< commit return-if-pressing-disallowed-Button1 >}}

and `Button2`:

{{< commit return-if-pressing-disallowed-Button2 >}}

and `Button3`:

{{< commit return-if-pressing-disallowed-Button3 >}}


## Using in-game messages

Watching for text being printed in the `Output` tab is not great.
We’ll add some in-game messages.

A new sprite has a costume for each message we want to show:

{{< commit add-Text-and-costumes >}}

At the start of the game, there is no message shown, so the `Text`
sprite should hide itself:

{{< commit init-Text-hidden >}}

This sprite will flash its ‘YES!’ costume when it receives the
`"correct"` message:

{{< commit flash-YES-on-message >}}

and show its ‘FAIL’ costume when it receives `"fail"`:

{{< commit flash-FAIL-on-message >}}

Here there’s no need to wait and then hide, because once the player
has failed, the whole game is over.

### Broadcasting the messages

Back inside `check_user_attempt()`, we broadcast the `"correct"`
message when the player has got the whole pattern right:

{{< commit launch-YES-on-success >}}

and the `"fail"` message if they make a mistake:

{{< commit launch-FAIL-on-failure >}}

Try this now!


## Tidying up

Now everything is working, we can delete the `print()` lines:

{{< commit remove-prints >}}


## Play with real buttons and lights

Using the GPIO ("general purpose input/output") features of the
Raspberry Pi 400, we can make this game flash real LEDs and react to
real buttons being pressed.  GPIOs are electrical connections which
your program can:

* measure (e.g., to tell whether a button is being pressed), or
* control (e.g., to light up an LED).

The Raspberry Pi 400 has around 25 pins which can be used like this.

The electronic circuit has been set up so that pins 22, 23 and 24
control the LEDs, and pins 16, 20, and 21 measure whether the buttons
are pressed.

### Light up the real LEDs

If we go back to our `LED1` sprite, we can add statements which turn
on the left-hand LED as the noise starts, and turn that LED off again
once the sound has finished.  The way your LEDs are wired, to turn an
LED on, you set the 'value' of its pin to `1`, and to turn it off, you
set its pin's value to `0`.

The left-hand real LED is connected to GPIO pin `22`, so we add these
lines:

{{< commit flash-HW-LED1 >}}

We add similar code to `LED2` — if you're copying and pasting, make
sure you update the pin number to `23`.

{{< commit flash-HW-LED2 >}}

And to `LED3`, whose real LED is connected to pin `24`:

{{< commit flash-HW-LED3 >}}

### React to the real buttons

Pytch lets us 'stack' hat-blocks, to allow more than one event to
start a script running.  The way these switch buttons are connected,
when the button is not pressed, the pin measures a _high_ voltage, and
when the button is pressed, the pin measures a _low_ voltage.  We want
to run the script when the pin goes _low_.

The left-hand button, `Button1`, is connected to pin `16`, so we add
this line:

{{< commit press-Button1-by-HW >}}

The centre button, `Button2`, is on pin `20`:

{{< commit press-Button2-by-HW >}}

And the right-hand button, `Button3`, is on pin `21`:

{{< commit press-Button3-by-HW >}}

### Try the physical game!

Play the game now, with its real buttons and lights!  You should be
able to either click the on-screen buttons, or press the real physical
buttons.


## Make your own improvements

Here are some ways you could change or improve the game.  Or try out
some ideas of your own!

### Show the player how they’re doing

Add a variable which keeps track of how many light-flashes the player
has got right.  You’ll need to work out what number the variable
should hold at the start of the game, and when it changes.  You can
show a global variable called `score` with this code:

``` python
pytch.show_variable(None, "score")
```

The name of the variable is given as a string here.

### Use different graphics

Find some images to use instead of the lights and buttons.  You’ll
need to think about how to show your lights ‘lighting up’ — or maybe
you could have characters which jump up and down instead of lights
which flash.

### Add another light and button

Can you see how to extend the code to have four lights and buttons?
You’ll need to find another sound.

### Change the speed of the game

To play the pattern more slowly, you can increase the `0.1` in the
`pytch.wait_seconds(0.1)` line.

To play the pattern more quickly, you can reduce that `0.1`, or even
get rid of the `pytch.wait_seconds()` line altogether.  But to make
the game faster than that, you’ll need to think harder.

In the code at the moment, the speed of playing the pattern is set by
how long the sounds play for.  To cut the sound short, you might need
to do something like

``` python
self.start_sound("note-1")
pytch.wait_seconds(0.3)
pytch.stop_all_sounds()
```

instead of the simple `self.play_sound_until_done("note-1")`.

### Add a time limit (advanced)

Add a timer so that the player has to press the buttons quickly
enough.  If they don't press a button for more than, let’s say two
seconds, they lose.
