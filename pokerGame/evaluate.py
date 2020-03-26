from collections import defaultdict

# I have created a class Evaluation due to the necesity of determine the type of the hand we have

# general observation: I analize the numbers of the cards in order to know how many
# of these have a repetition  
class Evaluation:
	def __init__(self, hand):
		self.hand = hand

	def check_royal_flush(self):

		hand = self.hand
		royal = ["A", "K", "Q", "J", "T"]

		flag = [True, "It is royal flush"]
		if self.check_straight_flush():

			values = [card[0] for card in hand]

			for value in values:
				aux = self.search_in_list(value, royal)[0]

				if aux == False:
					flag = [False, "La carta no es royal"]

			return flag
		else:
			return [False, "no es straigth flush"]

	def check_straight_flush(self):  # verified
		hand = self.hand

		if self.check_flush() and self.check_straight():
			return True
		else:
			return False

	def check_four_of_a_kind(self):  # verified
		hand = self.hand

		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		if sorted(value_counts.values()) == [1, 4]:
			return True
		return False

	def check_full_house(self): 
		hand = self.hand

		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		if sorted(value_counts.values()) == [2, 3]:
			return True
		return False

	def check_flush(self):  
		hand = self.hand

		suits = [card[1] for card in hand]
		if len(set(suits)) == 1:
			return True
		else:
			return False

	def check_straight(self): 
		hand = self.hand
		card_order_dict = {
			"2": 2,
			"3": 3,
			"4": 4,
			"5": 5,
			"6": 6,
			"7": 7,
			"8": 8,
			"9": 9,
			"T": 10,
			"J": 11,
			"Q": 12,
			"K": 13,
			"A": 14,
		}
		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		rank_values = [card_order_dict[i] for i in values]
		value_range = max(rank_values) - min(rank_values)
		if len(set(value_counts.values())) == 1 and (value_range == 4):
			return True
		else:
			# check straight with low Ace
			if set(values) == set(["A", "2", "3", "4", "5"]):
				return True
			return False

	def check_three_of_a_kind(self): 
		hand = self.hand

		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		if set(value_counts.values()) == set([3, 1, 1]):
			return True
		else:
			return False

	def check_two_pairs(self):  # verified
		hand = self.hand

		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		if sorted(value_counts.values()) == [1, 2, 2]:
			return True
		else:
			return False

	def check_one_pairs(self):  # verified
		hand = self.hand

		values = [card[0] for card in hand]
		value_counts = defaultdict(lambda: 0)
		for v in values:
			value_counts[v] += 1
		if 2 in value_counts.values():
			return True
		else:
			return False

	# this is the general evaluation. I give them a number based on the strong of the hand
	# If two hands have the same value (same category) i have to solve the tie with another function which is
	# in the other library -> Poker.py 
	def evaluate_hand(self):
		hand = self.hand

		if self.check_royal_flush()[0]:
			return 10

		elif self.check_straight_flush():
			return 9

		elif self.check_four_of_a_kind():
			return 8

		elif self.check_full_house():
			return 7

		elif self.check_full_house():
			return 6

		elif self.check_flush():
			return 5

		elif self.check_straight():
			return 4

		elif self.check_three_of_a_kind():
			return 3

		elif self.check_two_pairs():
			return 2

		elif self.check_one_pairs():
			return 1

		else:
			return 0

	#general function to search
	def search_in_list(self, card, list):

		answer = [False, "card is not in the list"]

		for s in list:
			if card == s:
				answer = [True, "card is in the list"]
		return answer

	
