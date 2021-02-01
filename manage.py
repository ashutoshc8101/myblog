from myblog import app
from sys import argv

def print_available_commands():
    print('''
Command line tool for managing myblog
Available commands
1. run - Runs development server 
2. migrate - Create migrations for database
3. populate - Fill db with dummy data
''')

if len(argv) <= 1:
    print_available_commands()
else:
    command = argv[1]
    if command == 'run':
        if __name__ == '__main__':
            app.config['ENV'] = 'devlopment'
            app.run(debug=True)
    elif command == 'migrate':
        from myblog.db import db
        db.session()
        print('Dropping existing tables...')
        db.drop_all()
        print('Creating new tables...')
        db.create_all()
        db.session.commit()
        print('Migrations successful')
    elif command == 'populate':
        pass

        # from myblog.db.Blog import Blog
        # from myblog.db import db
        # from myblog.db.User import User
        # from datetime import datetime
        # from myblog.db.Category import Category
        # from flask.ext.bcrypt import Bcrypt

        # categories = ['Fashion', 'Art', 'Music', 'Education', 'Space']
        # with open('dummy_content.txt') as rf:
        #     content = rf.read()
        # for category in categories:
        #     cat = Category(title=category, description='{} description'.format(category))
        #     blogs = ['How to be great', 'Bad music vs good music', 'Art is a gift', 'Einstein was wrong', 'Evolution of Fashion']
        #     for index, blog in blogs:
        #         blog = Blog(title=blog, category=cat, content=content)

        # db.session.commit()
        # print('Database populated')