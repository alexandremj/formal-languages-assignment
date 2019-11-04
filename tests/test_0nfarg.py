
from application.nfa import NFA

""" Tests the creation of a NFA that recognizes a language described by the RG
    given as a parameter"""


def test_rg_nfa_conversion_input_rg(rg_creation):
    states = {'S', 'A', 'B', 'Z'}
    input_symbols = {'a', 'b'}
    transition_function = {
        ('S', 'a'): ['A'],
        ('S', 'b'): ['B', 'Z'],
        ('A', 'a'): ['S'],
        ('A', 'b'): [],
        ('B', 'a'): [],
        ('B', 'b'): ['B', 'Z'],
        ('Z', 'a'): [],
        ('Z', 'b'): [],
    }
    initial_state = 'S'
    accept_states = {'B', 'Z'}

    dummy_nfa = NFA(states, input_symbols, transition_function,
                    initial_state, accept_states)

    print('DUMMY NFA: ' + str(dummy_nfa) + '\n\n')

    n = rg_creation.convert_to_nfa()

    print('CONVERTED NFA: ' + str(n) + '\n\n')

    assert dummy_nfa.states == n.states
    assert dummy_nfa.input_symbols == n.input_symbols
    assert dummy_nfa.transition_function == n.transition_function
    assert dummy_nfa.initial_state == n.initial_state
    assert dummy_nfa.accept_states == n.accept_states
