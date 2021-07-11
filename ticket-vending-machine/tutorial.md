# A vending machine for tickets

Our task is to make a simulation of a vending machine selling
tickets for a theme park.  The customer chooses between three sorts of
tickets, which have different prices.  The customer then pays using
coins or notes.  Finally, the machine displays how much change the
customer should receive.

The available tickets are:

* An adult ticket (€10)

* A child ticket (€6)

* A family ticket (€20)

Once a ticket has been chosen, the customer can insert €1 or €2 coins,
or €5 notes.

(This project was suggested as part of the course [*Programming
Pedagogy in Secondary Schools: Inspiring Computing
Teaching*](https://www.futurelearn.com/courses/secondary-programming-pedagogy)
published by the Raspberry Pi Foundation on the FutureLearn platform.)

---

## Planning: Main parts of the program

Before we start writing any code, our first job is to think about how
to break down the program into smaller chunks.  We will then write
code for the parts one at a time, breaking each part down further as
we go along.

From the task description, we can see that there are three main parts,
which happen in this order:

1. Let the customer choose a ticket.

1. Let the customer pay for that ticket.

1. Show how much change the customer needs.

We will now think a bit more about what has to happen in each of these
steps, and then start work.

#### Choosing the ticket

We will show the three tickets, and let the customer click on the one
they want.  We'll need to remember which ticket they chose.

#### Paying for the ticket

Once we know what ticket the customer wants, we will show the two
coins and one note, and let the customer click on them until they have
added enough money.  We'll need to keep track of how much money has
been received by the machine.

#### Showing the change

Once the customer has put enough (or maybe too much) money in, we'll
need to work out how much change the customer needs (if any), and show
this amount.


## Add a Sprite for the tickets

We want the customer to see the three ticket types, and be able to
click on one of them to make their choice.  The screen will show the
three tickets in a column, like this:

![Ticket menu](ticket-type-menu.png#img-float-left)

Just as we would do in Scratch, we will create a Sprite to be the
tickets.  We could make three Sprites, one for each sort of ticket,
but that would lead to a lot of copied code.  Instead we will make
just one Sprite, and use *clones* to show the different types of
ticket.

Our first job is to create a `Ticket` Sprite, and say that its
costumes are the three types of ticket.  Images for these tickets are
supplied as part of this tutorial — you can switch over to the "Images
and sounds" tab to see, and then switch back to this "Tutorial" tab.

In Pytch, you create a Sprite by *defining a `class`* for that Sprite,
with code like:

    class Ticket(pytch.Sprite):

then the code for that Sprite goes next.  You'll see this shortly.

In Pytch, you say what costumes a Sprite has by setting a `Costumes`
variable inside that Sprite.  You set `Costumes` to a Python list of
the images you want to use for costumes.  (You can do more advanced
things with costumes, but we won't need that for this project.)

Putting that all together, the starting code for our `Ticket` sprite
looks like this:

{{< commit add-Ticket-sprite >}}

Add those lines to your code, and try to predict what will happen when
you build it.  Then click `BUILD` and see whether you were right.


## Show all ticket types

We will write code to display all three ticket types when the green
flag is clicked.

### Child ticket

We start by moving the `Ticket` sprite to a good place for the child
ticket.  This is centred left-to-right, and quite near the top.  This
should happen when the green flag is clicked.  In Scratch, we would
put together a script like this:

![When-green-flag-clicked for child ticket](child-ticket-green-flag.png#img-center)

And in Pytch we do something very similar — add this code to your
program:

{{< commit show-child-ticket >}}

The main difference is that in Pytch we have to give the method a
name; `show_tickets()` is short and describes what the method does.

You can adjust the `120` in that piece of code if you think the ticket
should be a bit higher or lower.  Experiment until you're happy with
it.

### Adult ticket

To also show the adult ticket, we need to make a *clone* of the
`Ticket` sprite, and change the original `Ticket`'s costume to the
adult ticket, and move it to where we want the adult ticket to be.

There will be two snippets of code, which should look familiar
compared to the blocks you would use in Scratch.

One snippet will make the `Ticket` change to the adult-ticket costume and
move to the middle of the stage:

    self.switch_costume("adult")
    self.go_to_xy(0, 0)

And the other snippet will make a clone of the `Ticket`, exactly as it
is when the snippet runs:

    pytch.create_clone_of(self)

We need to decide the right order for these two snippets.  Should we

* Make a clone and then move the original to the new position with the
  new costume?

* Move the original to the new position with the new costume and then
  make a clone?

Decide which order you think is correct, then look at the new code
below to see whether you were right:

{{< commit show-adult-ticket >}}

The right order is to make a clone of the `Ticket` while it's still
showing the `child`-ticket costume, and then make the original
`Ticket` change to the `adult`-ticket costume and move to its new
position.

(Try to predict what would happen if you had the `create_clone_of()`
call after the `switch_costume()` and `go_to_xy()` calls.  Then
temporarily change the code, run it, and see if you were right.)

### Family ticket

Finally, we can do the same thing to show the `family` ticket.  We
create a clone of the `Ticket` which is showing the adult ticket, and
then switch the original `Ticket` to the `family`-ticket costume and
move it to the correct place.

{{< commit show-family-ticket >}}


## Make each Ticket clone know its cost

As well as being in different places on the screen, there is another
way we need the tickets to be different — they should all cost
different amounts.  We will store the cost of each ticket in a
variable belonging to that clone.  These variables work very like
Scratch's "for this Sprite only" variables.  In Python, though, you
just assign to a variable.  There is no separate step to create the
variable.

We will put the lines of code which set this variable just below the
lines which switch the costume, to make sure we get the right cost
with the right costume.

{{< commit store-ticket-costs >}}

When each clone is created, part of the cloning process is to copy the
`cost` variable, with its value at the moment the clone was created.
This way we end up with three `Ticket`s, each having their own `cost`
variable.

## Remember cost of chosen ticket

Once the customer clicks on one of the tickets, our program needs to
remember the cost of that ticket.  We will use a global variable for
this.  Global variables in Pytch are very like Scratch's "for all
Sprites" variables.  In Python, we can assign to a variable at the
"top level" of our program, which means outside any function, class,
or method.  Often we put this assignment near the top of the program.

When our program starts, the customer hasn't chosen a ticket yet, so
we will set the variable's initial value to `None`, which is the
Python way of saying 'no value'.  The code looks like this:

{{< commit declare-global-ticket-cost >}}

We now want each ticket clone to react to being clicked, by storing
its own cost into that global variable.  We can use the value of each
ticket's own `cost` variable.  We will write a method and ask Pytch to
run it when the sprite is clicked.  In Scratch, this would look like:

![Set global ticket-cost when Ticket clicked](set-ticket-cost.png#img-center)

And in Pytch, we have to give this method a name, and then the idea is
the same:

{{< commit set-cost-when-chosen >}}

One detail in this code is that we need to tell Python that we want to
set the value of the *global* `ticket_cost` variable.  We tell Python
this by saying `global ticket_cost`.  Without this, the code would set
a new variable `ticket_cost` which would exist just inside our method.

## Test the program so far

When we were writing code to show the ticket types, it was obvious
whether our program was working — we could just look at the screen to
see whether the right tickets were appearing in the right places.  But
we can't tell whether we're setting the global `ticket_cost` variable
correctly.

Temporarily, we will *show* this variable once we've set it, just to
be able to test our program.  In Scratch we would either tick the box
next to the variable, or include the block

![Show global ticket-cost](show-ticket-cost.png#img-center)

in a script.  In Pytch, we'll add this line to the `choose_ticket()`
method:

{{< commit show-ticket-cost-value >}}

Using `None` for the first argument to `show_variable()` means that we
want to show a global variable.

If you now build and green-flag your program, and click on one of the
tickets, you should see the correct `ticket_cost` shown in the watcher
at the top-left of the stage.

(As an experiment, temporarily take out, or comment out, the `global
ticket_cost` line.  Try to predict what will happen when you click on
a ticket.  Then run the code and see if you were right.  Put the line
back after you have investigated this.)

It's a good idea to do the test for each of the three tickets, to make
sure everything's working.

Once you're happy, take out the `show_variable()` line again:

{{< commit undo-show-ticket-cost-value >}}


## Show only the chosen ticket

We need to give some feedback to the customer once they have clicked
on the ticket they want.  We'll make the other ticket clones
disappear, leaving just the chosen one.

First we will write the method that does this, and then make it happen
when a ticket is chosen.  The question is:

* How does a clone know whether it is the chosen one?

By the time our program has to ask this question, the global
`ticket_cost` variable will be set to the cost of the chosen ticket.
So each clone can compare its own cost to the chosen cost.  If they're
the same, that clone was the chosen one.  Flipping this round, a
`Ticket` clone is *not* the chosen one if its own cost is *not equal
to* the chosen ticket's cost.  In code, this test is

    self.cost != ticket_cost

because `!=` is the Python operator for 'not equal to'.

**TODO:** Or:  Initially set `was_chosen` to false on all clones.
Inside on-click, set that clone's `was_chosen` to True.  Test
`was_chosen` in `hide_if_not_chosen()`.  Better/worse?

We can now write the code which hides a ticket clone if it is not
the chosen one:

{{< commit define-hide-if-not-chosen-method >}}

What do you think will happen now if you run your program and click on
a ticket?  Try it and see, then read on.

The program does in fact *not* yet hide the other tickets, because we
have not said when we want our new `hide_if_not_chosen()` method to
run.  It is exactly as if we had built this Scratch script:

![Hide Ticket if not chosen](hide-ticket-if-not-chosen.png#img-center)

but not put a 'hat block' on top.

We'll fix this now, by using a broadcast message.  When a ticket is
chosen, it will broadcast a message, which we will make *all ticket
clones* listen for with a `when_I_receive()` decorator:

{{< commit broadcast-hide-non-chosen >}}

### Test the code!

Run the code now to check it does what it should.  To be thorough,
check that the program works correctly for all choices of ticket.


## Move the chosen ticket into the corner

To make room to show the coins and note, we will animate the chosen
ticket into the corner of the stage.  We can do this within the same
`hide_if_not_chosen()` method, by adding an `else` clause saying what
to do if the clone *is* the chosen one:

{{< commit glide-chosen-ticket-to-top-right >}}

The *x* number (`135`) and *y* number (`125`) here took some
experimenting to make the ticket go to a sensible place.  You can
adjust them if you prefer the ticket to be a bit closer to or further
from the corner of the stage.  Experiment until you're happy with how
it looks.

What would happen if you changed the third number (`0.75`) in this
code?  Try it and see.

We've now completed the first part of the task: The customer can
choose the ticket they want.  Next we'll let the customer insert coins
or notes to pay for their ticket.


## Add a Sprite for the money

To show the different sorts of money (two coins and one note), we can
use the same ideas that we used for the tickets.  First we will add a
Sprite for the money, giving it three costumes:

{{< commit add-Money-sprite >}}

There will be a problem if you build your program now, though.  Can
you predict what will go wrong?

The problem is that a €1 coin will be in the middle of the stage, in
the way of the adult ticket.  To fix this, we need to make the `Money`
sprite hide itself when the simulation starts:

{{< commit hide-money-on-green-flag >}}

Our next job will be to write code to show the money at the right
time.


## Show the different sorts of money

![Money types in row](money-types-in-row.png#img-float-right)

To show the different sorts of money (two coins and one note), we can
re-use the ideas we used for showing the ticket types.  Copying the
way that code did it, we add a method `show_money()` to our `Money`
sprite.  The method sets costumes, moves, and makes clones exactly as
the `Ticket` sprite did.  This time, we'll arrange the money
horizontally across the centre of the stage, as shown to the right:

Because we've done this before, here is the code all in one piece:

{{< commit show-coins-and-note >}}

We have *not* yet put a decorator ('hat block') on this method,
because we first need to think about this question:

* When should the money appear?

And the answer is that it should appear once the chosen ticket has
finished moving to the corner.  We can give the `Ticket` sprite's
`choose_ticket()` method the job of sending a message for the `Money`
sprite to respond to.  First we go back to the `Ticket` sprite and add
code to broadcast a suitable message:

{{< commit broadcast-send-money >}}

And we also tell Pytch that the `show_money()` method inside our
`Money` sprite should run when it hears this message:

{{< commit receive-show-money >}}

### Test the code!

Run the program now, choose a ticket, and check that the money appears
in the right place once the chosen ticket has moved to the corner.


## Make each Money clone know its value

Each `Money` clone needs to know the value of the coin or note it
represents.  This is a very similar problem to when we had to make
sure each `Ticket` clone knew how much it costs.  So we will give each
`Money` clone a `value` variable, set to the number of euro it's worth:

{{< commit assign-value-to-money >}}


## Track money received

We now need to let the customer click on the coins or note, and keep
track of how much money (in euro) the machine has received from the
customer.  A global variable — `money_received` — will let us do this.
We'll declare it near the top of our program.  When the program starts
running, no money has been received, so we initialise the variable to
zero:

{{< commit declare-global-money-received >}}

When a `Money` clone is clicked, it should increase this
`money_received` variable by the clicked clone's own `value`.  In
Scratch, we could use a 'change variable' block, like:

![Accumulate value into money-received](accumulate-value-into-money-received.png#img-center)

In Python, we can use the `+=` operator, which does the same job.
Remember we need to declare `global money_received` to tell Python we
want to update a global variable.

{{< commit accumulate-money-received >}}

We're now facing another familiar problem — we don't know whether our
code is working, because we can't see the value of the
`money_received` variable.  As earlier, we'll *show* this variable,
after we've arranged the `Money` clones correctly in the
`show_money()` method:

{{< commit show-money-received >}}

Before, we took this code out once we were happy the rest of the code
code was working, but this time we'll leave the `money_received`
variable shown, to simulate the machine having a display showing how
much money has been received.

### Test the code!

Click build, then green-flag, then choose a Ticket.  Now check the
`money_received` display updates correctly as you click on the coins
or note.  Each time you click on a coin or note, the display should
update by the right amount.

Have we finished the whole task now?  If not, what's the next step?


## Planning: Detect when enough money received

We've mostly done the second part of the task — the customer can pay
for their ticket.  But it isn't quite done yet.  As the program is
now, the customer keeps putting in more and more money and never gets
their ticket or their change.

We need our program to check whether the amount of money received is
at least as much as the cost of the chosen ticket.  The only place
that this can become true is just after the customer has inserted more
money.  So we can add code to the `insert_money()` method of the
`Money` sprite to check whether the customer has now paid enough.

What do we want to happen when the customer has inserted enough money?

* Our program should work out how much change the customer needs —
  this can be zero if the customer has inserted exactly the right
  amount of money.

* The display of `money_received` should disappear, and be replaced
  with a display of how much change the customer is owed.

* The `Money` clones should all disappear.

Think about how you can check whether the customer has given the
machine enough money, and how you can make the above things happen,
before reading on.


## Compute amount of change needed

One way to do this will be to use a new variable to store the amount
of change needed.  We'll declare this at the top of our program,
initialising it to `None` because when the program starts running, we
don't know how much change will be needed.

{{< commit declare-global-change-needed >}}

And now we can add the `if` logic.  We need to ask the question

* Has enough money been received?

In terms of the variables of our program, we ask

* Is `money_received` greater than (or equal to) `ticket_cost`?

In Scratch, you cannot ask 'greater than or equal to' in one step.
You would have to use one of these two pieces of code:

![money-received >= ticket-cost](money-received-GE-ticket-cost.png#img-center)

Python has the `>=` operator to mean 'greater than or equal to', so we
can translate the question into Python code as

    if money_received >= ticket_cost:
        # ... Code to run if enough money has been inserted ...

The first task from our list above is to work out the amount of change
needed.  To find this, we subtract the cost of the ticket from the
amount of money received — for example, if the ticket is €6 and the
customer has given us €10, they need €10−€6=€4 change.  In code, this
will be

    change_needed = money_received - ticket_cost

but again we need to make sure Python knows we're talking about the
*global* `change_needed` variable.  Putting this all together, we'll
add in the `if` statement, starting with the code to compute the
amount of change needed:

{{< commit compute-change-needed >}}

The next task is 'replace display of money-received by display of
change-needed'.  It is cleanest to do this by hiding the
`money_received` variable and then showing the `change_needed`
variable.  We add code inside the `if` statement:

{{< commit show-change-needed-not-money-received >}}

(It would work to do these two things in the other order, but it's
cleaner to take away the old display before adding the new one.)

Finally, we need to hide all the money clones.  We do this with a
broadcast message, since we want *all* clones to hide, not just the
one which was just clicked on.  First we define the method on `Money`
which will make each clone hide:

{{< commit define-hide-money-method >}}

and then tell Pytch to run this method when the sprite receives a
suitable message:

{{< commit receive-hide-money >}}

and finally broadcast that message as the last task once we know
enough money has been received:

{{< commit broadcast-hide-money >}}


## Test the complete program

Think about how you can thoroughly test your program.  Does it always
compute the right amount of change?  Does it work if you give the
machine the exact money, as well as too much money?  What other ways
can you test it?

## Challenges

Here are some ideas you could use to make the program better.  Can you
think of others?

### Simulate dispensing the ticket

When the customer has inserted enough money, our vending machine shows
them the change they need.  The chosen ticket stays at the top of the
screen.  Can you simulate giving the customer the ticket, maybe by
smoothly moving the ticket to the centre of the screen?  Experiment
with the sequencing of hiding the coins and note, hiding the 'money
received' display, showing the change, and dispensing the ticket.
Which sequence looks best?

### Show the change in coins

Instead of just showing the change as a number, show the coins that
the customer should get back.  The most change a customer will ever
need is €4.  (Can you see a good argument why this is true?)  So it
will be easiest to just write code for each of the four cases where
change is needed (€1, €2, €3, €4), rather than try to work out a
general change-giving algorithm.
