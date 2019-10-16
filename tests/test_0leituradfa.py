from application.dfa import DFA
from application.regex import RE
from application.rg import RG
from application.serializer import Serializer

import logging
import os

# logger configuration for the serializer
logging.basicConfig(
    filename='newfile.log',
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

"""Test recording Deterministic Finite Automata using the Serializer class"""
def test_recording_dfa(dfa_creation):

    s = Serializer()
    s.serialize(dfa_creation, 'test_dfa')

    unpickled = s.deserialize('test_dfa')

    assert unpickled.states == dfa_creation.states
    assert unpickled.input_symbols == dfa_creation.input_symbols
    assert unpickled.transition_function == dfa_creation.transition_function
    assert unpickled.initial_state == dfa_creation.initial_state
    assert unpickled.accept_states == dfa_creation.accept_states

    # cleanup after tests
    os.remove('test_dfa.pkl')

"""Test recording Regular Expressions using the Serializer class"""
def test_recording_re():
    re = RE('1(10)*')

    s = Serializer()
    s.serialize(re, 'test_re')

    unpickled = s.deserialize('test_re')

    assert unpickled.expression == re.expression

    # cleanup after tests
    os.remove('test_re.pkl')

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

    # cleanup after tests
    os.remove('test_rg.pkl')

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
