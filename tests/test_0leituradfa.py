import json
import logging

from application.dfa import DFA
from application.serializer import Serializer

# logger configuration for the serializer
logging.basicConfig(
    filename='newfile.log',
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

"""
    Function for easier creation of dfa between tests
"""
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

def test_computing_strings(test_strings):
    d = dfa_creation()
    
    assert d.compute_on_string('aaaba') == True
    assert d.compute_on_string('bbaabab') == True
    assert d.compute_on_string('aabbbb') == False

def test_recording_dfa():
    dfa = dfa_creation()

    serializer = Serializer()
    serializer.serialize(dfa, 'test_dfa')

    unpickled_dfa = serializer.deserialize('test_dfa')

    assert unpickled_dfa.transition_function == dfa.transition_function



