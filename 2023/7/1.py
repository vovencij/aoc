# https://adventofcode.com/2023/day/7

from operator import attrgetter

internal_sortable_card_codes = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M"
}

kind_five_of_a_kind = 1
kind_four_of_a_kind = 2
kind_full_house = 3
kind_three_of_a_kind = 4
kind_two_pair = 5
kind_one_pair = 6
kind_high_card = 7

kind_str = {
    kind_five_of_a_kind: "Five of a kind",
    kind_four_of_a_kind: "Four of a kind",
    kind_full_house: "Full house",
    kind_three_of_a_kind: "Three of a kind",
    kind_two_pair: "Two pair",
    kind_one_pair: "One pair",
    kind_high_card: "High Card"
}


class Hand:
    def __init__(self, _hand, _bid):
        self.original_hand = _hand
        self.bid = _bid
        self.sortable_hand = self.to_sortable_hand(_hand)
        self.hand_kind = self.get_hand_kind(self.sortable_hand)

    def __repr__(self):
        return f"(Hand: {self.original_hand}, bid: {self.bid}, Kind: {kind_str[self.hand_kind]}, Internal: {self.sortable_hand})"

    @staticmethod
    def to_sortable_hand(_hand):
        res = ""
        for c in _hand:
            res += internal_sortable_card_codes[c]
        return res

    @staticmethod
    def get_hand_kind(_hand):
        sorted_hand = "".join(sorted(_hand))
        grouped_hand_str = ""
        prev_char = None
        for c in sorted_hand:
            if prev_char is not None and prev_char != c:
                grouped_hand_str += " "
            grouped_hand_str += c
            prev_char = c

        grouped_hand = grouped_hand_str.split(" ")
        group_lengths = []
        for group in grouped_hand:
            group_lengths.append(len(group))

        group_lengths.sort(reverse=True)

        if len(group_lengths) == 1:  # One group -> Five of a Kind (1)
            return kind_five_of_a_kind

        if len(group_lengths) == 2:
            if group_lengths[0] == 4:  # Two groups, one of them is 4 long -> Four of a kind (2)
                return kind_four_of_a_kind
            else:  # Two groups, 2 and 3 then -> Full house (3)
                return kind_full_house

        if len(group_lengths) == 3:
            if group_lengths[0] == 3:  # Three of a kind (4)
                return kind_three_of_a_kind
            else:  # Two pair (5)
                return kind_two_pair

        if len(group_lengths) == 4:  # one pair
            return kind_one_pair

        return kind_high_card  # High card


hands_input = open("input.txt").readlines()
# sample_hands_input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]
hands = []
for hand in hands_input:
    hand_bits = hand.split(" ")
    h = Hand(hand_bits[0], int(hand_bits[1]))
    print(h)
    hands.append(h)


print("=============")
sorted_hands = sorted(hands, key=attrgetter('hand_kind', 'sortable_hand'), reverse=True)
for hand in sorted_hands:
    print(hand)

print("=============")
winning = 0
for i in range(0, len(sorted_hands)):
    winning += (i+1) * sorted_hands[i].bid

print(f"Total winning {winning}")
