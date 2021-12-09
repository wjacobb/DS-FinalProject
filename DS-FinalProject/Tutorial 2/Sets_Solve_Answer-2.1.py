"""
Here's the answer sheet for the Sets reading problem
"""

alphabet = set()

# Here we're going to keep track as if it were in order. Your order may be different.
alphabet.add('a') # {'a'}
alphabet.add('b') # {'a', 'b'}
alphabet.add('c') # {'a', 'b', 'c'}
alphabet.add('z') # {'a', 'b', 'c', 'z'}
alphabet.add('x') # {'a', 'b', 'c', 'z', 'x'}
alphabet.add('a') # {'a', 'b', 'c', 'z', 'x'}
alphabet.add('y') # {'a', 'b', 'c', 'z', 'x', 'y'}
alphabet.add('s') # {'a', 'b', 'c', 'z', 'x', 'y', 's'}
alphabet.add('e') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e'}
alphabet.add('j') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e', 'j'}
alphabet.add('k') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e', 'j', 'k'}
alphabet.add('i') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e', 'j', 'k', 'i'}
alphabet.add('l') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e', 'j', 'k', 'i', 'l'}
alphabet.add('e') # {'a', 'b', 'c', 'z', 'x', 'y', 's', 'e', 'j', 'k', 'i', 'l'}

alphabet.remove('a') # {'b', 'c', 'z', 'x', 'y', 's', 'e', 'j', 'k', 'i', 'l'}
alphabet.remove('y') # {'b', 'c', 'z', 'x', 's', 'e', 'j', 'k', 'i', 'l'}
alphabet.remove('e') # {'b', 'c', 'z', 'x', 's', 'j', 'k', 'i', 'l'}
alphabet.remove('j') # {'b', 'c', 'z', 'x', 's', 'k', 'i', 'l'}

print(alphabet)

# The answer should be some variation of {'b', 'c', 'z', 'x', 's', 'k', 'i', 'l'}