"""Setup file for Mailroom Madness package."""
from setuptools import setup


dependences = ['ipython']
extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
}


setup(
    name='Mailroom Madness',
    description='401 Python project',
    version='0.1',
    authors='Anna, Morgan',
    author_email='morganelle@gmail.com',
    license='MIT',
    py_modules=['mailroom_madness', 'test_mailroom_madness'],
    package_dir={'': 'src'},
    install_requires=dependences,
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'mailroom_madness = mailroom_madness:main'
        ]
    }
)
