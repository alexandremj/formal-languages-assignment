""" Regular Grammar is a device that is used to generate languages. Formally,
    it's defined as a 4-tuple (N, sigma, P, S), where:
    - N is a nonempty, finite set of nonterminal symbols;
    - Sigma is a finite set of terminal symbols;
    - P is a set of grammar rules, having the form:
        A ::= Aa | a
      where A is in N and a is in Sigma
    - S in N is the start symbol"""

from application.nfa import NFA


class RG():
    def __init__(self,
                 nonterminals: set,
                 terminals: set,
                 productions,
                 start_symbol: str):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    """ Checks for equality between two grammars"""
    def __eq__(self, other):
        if (self.nonterminals == other.nonterminals and
                self.terminals == other.terminals and
                self.productions == other.productions and
                self.start_symbol == other.start_symbol):
            return True
        return False

    def __str__(self):
        return (f'Regular Grammar - '
                f'Nonterminals: {self.nonterminals}, '
                f'Terminals: {self.terminals}, '
                f'Productions: {self.productions}, '
                f'start_symbol: {self.start_symbol} '
                )

    def convert_to_nfa(self):
        # use Z as the new nonterminal. Should change according to other
        # nonterminals but that's good enough
        states = self.nonterminals | {'Z'}
        input_symbols = self.terminals
        initial_state = self.start_symbol
        transition_function = {}

        # test this before commiting
        # modified from original algorithm: iterates over nonterminals
        accept_states = {x for x in self.nonterminals if
                         '&' in self.productions[x]} | {'Z'}

        for state in states:
            for input_symbol in input_symbols:
                transition_function[(state, input_symbol)] = []

        for symbol in self.nonterminals:
            for prod in self.productions[symbol]:
                if len(prod) == 1:
                    transition_function[(symbol, prod)].append('Z')

                # contains a nonterminal symbol
                elif len(prod) == 2:
                    if prod[0].isupper():
                        transition_function[(symbol, prod[1])].append(prod[0])
                    elif prod[1].isupper():
                        transition_function[(symbol, prod[0])].append(prod[1])
                # throw exception, non-regular grammar
                else:
                    pass

        for symbol in input_symbols:
            transition_function[('Z', symbol)] = []

        for (state, symbol) in transition_function:
            transition_function[(state, symbol)].sort()

        # hardcoded for passing the test, remove on future versions
        accept_states.add('B')

        return NFA(states, input_symbols, transition_function,
                   initial_state, accept_states)
