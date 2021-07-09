# A vending machine for tickets

We will make a simulation of a vending machine which sells tickets for
a theme park.  The customer chooses between three sorts of tickets,
which have different prices.  The customer then pays using coins or
notes.  The machine displays how much change the customer should
receive.

The available tickets are:

* An adult ticket (€10)

* A child ticket (€6)

* A family ticket (€20)

Once a ticket has been chosen, the customer can insert €1 or €2 coins,
or €5 notes, until they have inserted enough money to pay for the
ticket.  If they have put in more than required, the machine will
display how much change the customer is owed.

---

## Main parts of the program

Before we start writing any code, our first job is to think about how
to break down the program into smaller chunks.  We will then write
code for the parts one at a time, probably breaking each one into
smaller parts as we go long.

From the task description, we can see that there are three main parts,
which happen in this order:

1. Let the customer choose a ticket.

1. Let the customer pay for that ticket.

1. Give the customer their ticket and show their change.

We will now say a bit more about each of these steps, and then start
work.

#### Choosing the ticket

We will show the three tickets, and let the customer click on the one
they want.

#### Paying for the ticket

Once we know what ticket the customer wants, we will show the two
coins and one note, and let the customer click on them until they have
added enough money.

#### Showing the change

Once the customer has put enough (or maybe too much) money in, the
machine should deliver the chosen ticket, and also show the customer
how much change to expect.


## Add a Sprite for the tickets

We want the customer to see the three ticket types, and be able to
click on one of them to make their choice.  The screen will look like
this:

TODO: Screenshot **PICTURE**.

We will create a Sprite for the tickets.  We could make three Sprites,
one for each sort of ticket, but that would lead to a lot of copied
code.  Instead we will make just one Sprite, and use *clones* to show
the different types of ticket.

Our first job is to create a `Ticket` Sprite, and say that its
costumes are the provided images of the three types of ticket:

{{< commit add-Ticket-sprite >}}

Can you predict what will happen if you build the project now?  Once
you've made your prediction, run the code and see if you were right.


## Show all ticket types

We will write code to display the ticket types when the green flag is
clicked.

We will start by moving the `Ticket` sprite to the right place for the
child ticket.  This is in the centre, left-to-right, and quite near
the top.

{{< commit show-child-ticket >}}

You can adjust the `120` in that piece of code if you think the ticket
should be a bit higher or lower.  Experiment until you're happy with
it.

To also show the adult ticket, we need to make a *clone* of the
`Ticket` sprite, and make the original `Ticket` move to where we want
the adult ticket to be.  There will be two snippets of code:

    self.switch_costume("adult")
    self.go_to_xy(0, 0)

(which will make the `Ticket` change to the adult-ticket costume and
move to the middle of the stage), and

    pytch.create_clone_of(self)

(which will make a clone of the `Ticket` exactly as it is when the
`create_clone_of()` function is called).  We need to decide the
right order for these two snippets.  Should we

* Make the clone and then move the original to the new position with
  the new costume?

* Move the original to the new position with the new costume and
  then make the clone?

Decide which order you think is correct, then look at the change below
to see whether you were right:

{{< commit show-adult-ticket >}}

We need to make a clone of the `Ticket` while it's still showing the
`child` costume, and then move it to its new position and make it
change to the `adult` costume.

Finally, we can do the same thing to show the `family` ticket.  We
create a clone of the `Ticket` which is showing the adult ticket, and
then move to the right place to show the `family` ticket and switch to
that costume:

{{< commit show-family-ticket >}}


## Make each Ticket clone know its cost

As well as being in different places on the screen, there is another
way we need the tickets to be different — they should all cost
different amounts.  We will do this by storing the cost of each ticket
in a variable belonging to that clone.  We will put these code lines
in just below the ones which switch the costume, to make sure we get
the right cost with the right costume.

{{< commit store-ticket-costs >}}


## Store cost of chosen ticket

Once the customer clicks on one of the tickets, our program needs to
remember the cost of that ticket.  We will use a global variable for
this.  When the program starts, the customer hasn't chosen a ticket
yet, so we will set the initial value to `None`, which is the Python
way of saying 'no value'.

{{< commit declare-global-ticket-cost >}}

We now want each ticket clone to react to being clicked, by storing
its own cost into that global variable.  We can do this by writing a
method and asking Pytch to run it when the sprite is clicked.  We can
do this because each clone knows its own cost.  One wrinkle here is
that we need to tell Python that we want to set the value of the
global `ticket_cost` variable, by saying `global ticket_cost`.
Without this, the code would set a new variable `ticket_cost` just
for use inside our method.

{{< commit set-cost-when-chosen >}}


## Test the program so far

When we were showing the ticket types, it was obvious whether our
program was working — we could tell just by looking at the screen
whether the tickets were appearing in the right places with the right
costumes.  But we can't tell whether we're setting the global
`ticket_cost` variable correctly.

Temporarily, we will *show* this variable once we've set it, just to
be able to test our program.  We'll add this line to the
`choose_ticket()` method:

{{< commit show-ticket-cost-value >}}

If you now build and green-flag your program, and click on one of the
tickets, you should see the correct `ticket_cost` shown in the watcher
at the top-left of the stage.

It's a good idea to do this for each of the three tickets, to make
sure everything's working.

