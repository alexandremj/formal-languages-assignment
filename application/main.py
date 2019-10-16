import dfa
import nfa
import re
import rg

def print_help():
    print("""
            Commands:

            h - prints this help text
            q - exit
        """)

def main():
    print('Formal Languages Assignment by Alexandre Muller Junior')
    print('This software is free. Refer to the license for more details')

    command_list = ['h', 'q']

    while True:
        command = input('>>> ')
        # ToDo print the available commands

        if command not in command_list:
            print('Unknown command!')
        elif command == 'h':
            print_help()
        elif command == 'q':
            print('Exiting project...')
            exit()

if __name__ == '__main__':
    main()
