# Gardening
For this tutorial, we will attempt to make a gardening simulation. 
To do that, we will write a script that will randomly place flower seeds at the start of the game,
a grid-based movement system that the player can use to select different tiles of soil, 
a water bucket for collecting water and watering soil and water sources.
We will also add animations to highlight the growing of plants, water levels and a moving gardener character.


---


## Use a nicer background

If you click the green flag button now, you will see that nothing interesting will happen. To change, we will start by
adding a more interesting background.

### Add garden backgrounds

{{< learner-task >}}

Add a more interesting background for your garden simulation game. In the media library there are two images called garden.png and tall_garden.png that you can choose.

{{< learner-task-help >}}

{{< jr-commit add-garden-backgrounds add-medialib-appearances-entry ["garden.png"] >}}

{{< /learner-task >}}


### Remove default background

If you try pressing the green flag now, you will see that, still, nothing has changed. 
That is because the stage only shows the first background by default. One way to solve this is to
manually delete the old background.

{{< learner-task >}}

Delete the `solid-white.png` backdrop from the Stage.

{{< learner-task-help >}}

{{< jr-commit remove-default-background delete-appearance [] >}}

{{< /learner-task >}}

## Spawn flower seeds

### Add soil sprite

Now, you need a _sprite_ to use as the soil on which the player can grow plants.

{{< learner-task >}}

Add a new sprite called `Soil` to your project.

{{< learner-task-help >}}

{{< jr-commit add-soil-sprite add-sprite [] >}}

{{< /learner-task >}}

### Add soil costumes

Next, your new `Soil` sprite needs some costumes to decide what it should look like when you run the project.   

{{< learner-task >}}

From the media library, add the "Garden plants" bundle of images as costumes for your `Soil` sprite.

{{< learner-task-help >}}

{{< jr-commit add-soil-costumes add-medialib-appearances-entry ["TODO-ENTRY-NAME"] >}}

{{< /learner-task >}}

Now, when you run your project, the `Soil` sprite should be included in your simulation.

{{< learner-task >}}

Try running the project again! Click the green flag button and see if anything has changed in your project.

**What is different?**

{{< learner-task-help >}}

You should now see a tree seedling in the center of your garden.

{{< /learner-task >}}

## Place multiple plant seeds

When we start our simulation, we want different types of flower seeds to be in our garden so that they can grow into 
different flowers.
On top off that, we also want the placement of the flower seeds to be different every time we run the project.
To do that, we can start by creating clones from our `Soil` sprite and then placing them next to each other in a row on the stage.

{{< learner-task >}}

Add a new script to the `Soil` sprite which runs when you click on the green button.

{{< learner-task-help >}}

{{< jr-commit create-empty-soil-spawn-script add-script [] >}}

{{< /learner-task >}}


Next, we need to write a line of code that allows to store where on the stage we want our clones to be placed.
To do that, we will define a variable called `Stage.soil_locations`and set it to an list. Lists are used to contain
multiple numbers, strings or other types of data inside one variable.
Our variable will only need to store the numbers `-2`, `-1`, `0`, `1`, and `2` to show five clones in a row.


{{< learner-task >}}

Add a line of code to the `Soil` script which sets the `Stage.soil_locations` variable to a list which has the values 
`-2`, `-1`, `0`, `1`, and `2`. 

{{< learner-task-help >}}

{{< jr-commit define-soil-locations-variable edit-script [] >}}

{{< /learner-task >}}

Next, we want to create a clone of the `Soil`sprite for all five numbers in our `Stage.soil_locations` variable. 
We can use a for-loop in this case, because it will allow us to use same line of code five times.

{{< learner-task >}}

Add two lines of code that will create five clone of the `soil` sprite, one for every number in `Stage.soil_locations`.

{{< learner-task-help >}}

One line of code is needed to create a clone of your sprite. 
Another line of code is needed above that one to repeat the cloning four more times. 

{{< learner-task-help >}}

Look in the Scratch/Python help to see which lines of code you can use to repeat a code block, 
get the length of a list and clone a sprite. 

{{< learner-task-help >}}

{{< jr-commit add-soil-clone-loop edit-script [] >}}

{{< /learner-task >}}

If you run the project now, you will see that nothing has changed yet. 
That is, because we still need to give our clones a unique location.


### Set soil locations

After we create our `Soil` clones, we want to calculate a unique x-position for them based on the values in our `Stage.soil_locations` variable. 
This way, every tile of soil will be displayed in a different location in our garden.

Since the images we are using for the `Soil` sprite all have a width of 48 pixels, 
we need to make sure that there are at least 48 pixels of space between the x-positions of our clones.
To compute unique x-positions for all the clones, we can use a different value from our `Stage.soil_locations` 
list for each clone.

