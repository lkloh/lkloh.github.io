import numpy as np
import random
import math

'''
Assumptions
===========
Values of coins are 
'''


'''
num_coins_in_bag = 10 (should be a large number)
'''
def get_amounts(value_upper_bound):
	value_lower_bound = 1
	num_coins_in_bag = value_upper_bound
	coins_in_bag = \
		np.random.randint(low=value_lower_bound, high=value_upper_bound, \
			size=num_coins_in_bag)
	coins = [coin for coin in coins_in_bag]

	amounts_paid = [-1] * num_coins_in_bag
	previous_coin = 0
	for i in range(num_coins_in_bag):
		remaining_range = num_coins_in_bag - i - 1
		index = random.randint(0, remaining_range)
		current_coin = coins[index]
		del coins[index]
		amounts_paid[i] = abs(current_coin - previous_coin)

		# update
		previous_coin = current_coin

	total_paid = sum(amounts_paid)

	#print 'num coins in bag: %d' % num_coins_in_bag

	return total_paid, np.mean(amounts_paid), np.std(amounts_paid)


def testing_randomize_amounts():
	total_paid, mean_amount_paid, std_paid = get_amounts(value_upper_bound=100)
	assert 100 <= total_paid and total_paid <= math.pow(100,2) 
	assert 1 <= mean_amount_paid and mean_amount_paid <= 100


def greater_than(total_payment_lower_bound, value_upper_bound, num_simulations):
	total_paid, mean_amount_paid, std_paid = get_amounts(value_upper_bound)
	num_greater_than_total_payment_lower_bound = 0
	for _ in range(num_simulations):
		total_paid, mean_amount_paid, std_paid = get_amounts(value_upper_bound)
		# print "total paid: %d" % total_paid
		if total_paid >= total_payment_lower_bound:
			num_greater_than_total_payment_lower_bound += 1
	return float(num_greater_than_total_payment_lower_bound) / num_simulations 



def answer():
	total_paid, mean_amount_paid, std_paid = get_amounts(value_upper_bound=20)

	print "total amount paid is %.10f" % total_paid 

	print "1: Mean amt paid is %.10f" % mean_amount_paid

	print "2: Standard deviation of total payment is %.10f" % std_paid


	print "What is the probability that your total payment is greater than or equal to 45 for N=10? %.10f" % greater_than(total_payment_lower_bound=45, value_upper_bound=10, num_simulations=1000)

	print "What is the probability that your total payment is greater than or equal to 160 for N=20? %.10f" % greater_than(total_payment_lower_bound=160, value_upper_bound=20, num_simulations=1000)


'''
Printing
'''
testing_randomize_amounts()
answer()

















