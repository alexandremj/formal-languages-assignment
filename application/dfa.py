""" Deterministic Finite Automata (DFA) are machines that recognize
    Regular Languages. They are defined as a 5-tuple:
    - A set of states Q 
    - A finite set of input symbols called the alphabet sigma
    - A transition function delta : Q x sigma into Q
    - An initial state q0
    - A set of accept states F contained on Q

    Given a string w = a1a2...an and a DFA D, we say that D **accepts** the 
    input s iff a sequence of states r0, r1, ..., rn exists in Q with the
    following conditions:

    1. r0 = q0
    2. ri+1 = delta(ri, ai+1), for i = 0, ..., n-1
    3. rn is a member of F"""

class DFA():

    def __init__(self, states : list, input_symbols : list, transition_function,
        initial_state : str, accept_states : list):

        # Q set of states
        self.states = []
        # input symbols sigma
        self.input_symbols = []
        # transition function delta
        self.transition_function = transition_function
        # initial state
        self.initial_state = initial_state

        # accept states F
        self.accept_states = accept_states

    """ Compute input_ on the DFA

        Arguments:
        input_ -- the string to be used as input on the DFA

        Returns:
        True if the DFA accepts the input, False otherwise
    """
    def compute_on_string(self, input_ : str):
        current_state = self.initial_state

        for symbol in input_:
            current_state = self.transition_function[(current_state, symbol)]

        return current_state in self.accept_states
