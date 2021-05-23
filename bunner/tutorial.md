# Bunner: make a frogger-like game

In this tutorial we will make a complete
[Frogger](https://en.wikipedia.org/wiki/Frogger)-style arcade game.

{{< run-finished-project >}}

---

## Making the stage

Let's start by getting a nice backdrop up. I've drawn one already, so
we can just load the image.

Begin by making a class to represent the stage. We can call it
anything we want so long as it is declared as being a
`pytch.Stage`. The second line of the class sets up a Python variable
with the list of background images that we can use (there's only one
for now but we will add more).

Each background has a name that we'll use in our code when we want to
switch backgrounds. When we just give the filename of the image file
that we want to use Pytch will use that (without the `.png` extension)
as the name of the costume.  You can see these files by clicking the
*Images and sounds* tab, then click on the *Tutorial* tab to get back
here.

{{< commit background-hollow-class >}}

If you build the project now, you'll see our backdrop appear.

## Create our hero

There is not much to do in our game yet, so let's add something for
the player to control.

The graphics are already there for the player's sprite, all we have to
do is create a class and set up the names of the costumes. Like the
stage, the name of our new class is up to us, but we have to declare
that it's a kind of `pytch.Sprite`.

{{< commit Bunny-with-costumes >}}

When green flag is clicked, we select the starting costume, and make
sure that the Bunny actor is in the right place and visible:

{{< commit Bunny-green-flag-go-to-start >}}

If you build the project, you'll see that the Bunny appears in the
middle of the stage, and only goes to the correct place when you click
the green flag.  This is a bit messy, so we'll change this to tell
Pytch to start off *not* showing the Bunny:

{{< commit start-Bunny-not-shown >}}

### Moving our hero

Now let's give the player a way to move the bunny around.

We will create a function that will move the bunny up the screen, and
tell Pytch to run that function whenever the up arrow key is pressed
on the keyboard. We add a simple check of the bunny Y-coordinate to
make sure that it is never moved off the top of the screen.

{{< commit move-bunny-up >}}

If you haven't already then this is a good place to build the project
and make sure it's working. Press the up arrow a few times, and make
sure that you're happy it works.

Once you are comfortable with it, you could add three more functions
for the other directions.  Remember, each function has to have its own
name or Python will not recognise it properly.

This is my version:

{{< commit move-in-all-directions >}}

## Create the cars

The next step is to create some obstacles to make it harder to reach
the top of the screen. Our first obstacles are the cars that will
travel left and right in three lanes of traffic that the bunny will
have to cross. There is room for three lanes in the background, but
we'll design our solution so that we could easily add more lanes of
traffic if we want.

So that there is some variety in how they look I have chosen two
different images for each car, each of which could be driving left or
right. Later on we will select at random the between the two different
versions of cars driving to the left (or right, depending on the lane)
for each car.

The file names for these graphics don't describe which direction they
show the cars facing so I have told Pytch I'd like to use my own
labels for the costumes (`left0`, `right0` and so on) instead of using
the file name.

{{< commit Car-with-costumes >}}

The original car is going to remain hidden, because we'll use *clones*
for the actual traffic. If a Sprite has a `start_shown` variable Pytch
will use it to decide if the sprite is visible immediately or not.

{{< commit Car-start-not-shown >}}

### Designing the traffic

For the next section of code I want to select the different costumes
at random so that there is some variety. Python has some random
number code available, we just need to import it so that it's
available

{{< commit import-random-module >}}

My plan is to use the original `Car` sprite as a template. Every time I want to add a new car to a lane of traffic I'll move the hidden Car sprite to the starting position for that lane and then make a clone. The clone will then show itself and drive across the screen.

The original `Car` sprite will have three scripts running, one for each lane, that will act as a kind of car factory, adding new cars with a bit of randomness to keep the gaps between the cars unpredictable.

### Making the first car factory script

I'll start with the lane closest to the bottom of the screen. Once we have this working we will be able to copy it to get the other lanes working.

As soon as the green flag is clicked the Car sprite starts a loop to manage the cars in the first lane of traffic. There's no need to have the loop running as fast as possible — that would make far too many cars — so I put in a little delay using `wait_seconds` so that the loop only runs ten times a second.

Each time the loop goes around I ask for a random number between 0 and 1, and if it's below 0.2 then the Car sprite moves to just off the screen, left of the first lane, and makes a clone at this position.

Because we might create another car in this lane the next time around we wait a little longer after creating the clone so that it has time to drive along the lane.

{{< commit start-one-traffic-row >}}

### Controlling the clone

We want the clone to run its own script when it's created, so we will use the `when_I_start_as_a_clone` event.  I will build up the loop that drives the car from left-to-right along the lane. First, I want the clone to choose a costume, either 'right0' or 'right1' (they are two different colours of cars, and it keeps the lane of traffic from looking too boring if there's a mix of costumes).

