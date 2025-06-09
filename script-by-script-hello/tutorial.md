# Hello there!

In this tutorial, you will learn how to create and run a Pytch project
with a _sprite_.

---

## What is a Pytch program?

Pytch programs are written in a programming language called _Python_.
As well as the normal Python features, Pytch also has extra commands
for sprites, sounds, and other things.  You make a Pytch project by
writing a Python program in the Pytch webapp.

{{< learner-task >}}

Although you haven't written any code yet, you can still run the
project, by clicking the green play button.  What happens?

{{< learner-task-help >}}

Nothing!  You haven't made any sprites or written any scripts yet.

{{< /learner-task >}}


## Create the sprite

To start, you will make a sprite that the player will control.

{{< learner-task >}}

Create a new sprite called **Snake**.

{{< learner-task-help >}}

{{< jr-commit create-snake-class add-sprite [] >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project, by clicking the green play button.  What happens?

{{< learner-task-help >}}

Nothing!  You haven't given the sprite any _costumes_ yet.

{{< /learner-task >}}

The sprite has no _costumes_ to say what it looks like.  The next
chapter will fix this.


## Add a costume

To say what a sprite looks like, you give it _costumes_.  For this
tutorial, the sprite will only have one costume, but in general, a
sprite can have lots of costumes, and your program can switch between
them.

{{< learner-task >}}

Add a suitable costume to your sprite.  There is one called
**Pytch-hello-snake** in the media library.

{{< learner-task-help >}}

{{< jr-commit snake-costume add-medialib-appearance ["Pytch-hello-snake.png"] >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project, by clicking the green play button.  You should see a
snake in the middle of the stage.

{{< /learner-task >}}


## Add a script

You will now make the Snake react when you click on it.  A sprite can
have _scripts_ — these are pieces of Python code which run when
certain things happen, for example, when the sprite is clicked, or
when a particular key is pressed.

{{< learner-task >}}

Add a script which will run when the sprite is clicked.

{{< learner-task-help >}}

{{< jr-commit add-when-clicked-script add-script [] >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project, by clicking the green play button.  What happens
when you click on the Snake?

{{< learner-task-help >}}

Nothing!  You have not written any Python code yet.

{{< /learner-task >}}

Nothing happens when you click on the Snake, because the script is
_empty_ — it has no Python code in it.  The next section will fix
this.

### Write the code for the script

Now you can make the Snake say something when it's clicked.

{{< learner-task >}}

Write Python code to make the Snake say _Hello there!_ when you click
on it.

{{< learner-task-help >}}

You have already made a script, so you just need to write a line of
Python code into that script.

{{< learner-task-help >}}

If you know Scratch, you might have used code like

``` scratch
say [Hello there!] for [2.0] seconds
```

Look in the help to learn how to do this in Python.

{{< learner-task-help >}}

{{< jr-commit add-script-body edit-script [] >}}

{{< /learner-task >}}

### Test it!

{{< learner-task >}}

Run your project, by clicking the green play button.  The Snake should
say your message when you click on it.

{{< /learner-task >}}


## The project is finished!

Congratulations on your first Pytch project!

### Challenges

Can you change your program to complete these challenges?

* Make the Snake say `"Hi there!"` instead of `"Hello there!"`.

* Make the Snake's speech balloon appear for 3&nbsp;seconds instead of
  2&nbsp;seconds.

* (More advanced:) Make the Snake say two things, one after the other.
  Maybe it could say `"Hi there!"` for two seconds, and then `"OK,
  bye!"` for two seconds.


### Credits

{{< asset-credits >}}