{{< learner-task >}}

Add a variable `soil_xpos` inside of the for-loop which calculates a unique x-position for every clone using the
values inside of the `Stage.soil_locations` list.

{{< learner-task-help >}}

To get a different elements from a list you need to use an index. 
You can find out how to use an index in the Python/Scratch help section.

{{< learner-task-help >}}

A formula you can use to calculate a different x-position for every clone is: 

48 * a number in `Stage.soil_locations` 

(for example, 48 * -2, 48 * -1, 48 * 0, ...).

{{< learner-task-help >}}

{{< jr-commit compute-soil-x-position edit-script [] >}}

{{< /learner-task >}}

Now that we have our unique x-positions stored in `soil_xpos`, we can apply them to our `Soil` sprite before cloning it.

{{< learner-task >}}

Add a line of code inside the for-loop which will set the x-position of our `Soil` sprite to `soil-xpos` and its 
y-position to the number `0`.  

{{< learner-task-help >}}

Look in the help area to see which Pytch method will do exactly this.

{{< learner-task-help >}}

{{< jr-commit set-soil-position edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Run your project with the green flag button. 

What is different? 

{{< learner-task-help >}}

There are now five different tree seedlings on the stage.

{{< /learner-task >}}


## Randomly select a flower seed

Now that we have five different soil clones visible on the stage, we can start to randomly change how each clone starts
in the simulation. To do that, we can use a randomly generated number change the costume of our sprite right before 
we clone it to look like either daisy seeds, rose seeds or an empty piece of soil. 
This way, everytime we run our project, each `Soil` clone has a chance to start with one of these three costumes.  

{{< learner-task >}}

Add a new variable called `rng` which will store a randomly generated number between `0` and `100` as its value. 

{{< learner-task-help >}}

Python has a library called `random` which has very useful methods for this task. You can find example for how to use 
them in the Python/Scratch help.

{{< learner-task-help >}}

{{< jr-commit generate-random-number edit-script [] >}}

{{< /learner-task >}}

To choose a seed with our random number, we now need to add conditions to our script which check the value of our `rng` 
variable against possible numbers. Depending on which numbers we use here, we can change the odds of a certain costume
being chosen.

{{< learner-task >}}

Check whether the value in `rng` is within a certain range, for example, between `0` and `24`. 
If it is, then switch the soil's costume to `rose_seed.png`. 

Otherwise, check if `rng` is in a different range,
for instance, between `25` and `49`. In that case, switch the costume `daisy_seed.png`. 

If `rng` is outside of both of these ranges, switch the soil's costume to `empty.png`.    

{{< learner-task-help >}}

{{< jr-commit choose-flower-seed edit-script [] >}}

{{< /learner-task >}}

### Hide the original `Soil` sprite

We still need to hide the original soil, which we used to generate our five clones, since for this tutorial,
we only need the soil's clones.

{{< learner-task >}}

Add a line of code at the end of the script which will hide the original `Soil` sprite.

{{< learner-task-help >}}

{{< jr-commit hide-original-soil edit-script [] >}}

{{< /learner-task >}}

## Add movement

To add some interactivity, we want our player to be able to hover over and eventually water the plants in our garden.
Before we can do that, however, we need to add a sprite that will control our movement within the row we soil tiles. 

{{< learner-task >}}

Add a new sprite called `hover` to the project.

{{< learner-task-help >}}

{{< jr-commit add-hover-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

From the media library, add the image "hover.png" as a costume for your `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit add-hover-costumes add-medialib-appearance ["TODO-DISPLAY-IDENTIFIER"] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the `Hover` sprite which runs when you click on the green button.

{{< learner-task-help >}}

{{< jr-commit create-empty-stage-green-flag-script add-script [] >}}

{{< /learner-task >}}

To track our player's movement, we need to define variable which stores which column we are currently hovering over.

{{< learner-task >}}

Add a new variable called `Stage.current_column` and set it to `0`.

{{< learner-task-help >}}

{{< jr-commit define-current-column-variable edit-script [] >}}

{{< /learner-task >}}

Next, we want to define a script that will be triggered everytime we want the player to move and update the x- and 
y-positions of our `Hover` sprite accordingly.

{{< learner-task >}}

Add a new script to the `Hover` sprite that will be run everytime the message "move" is broadcasted.

{{< learner-task-help >}}

{{< jr-commit create-hover-move-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Inside of the new script, move the `Hover` sprite based on the value in `Stage.current_column`.

{{< learner-task-help >}}

{{< jr-commit move-hover-to-current-column edit-script [] >}}

{{< /learner-task >}}

### Add keyboard controls

We want to be able to update the position of the `Hover` sprite every time we press the left or right arrow key.

{{< learner-task >}}

Add a new script that will be triggered when the left arrow key is pressed. 

{{< learner-task-help >}}

{{< jr-commit create-arrow-left-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code to the new script which reduces the current column by `1`.

{{< learner-task-help >}}

{{< jr-commit update-current-column-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new line below which broadcasts the "move" message to update the x- and y-position of the `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit broadcast-move-left edit-script [] >}}

{{< /learner-task >}}

We can now repeat the previous steps for the right arrow key. 

{{< learner-task >}}

Add a new script which will be called whenever the right arrow key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-arrow-right-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Update the `Stage.current_column` variable and broadcast the "move" message whenever the right arrow key is pressed.

{{< learner-task-help >}}

{{< jr-commit update-current-column-and-broadcast-move-right edit-script [] >}}

{{< /learner-task >}}

## Add invisible walls

While our player can now move horizontally, we still need to make sure that they won't move out of the boundaries of the stage.
We can use two new variables to specify the left and right boundary of our garden and check against those before moving.

{{< learner-task >}}

Add to new variables called `Stage.MAX_COLUMN` and `Stage.MIN_COLUMN`
 and set them to sensible values. For this tutorial we would suggest using the values `3` and `-3` respectively.

{{< learner-task-help >}}

{{< jr-commit define-max-and-min-column edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a condition such to the "when left arrow key pressed" script so that the `Stage.current_column` variable is only 
updated when we are not outside of the boundary defined by `Stage.MIN_COLUMN`.

{{< learner-task-help >}}

`Stage.current_column` should only be reduced if it is larger than the minimum value we want for it.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-min-column-arrow-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a condition such to the "when right arrow key pressed" script so that the `Stage.current_column` variable is only
updated when we are not outside of the boundary defined by `Stage.MAX_COLUMN`.

{{< learner-task-help >}}

`Stage.current_column` should only be increased if it is smaller than the maximum value we want for it.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-max-column-arrow-right edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again. Has anything changed?

{{< learner-task-help >}}

You can now no longer move out of frame.

{{< /learner-task >}}

## Add water bucket

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit show-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-arrow-up-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit decrement-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-arrow-up edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit broadcast-water_soil-arrow-up edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-water_soil-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit flower-create-condition-for-touching-hover edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-condition-for-seed-costume-check edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit switch-to-next-flower-costume edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit wait edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit repeat-flower-costume-change-and-wait edit-script [] >}}

{{< /learner-task >}}

## Add water source

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-water-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-water-costumes add-medialib-appearances-entry ["TODO-ENTRY-NAME"] >}}

