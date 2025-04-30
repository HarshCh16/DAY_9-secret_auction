from ascii_art import logo

print(logo)

print("Welcome to the Secret Auction Program.")

user_inputs = {}

bidders_left = True

while bidders_left == True:

    name = input("What is you name?\n")
    bid = int(input("What\'s your bid?\n$"))

    user_inputs[name] = bid

    bidders_left = input("Are there any other bidders? Type \'yes' or \'no'.\n").lower()

    if bidders_left == "no":
        bidders_left = False
    elif bidders_left == "yes":
        bidders_left = True

    print("\n" * 1)

highest_bid = 0
winner = ""

for key in user_inputs:
    if user_inputs[key] > highest_bid:
        highest_bid = user_inputs[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}.")