from random import choice

"""Initial lottery choices and winning ticket"""
lottery = ['J', 7, 'K', 88, 'L', 'B', 34, 53, 14, 'S', 20, 92, 78, 11, 49]
ticket = []

"""Create winning ticket with 5 characters"""
while len(ticket) < 5:
    winning = choice(lottery)

    if winning not in ticket:
        ticket.append(winning)
        
print("Winning ticket:")
print(ticket)
