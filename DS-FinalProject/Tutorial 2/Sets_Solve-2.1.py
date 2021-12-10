"""
Take a look at this question and try to solve.
Remember, the format will be in  {} brackets i.e. {1, 2, 3, 4, 5}
Additionally order will not matter
Solve without printing the set
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

# What does the alphabet3 and alphabet4 print? 
# Remember {} brackets and that order does not matter.
