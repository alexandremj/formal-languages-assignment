import json

from application.dfa import DFA
from application.serializer import Serializer

def test_dfa_creation():
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

s = ['aaaba', 'bbaabab', 'aabbbb']
def test_computing_strings(dfa, test_strings=s):
    for string in test_strings:
        print(f'{string} computed on the given automata returned
                {d.compute_on_string(string)}')

def test_recording_dfa(dfa):
    serializer = Serializer()
    serializer.serialize(dfa, 'test_dfa')

    assert serializer.deserialize('test_dfa') == dfa

def main():
    dfa = test_dfa_creation()
    test_computing_strings(dfa)
    test_recording_dfa(dfa)

if __name__ == '__main__':
    main()