Python has a handy `random.choice` function will return one of the items from the list we give it, randomly chosen.

The clone got its own copy of the `direction` variable containing whatever the Car sprite had in it at the moment the clone was created. It contains the string 'right', so combining that with either '0' or '1' gets us one of the costume names.  Also, the images are a bit big, so I'll shrink the clone to 65% of its original size.

{{< commit begin-drive-routine >}}

Once the sprite has appeared we start a loop that drives the car to the right.

You might wonder why I'm are checking the 'direction' variable, since it has to contain 'right'. The answer is that if we get this code correct for moving right we'll be able to use it for the left-moving lane as well.

In order to allow us to tweak how fast the lane of traffic moves I'll use a variable to change how much it moves. That way if I wanted to speed it up later on I can just change what's stored in the variable.

{{< commit drive-to-the-right >}}

The speed variable needs to be set up somewhere, which I do at the start of the `startTrafficRowOne` method.

{{< commit add-speed-var >}}

Once the car has moved far enough to be off the right-hand side of the screen I hide it and then delete the clone. Deleting the clone keeps things tidy and means there are not lots of useless clones lying around just off the stage edge.

{{< commit finish-car-clone >}}

Now, back to my idea of using the same code to control cars in the left-hand lane. If the direction is not 'right' then I suppose it must be 'left'. Those cars just move a _negative_ amount (and have moved far enough once their `x`-coordinate has moved off the left edge of the stage)

{{< commit drive-to-the-left >}}

### Making the rest of the car factories

Once we have that we can add two more loops that start on green flag. They are modelled on the loop that creates `Car` clones for lane 1, but they move to different x and y positions before cloning the car.  I'll set the lanes of traffic to all move at the same speed for now.

{{< commit start-traffic-two-and-three >}}

There's an important point to think about here. What if the row two loop moved the car, but before it got to set the `direction` or create the clone the row one loop ran a bit and altered the x and y position? We could end up with a car that was positioned off to the left of the screen, but which had its direction set to drive to the left, and it would just vanish right away!

In fact, this can't happen, but it's worth knowing why. Pytch will only allow another function to run at specific places. One of those places is at the end of a loop (another is when a function does `wait_seconds`). The manual has more information about this, but it's enough for now to know we are safe!

## Squish the bunny!

You'll notice that the cars don't actually present any sort of challenge at the moment, because the bunny can just hop through the lanes without being touched.

### Checking for collisions

Checking every time something moves will mean changes in lots of places in the code — I'd need to check when cars move _and_ when the bunny moves. Instead I'll create a new script that runs in each `Car` clone constantly checking for collisions. Writing `while True` means the loop will run forever (actually, just until the clone is deleted when it reaches the end of the lane).

I'll decide later what to actually do when there is a collision. So I can test my code I'll print out a message whenever there is a collision.  To see these messages, click on the *Output* tab.  You can come back to this tutorial by clicking on the *Tutorial* tab.

{{< commit check-for-squishing >}}

As soon as I test this I find there is a problem (try it out now). The car reports it's squishing a bunny when it drives past the bunny, even if it's not in the lane? What's going on?

