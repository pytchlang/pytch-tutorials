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

Try running your project again. 

**Has anything changed?**

{{< learner-task-help >}}

You can now no longer move out of frame.

{{< /learner-task >}}

## Add a watering can

With our player now being able to move around safely, we can add a new mechanic that allows the player to collect, 
carry and use water in their garden. 
To start off, we need to a new variable to track the amount of water that currently in our can.
We can use that variable in a new script to decide if the player is currently able to water a plant or pick up more water.
In that case, we can then update the remaining water.

{{< learner-task >}}

Add a variable to the Stage's "when green flag clicked script" called `Stage.water_level` and set it to a number larger than `0`.
For this tutorial, we chose `3` as the starting value.

{{< learner-task-help >}}

{{< jr-commit define-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code that will show the `Stage.water_level` Stage variable on screen when we run the project. 

{{< learner-task-help >}}

{{< jr-commit show-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the `Hover` sprite that is run everytime the Arrow Up key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-arrow-up-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code to our new script that reduces the `Stage.water_level` by a small amount. 
In our case, we chose to reduce the water level by `1`.

{{< learner-task-help >}}

Similar to how we have previously updated the Stage.current_column variable, here we are looking for one line of code
that will decrease the value of our variable. You can find it in the Scratch/Python help area in the top left of this page.

{{< learner-task-help >}}

{{< jr-commit decrement-water_level-variable edit-script [] >}}

{{< /learner-task >}}

{{< learner-task >}}

Add another line of code to the "when Arrow Up key is pressed" script of the `Hover` sprite that will check if our
watering can has water and if the column the player is currently standing in is part of the `Stage.soil_locations` list.
For this tutorial, we will assume that `0` is the smallest possible value for `Stage.water_level`.

{{< learner-task-help >}}

To complete this task with one line of code, you have to use a Python keyword that allows you to connect multiple tests in one check. 

{{< learner-task-help >}}

Python has a keyword called `and` that you can use for this purpose:
```python
 if your_test and your_second_test:
  code_to_run_if_both_tests_true`
```
{{< learner-task-help >}}

{{< jr-commit add-condition-arrow-up edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Broadcast the message "water_soil" right after decreasing the value in `Stage.water_level`.

{{< learner-task-help >}}

{{< jr-commit broadcast-water_soil-arrow-up edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**What has changed?**

{{< learner-task-help >}}

You can now pour water onto soil and the `Stage.water_level` variable shown on the screen will change, but the soil itself stays the same.

{{< /learner-task >}}

## Grow flowers

While we can now pour water onto the soil, we still need to get plant seeds to react to the water and grow into flowers.
To simulate this, we can change the costume of one of our `Soil` sprite clones whenever the player is hovering over it 
and the "water_soil" message is received.

{{< learner-task >}}

Add a new script to the `Soil` sprite that will be run when the "water_soil" message is received.

{{< learner-task-help >}}

{{< jr-commit create-empty-water_soil-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add some code that checks if the `Soil` clone is currently touching the `Hover` sprite. 

{{< learner-task-help >}}

{{< jr-commit flower-create-condition-for-touching-hover edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add another piece of code that checks if the current Soil's costume is either `rose_seed.png` or `daisy_seed.png`.

{{< learner-task-help >}}

To complete this task with one line of code, you have to use a Python keyword that allows you to connect multiple tests in one check.

{{< learner-task-help >}}

Python has a keyword called `or` that you can use for this purpose:
```python
 if your_test or your_second_test:
  code_to_run_if_one_of_these_tests_true`
```
{{< learner-task-help >}}

{{< jr-commit create-condition-for-seed-costume-check edit-script [] >}}

{{< /learner-task >}}

### Animate the flower growing

While we could just switch the soil's costume to that of a flower, it would be a nice touch to slowly animate the 
flower growing into a flower. In Pytch, we can do this by switching our soil's costume and briefly pausing our code until we have reached the flower's final costume.   

{{< learner-task >}}

Switch to the `Soil`'s next costume if it is being hovered over and if its current costume is a seed.  

{{< learner-task-help >}}

You will need to add one line of code inside the innermost if/then code block in your new script.

{{< learner-task-help >}}

{{< jr-commit switch-to-next-flower-costume edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

After switching costume, pause the code for one second.

{{< learner-task-help >}}

{{< jr-commit wait edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Repeat the previous two tasks, switching to the next costume and pausing the codem two more times.

{{< learner-task-help >}}

{{< jr-commit repeat-flower-costume-change-and-wait edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

You will see that now, whenever the player pours water onto flower seeds, they will slowly turn into flowers.

{{< /learner-task >}}

## Add water source

Now that we can water our flowers, it would be nice to be able to refill our watering can. 
For that, we can create a new sprite for watering holes and place them in different locations in our garden.

{{< learner-task >}}

Add a new sprite called `Water` to your project.

{{< learner-task-help >}}

{{< jr-commit create-water-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add the "Water hole" bundle of images as costumes to the `Water` sprite.

{{< learner-task-help >}}

{{< jr-commit add-water-costumes add-medialib-appearances-entry ["Water hole"] >}}

{{< /learner-task >}}


### Place water sources

Like we did with the `Soil` sprite, we are now creating a script that will place clones of the `Water` into the game.

{{< learner-task >}}

Add a new "when green flag is clicked" script to the `Water` sprite.

{{< learner-task-help >}}

{{< jr-commit create-spawn-water-green-flag-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Create a new variable called `Stage.water_locations` and set its value to a list with the numbers `-3` and `3`.

{{< learner-task-help >}}

{{< jr-commit define-water-locations-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a for-loop to the script that will run some code once for every element in the `Stage,water_locations` list.

{{< learner-task-help >}}

{{< jr-commit add-water-clone-loop edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add multiple lines of code inside of the for-loop that calculates an x-position every clone, sets the `Water`'s x-position to that calculated value and then creates a new clone. 

{{< learner-task-help >}}

{{< jr-commit add-and-implement-water-clone-loop edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Hide the original `Water` sprite after every clone was created.

{{< learner-task-help >}}

{{< jr-commit hide-original-water edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

When you run the project now, water holes will appear left and right of your garden.

{{< /learner-task >}}


## Refill can and water sources

Next, we want the player to be able to use the water holes to refill their water levels.
When the player does that, we also want the water source to be empty right afterwards and to refill itself after a few seconds.

{{< learner-task >}}

Create a new script in the `Hover` sprite that will run when the _Down Arrow_ key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-empty-arrow-down-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code to the new script that will check if the value of `Stage.current_column` is an item in
the `Stage.water_locations` list.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-current_column edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add some code to the if/then code block that broadcasts the message "get_water". 

{{< learner-task-help >}}

{{< jr-commit broadcast-get_water edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the `Water` sprite that will be run whenever the message "get_water" is received.

{{< learner-task-help >}}

{{< jr-commit create-empty-get_water-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the script that will reset the value of `Stage.water_level` to its starting/maximum value.

{{< learner-task-help >}}

For this tutorial, the starting value we chose is `3`.

{{< learner-task-help >}}

{{< jr-commit reset-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code in front of the previous line that checks if the current `Water` clone is touching the `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit water-create-condition-for-touching-hover edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a code block, meaning multiple lines of code, that will switch the `Water` sprite's costume to `water_empty.png`, 
pause the code for ten seconds, and then switch its costume back to `water.png`. 

{{< learner-task-help >}}

This code block needs to contain three lines of code: two are responsible for switching the costumes and one will be needed to wait for ten seconds.

{{< learner-task-help >}}

Since there are only two costumes in our `Water` sprite and Pytch will automatically loop our list of available costumes,
we can use the `self.next_costume()` command twice to get back to our original costume.

{{< jr-commit animate-water-refill edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

Water holes will now refill themselves ten seconds after using them.

{{< /learner-task >}}

## Spawn trees

In this chapter, we will increase the variety of plants in our garden by adding trees. 
Since trees will also have a unique mechanic to them, we want to make sure that every time we run the simulation,
we will start with one tree.

{{< learner-task >}}

Add a new variable called `Stage.tree_location` that stores a value which is currently in our Stage.soil_locations, 
like the center of our garden, for example.

{{< learner-task-help >}}

{{< jr-commit define-tree-location-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new block of code to the for-loop that checks if the value at index `ì` of `Stage.soil_locations` is equal to the value stored in `Stage.tree_location`.
For now, if it is, nothing new needs to happen. If it isn't, then the if/elif/else block from before should be followed.

{{< learner-task-help >}}

You need to wrap the current if/elif/else block into another if/then/else block, 
where the then part will stay empty for now and the else part will keep the code from before.

{{< jr-commit create-condition-for-tree_location-variable-check edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the new if/then/else code block, that will switch the soil's costume to "tree_with_fruits.png" 
if the soil's location is that of a tree.

{{< learner-task-help >}}

{{< jr-commit switch-soil-costume-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

When you run the project now, water holes will appear left and right of your garden.

{{< /learner-task >}}

## Shake down apples

Now that we have a tree in our game, it's time for our new mechanic: the player's ability to pick apples from the tree. 

{{< learner-task >}}

Add a new variable that tracks the amount of apples the player has collected. 

{{< learner-task-help >}}

{{< jr-commit create-and-show-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an empty script to the `Soil` script that is run when the _Space_ key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-empty-space-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new line of code to the script that checks if the current soil's costume is "tree_with_fruits.png" and 
if it is touching the `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-tree_with_fruits-and-touching edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code that increments the `Stage.apples` variable to the `Soil`'s script if the player is picking an apple.

{{< learner-task-help >}}

{{< jr-commit increment-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a block of code in the new if/then block that switches the costume of the `Soil` to "tree.png", waits for three seconds, and then switches it back to "tree_with_fruits.png".

{{< learner-task-help >}}

{{< jr-commit animate-tree-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

When you run the project now, water holes will appear left and right of your garden.

{{< /learner-task >}}

## Plant trees


{{< learner-task >}}

Add a new script to the `Soil` sprite that runs everytime the _P_ key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-empty-p-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an if/then code block that checks if the `Stage.apples` variable is larger than `0` and if the `Soil` sprite is touching the `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-apples-variable-and-touching edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code that will reduce the `Stage.apples` variable by one if the test inside the new if/then block is true.

{{< learner-task-help >}}

{{< jr-commit decrement-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the new if/then block that will switch the costume of the `Soil` sprite to "tree_seedling.png". 

{{< learner-task-help >}}

{{< jr-commit switch-soil-costume-to-tree_seedling edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again. In what ways can you now interact with the garden?

{{< learner-task-help >}}

You can now move around and  collect apples from trees by pressing the spacebar in front of a tree with fruits 
and plant them by pressing p onto soil tile without a tree.

{{< /learner-task >}}


## Grow trees

In this chapter, we are going to animate the tree seedling growing into a tree with fruits when it is watered.

{{< learner-task >}}

Add an else-statement to the if/then code block in the "when I receive 'water_soil'" in the `Soil` sprite.

{{< learner-task-help >}}

{{< jr-commit add-condition-to-check-for-tree_seedling edit-script [] >}}

{{< /learner-task >}}

{{< learner-task >}}

Add a code block to the if/then/else block that switches the costume of the soil and waits for two seconds repeatedly, 
until the soil is using the "tree_with_fruits.png" costume.

{{< learner-task-help >}}

The soil's sprite will need to be changed three times.

{{< learner-task-help >}}

{{< jr-commit animate-tree-growing edit-script [] >}}

{{< /learner-task >}}




[//]: # ({{< learner-task >}})

[//]: # ()
[//]: # (Create a new script that is run when the "save_position" message is received.)

[//]: # ()
[//]: # ({{< learner-task-help >}})

[//]: # ()
[//]: # ({{< jr-commit create-empty-save_position-script add-script [] >}})

[//]: # ()
[//]: # ({{< /learner-task >}})

[//]: # ()
[//]: # ()
[//]: # ({{< learner-task >}})

[//]: # ()
[//]: # (Add a line of code that will update the `Stage.old_column` variable to the value of the `Stage.current_column` variable.)

[//]: # ()
[//]: # ({{< learner-task-help >}})

[//]: # ()
[//]: # ({{< jr-commit update-old_column-variable edit-script [] >}})

[//]: # ()
[//]: # ({{< /learner-task >}})

### Try it!

{{< learner-task >}}

Try running your project again. In what ways can you now interact with the garden?

{{< learner-task-help >}}

When you water a tree seedling after planting it, it now grows into a tree with fruits.

{{< /learner-task >}}


## Add gardener sprite


{{< learner-task >}}

Create a new sprite called `Player` in your project.

{{< learner-task-help >}}

{{< jr-commit add-player-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

From the media library, add the "Hijabi" bundle of images as costumes for your `Player` sprite.

{{< learner-task-help >}}

{{< jr-commit add-player-costumes add-medialib-appearances-entry ["TODO-ENTRY-NAME"] >}}

{{< /learner-task >}}


{{< learner-task >}}

Create a "when green flag is clicked" script in your new `Player` sprite.

{{< learner-task-help >}}

{{< jr-commit create-empty-spawn-player-script add-script [] >}}

{{< /learner-task >}}

### Make the gardener fit on the stage

Feel free to try running your project now. You will notice that while the Player sprite is now visible on stage,
it is quite large and obstructing our view. To fix that, we will need to add some code to our script that reduces the
size of our sprite and moves it downwards along the y-axis. The idea is to set to make our gardener move with the player,
while also letting the player see the sprite they are hovering over.

{{< learner-task >}}

Add a line of code that sets the size of the player sprite to something more sensible. 
We suggest setting it to about 7.5% of its original size.

{{< learner-task-help >}}

Use the help to find what Pytch statements will set the size of a sprite.

{{< learner-task-help >}}

You might know that, to make a sprite smaller in Scratch, you can use something like:

```scratch
set size to (7.5) %
```

To make the same happen for our gardener in Pytch, you can say

```python
self.set_size()
```

and put a value larger than `0` and smaller than `1` between the `()`s. 

{{< learner-task-help >}}

{{< jr-commit set-player-sprite-size edit-script [] >}}

{{< /learner-task >}}

Now, that the gardener should have a better size, we just need to adjust y-position so the soil the gardener is standing 
on remains visible.

{{< learner-task >}}

Add a line of code that will set the `Player`'s y-position downwards by a few pixels.

{{< learner-task-help >}}

We suggest moving the `Player` sprite downwards by around 8 pixels.

To move a sprite below the center of the stage in Pytch, you can say 

```python
self.set_y()
```

and enter a negative number between 0 and -180.

{{< learner-task-help >}}

{{< jr-commit set-player-y-position edit-script [] >}}

{{< /learner-task >}}


## Move the gardener

Add a new script to the `Player` sprite that is run when the "move" message is received.

{{< learner-task-help >}}

{{< jr-commit create-empty-move-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code to the new script that calculates the x-position of our gardener based on the `Stage.current_column`
variable and the 48 pixel width of our soil sprites and assign it to a new variable called `new_x`. 

{{< learner-task-help >}}

{{< jr-commit compute-player-x-position edit-script [] >}}

{{< /learner-task >}}


With Pytch you can say the following to smoothly move between two locations:

```python
self.glide_to_xy(,,)
```

You will need to add the x-position, the y-position and the amount of seconds it should take to move between 
the brackets and separated by commas.

{{< learner-task >}}

Add a line of code that smoothly glides the `Player` sprite to the new x-position in about 0.25 seconds. 

{{< learner-task-help >}}

{{< jr-commit update-player-xy-positions edit-script [] >}}

{{< /learner-task >}}



{{< learner-task >}}

Add a line of code that sets the variable `Stage.old_column` to the value of the `Stage.current_column` variable 
after the `Player` sprite has moved.

{{< learner-task-help >}}

{{< jr-commit update-old_column-variable-to-be-fixed edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Once again, try running your project. Has anything changed?

{{< learner-task-help >}}

Whenever the player changes its position in the garden, the gardener should smoothly follow and move to a nearby location.

{{< /learner-task >}}



## Animate gardener movement

### Store the player's last position

{{< learner-task >}}

Add a `Stage.old_column` variable to the Stage's "when green flag is clicked" script and set it to `0`.

{{< learner-task-help >}}

{{< jr-commit define-old_column-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code to the "move" script of your `Player` sprite to check if the player has moved left by testing if
the `Stage.current_column` variable is smaller then the `Stage.old_column` variable.

{{< learner-task-help >}}

{{< jr-commit add-condition-checking-player-moved-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add some code inside the new if/then code block to switch the `Player` sprite's costume to "player_left.png".

{{< learner-task-help >}}

{{< jr-commit switch-player-costume-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an else statement to your script that switches the `Player` sprite's costume to "player_right.png".

{{< learner-task-help >}}

{{< jr-commit animate-move-player-right edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Finally, add one more line of code that sets the costume of the `Player` sprite to "player_front.png".

{{< learner-task-help >}}

{{< jr-commit end-move-player-animation edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again. In what ways can you now interact with the garden?

{{< learner-task-help >}}

When the gardener moves, their costume should be updated according to the direction they are moving in.

{{< /learner-task >}}



## Questions and challenges

Can you change your program to solve these challenges?

Add another type of plant that can grow in the garden besides daisies and roses.
Add sound effects to the game.
Also, consider how you could use a micro:bit and its features (microphone, gyrosensor, LED display) in this game/simulation.
Very difficult: Make the player move in four directions (Feel to use the "tall_garden.png" backdrop).
