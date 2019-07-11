#!/usr/bin/env python3

from setuptools import find_packages, setup


setup(
    name='fill-word-solver',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=find_packages('src', include=[
        'guss',
    ]),
    include_package_data=True,
    zip_safe=False,
    # see Pipfile
    install_requires=[],
    url='https://github.com/Abzac/fill-word-solver',
    license='',
    author='Abzac',
    author_email='',
    description='Fill Word Solver',
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