The answer is in our costumes. The very nice costumes we're using (courtesy of the [Code The Classics](https://wireframe.raspberrypi.org/books/code-the-classics1) book) are actually bigger than they look. Pytch checks for 'touching' by checking whether rectangles drawn around the entire costume of each sprite overlap. The `Car` costume and the `Bunny` costume overlap when the bunny is _next_ to the lane (you can see that the car costumes have some shadows under them that stick out into the lane below. It looks nice but it messes up how `touching` works).

The easiest thing to do is write a special bit of code to check whether a clone is hitting another sprite. If we check that the `y` coordinates are close together (say, within 10 pixels) and the `x` coordinates are within 40 then it works pretty well.

This function works by comparing the coordinates of the clone (`self`) and some other sprite that we provide as input.

{{< commit special-hitbox-for-cars >}}

When Pytch sees me say `touching(Bunny)` it interprets it as "if this sprite is touching _any_ Bunny sprite", original _or_ clone.

In order to use this in place of `touching` we can't pass `Bunny`, because that's a sprite _class_. We need to supply the _instance_. The Pytch `the_original` function lets us get the sprite from a sprite class. (There is another function to get a list of all the clones, which we will see later.)

{{< commit use-new-hits-method >}}

This works much better at printing messages for the bunny and car colliding, when I try it out I only see the "Squish the bunny!" message printed when the sprites actually _look_ like they are overlapping now.

Now that this is working I'd like to get the bunny to react to being squished. This is really something for the `Bunny` sprite to take care of. I can send a message that something has happened using the `broadcast` system.

{{< commit broadcast-squish >}}

### Responding to being squished

Back in the `Bunny` sprite I want to add some costumes to show when the bunny gets driven on. I'm making sure the names of these match up with the names of the "main" costumes so that I can easily pick the right one to show.

{{< commit add-squish-costumes >}}

To respond to a broadcast, a Sprite uses `when_I_receive`.  When the bunny sprite sees the squishing broadcast I want to change to a costume that matches the direction that the bunny was already facing. I can look up the name of the current costume and then add "_squished" to get the name of a new costume.

{{< commit act-on-squish >}}

There's still a problem, though. The car clone broadcasts 'squish bunny' and we change costume... but then a moment later the car sprite runs its hit checking again and broadcasts squish _again_, and we run through this code again (choosing a costume like `"up_squished_squished"`). That's a problem!  If you try it, and get squished, you'll see an error pop up in the *Errors* tab.  You can come back to this tutorial by clicking on the *Tutorial* tab.

To fix it I'll introduce a way for the bunny to know that it has already acted on the message (I'll have other uses for this idea soon).

## Setting modes for the player

I'll create a set of three variables to describe three "states" the bunny could be in:

* Waiting for the game to start
* Letting the player control it
* Sitting squished on the road

I just want these variables so that I have three _names_ I can use for these states, because it'll make my program easier to read. A neat Python trick to set up a set of variables so that they have different values looks like this:

{{< commit add-first-bunny-modes >}}

This sets `WAITING` to be zero, `PLAYING` to be 1, and so on.

Later on I plan to add a title screen (and the bunny will start out waiting), but for now the bunny starts out playing.

{{< commit set-initial-mode-playing >}}

Now I can set up the squishing code so that the bunny won't squish _again_ if it's already showing as squished.

{{< commit guard-squishing-routine >}}

