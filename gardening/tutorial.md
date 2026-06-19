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

Now, when you run your project, you should see a tree seedling in the center of your garden

## Place the soil

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-soil-spawn-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-soil-locations-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-soil-clone-loop edit-script [] >}}

{{< /learner-task >}}


### Set soil locations

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit compute-soil-x-position edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit set-soil-position edit-script [] >}}

{{< /learner-task >}}

## Randomly select a flower seed

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit generate-random-number edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit choose-flower-seed edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit hide-original-soil edit-script [] >}}

{{< /learner-task >}}

## Add movement

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-hover-sprite add-sprite [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-hover-costumes add-medialib-appearance ["TODO-DISPLAY-IDENTIFIER"] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-empty-stage-green-flag-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-current-column-variable edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-hover-move-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit move-hover-to-current-column edit-script [] >}}

{{< /learner-task >}}

### Add keyboard controls

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-arrow-left-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit update-current-column-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit broadcast-move-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit create-arrow-right-script add-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit update-current-column-and-broadcast-move-right edit-script [] >}}

{{< /learner-task >}}

## Add invisible walls

{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit define-max-and-min-column edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-for-min-column-arrow-left edit-script [] >}}

{{< /learner-task >}}


{{< learner-task >}}

{{< learner-task-help >}}

{{< jr-commit add-condition-for-max-column-arrow-right edit-script [] >}}

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