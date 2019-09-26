from application.dfa import DFA
from application.re import RE
from application.rg import RG
from application.serializer import Serializer

import logging

# logger configuration for the serializer
logging.basicConfig(
    filename='newfile.log',
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

"""Function for easier creation of dfa between tests"""
def dfa_creation():
    states = ['q0', 'q1', 'q2', 'q3']
    symbols = ['a', 'b']
    transition_function = {
        ('q0', 'a') : 'q1',
        ('q0', 'b') : 'q0',
        ('q1', 'a') : 'q2',
        ('q1', 'b') : 'q1',
        ('q2', 'a') : 'q3',
        ('q2', 'b') : 'q2',
        ('q3', 'a') : 'q3',
        ('q3', 'b') : 'q3',
    }
    initial_state = 'q0'
    final_states = ['q3']

    return DFA(states, symbols, transition_function, initial_state, final_states)

"""Test recording Deterministic Finite Automata using the Serializer class"""
def test_recording_dfa():
    dfa = dfa_creation()

    s = Serializer()
    s.serialize(dfa, 'test_dfa')

    unpickled = s.deserialize('test_dfa')

    assert unpickled.states == dfa.states
    assert unpickled.input_symbols == dfa.input_symbols
    assert unpickled.transition_function == dfa.transition_function
    assert unpickled.initial_state == dfa.initial_state
    assert unpickled.accept_states == dfa.accept_states

"""Test recording Regular Expressions using the Serializer class"""
def test_recording_re():
    re = RE('1(10)*')

    s = Serializer()
    s.serialize(re, 'test_re')

    unpickled = s.deserialize('test_re')

    assert unpickled.expression == re.expression

"""Test recording Regular Grammars using the Serializer class"""
def test_recording_rg():
    nonterminals = ['S', 'A', 'B']
    terminals = ['a', 'b']
    productions = {'S': ['Aa', 'a', 'Ba'], 'A': ['a', 'Ba'], 'B': ['b', 'Ab']}
    start_symbol = 'S'

    rg = RG(nonterminals, terminals, productions, start_symbol)

    s = Serializer()
    s.serialize(rg, 'test_rg')

    unpickled = s.deserialize('test_rg')

    assert unpickled.nonterminals == rg.nonterminals
    assert unpickled.terminals == rg.terminals
    assert unpickled.productions == rg.productions
    assert unpickled.start_symbol == rg.start_symbol

"""Tests the edition modes of the DFA class"""
def test_editing_dfa():
    # TODO implement
    pass

"""Tests the edition modes of the RG class"""
def test_editing_rg():
    # TODO implement
    pass

"""Tests the edition modes of the RE class"""
def test_editing_re():
    re = RE('1(10)*')

    exp = re.expression
    re.edit_expression('0(01)*')

    assert re.expression != exp