You might not have tried this, but if you press the arrow keys when the bunny is squished on the road the moving functions still run (of course they do, we didn't do anything to switch them off). That's not great!

Now that the bunny knows when it's supposed to be letting the player play and when it's supposed to be squished, we can add a check to each of the moving routines to skip through them if the bunny isn't supposed to move.

{{< commit dont-move-unless-playing >}}

Once we have done that the game seems to be over once the bunny is squished. The next step is to give the player a number of lives and let the game end and restart.

## End and restart the game when the bunny is squished

I'm going to rearrange the code in the Bunny sprite so that it will be easier to reset the game when the player loses all their lives. The first step is to split out the things that we want to do at the start of the game from the things that we do every time we play one life. Right now they are all mixed together in `go_to_starting_position` and it runs when the green flag is clicked.

So I'll make a new function that has the stuff we want to run at the start of each game.

{{< commit set-game-start-code >}}

I will switch the bunny from visible to invisible when the project first loads (this is paving the way for a splash screen at the start)

{{< commit remove-game-specific-setup-from-init >}}

Now I have a use for the `WAITING` mode we created recently. Before the game actually begins the bunny is neither squished nor playing.

{{< commit wait-at-the-start >}}

Now I can add a use of this setup function to the code that handled the bunny being squished. We pause for a while to let the player see the costume of the squished bunny, and then reset the game.

{{< commit restart-game-when-squished >}}

The `start_game` function is run by Pytch when the green flag is clicked, but I can run it whenever I want by using its name.

It doesn't affect what I'm doing here, but it's worth pointing out the difference between running `start_game` from the green flag event and running it by using its name. The second way doesn't run `start_game`  alongside `squish`, so if there was another statement in `squish` it wouldn't run until `start_game` had finished.

## Adding a life counter

Restarting the game after the bunny has been squished once is a bit unfair, it would be better to give the player a few attempts (say, the traditional three lives).

At the start of the game I'll set a new variable in the bunny sprite

{{< commit set-three-lives >}}

In the initialization for the bunny I'll set this to a number that suggests the game hasn't started yet (it'll be set to something else when the bunny is ready to play).

{{< commit add-notion-of-lives >}}

Each time the bunny gets squished I'll reduce that counter by one.

Moving some code around again, I want to separate the idea of _starting the game_ from the idea of _playing a life_. So I'll create a new function that has the code relevant to playing a life (moving back to the start row and selecting a costume).

{{< commit define-play-one-life >}}

I can run this function in the `start_game` routine

{{< commit call-play-one-life >}}

And I can also call it when the bunny is squished:

{{< commit play-another-life-after-death >}}

## Running out of lives

The next thing I want to do is end the game when the player has used up all their lives. That means that after the player is asked to play a life I'll check whether it's actually possible to do that. If there aren't then the bunny will go into its "waiting" state until a new game starts, and we'll announce to all the other sprites and clones that the game has ended.

{{< commit announce-game-over >}}

When the clone cars see that the game has ended I want them all to vanish (even if they haven't reached the edge of the canvas yet). When a clone is deleted all of its running scripts stop, of course.

{{< commit game-over-deletes-clone-cars >}}

The original `Car` sprite is still running its traffic factory scripts, of course, and they will just create more cars unless they are stopped.

Although the original `Car` sprite will receive the game over broadcast and run the `vanish` script that won't stop the car factories. The original sprite is immune to `delete_this_clone` actions (because it's not a clone!). So I'll have to do something else to stop those scripts.

One way to handle this would be to change the loop in those factory scripts so that instead of running forever they only ran as long as the game was playing. Something like this:

{{< commit game-over-end-traffic1 >}}

To make this work I add a new global variable. I could try to use the bunny state for this, but the question of whether the bunny can be moved is different to whether the game is playing or not so I decided to track them separately.

{{< commit add-global-running-flag >}}

The bunny notes that the game is running by setting this variable to `True`.

{{< commit bunny-sets-game-running >}}

When the bunny runs out of lives it notes that the game should be over by setting this variable to false (I could have chosen to set this to false in a function that is run when the "game over" broadcast is received, that would work too)

{{< commit game-over-unsets-running-flag >}}

Now I can make the same changes I made to the first factory script to the other two:

{{< commit game-over-end-traffic2 >}}

{{< commit game-over-end-traffic3 >}}

Once all of the treaffic has been stopped and the clones have vanished I decided to add a new backdrop with a game over message and switch to showing that.

{{< commit show-game-over-backdrop >}}

{{< commit add-game-over-background >}}

## The start button

When the game is over I would like a way to start it again. This is where the rearranging of code I did earlier on will pay off.

First I make a new sprite that will act as a 'start game' button

{{< commit create-start-button >}}

I want it to react to being clicked with the mouse.  When it's clicked it announces to the rest of the project that it's time to start a new game, then the button hides itself.

{{< commit make-start-button-clickable >}}

The bunny should start a new game when this message is received, not when the green flag is clicked

{{< commit make-bunny-start-game-on-message >}}

The traffic factories should also begin making cars when the game starts, not when the green flag is clicked.

{{< commit start-traffic-on-message1 >}}

{{< commit start-traffic-on-message2 >}}

{{< commit start-traffic-on-message3 >}}

When the game starts the stage needs to switch to the world costume (it might have been showing the 'game over' screen)

{{< commit show-world-on-game-start >}}

Now we have a whole game that can be started by the player, runs through the player's 3 lives, ends, and can be started again!

## Keeping score

We should be showing the lives remaining somewhere on the stage, but before we get to that we can add another small but important feature.

Most games are more fun if there's a way to keep track of how well the player is doing. I'm going to introduce a score that increases as the player heads up the screen.

First I'll add a new global variable to track the score (I'm using a global variable because there are going to be several parts of the project that will access the score, but I could have made it a variable in the Bunny sprite and used `Bunny.the_original` to access it from other parts of the project)

{{< commit introduce-score-global >}}

The score starts at zero at the start of the game

{{< commit initialise-score >}}

We could let the player earn a point every time they manage to move up the stage towards the goal at the top:

{{< commit increment-the-score-every-time-we-move-up >}}

The problem with this is that if the player just taps 'up' then 'down' then 'up' they get two points. They could run up a very high score just hopping from the start onto the first row of traffic and then back down again and never really making any progress.

So I decided that I would change it so that they only earn a point if they are making progress up the stage. I created a variable to keep track of how high up the stage the bunny is, and another to count the highest row the bunny has reached.

{{< commit introduce-current-row-counters >}}

These both start at zero:

{{< commit init-row-counters-at-start >}}

Every time the bunny moves up the stage I add one to the current row

{{< commit increment-current-row-counter >}}

And lower it when the bunny moves down

{{< commit lower-row-count-on-backstep >}}

Every time we move up I check if this is a new 'highest ever reached' row. If it is then the player gets a point (but I also remember that the highest rows reached has gone up, so the player has to go even further up the stage to get another point).

{{< commit only-score-if-new-row-record >}}

Now we have a way to count score, it would be nice to display it on the stage instead of just printing it.

## Showing score

To show the score I'm going to create two new sprites that will be used to show the digits of the score (I'll only track scores up to 99)

