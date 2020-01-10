from collections import Counter

# keep track f frequencies
txt = "This is a vast world you can't traverse world in a day"

# any iterable you give counter will be counted for frequencies

counts = Counter(txt.split())

# the result is a dictionary of frequencies of words in our text

print(counts)

# query the two most common words

print(counts.most_common(2))

# get specific word

print(counts['world'])

# get total of occurences

print(sum(counts.values()))

# apply some set operations on counters, such as joining them, subtracting them, or checking for intersections:

print(Counter(["hello", "world"]) + Counter(["hello", "you"]))

print(Counter(["hello", "world"]) & Counter(["hello", "you"]))

# do it without counter

counting = {}

for word in 'hello world this is a very nice day in this world'.split():
  if word in counting:
    counting[word] += 1
  else:
    counting[word] = 1

print(counting)