{{< /learner-task >}}


### Spawn water

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-spawn-water-green-flag-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-water-clone-loop edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-water-locations-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-and-implement-water-clone-loop edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit hide-original-water edit-script [] >}}

{{< /learner-task >}}

## Animate water

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-arrow-down-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-for-current_column edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit broadcast-get_water edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-get_water-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit reset-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit water-create-condition-for-touching-hover edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit animate-water-refill edit-script [] >}}

{{< /learner-task >}}

## Spawn trees

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-tree-location-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-condition-for-tree_location-variable-check edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit switch-soil-costume-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}

## Grow trees

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-to-check-for-tree_seedling edit-script [] >}}

{{< /learner-task >}}

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit animate-tree-growing edit-script [] >}}

{{< /learner-task >}}


## Shake down apples

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-and-show-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-space-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-for-tree_with_fruits-and-touching edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit increment-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit animate-tree-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}


## Plant trees


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-p-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-for-apples-variable-and-touching edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit decrement-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit switch-soil-costume-to-tree_seedling edit-script [] >}}

{{< /learner-task >}}


## Store position

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-old_column-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-save_position-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit update-old_column-variable edit-script [] >}}

{{< /learner-task >}}


## Add gardener sprite


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-player-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-player-costumes add-medialib-appearances-entry ["TODO-ENTRY-NAME"] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-spawn-player-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit set-player-sprite-size edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit set-player-y-position edit-script [] >}}

{{< /learner-task >}}


## Move gardener


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-move-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit compute-player-x-position edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit update-player-xy-positions edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit update-old_column-variable-to-be-fixed edit-script [] >}}

{{< /learner-task >}}


## Animate gardener movement


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-checking-player-moved-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit switch-player-costume-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit animate-move-player-right edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit end-move-player-animation edit-script [] >}}

{{< /learner-task >}}


## Questions and challenges