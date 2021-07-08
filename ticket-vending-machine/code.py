import pytch


ticket_cost = None


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

    @pytch.when_I_receive("hide-non-chosen")
    def hide_if_not_chosen(self):
        if self.cost != ticket_cost:
            self.hide()
