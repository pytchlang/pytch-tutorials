# Multiple choice quiz

In this project we're going to make a quiz, where the player has to
choose between three possible answers.

---

## Make the narrator

{{< commit add-Narrator-Sprite >}}

{{< commit make-Narrator-announce-quiz >}}


## How to store the quiz questions?

What are parts of a quiz question?  The actual question, the three
possible answers, and something saying which answer is the correct
one.

We're going to use a Python feature called a *list*.  This is very
like a Scratch list, but more powerful in ways we'll see later on.

The items in the list will be

* Question
* Answer A
* Answer B
* Answer C
* Number saying which answer is correct: 0 for A, 1 for B, 2 for C

(Using 0, 1, 2 to match Python convention of counting from zero.)

**TODO for tutorial author: Would we be better to use "A", "B", "C" as
the indicator for correct answer?**

In Python, lists are put between `[]` and have their items separated
by commas (`,`).

{{< commit add-first-question-info >}}

First we'll explore how to use the different pieces of information in
this list.  We'll use the Python built-in function `print()`.

{{< commit print-single-question-info >}}

To see this output, go to the `Output` tab.  Come back to this
`Tutorial` tab when you're ready to continue.

Worth thinking about how to not waste our own time while we're
developing this program.  At the moment, have to wait 3 seconds
every time we run the program.  Adds up, no point.  So we'll shorten
the introduction speech:

{{< commit shorten-lets-play-speech >}}

To get items out of a list, use `[]`s.  Number counts from zero.

{{< commit print-item-0 >}}

{{< commit print-item-1 >}}

{{< commit print-item-4 >}}

Experiment with a list index which doesn't make sense, and see what
happens:

{{< commit print-item-12 >}}

We've finished exploring this now:

{{< commit remove-print-item >}}

## How to store more than one question?

Think ahead to asking more than one question.  Natural thing here is
to put the questions into a list.  In Scratch, the items in a list
have to be strings or numbers (**TODO: or bools, but they might be
coerced to strings?**).  In Python, lists can hold other lists, which
is perfect for us:

{{< commit remove-question-info-assignment >}}

{{< commit create-all-questions-info-list >}}

{{< commit reindent-first-question-info >}}

{{< commit add-trailing-comma-first-question-info >}}

Use some `print()` functions to check we know what's going on:

{{< commit print-all-questions-info >}}

{{< commit print-all-questions-info-item-0 >}}

{{< commit print-all-questions-info-item-0-item-2 >}}

Finished exploring now:

{{< commit remove-print >}}

## Ask a question

Give a name to the info for the question we're going to ask the
player:

{{< commit assign-question-info-temporarily >}}

And pick out the bits.  We don't *have* to do this (we could just keep
saying `question_info[0]` whenever we want to use the question
itself), but it makes the program easier to read by a human, which is
important.

{{< commit assign-actual-question >}}

{{< commit assign-answer-variables-v1 >}}

