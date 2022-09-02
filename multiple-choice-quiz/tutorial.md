# Multiple choice quiz

In this project we're going to make a quiz, where the player has to
choose between three possible answers to each question.

---

## Make the narrator

Our game will be run by a *narrator*.  We will first make a `Narrator`
sprite, with a costume of a question mark.  The graphics file for
this, `"button-question.png"`, comes with this tutorial.

{{< commit add-Narrator-Sprite >}}

If you run the program now, the question-mark button should appear in
the middle of the screen.

Let's make the narrator announce the quiz when the program starts.  To
do this we'll write some code which runs when the green flag is
clicked:

{{< commit make-Narrator-announce-quiz >}}


## How to store the quiz questions?

Before we write more code, we need to stop and think about how we're
going to store the information needed to make a quiz.  A quiz is made
up of questions, so we'll start by thinking about a single quiz
question.

What are the parts of a quiz question?  We need to know:

* the actual question;
* the three possible answers;
* which answer is the correct one.

To record all these things, we're going to use a Python feature called
a *list*.  This is very like a Scratch list, but more powerful in ways
we'll see later on.

The five items in the list will be

* the question;
* answer A;
* answer B;
* answer C;
* a letter saying which answer is correct (`"A"`, `"B"`, or `"C"`).

In Python, the items of a list are written between square brackets
(`[]`) and have their items separated by commas (`,`).

Let's add a question to our program, stored in a variable, to get some
experience working with Python lists:

{{< commit add-first-question-info >}}

You'll see that I've added the code spread across seven lines, to make
it easier for a human to read.  Python lets you split code across
lines in some situations, such as when giving the items in a list like
this.  Python also allows you to have a comma after the last item in a
list, which I've included here.

### Working with lists in Python: experimental code

First we'll explore how to use the different pieces of information in
this list.  We'll write some code which is not going to be in our
final game.  This code will let us try out a few things and learn how
lists work in Python.

Let's start by printing out the list we've just created, using the
Python built-in function `print()`:

{{< commit print-single-question-info >}}

In standard Python, things you `print()` usually get displayed on the
screen.  In Pytch, `print()` output is recorded in the `Output` tab.
So to see what the above code does, select the `Output` tab.  Come
back to this `Tutorial` tab when you're ready to continue.

Often we want to get particular items out of a list.  In Scratch, you
would use, for example, this block:

``` scratch
(item (3) of [colours v])
```

to get the third item of the `colours` list.  In Python, we use the
same `[]`s as are used to write a list.  The other difference between
Scratch and Python is that in Python, the positions are numbered
starting at *zero*, so the first item in the list is `[0]`, the second
item is `[1]`, and so on.

To see this working, we'll print the first item from our question-info
list, by changing the `print()` line:

{{< commit print-item-0 >}}

And now the second item:

{{< commit print-item-1 >}}

And the fifth:

{{< commit print-item-4 >}}

Just to see what happens, experiment with asking for the item at a
position which doesn't make sense.  For example, our list only has
five items in it, so it doesn't make sense to ask for the item at
position 12:

{{< commit print-item-12 >}}

You'll see an *error* in the `Errors` tab.  Switch back to this
`Tutorial` tab when you've checked what the error says.

We've finished exploring this now, so let's delete the temporary code:

{{< commit remove-print-item >}}


## How to store more than one question?

A little bit more thinking now will save us time later.  After the
testing we did using `print()`, we're happy that we can get at the
different pieces of information which make up a single quiz question.
The next thing to think about is how we're going to store more than
one question.

We will put the questions into a list.  In Scratch, the items in a
list have to be strings or numbers.  In Python, lists can hold other
lists, which is perfect for us.

### Make a list of lists

We'll make some small changes to the code we've already written, and
make a *list of lists* to store the information about the whole quiz.
First remove the `question_info` variable name but keep the opening
square bracket:

{{< commit remove-question-info-assignment >}}

Then add a line opening a new list `all_questions_info` and a line
closing that same list:

{{< commit create-all-questions-info-list >}}

Indent the list we already have for storing the first question (this
can be done by highlighting the lines and pressing the `TAB` key):

{{< commit reindent-first-question-info >}}

We want to be able to add more questions, so add a comma after the
closing bracket of our question's list:

{{< commit add-trailing-comma-first-question-info >}}

We're now ready to add more questions when we're ready, but first
we'll get some experience working with this idea of a list of lists.

### Explore how to get items from the list of lists

