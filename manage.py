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
        db.create_all()
        print('Migrations successfull')
    elif command == 'populate':
        from myblog.db.Blog import Blog
        from myblog.db import db
        from datetime import datetime
        for i in range(1,11):
            blog = Blog(category='Fashion', title='Morbi dapibus condimentum', content='You can browse different tags such as multi-page, resume, video, etc. to see more CSS templates. Sed hendrerit rutrum arcu, non malesuada nisi. Sed id facilisis turpis. Donec justo elit, dapibus vel ultricies in, molestie sit amet risus. In nunc augue, rhoncus sed libero et, tincidunt tempor nisl. Donec egestas, quam eu rutrum ultrices, sapien ante posuere nisl, ac eleifend eros orci vel ante. Pellentesque vitae eleifend velit. Etiam blandit felis sollicitudin vestibulum feugiat.\n\nDonec tincidunt leo nec magna gravida varius. Suspendisse felis orci, egestas ac sodales quis, venenatis et neque. Vivamus facilisis dignissim arcu et blandit. Maecenas finibus dui non pulvinar lacinia. Ut lacinia finibus lorem vel porttitor. Suspendisse et metus nec libero ultrices varius eget in risus. Cras id nibh at erat pulvinar malesuada et non ipsum. Suspendisse id ipsum leo.', tags='Best Templates, TemplateMo', comments='a,b,c', created_by='ashutosh', created_at=datetime.now())
            db.session.add(blog)
        db.session.commit()
        print('Database populated')
# a = 'INSERT INTO `myblog`.`blog` (`id`, `banner_url`, `category`, `title`, `content`, `tags`, `comments`, `created_by`, `created_at`) VALUES (3, '/static/store/banners/3.jpg', 'Fashion', 'Morbi dapibus condimentum', 'You can browse different tags such as multi-page, resume, video, etc. to see more CSS templates. Sed hendrerit rutrum arcu, non malesuada nisi. Sed id facilisis turpis. Donec justo elit, dapibus vel ultricies in, molestie sit amet risus. In nunc augue, rhoncus sed libero et, tincidunt tempor nisl. Donec egestas, quam eu rutrum ultrices, sapien ante posuere nisl, ac eleifend eros orci vel ante. Pellentesque vitae eleifend velit. Etiam blandit felis sollicitudin vestibulum feugiat.\n\nDonec tincidunt leo nec magna gravida varius. Suspendisse felis orci, egestas ac sodales quis, venenatis et neque. Vivamus facilisis dignissim arcu et blandit. Maecenas finibus dui non pulvinar lacinia. Ut lacinia finibus lorem vel porttitor. Suspendisse et metus nec libero ultrices varius eget in risus. Cras id nibh at erat pulvinar malesuada et non ipsum. Suspendisse id ipsum leo.', 'Best Templates, TemplateMo', 'a,b,c', 'dev', '2021-01-30 17:03:56');     '