import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = [random.choice(cards), random.choice(cards)]
comp_cards = [random.choice(cards), random.choice(cards)]

print(f"Your initial hand: {user_cards}")
print(f"Computer initial hand: {comp_cards}")

def calculate_sum(hand):
    # Calculate the sum of the hand and adjust for the presence of an 11
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

while calculate_sum(user_cards) < 21:
    another_card = input("Do you want another card? (Yes/No): ")
    if another_card.lower() == "yes":
        user_cards.append(random.choice(cards))
        print(f"Your hand: {user_cards}")
    else:
        break

while calculate_sum(comp_cards) < 17:
    comp_cards.append(random.choice(cards))

print(f"Your final hand: {user_cards} (Sum: {calculate_sum(user_cards)})")
print(f"Computer final hand: {comp_cards} (Sum: {calculate_sum(comp_cards)})")

if calculate_sum(user_cards) > 21:
    print("You went over. You lose.")
elif calculate_sum(comp_cards) > 21:
    print("Computer went over. You win!")
elif calculate_sum(user_cards) == calculate_sum(comp_cards):
    print("It's a draw!")
elif calculate_sum(user_cards) > calculate_sum(comp_cards):
    print("You win!")
else:
    print("You lose. Computer wins.")
