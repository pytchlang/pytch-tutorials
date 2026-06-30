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

Add a more interesting background for your garden simulation game. In the media library there is a bundle of two images called `Garden` that you can choose.

{{< learner-task-help >}}

{{< jr-commit add-garden-backgrounds add-medialib-appearances-entry ["Garden"] >}}

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

Now, your game should have a more interesting background.

{{< learner-task >}}

Try it! Click the green play button to run your game. 
You should see the new garden background.

{{< /learner-task >}}

## Spawn a plant

Now that we have a new background, we want to add a plant to the flower patch that is shown in our background image. 
For that, we need to create a new sprite called `Soil` which will act as the soil in our flower patch and decide when a 
plant is growing in it and which plant it will be.

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

{{< jr-commit add-soil-costumes add-medialib-appearances-entry ["Garden plants"] >}}

{{< /learner-task >}}

Now, when you run your project, the `Soil` sprite should be included in your simulation.

{{< learner-task >}}

Try running the project again! Click the green flag button and see if anything has changed in your project.

**What is different?**

{{< learner-task-help >}}

You should now see a tree seedling in the center of your garden.

{{< /learner-task >}}

## Place multiple plant seeds

Now that we have a plant in the center of our flower patch, we might want to add more variety to our garden by adding different flower seeds to different parts of the patch.
We also want the placement of the flower seeds to be different every time we run the project.
Pytch has a very useful feature for this purpose called _clones_. 
Clones are exact copies of a sprite that can be created while the project is running. 

Clones are very similar to the clones you can create in Scratch by saying

```scratch
create clone of [myself v]
```

except in Pytch you would say

```python
 self.create_clone()
```

We can use clones to create enough copies of our `Soil` sprite to fill out our entire flower patch without having to copy and paste the code that every piece of soil needs.

{{< learner-task >}}

Add a new script to the `Soil` sprite which runs when you click on the green button.

{{< learner-task-help >}}

{{< jr-commit create-empty-soil-spawn-script add-script [] >}}

{{< /learner-task >}}


Next, we can write a line of code in our new script that defines where on the stage we want all of our `Soil` clones to be placed.
To do that, we can define a variable called `Stage.flower_patch_locations`and set its value to a list of numbers. 

Lists are used in Python to contain multiple numbers, strings or other types of data inside one variable.

To create a list with, for example, three values, in Python you can write

```python
variable_name = [value_1, value_2, value_3]
```
and replace `variable_name` with the name of your variable and `value_1`, `value_2` and `value_3` with the values 
you would like to refer to.

Since we will use a formula to calculate where exactly our `Soil` clones should be, 
this variable only needs to contain the numbers `-2`, `-1`, `0`, `1`, and `2` to help us place five pieces of soil into our project.

{{< learner-task >}}

Add a line of code to the `Soil` script which makes the `Stage.flower_patch_locations` variable refer to a list with the values 
`-2`, `-1`, `0`, `1`, and `2`. 

{{< learner-task-help >}}

You can look into the Scratch/Python help to find out more about how to make a variable refer to a value.

{{< learner-task-help >}}

{{< jr-commit define-soil-locations-variable edit-script [] >}}

{{< /learner-task >}}

Next, we want to create a clone of the `Soil` sprite for all five numbers in our `Stage.flower_patch_locations` variable. 
We can use a for loop in this case.

Programming languages often have for loops because they allow us to repeat a line of code without having 
to write the same code over and over again. 

For this next task, a for loop will help us use the same line of code five times, once for every clone we want to create for our flower patch.

In Python, a for loop uses a so-called iterable object, which is an object (e.g. lists, ranges) which contains a countable number of objects (e.g. numbers, strings).
The loop then runs the code block inside of it one time for every element inside the iterable object. 
for loops also have a loop variable which will become useful to us later. 

{{< learner-task >}}

Add two lines of code that will create five clones of the `Soil` sprite, one for every number in `Stage.flower_patch_locations`.
Make sure to use a for loop and to give its loop variable the name `flower_patch_location`.

{{< learner-task-help >}}

The first line of code will create a for loop that runs once for every element in the `Stage.flower_patch_locations` list.
The second line underneath it needs to be indented and create a clone of the `Soil` sprite. 
That way, the second line of code will be used multiple times to create all the clones we need.

{{< learner-task-help >}}

Look in the Scratch/Python help to see which lines of code you can use to repeat a code block, 
get the length of a list and clone a sprite. 

{{< learner-task-help >}}

{{< jr-commit add-soil-clone-loop edit-script [] >}}

{{< /learner-task >}}

If you run the project now, you will see that nothing has changed yet. 
That is, because we still need to give our clones a unique location.


### Set soil locations

