# Bunner: make a frogger-like game

In this tutorial we will make a complete [Frogger](https://en.wikipedia.org/wiki/Frogger)-style arcade game.

{{< run-finished-project >}}



--- 

## Making the stage

Let's start by getting a nice backdrop up. I've drawn one already, so we can just load the image.

First, we make a Stage class. We can call it anything we want so long as it is declared as being a Stage. The second line of the class sets up a Python variable with the list of background images that we can use (there's only one for now but we will add more).

Each background has a name that we'll use in our code when we want to switch backgrounds. We also have to list the file name from the Pytch examples folder that we want to use. 

{{< commit background-hollow-class >}}

Every Python object has to have an initialisation function. Pytch will use this to create the Stage as soon as the program is loaded (even before the Green Flag is clicked).

{{< commit add-stage-initialisation >}}

I've added two steps in this initialisation: the first activates the _standard_ Stage setup which lets Pytch link in the stage object. If you forget this line then the Stage won't work properly.

The second step selects a backdrop to show so that the canvas has something in it right away.

If you build the project now you'll notice that the stage backdrop does not actually appear. That's because there is one more thing we need to do in order to have the Stage hooked up to our project. We need to _register_ it with Pytch. We will have to do this for each new Sprite class as well, so that the Pytch project knows about them.

## Create our hero

There is not much to do in our game yet, so let's add something for the player to control. 

We want to talk about Sprites:

{{< commit import-Sprite >}}

The graphics are already there for the players sprite, all we have to do is create a class and set up the names of the costumes. Like the stage, the name of our new class is up to us, but we have to declare that it's a kind of ```Sprite```.

{{< commit simple-player-sprite >}}

Each costume has two numbers after it - these are the position of the _centre_ of the costume. The Bunny graphics are 60 pixels wide and 60 pixels tall, so that puts it right in the centre of the costume. When we issue a ```go_to_xy``` command it's that point on the costume that will be at exactly the ```x``` and ```y``` coordinates.

We select a costume and make sure that the Bunny actor is visible.


### Moving our hero

Now let's give the player a way to move the bunny around. We need to import the Pytch keyboard event.

{{< commit import-when-key-pressed >}}

Now we can create a function that will move the bunny up the screen, and tell Pytch to run that function whenever the up arrow key is pressed on the keyboard. We add a simple check of the bunny Y-coordinate to make sure that it is never moved off the top of the screen.

{{< commit move-bunny-up >}}

If you haven't already then this is a good place to build the project and make sure it's working. Press the up arrow a few times, make sure that you're happy it works.

Once you are comfortable with it, you could add three more functions for the other directions.  Remember, each function has to have it's own name or Python will not recognise them properly. 

This is my version:

{{< commit move-in-all-directions >}}

## Create the cars

{{< commit simple-car-sprite >}}

{{< commit import-green-flag >}}

{{< commit start-one-traffic-row >}}

{{< commit import-when-i-start-as-a-clone >}}

{{< commit begin-drive-routine >}}

{{< commit drive-to-the-right >}}

{{< commit add-speed-var >}}

{{< commit finish-car-clone >}}

{{< commit drive-to-the-left >}}

{{< commit start-traffic-two-and-three >}}

## Squish the bunny!

{{< commit check-for-squishing >}}

{{< commit special-hitbox-for-cars >}}

{{< commit use-new-hits-method >}}

{{< commit broadcast-squish >}}

{{< commit add-squish-costumes >}}

{{< commit import-when-i-receive >}}

{{< commit act-on-squish >}}

## Setting modes for the player

{{< commit add-first-bunny-modes >}}

{{< commit set-initial-mode-playing >}}

{{< commit guard-squishing-routine >}}

{{< commit dont-move-unless-playing >}}

## Adding a life counter

{{< commit remove-game-specific-setup-from-init >}}

{{< commit set-game-start-code >}}

{{< commit wait-at-the-start >}}

{{< commit restart-game-when-squished >}}

{{< commit add-notion-of-lives >}}

{{< commit set-three-lives >}}

{{< commit call-play-one-life >}}

{{< commit define-play-one-life >}}

{{< commit play-another-life-after-death >}}

## Letting the game end

{{< commit announce-game-over >}}

{{< commit game-over-deletes-clone-cars >}}

{{< commit add-global-running-flag >}}

{{< commit bunny-sets-game-running >}}

{{< commit game-over-unsets-running-flag >}}

{{< commit game-over-end-traffic1 >}}

{{< commit game-over-end-traffic2 >}}

{{< commit game-over-end-traffic3 >}}

{{< commit show-game-over-backdrop >}}

{{< commit add-game-over-background >}}

## The start button

{{< commit create-start-button >}}

{{< commit import-when-this-sprite-clicked >}}

{{< commit make-start-button-clickable >}}

{{< commit make-bunny-start-game-on-message >}}

{{< commit start-traffic-on-message1 >}}

{{< commit start-traffic-on-message2 >}}

{{< commit start-traffic-on-message3 >}}

## Keeping score

We should be showing the lives remaining, but before we get to that we can add another small but important feature.

{{< commit introduce-score-global >}}

{{< commit initialise-score >}}

{{< commit increment-the-score-every-time-we-move-up >}}

{{< commit introduce-current-row-counters >}}

{{< commit init-row-counters-at-start >}}

{{< commit increment-current-row-counter >}}

{{< commit only-score-if-new-row-record >}}

{{< commit lower-row-count-on-backstep >}}


## Showing score

{{< commit introduce-score1-class >}}

{{< commit compute-score-digit-costumes >}}

{{< commit display-digits-on-message1 >}}

{{< commit broadcast-score-change-message >}}

{{< commit create-score-2-class >}}

## More status displays

{{< commit introduce-life-display >}}

{{< commit update-life-counter >}}

## Adding the water hazard

{{< commit introduce-log-class >}}

{{< commit start-a-single-row >}}

{{< commit start-3-rows-of-logs >}}

{{< commit drive-log-along-row >}}

{{< commit check-bunny-alive-on-log >}}

{{< commit add-drowning-state >}}

{{< commit remove-logs-at-end-of-game >}}

{{< commit fuzzy-hit-detection-for-logs >}}

{{< commit add-drowning-costumes >}}

{{< commit regularly-scan-for-drowning >}}

{{< commit play-drowning-animation >}}

{{< commit lose-a-life-to-drowning >}}

{{< commit play-after-drowning >}}

## Finishing the level

{{< commit check-if-we-won >}}

{{< commit detect-final-row >}}

{{< commit new-dancing-state >}}

{{< commit start-another-round >}}
