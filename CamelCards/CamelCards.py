import functools

file = open("input.txt")

ranks = ['high', '1p', '2p', '3k', 'full', '4k', '5k']
card_ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def compare(player1, player2):
    hand1, type1, _ = player1
    hand2, type2, _ = player2
    if ranks.index(type1) < ranks.index(type2):
        return -1
    elif ranks.index(type1) > ranks.index(type2):
        return 1
    else:
        for i in range(len(hand1)):
            if card_ranks.index(hand1[i]) < card_ranks.index(hand2[i]):
                return -1
            elif card_ranks.index(hand1[i]) > card_ranks.index(hand2[i]):
                return 1
    return 0


cards = []
for line in file:
    hand, val = line.strip().split()
    hand_t = 'high'
    max_appear = 1
    hand_count = dict()
    for char in hand:
        hand_count[char] = hand_count.setdefault(char, 0) + 1
    count_hand = dict()
    for key, num in hand_count.items():
        if key == 'J':
            continue
        if num in count_hand:
            count_hand[num].append(key)
        else:
            count_hand[num] = [key]
    jokers = hand_count.get('J', 0)
    if 5 - jokers in count_hand or jokers == 5:
        hand_t = '5k'
    elif 4 - jokers in count_hand:
        hand_t = '4k'
    elif (3 in count_hand and 2 in count_hand) or (2 in count_hand and len(count_hand[2]) == 2 and jokers == 1):
        hand_t = 'full'
    elif 3 - jokers in count_hand:
        hand_t = '3k'
    elif 2 in count_hand and len(count_hand[2]) == 2:
        hand_t = '2p'
    elif 2 - jokers in count_hand:
        hand_t = '1p'
    cards.append((hand, hand_t, int(val)))

cards.sort(key=functools.cmp_to_key(compare))

total = 0
for i in range(len(cards)):
    total += cards[i][2] * (i + 1)
print(total)