from collections import Counter
from statistics import mean
def textAnalyzer(file):
	f = open(file,"r")
	lines = f.readlines()
	lines = [line.replace('\n', '') for line in lines]
	words = []
	for line in lines:
		word = line.split(' ')
		words += word
	unique_words = set(words)
	word_dict = dict()
	for u in unique_words:
		if u == '':
			continue
		word_dict[u] = {}
		temp_count = 0
		for w in words:
			if w == u:
				temp_count += 1
		word_dict[u] = temp_count
	word_sorted = {k: v for k, v in reversed(sorted(word_dict.items(), key=lambda x: x[1]))}
	top = {}
	count = 0
	while count < 5:
		top[list(word_sorted.keys())[count]] = word_sorted[list(word_sorted.keys())[count]]
		count += 1
	return top

	longest = 0
	longest_word = ''
	word_length = []
	for i in words:
		word_length += [len(i)]
		if len(i) > longest:
			longest = len(i)
			longest_word = i
	return "Longest Word: " + longest_word
	return round(mean(word_length),2)

print(textAnalyzer("/Users/deepak/Desktop/CMU/Berkeley Extension - Programming Python/Random Files/file.txt"))