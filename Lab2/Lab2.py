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

    @staticmethod
    def from_nfa_to_dfa(fa):
        # Define transitions_dict
        transitions_dict = fa.Delta

        # Create a dictionary to hold the transition function of the DFA
        delta_dfa = {}

        # Implement the epsilon-closure function
        def epsilon_closure(state):
            closure = set()
            stack = list(state)  # Convert state to list to handle single state or set of states

            while stack:
                cur = stack.pop()
                closure.add(cur)
                transitions = transitions_dict.get((cur, 'e'), [])
                for next_state in transitions:
                    if next_state not in closure:
                        stack.append(next_state)
            return frozenset(closure)  # Convert to frozenset

        # Initialize epsilon-closure for all states
        epsilon_closures = {state: epsilon_closure(state) for state in fa.Q}

        # Initialize the start state of the DFA as the epsilon-closure of the start state of the NFA
        start_dfa = epsilon_closures[fa.q0]  # No need to convert to frozenset here

        # Initialize the set of states of the DFA
        states_dfa = {start_dfa}

        # Initialize the stack for processing the states of the DFA
        stack = [start_dfa]

        # Initialize the alphabet of the DFA
        alphabet_dfa = fa.Sigma

        # While there are unprocessed states in the stack
        while stack:
            current_set = stack.pop()
            for symbol in alphabet_dfa:
                # Calculate the transition from the current set of states on the current symbol
                next_set = set()
                for state in current_set:
                    next_states = transitions_dict.get((state, symbol), [])
                    for next_state in next_states:
                        next_set.update(epsilon_closures[next_state])
                next_set = frozenset(next_set)  # Convert to frozenset
                if next_set not in states_dfa:
                    states_dfa.add(next_set)
                    stack.append(next_set)
                delta_dfa[(current_set, symbol)] = next_set

        # Determine the set of final states of the DFA
        final_states_dfa = {state for state in states_dfa if any(final in state for final in fa.F)}

        # Create the DFA object
        dfa = FiniteAutomaton(Q=states_dfa, Sigma=alphabet_dfa, Delta=delta_dfa, q0=start_dfa, F=final_states_dfa)

        return dfa


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
