# Create dictionary
auction_dictionary = {
    "A": 121,
    "B": 131,
    "C": 118,
    "D": 125,
}

x = 0
y = 0
for key in auction_dictionary:
    y = auction_dictionary[key]
    x = max(x, y)

print(x)