"""Regular Expression explanation text"""

class RE():
    def __init__(self, expression: str):
        self.expression = expression

    """ Returns a DFA equivalent to this Regular Expression using the syntax
        tree algorithm """
    def convert_to_dfa(self):
        #TODO implement
        pass
    
    def edit_expression(self, new_expression: str):
        self.expression = new_expression