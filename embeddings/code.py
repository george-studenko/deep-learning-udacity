def get_target(words, idx, window_size=5):
	rnd = randint(0, window_size)
	start_index, end_index = idx - rnd, idx + rnd
	word_list = []
	for i in range(start_index, end_index):
		word_list.append(words[i])	
	return word_list