After we create our `Soil` clones, we want to calculate a unique x-position for them based on the values in our `Stage.flower_patch_locations` variable. 
This way, every piece of soil will be displayed in a different location in our garden.

To do this, we can make use of all the values inside our list in our for loop by using the loop variable. With loop variables we can use a different element every time the code inside of the for loop is run.
By using loop variables together with lists, we can write what would 
otherwise be many lines of code which would do very similar but different things in way fewer lines.

The code that we want to add to our for loop needs to calculate a different position for each clone of our `Soil` sprite, 
so that a plant can grow everywhere in our patch.
Since the images we are using for the `Soil` sprite all have a width of 48 pixels, and exactly five `Soil` pieces fit into the flower patch,
we want our formula to create five positions that are exactly 48 pixels apart on the stage's x-axis. 

To compute unique x-positions for all the clones, we can use all of the five values in our `Stage.flower_patch_locations`, one for each clone.

{{< learner-task >}}

Add a variable called `soil_xpos` inside the for loop. 
Calculate each clone's x-position using a different value in the `Stage.flower_patch_locations` list and set the value of `soil_xpos` 
with this formula:

`flower_patch_location * 48`

The result should be that the first clone will receive the x-position `-96`, the second clone will receive `-48`, the third one `0`, and so on.

{{< learner-task-help >}}

To get a different elements from a list you need to use the loop variable. 
You can find out how to use loop variables in the Python/Scratch help section.

{{< learner-task-help >}}

{{< jr-commit compute-soil-x-position edit-script [] >}}

{{< /learner-task >}}

Now that we have our unique x-positions stored in `soil_xpos`, we can apply them to our `Soil` sprite before cloning it.

{{< learner-task >}}

Add a line of code inside the for loop which will set the x-position of our `Soil` sprite to `soil_xpos` and its 
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
in the simulation. To do that, we can use a randomly generated number to change the costume of our sprite right before 
we clone it to look like either daisy seeds, rose seeds or an empty piece of soil. 
This way, every time we run our project, each `Soil` clone has a chance to start with one of these three costumes.  

{{< learner-task >}}

Add a new variable called `rng` to the for loop which will store a randomly generated number between `0` and `4` as its value. 

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

Check whether the value in `rng` is a certain value, for example, `0`. 
If it is, then switch the soil's costume to `rose_seed.png`. 

Otherwise, check if `rng` is a different value,
for instance, `1`. In that case, switch the costume `daisy_seed.png`. 

If `rng` is neither of these values, switch the soil's costume to `empty.png`.    

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
Before we can do that, however, we need to add a sprite that will control our movement within the row of soil tiles. 

{{< learner-task >}}

Add a new sprite called `Hover` to the project.

{{< learner-task-help >}}

