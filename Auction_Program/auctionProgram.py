from art import logo
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

bids = {}
bidding_finished = False


def highest_bidder(bidding_record):
    """Checks bids and display highest bidder"""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with bid of ${highest_bid}")


# if other bidders, keep running the program
while not bidding_finished:
    name = input("What is your Name: ")
    bidPrice = int(input("What is your Bid?:$ "))
    # Add key-name and value- bidPrice to empty dict
    bids[name] = bidPrice

    # Ask user if there are any other bidder
    otherBidder = input("Are there any other bidders? Type 'yes' or 'no'")

    # Stop program if no other bidders
    if otherBidder == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif otherBidder == "yes":
        # Clears the terminal
        clear()
