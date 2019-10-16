import dfa
import nfa
import regex
import rg
import serializer

structure_letters = ['D', 'E', 'N', 'R']
loaded_structures = []
command_list = ['b', 'c', 'h', 'l', 'q']

def print_help():
    print("""
            Commands:
            c - create a new automaton/grammar/regex
            h - prints this help text
            l - loads a structure
            q - exit
        """)

def create_new():
    structure_type = ''

    while True:
        structure_type = input('Create: (D)FA, (N)FA, R(E), (R)G or (q)uit ')

        if structure_type == 'q':
            return

        if not structure_type in structure_letters:
            print('Invalid structure selected... ')
        else:
            break

    # ToDo
    # check for consistency issues (e.g. function contains a state not in
    # states
    # 
    # discover how to convert the transition function to required format
    if structure_type == 'D':
        print('Creating Deterministic Finite Automaton')

        states = input('Insert the states: ').split('')
        input_symbols = input('Insert the input symbols: ').split('')
        transition_function = input('Insert the transition function: ')
        initial_state = input('Insert the initial state: ')
        accept_states = input('Insert the accept states: ').split('')

        d = dfa.DFA(states, input_symbols, transition_function,
                        initial_state, accept_states)

        print(d)
        loaded_structures.append(d)
        return d

    elif structure_type == 'E':
        print('Creating Regular Expression')

        expression = input('Insert the base expression: ')

        r = regex.RE(expression)

        print(r)
        loaded_structures.append(r)
        return r

    elif strucuture_type == 'G':
        print('Creating Regular Grammar')

        nonterminals = input('Insert the nonterminal symbols: ').split('')
        terminals = input('Insert the terminal symbols: ').split('')
        productions = input('Insert the grammar productions: ')
        start_symbol = input('Insert the start symbol: ')

        g = rg.RG(nonterminals, terminals, productions, start_symbol)

        print(g)
        loaded_structures.append(g)
        return g

    elif structure_type == 'N':
        print('Creating Nondeterministic Finite Automaton')
        
        states = input('Insert the states: ').split('')
        input_symbols = input('Insert the input symbols: ').split('')
        transition_function = input('Insert the transition function: ')
        initial_state = input('Insert the initial state: ')
        accept_states = input('Insert the accept states: ').split('')

        n = nfa.NFA(states, input_symbols, transition_function,
                        initial_state, accept_states)

        print(n)
        loaded_structures.append(n)
        return n

# ToDo insert this into a buffer of currently loaded structures
def load_structure():
    serializer_instance = serializer.Serializer()

    file_name = ''

    while True:
        file_name = input('Insert the pickle file name or (q)uit: ')

        if file_name == 'q':
            break
        
        try:
            loaded_structures.append(
                serializer_instance.deserialize(file_name)
            )
        except OSError: 
            print('Error: could not open file.')

def main():
    print('Formal Languages Assignment by Alexandre Muller Junior')
    print('This software is free. Refer to the license for more details')

    while True:
        command = input('>>> ')
        # ToDo print the available commands

        if command not in command_list:
            print('Unknown command!')
        elif command == 'b':
            # ToDo make loaded_structures human-readable
            print(loaded_structures)
        elif command == 'c':
            create_new()
        elif command == 'h':
            print_help()
        elif command == 'l':
            load_structure()
        elif command == 'q':
            print('Exiting project...')
            exit()

if __name__ == '__main__':
    main()
