from evaluate import Evaluation
from collections import Counter
import itertools

#create a class with all the characteristics of the hand
class PokerHand:
	def __init__(
		self,
		hand,
		first_card=None,
		second_card=None,
		third_card=None,
		fourth_card=None,
		fifth_card=None,
		
	):
	
		self.hand = hand 
		self.first_card = first_card
		self.second_card = second_card
		self.third_card = third_card
		self.fourth_card = fourth_card
		self.fifth_card = fifth_card

	#function that returns the list with all the cards
	def get_cards(self):

		cards = self.hand.split()
		self.first_card = cards[0]
		self.second_card = cards[1]
		self.third_card = cards[2]
		self.fourth_card = cards[3]
		self.fifth_card = cards[4]

		list_cards = []
		list_cards.append(self.first_card)
		list_cards.append(self.second_card)
		list_cards.append(self.third_card)
		list_cards.append(self.fourth_card)
		list_cards.append(self.fifth_card)

		return list_cards

	# evaluate function that involves Evaluation.py
	def evaluate_hand(self,list_cards):

		evaluation = Evaluation(list_cards).evaluate_hand()
		return evaluation

	# Here we compare two hands
	def compare_with(self,poker_hand2):
				
		cards1 = self.get_cards()
		cards2 = poker_hand2.get_cards()

		score1 = self.evaluate_hand(cards1)
		score2 = self.evaluate_hand(cards2)              

		if score1 > score2:
			ans = "WIN"
		elif score1 < score2:
			ans = "LOSS"

		else :
			aux = self.check_high_card(cards1,cards2)

			if aux == 1:
				ans = "WIN"
			elif aux == 2:
				ans = "LOSS"
			else :
				ans = "tie"

		return ans
	
	# If we have a tie we use this function to solve the problem
	@staticmethod
	def check_high_card(cards1,cards2):
		
		A = [card[0] for card in cards1]
		B = [card[0] for card in cards2]

		dic1 = {}
		dic2 = {}

		#detection of a lower hand
		if set(A) == set(["A", "2", "3", "4", "5"]):
			dic1 = {"T":'10',"J":'11',"Q":'12',"K":'13',"A":'1'}
		else:
			dic1 = {"T":'10',"J":'11',"Q":'12',"K":'13',"A":'14'}

		if set(B) == set(["A", "2", "3", "4", "5"]):
			dic2 = {"T":'10',"J":'11',"Q":'12',"K":'13',"A":'1'}
		else:
			dic2 = {"T":'10',"J":'11',"Q":'12',"K":'13',"A":'14'}

		values1 = [dic1.get(n, n) for n in A]
		values2 = [dic2.get(n, n) for n in B]
		# we get a list with the numbers of the cards and sort by the number of repetitions
		counts1 = Counter(values1)
		new_list1 = sorted(counts1, key=lambda x: (counts1[x]), reverse=True)

		counts2 = Counter(values2)
		new_list2 = sorted(counts2, key=lambda x: (counts2[x]), reverse=True)

		winner_hand = 0
		for(a,b) in zip(new_list1,new_list2):
			
			if winner_hand == 0:
				if int(a) > int(b):
					winner_hand = 1					
				elif int(b) > int(a):
					winner_hand = 2					
				else:
					pass
		return winner_hand
  	



