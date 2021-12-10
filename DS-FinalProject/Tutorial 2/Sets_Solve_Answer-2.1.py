"""
Here's the answer sheet for the Sets reading problem
"""

alphabet = set()
alphabet2 = set()

alphabet.add('a')
alphabet.add('b')
alphabet.add('c')
alphabet.add('z')
alphabet.add('x')
alphabet.add('a')
alphabet.add('y')
alphabet.add('s')
alphabet.add('e')
alphabet.add('j')
alphabet.add('k')
alphabet.add('i')
alphabet.add('l')
alphabet.add('e')

alphabet2.add('a')
alphabet2.add('b')
alphabet2.add('c')
alphabet2.add('d')
alphabet2.add('e')
alphabet2.add('f')
alphabet2.add('g')
alphabet2.add('h')
alphabet2.add('i')
alphabet2.add('j')

alphabet.remove('a')
alphabet.remove('y')
alphabet.remove('e')
alphabet.remove('j')

alphabet3 = alphabet & alphabet2
alphabet4 = alphabet | alphabet2

print(alphabet3) # {b, c, i}
print(alphabet4) # {a, l, b, j, c, z, e, f, h, x, s, i, d, k, g}

# The answer may not be in the same order, but should match in general