(You might notice that we haven't used `question_info[4]` yet.  This
holds the index of the correct answer.  We'll use this later.

Now we want to glue these parts together into one string.  In Scratch,
would do something like

``` scratch
(join (question) (join (ans_A) (join (ans_B) (ans_C))))
```

In Python, you can join strings together using the `+` symbol; many
programming languages use `+` for this, because joining two strings
together is a bit like adding them together.

{{< commit concatenate-text-parts >}}

And say the final text:

{{< commit say-concatenated-text >}}

We want to start each answer on a new line.  In a string, the sequence
`"\n"` gets converted into a special character which starts a new
line, so we want to put some of those in:

{{< commit interleave-newlines-in-text >}}

And label the answers so the player knows which one is which:

{{< commit label-answer-A-text >}}

{{< commit label-answer-B-text >}}

{{< commit label-answer-C-text >}}

## Add another question

{{< commit add-centimetres-in-metre-question >}}

Test by adjusting the item we pull out of `all_questions_info`:

{{< commit ask-question-1 >}}

That's working; put it back:

{{< commit ask-question-0-again >}}

## Ask both questions

Want to ask the two questions, one after the other.

Need to wait after asking the first one:

{{< commit add-wait-after-question-0 >}}

Copy and paste the code we already have:

{{< commit copy-paste-to-ask-question-0-again >}}

But this will just ask the first question twice.

Can you work out what we need to change to ask the second question
(which has index `1`) instead of the first question (which has index
`0`) in the copy we've just made of the code?

**TODO: Would be good to have button to only reveal this diff if the
learner clicks "help".**

{{< commit ask-question-1-after-question-0 >}}

## Use a loop to ask both questions

This is going to get annoying when more questions.  Use the idea of a
*loop* to fix the code and make work with any number of questions.

Difference between the copies of the code is in the index we use to
pull out the question.

Make a variable to hold the index of the current question:

{{< commit add-question-index-variable >}}

And use this in the code:

{{< commit use-question-index-when-0 >}}

For second, question, our index variable needs to be `1`:

{{< commit update-question-index-to-1 >}}

And use it:

{{< commit use-question-index-when-1 >}}

### Loop over the questions

In Scratch, you could find out how many items there are in a list
called `all_questions_info` by using this block:

``` scratch
(length of [all_questions_info v])
```

In Python we can do something very similar:

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

In Python, use `while` loop, which keeps going as long as the test
gives a `True` answer.  We want to keep asking questions as long as
the index is valid, i.e., is less than the number of questions.

Remember that if there are, say, 5 questions, the valid indexes are

    0, 1, 2, 3, 4

so the test we want is `question_index < n_questions`:

{{< commit add-while-loop-condition-line >}}

And then we need to move the following code "inside" the `while` loop.

The following looks fiddly but it's just moving all of this code
across to the right by one indentation level.  You can do this in the
editor by highlighting the code, and pressing the `TAB` key.

{{< commit indent-what-is-now-while-loop-body >}}

At the end of each time round the loop, move on to next question:

{{< commit increment-question-index >}}

Get rid of the copy we made, since all now done in the loop:

{{< commit remove-redundant-code >}}

## Add a third question

This is now easy!  We have written our code so that the only thing
that needs changing is the *data*.  This is a powerful idea.

{{< commit add-third-question >}}

## Add the answer buttons

Now need to have some way for the player to answer the questions.

Add a button

{{< commit add-AnswerA-sprite >}}

This starts off right on top of the narrator; no good.  Make button
move to sensible place when program starts:

{{< commit init-AnswerA-position >}}

A button if the player thinks "B" is the right answer:

{{< commit add-AnswerB-sprite-and-init-position >}}

And "C":

{{< commit add-AnswerC-sprite-and-init-position >}}

You might be thinking that there must be a better way to do this than
copying and pasting and making small changes to the code.  You're
right, but those ways would take us too far astray from this tutorial.

## Wait for player to click an answer button

There are a few ways different Sprites can work together.  We're going
to use a *shared variable* which will say whether the player has
clicked a button yet for this question.

The Narrator will set this to `False` when asking a question, and the
Answer buttons will set it to `True` when they're clicked.

Because the Narrator and the three Answer sprites all need to work
with this variable, we'll make it global by defining it near the top
of the program, outside any sprite:

{{< commit add-global-clicked-variable >}}

The Narrator needs to work with this variable, and in Python you need
to say when you're using a global variable:

{{< commit declare-global-clicked-in-Narrator-play-quiz >}}

Once the Narrator has asked the question, it needs to record the fact
that no button has yet been clicked, and then wait until a button has
been clicked.

{{< commit busy-wait-Narrator-until-clicked >}}

And we don't need the delay any more:

{{< commit remove-wait-2-seconds >}}

Each Answer needs to respond to being clicked by setting the global
`clicked` variable to `True`.

**TODO: Does this need breaking down into more steps?**

{{< commit add-AnswerA-clicked-handler >}}

Same for B:

{{< commit add-AnswerB-clicked-handler >}}

And for C:

{{< commit add-AnswerC-clicked-handler >}}

Now you should be able to move onto the next question by clicking any
answer button.

## Check the player's answer

Nearly there.  Need to know *which* Answer button the player has
clicked.  We'll use another global variable for this, so define near
top:

{{< commit add-global-answer-variable >}}

The `None` is a special Python value which means "no value".  We have
to assign *something* to a variable when declaring it.

Within the click handler of each AnswerA, we need to be able to work
with this variable, so declare:

{{< commit add-global-answer-declaration-to-AnswerA >}}

And set to the answer chosen by the player:  **TODO: This makes more
sense if the code is "A" "B" "C" not 0 1 2.**

{{< commit assign-answer-0-in-AnswerA >}}

And same for B:

{{< commit assign-answer-1-in-AnswerB >}}

And C:

{{< commit assign-answer-2-in-AnswerC >}}

Back in the Narrator, we use the `[4]` item in our `question_info`
list to know what the correct answer is:

{{< commit define-correct-answer-variable >}}

And now use an `if`/`else` statement to say something different
depending on whether the player's answer is correct.  Notice that `==`
is how you ask "are these two things equal?"; it's easy to confuse
this with `=`, which means "set a variable".

{{< commit tell-user-whether-answer-correct >}}

## Keep track of the player's score

Only the Narrator needs to know the score, so use a *local* variable
for this.  At start of quiz, player has no points:

{{< commit initialise-local-score-variable >}}

If they get a question right, they get a point:

{{< commit award-point-for-correct-answer >}}

After asking all the questions, the Narrator can announce the score:

Watch indentation here!

{{< commit announce-final-score >}}

**TODO: OK to use f-strings? Or better to use `str()` and `+`?**

Finally, tidy up by putting the introductory announcement back to a
sensible length of time:

{{< commit lengthen-intro-announcement >}}

## Challenges

Add more questions.

Add some sounds for when the user gets a right answer or a wrong one.
Suggested sounds included.

Make narrator say score so far after each question has been answered.

(Harder:) Make there be *four* possible answers for each question.

## Image and sound credits

{{< asset-credits >}}
