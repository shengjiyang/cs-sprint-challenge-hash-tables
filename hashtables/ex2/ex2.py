class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    d = {}
    for ticket in tickets:
        d[ticket.source] = ticket.destination

    route = []
    for ticket in d.keys():
        if ticket == "NONE":
            route.append(d[ticket])

    for i in range(length - 1):
        route.append(d[route[i]])

    return route


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    print(reconstruct_trip(tickets, length=len(tickets)))