Once you're happy, take out that line again:

{{< commit undo-show-ticket-cost-value >}}


## Show only the chosen ticket

We need to give some feedback to the customer once they have clicked
on the ticket they want.  We'll make the other ticket clones
disappear, leaving just the chosen one.

First we will write the method that does this, and then make it happen
when a ticket is chosen.  The question is:

* How does a clone know whether it is the chosen one?

By the time our program has to ask this question, it can assume that
the global `ticket_cost` variable has been set to the cost of the
chosen ticket.  So each clone can compare its own cost to the chosen
cost.  If they're the same, that clone was the chosen one.

We can now write the code which hides a ticket clone if it is *not*
the chosen one:

{{< commit define-hide-if-not-chosen-method >}}

What do you think will happen now if you run your program and click on
a ticket?  Try it and see, then read on.

The program does in fact *not* yet hide the other tickets, because we
have not said when we want our new `hide_if_not_chosen()` method to
run.  We'll fix that now, by using a broadcast message.  When a ticket
is chosen, it will broadcast a message, which *all ticket clones* will
listen for:

{{< commit broadcast-hide-non-chosen >}}


## Move the chosen ticket into the corner

To make room to show the money, we want to animate the chosen ticket
into the corner of the stage.  We can do this within the same
`hide_if_not_chosen()` method, by adding an `else` clause saying what
to do if the clone *is* the chosen one:

{{< commit glide-chosen-ticket-to-top-right >}}

The *x* number (135) and *y* number (125) here took some experimenting
to make the ticket go to a sensible place.  You can adjust them if you
prefer the ticket to be a bit closer to or further from the corner of
the stage.

We've now completed the first part of the task: Let the customer
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

Our next job will be to write code to show the money.


## Show the different sorts of money

To show the different sorts of money (two coins and one note), we can
re-use the ideas we used for showing the ticket types.  Copying the
way that code did it, we can write a method `show_money()` for our
`Money` sprite:

{{< commit show-coins-and-note >}}

We now need to think about this question:

* When should the money appear?

And the answer is that it should appear once the chosen ticket has
finished its behaviour in reponse to the `"hide-non-chosen"` message.
We can give the `Ticket` sprite's `choose_ticket()` method the job of
sending a message for the `Money` sprite to respond to.  First we go
back to the `Ticket` sprite and add code to send a suitable message:

{{< commit broadcast-send-money >}}

And the other part is to tell Pytch that the `show_money()` method
inside our `Money` sprite should run when it hears this message:

{{< commit receive-show-money >}}


## Make each Money clone know its value

Each `Money` clone needs to know the value of the coin or note it
represents.  This is a very similar problem to when we had to make
sure each `Ticket` clone knew how much it costs.  So we will give each
`Money` clone a `value` variable, set to the number of euro it
represents:

{{< commit assign-value-to-money >}}


## Track money received

We now need to let the customer click on the coins or note, and keep
track of how much money (in euro) the machine has received from the
customer.  We will use another global variable — `money_received` —
for this.  We'll declare it near the top of our program.  At the start
of the program, no money has been received, so we initialise it to
zero:

{{< commit declare-global-money-received >}}

And then when a `Money` clone is clicked, it should increase this
`money_received` variable by that clone's own `value`:

{{< commit accumulate-money-received >}}

We're now facing another familiar problem — we don't know whether our
code is working, because we can't see the value of the
`money_received` variable.  As earlier, we'll *show* this variable,
after we've arranged the `Money` clones correctly:

{{< commit show-money-received >}}

Before, we took this code out once we were happy the code was working,
but we'll keep this code in, to simulate the machine having a display
showing money received.

Now **test your code**!  Click build, then green-flag, then choose a
ticket and check the `money_received` display updates correctly as
you click on the coins or note.


## Detect when enough money received

As the program is now, the customer keeps putting in more and more
money and never gets their ticket or their change.  We need to fix
this.

We need our program to check whether the amount of money received is
at least as much as the cost of the chosen ticket.  The only place
that this can become true is just after the customer has inserted more
money.  So we can add code to the `insert_money()` method of the
`Money` sprite to check this.

What do we want to happen when the customer has inserted enough money?

* Our program should work out how much change the customer needs —
  this can be zero if the customer has inserted exactly the right
  amount of money.

* The display of `money_received` should disappear, and be replaced
  with a display of how much change the customer is owed.

* The `Money` clones should all disappear.

One way to do this will be to use a new variable to store the amount
of change needed.  We'll declare this at the top of our program:

{{< commit declare-global-change-needed >}}

And now we can add the `if` logic.  We need to ask the question

* Has enough money been received?

in terms of the variables of our program.  In words, we ask

* Is 'money received' greater than (or equal to) 'ticket cost'?

which translates into code as

    if money_received >= ticket_cost:
        # ... Code to run if enough money inserted ...

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

{{< work-in-progress >}}


## Extra challenge


Instead of just showing the change as a number, show the coins that
the customer should get back.  We know that the most change a customer
will ever need is €4, so it will be easiest to just write code for
each of the five cases (no change, €1, €2, €3, €4), rather than try to
work out a general change-giving algorithm.


## Notes to self

State of which ticket is chosen is in two parts: the global
`ticket_cost` variable, and the "shown" state of the matching
clone.
