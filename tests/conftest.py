""" Definition of fixtures used throughout the tests of this app """

from application.dfa import DFA
from application.re import RE
from application.rg import RG

import pytest
import logging

# logger configuration for the serializer
logging.basicConfig(
    filename='newfile.log',
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

"""Easier creation of dfa between tests"""
@pytest.fixture
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
