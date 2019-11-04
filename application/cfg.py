""" Context-Free Grammar is a device that is used to generate languages.
    Formally, it's defined as a 4-tuple (N, sigma, P, S), where:
    - N is a nonempty, finite set of nonterminal symbols;
    - Sigma is a finite set of terminal symbols;
    - P is a set of grammar rules, having the form:
        A ::= Aa | a
      where A is in N and a is in Sigma
    - S in N is the start symbol"""


class CFG():

    def __init__(self,
                 nonterminals: set,
                 terminals: set,
                 productions,
                 start_symbol: str):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def __str__(self):
        return (f'Context-Free Grammar - '
                f'Nonterminals: {self.nonterminals}, '
                f'Terminals: {self.terminals}, '
                f'Productions: {self.productions}, '
                f'start_symbol: {self.start_symbol} '
                )

    """ A Context-Free Grammar is in its Chomsky Normal Form if its
        productions are in one of two forms:
        A -> BC, where A, B, C are nonterminals; or
        A -> a, where A is nonterminal and a is a terminal

        Also, G should have no useless symbols"""
    def to_chomsky_normal_form(self):
        self.remove_free_epsilon()
        self.remove_unitary_productions()
        self.remove_useless_symbols()

        # by now, the grammar will only have productions such as
        # A -> a, or whose body length is equal or greater to 2

        # ToDo implement algorithm

        # Part 1 - for each terminal symbol on the body of a production of
        # length >= 2, create a new nonterminal A whose only production is
        # A -> a
        #
        # Then use A instead of a in every production of length >= 2 where
        # there's an a

        # Part 2 - For each production of form A -> B1B2...Bk for k >= 3,
        # create k - 2 new variables C1, C2, ..., Ck - 2. The original
        # production is substituted by k - 1 new productions of form:
        # A -> B1C1, C1 -> B2C2, ... ,Ck-3 -> Bk-2 Ck-2, Ck-2 -> Bk-1 Bk

    def remove_useless_symbols(self):
        self.remove_unreachable_symbols()
        self.remove_unproductive_symbols()

    """ Removes the unreachable symbols from the Context-Free Grammar

        The substitution is realized in-place
    """
    def remove_unreachable_symbols(self):
        rs = [self.start_symbol]

        while True:
            # Find a string comprehension that represents the set
            # X | X E N U T and X !E RS and theres at least a production
            # Y -> aXb e Y E RS

            rs = rs.append(m)

            if not m:
                break

        self.nonterminals = intersection(nonterminals, rs)
        self.terminals = intersection(terminals, rs)

        # ToDo implement productions
        # self.productions =
        # P' = {p | p E P and all symbols of p are in rs}

    def remove_unproductive_symbols(self):
        pass

    def remove_free_epsilon(self):
        pass

    def remove_unitary_productions(self):
        pass

    def remove_nondeterminism(self):
        pass

    def remove_recursions(self):
        pass
