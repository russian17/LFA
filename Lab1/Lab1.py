import random
class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S

    def generateValidStrings(self, count):
        def generateFromSymbol(symbol):
            if symbol in self.VT:
                return symbol
            else:
                production = random.choice(self.P[symbol])
                return ''.join(generateFromSymbol(s) for s in production)

        valid_strings = []
        for _ in range(count):
            valid_strings.append(generateFromSymbol(self.S))
        return valid_strings

    def toFiniteAutomaton(self):
        Q = self.VN.union({'X'})  # States of the FA are the non-terminals of the grammar plus an additional state X
        Sigma = self.VT  # Alphabet of the FA is the set of terminals of the grammar
        Delta = {}  # Transition function
        q0 = {self.S}  # Initial state is the start symbol of the grammar
        F = {'X'}  # Set of final states

        # Initialize Delta with empty sets for all state-symbol pairs
        for state in Q:
            for symbol in Sigma:
                Delta[(state, symbol)] = set()

        # Construct transition function Delta
        for non_terminal, productions in self.P.items():
            for production in productions:
                if len(production) == 1 and production[0] in self.VT:  # Non-terminal to terminal transition
                    Delta[(non_terminal, production[0])].add('X')
                elif len(production) == 2 and production[0] in self.VT:  # Non-terminal to non-terminal transition
                    Delta[(non_terminal, production[0])].add(production[1])
                elif len(production) == 1 and production[0] in self.VN:  # Non-terminal to terminal transition
                    Delta[(non_terminal, '')].add(production[0])
                    F.add(production[0])  # Production is a final state

        return FiniteAutomaton(Q, Sigma, Delta, q0, F)


class FiniteAutomaton:
    def __init__(self, Q, Sigma, Delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.Delta = Delta
        self.q0 = q0
        self.F = F

    def stringBelongToLanguage(self, w):
        currentStates = self.q0
        for letter in w:
            nextStates = set()
            for state in currentStates:
                if (state, letter) in self.Delta:
                    nextStates.update(self.Delta[(state, letter)])
            currentStates = nextStates
        return any(state in self.F for state in currentStates)


# Grammar variant 11
VN = {'S', 'B', 'D'}
VT = {'a', 'b', 'c'}
P = {
    'S': ['aB', 'bB'],
    'B': ['bD', 'cB', 'aS'],
    'D': ['b', 'aD']
}
S = 'S'

# Create an instance of Grammar
grammar = Grammar(VN, VT, P, S)

# Generate 5 valid strings
valid_strings = grammar.generateValidStrings(5)
print("Generated strings:")
for s in valid_strings:
    print(s)

print("-------------------------------------------------------------")

# Test Finite Automaton functionality
finiteAutomaton = grammar.toFiniteAutomaton()
listOfStrings = ["bbb", "ababab", "acaaaabb", "ababababab", "abb"]
for word in listOfStrings:
    print(f'{word} can be obtained via the state transition: {finiteAutomaton.stringBelongToLanguage(word)}')