{{< jr-commit add-hover-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

From the media library, add the image `hover.png` as a costume for your `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit add-hover-costumes add-medialib-appearance ["hover.png"] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the stage which runs when you click on the green button.

{{< learner-task-help >}}

{{< jr-commit create-empty-stage-green-flag-script add-script [] >}}

{{< /learner-task >}}

To track our player's movement, we need to define a variable which stores which column we are currently hovering over.

{{< learner-task >}}

In the stage, add a new variable called `Stage.current_column` and set it to `0`.

{{< learner-task-help >}}

{{< jr-commit define-current-column-variable edit-script [] >}}

{{< /learner-task >}}

Next, we want to have a script that is run every time the player wants to move so we can update the x- and 
y-positions of our `Hover` sprite.

{{< learner-task >}}

Add a new script to the `Hover` sprite that will be run every time the message "move" is broadcasted.

{{< learner-task-help >}}

{{< jr-commit create-hover-move-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Inside of the new script, move the `Hover` sprite based on the value in `Stage.current_column`. 
The formula for calculating the new x-position of the `Hover` sprite, similar to the one from chapter 3 is

_the value in Stage.current_column_ * 48

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

Add a new line below which broadcasts the "move" message.

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

In the stage, add two new variables called `Stage.MAX_COLUMN` and `Stage.MIN_COLUMN`
 and set them to sensible values. For this tutorial we would suggest using the values `3` and `-3` respectively.

{{< learner-task-help >}}

{{< jr-commit define-max-and-min-column edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a condition to the "when left arrow key pressed" script in the `Hover` sprite so that the sprite only moves when
we are inside the boundary set by `Stage.MIN_COLUMN`.

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

Since we want to show multiple variables later, we want this one to appear on the right side of the screen.
You can do this by writing something like this

```python
 self.show_variable("variable_name", right=236)
```

and replace _variable_name_ with the variable you want to show.

Leaving out the `, right=236` puts the variable at the top left of the screen. 

{{< learner-task >}}

Add a line of code that will show the `Stage.water_level` Stage variable on the top right of the screen when we run the project. 

{{< learner-task-help >}}

{{< jr-commit show-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the `Hover` sprite that is run every time the Arrow Up key is pressed.

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

Add another line of code above our last one which will check if the `Stage.current_column` variable is
part of the `Stage.flower_patch_locations` list and if `Stage.water_level` is larger than `0`.

{{< learner-task-help >}}

To complete this task with one line of code, you have to use a Python keyword that allows you to connect multiple tests in one check. 

{{< learner-task-help >}}

Python has a keyword called `and` that you can use for this purpose:

```python
 if your_test and your_second_test:
     code_to_run_if_both_tests_true
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

For this next task, we want to create a new if statement without any code inside of it yet. However, Python does not allow us 
to create empty if statements. To prevent an error, we can use the `pass` keyword like this:

```python
 if your_test:
     pass
```

The `pass` keyword is a placeholder in Python, which means that it does nothing and is usually only there to be replaced later on.  

{{< learner-task >}}

Add an if statement to the new script that checks if the `Soil` clone is currently touching the `Hover` sprite.
For now, nothing needs to happen if the statement is `True` so to avoid error messages, you write the keyword `pass` in the line below the if statement.

{{< learner-task-help >}}

{{< jr-commit flower-create-condition-for-touching-hover edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add another empty if statement inside the if statement we just created that checks if the current Soil's costume is either `rose_seed.png` or `daisy_seed.png`.
Since the outer if statement won't be empty anymore, you will only need one `pass` keyword.

{{< learner-task-help >}}

To complete this task with one line of code, you have to use a Python keyword that allows you to connect multiple tests in one check.

{{< learner-task-help >}}

Python has a keyword called `or` that you can use for this purpose:
```python
 if your_test or your_second_test:
     code_to_run_if_one_of_these_tests_true
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

You will need to add one line of code inside the innermost if statement in your new script.

{{< learner-task-help >}}

{{< jr-commit switch-to-next-flower-costume edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

After switching costume, pause the code for two seconds.

{{< learner-task-help >}}

{{< jr-commit wait edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Switching to the next costume and pause the code two more times.

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

Add a for loop to the script that will run some code once for every element in the `Stage.water_locations` list.

{{< learner-task-help >}}

{{< jr-commit add-water-clone-loop edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add multiple lines of code inside of the for loop that calculate the x-position of every clone, sets the `Water`'s x-position to that calculated value and then creates a new clone. 

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

Add some code to the if statement that broadcasts the message "get_water". 

{{< learner-task-help >}}

{{< jr-commit broadcast-get_water edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new script to the `Water` sprite that will be run whenever the message "get_water" is received.

{{< learner-task-help >}}

{{< jr-commit create-empty-get_water-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an if statement to the new script that tests if the current `Water` clone has the `water.png` costume on.

{{< learner-task-help >}}

{{< jr-commit water-create-condition-for-costume-water edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the new if statement that resets the value of `Stage.water_level` to its starting number (or any other positive number).

{{< learner-task-help >}}

For this tutorial, the starting value we chose is `3`.

{{< learner-task-help >}}

{{< jr-commit reset-water_level-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the if statement that will switch the `Water` sprite's costume to `water_empty.png`, 
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

Add a new variable called `Stage.tree_location` to the Soil's "when green flag is clicked" script which stores a value 
in our Stage.flower_patch_locations, like `0`, for example.

{{< learner-task-help >}}

{{< jr-commit define-tree-location-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new block of code to the for loop in the `Soil` sprite that checks if the value at `flower_patch_location` 
is equal to `Stage.tree_location`.
For now, if it is, nothing new needs to happen. If it isn't, then the script should choose between a seed and an empty costume, like before.

{{< learner-task-help >}}

You need to wrap the current if-elif-else block into another if-then-else block, 
where the then part will stay empty for now and the else part will keep the code from before.

{{< jr-commit create-condition-for-tree_location-variable-check edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the new if-then-else block, that will switch the soil's costume to `tree_with_fruits.png` 
if the soil's location is that of a tree.

{{< learner-task-help >}}

{{< jr-commit switch-soil-costume-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

When you run the project now, you should see a tree in the center of your garden.

{{< /learner-task >}}

## Shake down apples

Now that we have a tree  our game, it's time for our new mechanic: the player's ability to pick apples from the tree. 

{{< learner-task >}}

Add a new variable called `Stage.apples` to the stage that tracks the amount of apples the player has collected and set it to `0`.
Show it on the stage.

{{< learner-task-help >}}

{{< jr-commit create-and-show-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an empty script to the `Soil` script that is run when the _Space_ key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-empty-space-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a new line of code to the script that checks if the current soil's costume is `tree_with_fruits.png` and 
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

Add a block of code in the new if statement that switches the costume of the `Soil` to `tree.png`, waits for three seconds, and then switches it back to `tree_with_fruits.png`.

{{< learner-task-help >}}

{{< jr-commit animate-tree-to-tree_with_fruits edit-script [] >}}

{{< /learner-task >}}

### Try it!

{{< learner-task >}}

Try running your project again.

**Has anything changed?**

{{< learner-task-help >}}

When you run the project now and you press the _Space_ key while hovering over a tree, you should be able to collect an apple and watch the tree grow new ones.

{{< /learner-task >}}

## Plant trees

In this chapter, we will work on a feature that lets the player use the apples they can now collect to plant new trees.

{{< learner-task >}}

Add a new script to the `Soil` sprite that runs every time the _P_ key is pressed.

{{< learner-task-help >}}

{{< jr-commit create-empty-p-key-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add an if statement that checks if the `Stage.apples` variable is larger than `0` and if the `Soil` sprite is touching the `Hover` sprite.

{{< learner-task-help >}}

{{< jr-commit add-condition-for-apples-variable-and-touching edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add a line of code that will reduce the `Stage.apples` variable by one if the test inside the new if statement is true.

{{< learner-task-help >}}

{{< jr-commit decrement-apples-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add code to the new if statement that will switch the costume of the `Soil` sprite to `tree_seedling.png`. 

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

Add an elif-statement to the inner if statement in the "when I receive 'water_soil'" script in the `Soil` sprite.
In it, check if the soil's costume name is `tree_seedling.png`.

{{< learner-task-help >}}

{{< jr-commit add-condition-to-check-for-tree_seedling edit-script [] >}}

{{< /learner-task >}}

{{< learner-task >}}

Add a code block to the if/then/else block that switches to the next costume of the soil and waits for two seconds 
twice, so that the soil is using the `tree_with_fruits.png` costume.

{{< learner-task-help >}}

The soil's costume will need to be changed three times.

{{< learner-task-help >}}

{{< jr-commit animate-tree-growing edit-script [] >}}

{{< /learner-task >}}


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

{{< jr-commit add-player-costumes add-medialib-appearances-entry ["Hijabi"] >}}

{{< /learner-task >}}


{{< learner-task >}}

Create a "when green flag is clicked" script in your new `Player` sprite.

{{< learner-task-help >}}

{{< jr-commit create-empty-spawn-player-script add-script [] >}}

{{< /learner-task >}}

### Make the gardener fit on the stage

Feel free to try running your project now. You will notice that while the Player sprite is now visible on stage,
it is quite large and obstructing our view. To fix that, we will need to add some code to our script that reduces the
size of our sprite and moves it downwards along the y-axis. The idea is to make our gardener move with the player
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

Now that we have a sprite for our gardener, it would be nice if they could follow our player around to wherever they
are currently hovering over in our garden.

{{< learner-task >}}

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

### Try it!

{{< learner-task >}}

Once again, try running your project. Has anything changed?

{{< learner-task-help >}}

Whenever the player changes its position in the garden, the gardener should smoothly follow and move to a nearby location.

{{< /learner-task >}}



## Animate gardener movement

While our gardener can now move around smoothly and follow our player, we can still add an animation for direction that our gardener can walk in so that their movement feels a bit more natural.
To do that, however, we first need to have a way of testing which direction our gardener is currently walking in.

### Store the player's last position

{{< learner-task >}}

Add a line of code to the "move" script of your `Player` sprite to check if the player has moved left by testing if
the `new_x` variable is larger than the sprite's current x-position.

{{< learner-task-help >}}

{{< jr-commit add-condition-checking-player-moved-right edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add some code inside the new if statement to switch the `Player` sprite's costume to `player_right.png`.

{{< learner-task-help >}}

{{< jr-commit switch-player-costume-right edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Add another if statement underneath (but outside) the previous if statement to switch the `Player` sprite's costume to 
`player_left.png` if `new_x` is smaller than the sprite's current x-position.

{{< learner-task-help >}}

{{< jr-commit animate-move-player-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

Finally, add one more line of code that sets the costume of the `Player` sprite to `player_front.png`.

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

- Customise your character's look. Feel free to find an import images from the internet as new costumes using a search engine of your choice. 
- Add sound effects to the game.
- Add another type of plant that can grow in the garden.
- Harder challenge: Make the player move in four directions (Feel to use the `tall_garden.png` backdrop).
- Harder challenge: Make flowers randomly grow in neighbouring spots 
- Harder challenge: Add a day and night cycle to your simulation. Think about how that could change the way your plants grow. 

Also, feel free to think about how you could use the features of a micro:bit controller (microphone, gyrosensor, LED display) in your project.
