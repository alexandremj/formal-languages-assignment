""" Regular Grammar is a device that is used to generate languages. Formally,
    it's defined as a 4-tuple (N, sigma, P, S), where:
    - N is a nonempty, finite set of nonterminal symbols;
    - Sigma is a finite set of terminal symbols;
    - P is a set of grammar rules, having the form:
        A ::= Aa | a
      where A is in N and a is in Sigma
    - S in N is the start symbol"""

from typing import List

class RG():
    def __init__(self,
                nonterminals : List[str],
                terminals : List[str],
                productions,
                start_symbol : str):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def __str__(self):
        return (f'Regular Grammar - '
                f'Nonterminals: {self.nonterminals}, '
                f'Terminals: {self.terminals}, '
                f'Productions: {self.productions}, '
                f'start_symbol: {self.start_symbol} '
                )
    
    # TODO
    def convert_to_nfa(self):
        pass