{{< commit introduce-score1-class >}}

There are ten costumes, which I want to name "digit-0" to "digit-9". Instead of typing each of the ten costumes out by hand I decided to use a Python shortcut for making lists with this kind of pattern. There are two parts to this:

The first is writing a `range` statement inside the list definition, for example `[ n for n in range(10) ]` creates the list `[0,2,3,4,5,6,7,8,9]` (`n` in this is just a temporary variable that is created for setting up the list only).

The second trick is that we can fill in "placeholders" in a string using Python's special "f-strings" (formatted string literals). The basic idea of these is that you write a string that mentions some variables in it, within curly braces and Python will fill in the value of the variable.

For example, if you write `f"digit-{n}"` when the variable `n` has the number `3` in it then the final string would be `"digit-3"`. The `f` in front of the first double-quote is what tells Python that it should look for variables marked by curly braces inside the string.

We can combine this with a range loop to get several strings that follow some pattern.

{{< commit compute-score-digit-costumes >}}

When the score changes I'll get the bunny sprite to send out a broadcast message. When this score sprite receives that it will look up the score, calculate the _first digit_ of the score, and set the costume to the corresponding digit. I use the f-string trick in this to select the right costume name based on the "tens" value of the score.

{{< commit display-digits-on-message1 >}}

I get the bunny to announce score changes using a broadcast:

{{< commit broadcast-score-change-message >}}

To show the 'tens' digit of the score I make a second sprite that's almost identical. The only differences are where on the screen it appears, and the calculation done in `show_correct_digit`, where I use the `//` operator (which divides a number and throws away any decimal part).

