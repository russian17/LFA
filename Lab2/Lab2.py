class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN  # Non-terminals
        self.VT = VT  # Terminals
        self.P = P    # Production rules
        self.S = S    # Start symbol

class FiniteAutomaton:
    def __init__(self, Q, Sigma, Delta, q0, F):
        self.Q = Q        # Set of states
        self.Sigma = Sigma  # Alphabet
        self.Delta = Delta  # Transition function
        self.q0 = q0        # Initial state
        self.F = F          # Set of final states

    def is_deterministic(self):
        for state in self.Q:
            for symbol in self.Sigma:
                if len(self.Delta.get((state, symbol), [])) > 1:
                    return False
        return True


class FiniteAutomatonToRegularGrammar:
    def __init__(self, fa):
        self.fa = fa

    def toRegularGrammar(self):
        VN = self.fa.Q  # Non-terminals are the states of the FA
        VT = self.fa.Sigma  # Terminals are the alphabet of the FA
        P = {}  # Production rules

        for state, symbol in self.fa.Delta:
            next_states = self.fa.Delta[(state, symbol)]
            P[(state, symbol)] = P.get((state, symbol), []) + list(next_states)

        S = self.fa.q0  # Start symbol is the initial state of the FA
        return Grammar(VN, VT, P, S)
