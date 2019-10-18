""" Nondeterministic Finite Automata (NFA) are machines that recognize 
    Regular Languages. They are defined as a 5-tuple:
    - A set of states Q 
    - A finite set of input symbols called the alphabet sigma
    - A transition function delta : Q x sigma into the power set of Q
    - An initial state q0
    - A set of accept states F contained on Q

    Given a string w = a1a2...an and a NFA N, we say that N **accepts** the 
    input s iff a sequence of states r0, r1, ..., rn exists in Q with the
    following conditions:

    1. r0 = q0
    2. ri+1 = delta(ri, ai+1), for i = 0, ..., n-1
    3. rn is a member of F"""

class NFA():
    def __init__(self,
                states : set,
                input_symbols : set,
                transition_function : dict,
                initial_state : str,
                accept_states : set):
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

    def __str__(self):
        return (f'NFA - '
                f'States: {self.states} '
                f'Input Symbols: {self.input_symbols}'
                f'Transition Function: {self.transition_function}'
                f'Initial State: {self.initial_state}'
                f'Accept States: {self.accept_states}'
                )

    """Returns a DFA that is equivalent to this NFA"""
    def convert_to_dfa(self):
        d_states = self.states.copy()
        d_input_symbols = self.input_symbols.copy()
        d_initial_state = self.initial_state.copy()
        d_accept_states = []

        # add states reachable by one step of non-deterministic transitions
        # without epsilon
        for state in self.states:

            for symbol in self.input_symbols:
                # sort is needed to avoid overlap between concatenated states with
                # different order
                transitioned_states = transition_function[(state, symbol)].sort()

                new_state = ''

                for s in transitioned_states:
                    new_state += s
                
                if not new_state in d_states:
                    d_states.append(new_state)

        # try transitioning on the new states
        
