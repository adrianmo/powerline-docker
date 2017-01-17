# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name             = 'powerline-docker',
    description      = 'A Powerline segment for showing Docker container statuses',
    version          = '1.0.4',
    keywords         = 'powerline docker container status',
    license          = 'MIT',
    author           = 'Adrian Moreno Martinez',
    author_email     = 'adrian@morenomartinez.com',
    url              = 'https://github.com/adrianmo/powerline-docker',
    packages         = ['powerline_docker'],
    install_requires = ['powerline-status', 'docker-py'],
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
