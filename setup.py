from setuptools import setup, find_packages
 
setup(
    name                = 'codesave',
    version             = '0.0.1',
    description         = 'Save the code automatically.',
    author              = 'sawol',
    author_email        = 'sawol634@gmail.com',
    url                 = 'https://github.com/sawol/codesave/',
    download_url        = '',
    install_requires    =  ['beautifulsoup4', 'requests', 'lxml', 'selenium', 'github'],
    packages            = find_packages(),
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)


