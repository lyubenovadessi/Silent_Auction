import auction_logo
print(auction_logo.auction_logo)

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}

is_bidding = True
while is_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    while (should_continue := input("Are there any other bidders? Type 'yes' ot 'no': \n").lower()) not in ('yes', 'no'):
        print("Please enter yes or no.")
    if should_continue == "no":
        is_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