Notice in this class that I was able to re-use the `score_costumes` variable.

{{< commit create-score-2-class >}}

## More status displays

Now that we have a way to show some digits we could also use this to show the number of lives remaining. A third sprite that has the same costumes and which updates whenever the lives change can do this:

{{< commit introduce-life-display >}}

I also add a 'lives changed' broadcast to tell this when to update.

{{< commit update-life-counter >}}

Why not just update this when we see the 'bunny squished' message, which is what causes the lives to change? Because the very next thing in this tutorial is to add a new way for the bunny to lose a life!

## Adding the water hazard

The final obstacle to add to the game is the water hazard. At the moment once the bunny has passed the three lanes of traffic all it has to do is make its way to the top of the screen to reach the goal.

I'm going to add a new check that makes the bunny drown (and lose a life) if it's on the water. But first I want to add some way to get across the water!

Based on the same design as the `Car` sprite, I make a `Log` sprite:

{{< commit introduce-log-class >}}

I could copy the `Car` factory approach exactly, but I want to show how to reduce the amount of code a little. So I create a function for a "log factory" that takes the direction and the y-coordinate of the lane. This is the factory:

{{< commit start-a-single-row >}}

Then I start three separate factory scripts, each providing different inputs to the factory. This will get me three different factory scripts running, all based on the same `start_row` code:

{{< commit start-3-rows-of-logs >}}

Each `Log` clone drives along the lane just as the cars do. But instead of checking to see if they have "squished" a bunny they check to see if the bunny is standing on the clone. If it is then the bunny is carried along with the log.

{{< commit drive-log-along-row >}}

Just as with the `Car` we will remove the clone logs when the game ends

{{< commit remove-logs-at-end-of-game >}}

And just like the `Car` we need to have a special collision detection function (otherwise the slightly-too-large sprite costumes will detect collisions at times that don't really look good to the player)

{{< commit fuzzy-hit-detection-for-logs >}}

### Drowning in the water

Now we are ready to make the water hazardous. I'll add a new stage for the bunny. Just like when the bunny is squished, I don't want the movement keys to work while the bunny is drowning.

{{< commit add-drowning-state >}}

There is a set of seven costumes showing different frames of a splash. I want to add all of them. To avoid having to write out the names of them all I use the same trick I used in making the digit costumes, and then add that list of new costumes onto the end of the bunny's costume list:

{{< commit add-drowning-costumes >}}

When the game is running the bunny will regularly scan to see if it's in the water section of the canvas (that's checked using the `y` coordinate). If it is then unless it's touching one of the `Log` clones it starts drowning.


{{< commit regularly-scan-for-drowning >}}

Now, there are two things to fix here. The first is easy, we need to make sure that we run this and `start_playing` in the correct order. They both run when a `start playing` message is received, but we can't be sure which of them runs first, and if `watch_for_water` were to run first then `start_playing` would not have had a chance to set `game_running` yet and so the loop in `watch_for_water` would end and the bunny wouldn't be checking if it should drown. We can fix that easily, because we made sure that  `start_playing` sets `game_running` before it sets the mode. So we just do an extra loop that will stall for a while if `start_playing` hasn't set things up yet.

{{< commit wait-until-game-really-starts >}}

This code is not quite right, because I'm using the `touching` routine and as we know it's possible for the bunny to be on a row below or above a log and stil register as touching it. We really want to use the custom `hits` routine. I'm going to make a custom version of the `touching` routine that solves this. The plan is to get a list containing all the clones, and then check them one-by-one to see if the the bunny is touching them.

This uses `all_clones`, the counterpart to the `the_original` function we used back when we wanted to access the Bunny sprite. I use the Python `for` loop to check each one in turn, using my `hits` function. If `hits` ever returns `True` to say that that particular log has hit the bunny then I return from the `touching_any_log` function immediately. I can't return `False` until I have checked _every_ log, of course, because even if the first log we check returns `False` for the hit checking one we check later in the list might still return `True`.

