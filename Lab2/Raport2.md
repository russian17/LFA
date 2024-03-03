# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.
### Course: Formal Languages & Finite Automata
### Author: Cuzmin Simion
----

## Theory
In the realm of theoretical computer science, the study of automata theory serves as a fundamental cornerstone. This laboratory work delves into three pivotal concepts within this domain: Determinism in Finite Automata, Conversion from Non-Deterministic Finite Automata (NDFA) to Deterministic Finite Automata (DFA), and the Chomsky Hierarchy.

#### 1)Determinism in Finite Automata
- Finite Automata are abstract models of computation that exhibit finite sets of states and transitions between these states based on input symbols. Deterministic Finite Automata (DFA) are a subset of finite automata where each state transition is uniquely determined by the current state and the input symbol. This characteristic of determinism simplifies the behavior of automata, making them predictable and efficient in processing inputs. Understanding determinism is crucial for analyzing the computational capabilities and limitations of finite automata.

#### 2)Conversion from NDFA to DFA
- Non-Deterministic Finite Automata (NDFA) allow for multiple possible transitions from a given state for a specific input symbol. While NDFA are conceptually powerful, they can be challenging to implement and analyze due to their non-deterministic nature. Conversion from NDFA to DFA involves transforming an NDFA into an equivalent DFA, where each transition is uniquely determined. This conversion simplifies the automaton's behavior, enabling clearer analysis and implementation. It is a fundamental technique in automata theory and plays a vital role in various computational tasks, including lexical analysis in compilers.

#### 3)Chomsky Hierarchy
- The Chomsky Hierarchy classifies formal grammars and languages into four levels based on their generative power. These levels are Type-0 (Unrestricted Grammar), Type-1 (Context-Sensitive Grammar), Type-2 (Context-Free Grammar), and Type-3 (Regular Grammar). Each level corresponds to a different class of automata: recursively enumerable languages, context-sensitive languages, context-free languages, and regular languages, respectively. Understanding the Chomsky Hierarchy provides insights into the expressive capabilities of different grammar types and their associated automata. This hierarchy serves as a foundational framework for studying the computational complexity and expressive power of formal languages.
## Objectives:

1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

Please consider that all elements of the task 3 can be done manually, writing a detailed report about how you've done the conversion and what changes have you introduced. In case if you'll be able to write a complete program that will take some finite automata and then convert it to the regular grammar - this will be **a good bonus point**.


## Implementation description
#### 1. Lab2/Lab2_Chomsky_classification.py (2B):
  The Grammar class represents a context-free grammar (CFG).
  - Attributes:
    - `VN`: Set of non-terminal symbols.
    - `VT`: Set of terminal symbols.
    - `P`: Production rules, where each non-terminal symbol maps to a list of production rules.
    - `S`: Start symbol.
  - Methods:
    - `classifyChomskyHierarchy()`: Determines the Chomsky Hierarchy classification of the grammar based on its production rules. The method defines several nested helper functions (type0(), type1(), type2(), type3_LL(), and type3_RL()) to classify the grammar according to the Chomsky Hierarchy.
#### Results
![Screenshot 2024-03-03 231139](https://github.com/russian17/LFA/assets/120457811/326e7e69-2e32-47c4-84cd-eea740c49732)



#### 2. Lab2/Lab2.py(3A-3B)
The Grammar class represents a context-free grammar (CFG).
Attributes:
- `VN`: Set of non-terminal symbols representing variables.
- `VT`: Set of terminal symbols representing alphabet symbols.
- `P`: Production rules, where each non-terminal symbol maps to a list of production rules.
- `S`: Start symbol indicating where the generation of strings begins.

The `FiniteAutomaton` class represents a deterministic finite automaton (DFA), which is a mathematical model for computation.
Attributes:
- `Q`: Set of states.
- `Sigma`: Alphabet or set of input symbols.
- `Delta`: Transition function specifying state transitions upon input symbols.
- `q0`: Initial state.
- `F`: Set of final or accepting states.
Methods:
- `is_deterministic()`: Checks whether the DFA is deterministic, i.e., each state has only one transition for each input symbol. If any state has multiple transitions for the same input symbol, the DFA is not deterministic.

The `FiniteAutomatonToRegularGrammar` class converts a deterministic finite automaton (DFA) into a regular grammar, which generates the same language as the DFA.
Attributes:
- `fa`: The DFA to be converted into a regular grammar.
Methods:
- `toRegularGrammar()`: Converts the DFA into a regular grammar.
  - `VN`: Non-terminals are the states of the DFA.
  - `VT`: Terminals are the alphabet symbols of the DFA.
  - `P`: Production rules are generated by examining transitions in the DFA and constructing rules accordingly.
  - `S`: The start symbol of the regular grammar is the initial state of the DFA.

#### Results
![Screenshot 2024-03-03 231204](https://github.com/russian17/LFA/assets/120457811/224bab29-ca2f-4191-b520-a0e4001c0530)


#### 3. Lab2/NFA_to_DFA.py(3C)
The `NFA` class represents a Non-Deterministic Finite Automaton.
Attributes:
- `no_state`: Number of states in the NFA.
- `states`: List of state names in the NFA.
- `no_alphabet`: Number of alphabets in the NFA.
- `alphabets`: List of alphabet symbols in the NFA.
- `start`: Start state of the NFA.
- `no_final`: Number of final states in the NFA.
- `finals`: List of final states in the NFA.
- `no_transition`: Number of transitions in the NFA.
- `transitions`: List of transition tuples `(from_state, symbol, to_state)`.
Methods:
- `getEpsilonClosure(state)`: Retrieves the Epsilon Closure of a state in the NFA.
- `getStateName(state_list)`: Gets the name from a set of states to display in the final DFA diagram.
- `isFinalDFA(state_list)`: Checks if a set of states is a final state in the DFA.
Explanation of Method:
- `__init__`: Initializes the NFA object with the provided parameters.
  - It adds an epsilon alphabet to the list of alphabets and increments the alphabet count.
  - Constructs transition table to represent transitions from states on alphabets.
  - Initializes dictionaries to map states and alphabets to their respective
  - 
#### Results
#### DFA:
![Screenshot 2024-03-03 233026](https://github.com/russian17/LFA/assets/120457811/93c97575-0f40-4847-bacc-f6ae915ab1f9)
#### NFA:
![Screenshot 2024-03-03 233055](https://github.com/russian17/LFA/assets/120457811/36c15304-e121-4d76-8b08-20941e23a09d)


## Conclusions
In the study of formal languages and finite automata, we explored the concepts of determinism, conversion between automaton types, and the Chomsky Hierarchy.

Finite Automata, as abstract models of computation, exhibit deterministic behavior in Deterministic Finite Automata (DFA), where state transitions are uniquely determined by input symbols. This deterministic nature simplifies automata behavior, making them predictable and efficient.

Conversion from Non-Deterministic Finite Automata (NDFA) to DFA simplifies automata behavior, enabling clearer analysis and implementation. This conversion process is essential for various computational tasks, including lexical analysis in compilers.

The Chomsky Hierarchy categorizes formal grammars and languages into four levels based on their generative power. Understanding this hierarchy provides insights into the expressive capabilities of different grammar types and their associated automata, serving as a foundational framework in theoretical computer science.
