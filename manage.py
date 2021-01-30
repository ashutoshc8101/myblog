from myblog import app
from sys import argv

def print_available_commands():
    print('''
Command line tool for managing myblog
Available commands
1. run - Runs development server 
''')

if len(argv) <= 1:
    print_available_commands()
else:
    if argv[1] == 'run':
        if __name__ == '__main__':
            app.config['ENV'] = 'devlopment'
            app.run(debug=True)