from setuptools import setup

with open("README.md", 'r') as fh:
    long_description = fh.read()


setup(
    name='myblog-ashutoshc8101',
    version='0.0.1',
    author='ashutoshc8101',
    url='https://github.com/ashutoshc8101/myblog',
    packages=['myblog'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    description='Blog application!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email= 'ashutoshc8101@gmail.com'

)