{{< commit make-custom-check-all-hits-function >}}

Now in the original `watch_for_water` function I can replace the built-in `touching` with a call to my custom `touching_any_log`.

{{< commit check-bunny-touching-log-clone >}}

There's one final tweak to this hit check, though. When we were talking about the traffic started I said that we didn't have to worry about two pieces of code that were running at the same time interfering, because they would only give way to each other at specific places, like at the end of a loop.

This is a problem for us now — in `touching_any_log` it could happen that the code checks the first couple of logs in the list, and then the code that moves the first log gets to run and moves the log a bit so that it's under the bunny. Then `touching_any_log` gets to run some more, but it has already moved past that first log in it's checking. The result would be that our hit check says the bunny isn't touching a log (so we decide the bunny is drowning), but to the player it looks like the bunny was under the log.

This can't normally happen because the built in Pytch `touching` function doesn't let anything else run while it's checking to see if you touch anything. We can tell Pytch that we want it to treat our function the same way. We can add a special kind of "hat block" to a function that orders this (you can have this along with a normal hat block, just list one after the other).

Pytch will still let other code run if this function takes too long about getting through its loops (about a second, by default). That will be just fine for us.

{{< commit non-yielding-hit-check-loop >}}


Once we have determined that the bunny is drowning we play the frames of the 'splash' animation one after the other:

{{< commit play-drowning-animation >}}

We pause for a moment to let the player gather themselves:

{{< commit lose-a-life-to-drowning >}}

and play another life

{{< commit play-after-drowning >}}

Finally, if you try this you might find that while the animation is playing a log comes along and seems to "push" the splash animation along. That's because the log is pushing the bunny sprite with it! I  add a simple check to the code that handles this so that the bunny is only moved if it is really sitting on the log, and not if it's already under water.

{{< commit check-bunny-alive-on-log >}}


## Finishing the level

The final part of the game is to give the player a reward for reaching the goal at the top of the screen. Every time we move up to a new highest row I'll check to see whether that was the top of the screen

{{< commit check-if-we-won >}}

If it is then I run a loop that moves the bunny through facing its four directions (so that it looks like it's dancing).

{{< commit detect-final-row >}}

I added a new `DANCING` mode as well so that the bunny isn't `PLAYING` (I don't want the player to be able to move the bunny during the victory dance and it felt wrong to pretend the bunny was in a `SQUISHED` or `WAITING` mode )

{{< commit new-dancing-state >}}

Once the dance is complete the bunny moves back to the bottom of the stage and the level starts again.

{{< commit start-another-round >}}


## Challenges

You have reached the end of this tutorial, but there's lots more that you could do with this project. Here are some ideas:

* Make the game more challenging for the player. Add a broadcast that goes out when the player reaches the goal. This broadcast could tell the logs and cars that this was a new round, and use that to have them move faster, or have more cars and fewer logs appear by adjusting the numbers in the car and log factories.

* Improve the accuracy of the `hits` routines (the log one, especially, is a bit over-sensitive, it's easy for the bunny to fall off the smaller logs without it looking like it should have)

* Add some different types of obstacles (longer cars, using a lorry costume, for example)

* Vary the speed of the logs and cars in different lanes (you probably don't want to vary the speed within a lane unless you can account for the possibility of cars or logs hitting each other!)

* It's easy to dodge over the road at the start of the game because all the cars drive in from the edges but the bunny starts in the middle. Have the car factories create some cars in the middle of the road at the start of the game so that there isn't a time when the roads are totally clear.

* At the moment the bunny sprite is drawn so that it appears _under_ a car when it's squished, but on top of the logs when it jumps onto them. But we didn't do anything special to make that happen, it's just how it worked out, and you might have noticed that it looks wrong if the we're drawing the bunny drowning animation and a log passes over it (the "splash" animation draws on top of the log!). You can fix this by using the Pytch _layers_ to move the bunny under and over other sprites as needed (use `self.move_to_front_layer()` and `self.move_to_back_layer()`). Fix this drawing problem by moving the bunny back and forward through the layers.
