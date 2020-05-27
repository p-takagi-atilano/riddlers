# Paolo Takagi-Atilano
# Submission for the following 538 Riddler:
# 	https://fivethirtyeight.com/features/somethings-fishy-in-the-state-of-the-riddler/

from collections import defaultdict

def get_states():
	states = set()
	with open('states.txt') as f:
		state = f.readline().strip().lower()
		while state:
			states.add(state)
			state = f.readline().strip().lower()
	return states

def get_words():
	words = set()
	with open('words.txt') as f:
		word = f.readline().strip().lower()
		while word:
			words.add(word)
			word = f.readline().strip().lower()
	return words

def no_overlapping_letters(state, word):
	state_letters = set()
	for c in state:
		state_letters.add(c)
	
	for c in word:
		if c in state_letters:
			return False

	return True

def get_state_to_mackerel_map(states, words):
	state_to_mackerel_map = defaultdict(list)
	for word in words:
		candidate_state_for_mackerel = None
		for state in states:
			if no_overlapping_letters(state, word):
				if candidate_state_for_mackerel is None:
					candidate_state_for_mackerel = state
				else:
					candidate_state_for_mackerel = None
					break
		if candidate_state_for_mackerel is not None:
			state_to_mackerel_map[candidate_state_for_mackerel].append(word)
	return state_to_mackerel_map

def spot_check_test(state_to_mackerel_map):
	assert('mackerel' in state_to_mackerel_map['ohio'])
	for state in state_to_mackerel_map:
		if state != 'ohio':
			assert('mackerel' not in state_to_mackerel_map[state])

	assert('goldfish' in state_to_mackerel_map['kentucky'])
	for state in state_to_mackerel_map:
		if state != 'kentucky':
			assert('goldfish' not in state_to_mackerel_map[state])

	assert('jellyfish' in state_to_mackerel_map['montana'])
	for state in state_to_mackerel_map:
		if state != 'montana':
			assert('jellyfish' not in state_to_mackerel_map[state])

	assert('monkfish' in state_to_mackerel_map['delaware'])
	for state in state_to_mackerel_map:
		if state != 'delaware':
			assert('monkfish' not in state_to_mackerel_map[state])

def question(state_to_mackerel_map):
	max_mackerels = [""]
	for state in state_to_mackerel_map:
		for mackerel in state_to_mackerel_map[state]:
			if len(mackerel) > len(max_mackerels[0]):
				max_mackerels = [mackerel]
			elif len(mackerel) == len(max_mackerels[0]):
				max_mackerels.append(mackerel)
	print('Question: {}'.format(max_mackerels))

def extra_credit(state_to_mackerel_map):
	max_states = []
	max_len = 0
	for state in state_to_mackerel_map:
		if len(state_to_mackerel_map[state]) > max_len:
			max_states = [state]
			max_len = len(state_to_mackerel_map[state])
		elif len(state_to_mackerel_map[state]) == max_len:
			max_state.append(state)
	# I added the number of states to this print statment after I learned that there was
	# only one max mackerel state, out of interest:
	print('Extra Credit: {} with {} mackerels'.format(max_states, len(state_to_mackerel_map[max_states[0]])))

# Get states and words:
states = get_states()
words = get_words()

# Load state to mackerel map:
state_to_mackerel_map = get_state_to_mackerel_map(states, words)

# Spot check test to see if state to mackerel map works
spot_check_test(state_to_mackerel_map)

# Get answer to question
question(state_to_mackerel_map)

# Get answer to extra credit
extra_credit(state_to_mackerel_map)
