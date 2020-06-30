# Boing from Code The Classics

{{< image-right screenshot.png >}}

In this tutorial, we'll write a version of the classic 'pong' game.
We'll follow the example in the _Code The Classics, vol.1_ book.

{{< run-finished-project >}}


----------------------------------------------------------------

## Set up the background

We’re going to create our own version of the Stage, so we import the
`Stage` class from `pytch`:

{{< commit import-Stage >}}

Now we can define our own class, `BoingBackground`, which is a special
kind of `Stage`.  This is done by putting the base class in
parentheses after the name of the class we’re defining.  The body of
the class sets up the background image from the library:

{{< commit define-BoingBackground-class >}}

And finally we need to make our class part of the project:

{{< commit register-BoingBackground >}}


## Create the player’s bat

The first job is to bring in the `Sprite` class from `pytch`:

{{< commit import-Sprite >}}

The player’s bat will be a sort of Sprite, so we define a class for
it.  The body of the class says which image from the library to use:

{{< commit define-Bat-class >}}

In the same way that we need to tell Pytch about the sort of Stage we
want to use, we also have to tell it that this class should be part of
the project:

{{< commit register-Bat >}}


## Give the bat some simple behaviour

To get things started, we’re going to make the bat appear in the right
place when the green flag is clicked.  The first job is to bring in
the _decorator_ which we’ll use to say that we want our code to run
when the green flag is clicked:

{{< commit import-green-flag >}}

Now we can define a _method_ in the `Bat` class which we want to run
when the green flag is clicked.  There are two parts here: define the
method, and then _decorate_ it to say when we want it to run.

{{< commit centre-bat-on-start >}}

### Allow movement with `q` and `a`

Once the bat is in the right place, we want to enter an endless loop
(this would be _forever_ in Scratch), moving up or down according to
whether the `q` or `a` key is pressed:

{{< commit move-with-qa-keys >}}
