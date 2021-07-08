import pytch


ticket_cost = None
money_received = 0


class Ticket(pytch.Sprite):
    Costumes = ["child.png", "adult.png", "family.png"]

    @pytch.when_green_flag_clicked
    def show_tickets(self):
        self.switch_costume("child")
        self.cost = 6
        self.go_to_xy(0, 120)
        pytch.create_clone_of(self)
        self.switch_costume("adult")
        self.cost = 10
        self.go_to_xy(0, 0)
        pytch.create_clone_of(self)
        self.switch_costume("family")
        self.cost = 20
        self.go_to_xy(0, -120)

    @pytch.when_this_sprite_clicked
    def choose_ticket(self):
        global ticket_cost
        ticket_cost = self.cost
        pytch.broadcast_and_wait("hide-non-chosen")
        pytch.broadcast_and_wait("show-money")

    @pytch.when_I_receive("hide-non-chosen")
    def hide_if_not_chosen(self):
        if self.cost != ticket_cost:
            self.hide()
        else:
            self.glide_to_xy(135, 125, 0.75)


class Money(pytch.Sprite):
    Costumes = ["coin-1.png", "coin-2.png", "note-5.png"]

    @pytch.when_green_flag_clicked
    def start_hidden(self):
        self.hide()

    @pytch.when_I_receive("show-money")
    def show_money(self):
        self.switch_costume("coin-1")
        self.value = 1
        self.go_to_xy(-165, -50)
        self.show()
        pytch.create_clone_of(self)
        self.switch_costume("coin-2")
        self.value = 2
        self.go_to_xy(-45, -50)
        pytch.create_clone_of(self)
        self.switch_costume("note-5")
        self.value = 5
        self.go_to_xy(120, -50)

    @pytch.when_this_sprite_clicked
    def insert_money(self):
        global money_received
        money_received += self.value