As before, we will use some temporary `print()` function calls to
check we know what's going on.

Let's print the whole list of lists:

{{< commit print-all-questions-info >}}

And now, instead, we'll print that list's first item.  This will be
the one-question list we had a minute ago:

{{< commit print-all-questions-info-item-0 >}}

To get a particular item from *that* list, we use the `[]` notation
*again*:

{{< commit print-all-questions-info-item-0-item-2 >}}

Experiment with changing these numbers and check you understand what
you see printed and what errors you get when the numbers don't make
sense.

When you're happy, get rid of the temporary code:

{{< commit remove-print >}}


## Ask a question

We're now ready to start asking a quiz question!

We'll start by giving a name to the list of information for the
question we're going to ask the player.  We only have one question at
the moment, so we need the item at position zero in the all-questions
list:

{{< commit assign-question-info-temporarily >}}

Next we will pick out and give names to the individual pieces of
information.  We don't *have* to do this (we could, for example, just
keep saying `question_info[0]` whenever we want to use the question
itself), but it makes the program easier to read by a human, which is
important.

The question itself:

{{< commit assign-actual-question >}}

And the three different answers the player will choose from:

{{< commit assign-answer-variables-v1 >}}

(You might notice that we haven't used `question_info[4]` yet.  This
value tells us which answer is correct.  We'll use this later.)

Now we want to glue these parts together into one string.  In Scratch,
you would do something like

``` scratch
(join (question) (join (ans_A) (join (ans_B) (ans_C))))
```

In Python, you can join strings together using the `+` symbol; many
programming languages use `+` for this, because joining two strings
together is a bit like adding them together.

We'll make the text by joining together the question and the three
possible answers:

{{< commit concatenate-text-parts >}}

And now the narrator can say the final text:

{{< commit say-concatenated-text >}}

This is nearly right, but needs improving.  Let's start each answer on
a new line.  In a Python string, the sequence `\n` gets converted into
a special character which starts a new line, so we want to put some of
those in:

{{< commit interleave-newlines-in-text >}}

And let's label the answers so the player knows which one is which.
We'll insert `"A: "` before the first answer:

{{< commit label-answer-A-text >}}

and `"B: "` before the second:

{{< commit label-answer-B-text >}}

and `"C: "` before the third:

{{< commit label-answer-C-text >}}

Now what the narrator says should look much better.


## Add another question

Let's now test the way we've decided to store more than one question.
We want to add a second item to our `all_questions_info` list.  Just
before the `]` which closes that list, insert an inner list with the
pieces of information needed for another question:

{{< commit add-centimetres-in-metre-question >}}

Check you understand what the five different items in this list are.

We can test this by changing which item we pull out of
`all_questions_info`:

{{< commit ask-question-1 >}}

The narrator should now ask the new question instead of the original
one.

When you're happy that this is working, put the code back so it asks
the first question:

{{< commit ask-question-0-again >}}


## Ask both questions

The next step will be to ask the two questions, one after the other.

We will need to wait after asking the first question:

{{< commit add-wait-after-question-0 >}}

And then we want the narrator to ask the second question.  To make a
start on this, let's just copy and paste the code we already have for
asking the first question:

{{< commit copy-paste-to-ask-question-0-again >}}

Try this now.  What you should find is that the game just asks the
first question twice.  This makes sense, because we just copied the
code.

Can you work out what we need to change in this code, so that the
narrator asks the second question (which is at position `1` in the
`all_questions_info` list) instead of the first question (which is at
position `0`)?

This is what we need to change:

{{< commit ask-question-1-after-question-0 >}}

Your game should now ask both questions, one after the other.

## Use a loop to ask both questions

Working like this is going to get very annoying when we have more
questions.  We're going to use the idea of a *loop* to fix the code
and make it work with any number of questions.

Look at the difference between the copies of the code.  The only
difference is that we ask for the item at a different position in the
`all_questions_info` list.

To see how this can be tidied up, we'll make a variable to hold the
position of the current question.  The word *index* is often used to
mean what position in a list we're talking about, so we'll call this
variable `question_index`.  To ask the first question, we need
`question_index` to be zero:

{{< commit add-question-index-variable >}}

And we want to use this variable in the code:

{{< commit use-question-index-when-0 >}}

For the second question, our index variable needs to be `1`:

{{< commit update-question-index-to-1 >}}

And we need to use it:

{{< commit use-question-index-when-1 >}}

Test that your program still works.  It should ask the two questions
one after the other.


### Loop over the questions

In Scratch, you could find out how many items there are in a list
called `all_questions_info` by using this block:

``` scratch
(length of [all_questions_info v])
```

In Python we can do something very similar — there's a built-in
`len()` function.  We'll use this to compute the value of a variable
telling us how many questions there are.  We'll do this at the top of
the program, just after the list of questions:

{{< commit define-n-questions >}}

Now we can put the actual loop in.  This is *similar* to the Scratch
blocks

``` scratch
repeat until <>
```

or

``` scratch
repeat ()
```

but not quite the same.

In Python, we can use a `while` loop, which keeps going as long as a
test gives a `True` answer.  We want to keep asking questions as long
as the index makes sense, i.e., is less than the number of questions.

To see why we need the index to be less than the number of questions,
remember that if there are, say, 5 questions, the index values we want
to go through one at a time are

    0, 1, 2, 3, 4

so the test we want is `question_index < n_questions`.

{{< commit add-while-loop-condition-line >}}

And then we need to move the code to ask the question so that it's
"inside" the `while` loop.

The following change looks fiddly, but all that's happening is that
the code moves across to the right by one indentation level.  You can
do this in the editor by highlighting the code, and pressing the `TAB`
key.

{{< commit indent-what-is-now-while-loop-body >}}

At the end of each time round the loop, we need to move on to next
question by adding one to the index variable:

{{< commit increment-question-index >}}

Finally, we can get rid of the code we copied, since the work is now
being done in our loop:

{{< commit remove-redundant-code >}}

Try your program — it should *still* ask both questions, one after the
other.

It might seem like we've just done a lot of work for no real benefit,
but we're about to see why writing this loop is so useful.


## Add a third question

This is now easy!  We have written our program so that, to add more
questions, the only thing we need to change is the *data*, not the
*code* itself.  This is a powerful idea in computer programming.

To add another question, we just add it to our `all_questions_info`
list near the top of the program:

{{< commit add-third-question >}}


## Add the answer buttons

We're making good progress.  The narrator now asks all the questions,
one after another.

We now need a way for the player to answer the questions.  We'll do
this by adding three buttons.  The player will click on the button for
the answer they think is correct.

We'll start with a button to press if the player thinks "A" is the
right answer.  This is a new sprite, with a costume that's provided
with this tutorial:

{{< commit add-AnswerA-sprite >}}

If you try this, you'll see that the new sprite starts off right on
top of the narrator, which is no good.  Make the button move to a
sensible place when the program starts:

{{< commit init-AnswerA-position >}}

Going a bit more quickly now, we can add a button the player can click
if they think "B" is the right answer.  This is very similar to the
"A" button, but it has a different costume, and different starting
coordinates.

{{< commit add-AnswerB-sprite-and-init-position >}}

And one for "C":

{{< commit add-AnswerC-sprite-and-init-position >}}

You might be thinking that there must be a better way to do this than
copying and pasting and making small changes to the code.  You're
right, but those ways would take us too far astray from this tutorial.


## Wait for player to click an answer button

There are a few ways different Sprites can work together in Pytch.
We're going to use a *shared variable* which will say whether the
player has clicked a button yet for this question.  It's *shared*
because more than one sprite will use it.

The narrator will set the variable to `False` when asking a question,
and each answer button will set it to `True` when it's clicked.

Because the narrator and the three answer sprites all need to work
with this variable, we'll make it *global* by defining it near the top
of the program, outside any sprite:

{{< commit add-global-clicked-variable >}}

In Python, you have to give a starting value to a variable.  We're
using `False` here, because when the program starts, a button has not
been clicked.

The narrator needs to work with this variable, and in Python you need
to say when you're using a global variable:

{{< commit declare-global-clicked-in-Narrator-play-quiz >}}

As soon as the narrator has asked the question, it needs to record the fact
that no button has yet been clicked:

{{< commit clear-clicked-before-asking-question >}}

And then wait until a button has been clicked.  We want to keep doing
nothing as long as `clicked` is `False`.  We can write this test in a
more natural-sounding way by using the `not` operator:

{{< commit busy-wait-Narrator-until-clicked >}}

The `pass` statement here does nothing.  Python needs *some*
statements inside a `while` loop, even if you don't want anything to
happen, so the `pass` statement is what we use.

We won't need the delay any more:

{{< commit remove-wait-2-seconds >}}

This is one half of the problem — we've made the narrator wait until
the `clicked` variable indicates that an answer button has been
clicked.  But nothing is yet setting that variable to `True`, so the
narrator will wait forever!

Each answer needs to respond to being clicked by setting the global
`clicked` variable to `True`.

Moving a bit more quickly now, we need code which says we're using the
global `clicked` variable, and then sets it to `True`.  For the first
answer button (`AnswerA`), the code we need is:

{{< commit add-AnswerA-clicked-handler >}}

And we need the same for `AnswerB`:

{{< commit add-AnswerB-clicked-handler >}}

And for `AnswerC`:

{{< commit add-AnswerC-clicked-handler >}}

Now you should be able to move onto the next question by clicking any
answer button.  Try it!

(Again, if you're wondering whether there's a better way to do all
this than copying and pasting code, you're right, but we don't have
space in this tutorial to discuss it.)


## Check the player's answer

We're now very close to a working quiz game.  The narrator asks
questions, and the player can click on buttons to answer them.  But we
don't tell the player whether they got the questions right.

We need to know *which* answer button the player has clicked.  We'll
use another global variable for this information, so we'll define a
new variable near the top of the program:

{{< commit add-global-answer-variable >}}

The `None` value is a special Python value which means "nothing" or
"no value".  We have to assign *something* to a variable when
declaring it.

Starting with the `AnswerA` sprite, within its
`when_this_sprite_clicked` code, we need to be able to work with this
variable.  Add a declaration:

{{< commit add-global-answer-declaration-to-AnswerA >}}

And add code to set the `answer` variable to the answer chosen by the
player if they click `AnswerA`:

{{< commit assign-answer-var-in-AnswerA >}}

We can do something very similar for `AnswerB`:

{{< commit assign-answer-var-in-AnswerB >}}

And for `AnswerC`:

{{< commit assign-answer-var-in-AnswerC >}}

Back in the narrator, once the `clicked` variable has turned `True`,
we can use the `[4]` item in our `question_info` list to know what the
correct answer is:

{{< commit define-correct-answer-variable >}}

And now we can use an `if`/`else` statement to say something different
depending on whether the player's answer is correct.  Notice that `==`
(two equals signs) is how you ask "are these two things equal?".  It's
easy to confuse this with `=` (just one equals sign), which means "set
a variable".

{{< commit tell-user-whether-answer-correct >}}

Try your quiz now — the narrator should tell you whether you got each
question right or wrong.


## Keep track of the player's score

A nice feature would be to tell the player how many questions they got
right.

We'll keep track of the player's score as they answer the questions
one at a time.  Only the narrator needs to know the score, so we'll
use a *local* variable for this.  At the start of the quiz, the player
has no points, so we'll start `score` off at zero:

{{< commit initialise-local-score-variable >}}

If the player gets a question right, they get a point.  We can add
code inside the `if`/`else` code we used to tell the player whether
they got the question right:

{{< commit award-point-for-correct-answer >}}

After asking all the questions, we want the narrator to announce the
score.  First we'll put together the text of what the narrator will
say.  We have already seen how to glue strings together to make one
big string by using the `+` operator.  But this time it's more
complicated, because the pieces we want to assemble are:

* the string `"You got"`;
* the number of questions the player got right — this is the value of
  the variable `score`;
* the string `"out of"`;
* the total number of questions — this is the value of the variable
  `n_questions`.

But we can't just do

``` python
"You got" + score + "out of" + n_questions
```

because `score` refers to a *number* not a *string*.  Before we can
use `+` to join `"You got"` to the score, we have to convert the value
of `score` into a string.  Python has a built-in function `str()` for
this.

Another detail is that we need to include the space between `"You
got"` and the score, and the spaces around `"out of"`.

Putting this all together, we want to compute

``` python
"You got " + str(score) + " out of " + str(n_questions)
```

We'll store the result in the variable `text`.  Be very careful of the
indentation of the next line of code — it needs to be level with the
`while` at the top of the loop.

{{< commit compute-final-score-text >}}

And then we can make the narrator make the announcement:

{{< commit announce-final-score >}}

Congratulations!  You should now have a working quiz game!


## Challenges

Here are some ways you could improve the quiz:

* Add more questions.

* Play a sound when the user gets an answer right, and a different
  sound if they get an answer wrong.  This tutorial comes with two
  sounds which might be useful for this, or you can use others.

* Make narrator say the player's score so far, after each question has
  been answered.

* (Harder:) Make there be *four* possible answers for each question.
  This tutorial comes with an image of a 'D' button you can use if you
  like.


## Image and sound credits

{{< asset-credits >}}
