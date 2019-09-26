from application.dfa import DFA
from application.serializer import Serializer

"""Test computing strings on the automaton defined on dfa_creation()"""
def test_computing_strings(dfa_creation):
    
    assert dfa_creation.compute_on_string('aaaba') == True
    assert dfa_creation.compute_on_string('bbaabab') == True
    assert dfa_creation.compute_on_string('aabbbb') == False