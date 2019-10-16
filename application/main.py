import dfa
import nfa
import re
import rg

structure_letters = ['D', 'E', 'N', 'R']
command_list = ['c', 'h', 'q']

def print_help():
    print("""
            Commands:
            c - create a new automaton/grammar/regex
            h - prints this help text
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
        return d

    elif structure_type == 'E':
        print('Creating Regular Expression')

        expression = input('Insert the base expression: ')

        r = re.RE(expression)

        print(r)
        return r

    elif strucuture_type == 'G':
        print('Creating Regular Grammar')

        nonterminals = input('Insert the nonterminal symbols: ').split('')
        terminals = input('Insert the terminal symbols: ').split('')
        productions = input('Insert the grammar productions: ')
        start_symbol = input('Insert the start symbol: ')

        g = rg.RG(nonterminals, terminals, productions, start_symbol)

        print(g)
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
        return n

def main():
    print('Formal Languages Assignment by Alexandre Muller Junior')
    print('This software is free. Refer to the license for more details')

    while True:
        command = input('>>> ')
        # ToDo print the available commands

        if command not in command_list:
            print('Unknown command!')
        elif command == 'c':
            create_new()
        elif command == 'h':
            print_help()
        elif command == 'q':
            print('Exiting project...')
            exit()

if __name__ == '__main__':
    main()
