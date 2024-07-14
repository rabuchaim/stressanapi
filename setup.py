import codecs
from setuptools import setup, find_packages

setup(
    name='stressanapi',
    version='1.0.1',
    description='StressAnAPI is a Pure Python application for stress testing on APIs. Easily configurable with a json file. Use the arrow keys to control speed, bursts, threads, see results, requests per seconds and much more.',
    url='https://github.com/rabuchaim/StressAnAPI',
    author='Ricardo Abuchaim',
    author_email='ricardoabuchaim@gmail.com',
    maintainer='Ricardo Abuchaim',
    maintainer_email='ricardoabuchaim@gmail.com',
    project_urls={
        "Issue Tracker": "https://github.com/rabuchaim/StressAnAPI/issues",
        "Source code": "https://github.com/rabuchaim/StressAnAPI",
    },    
    bugtrack_url='https://github.com/rabuchaim/StressAnAPI/issues',    
    license='MIT',
    keywords=['stressanapi','stress','stresstest','stress-test','api'],
    packages=['stressanapi'],
    py_modules=['stressanapi', 'stressanapi'],
    package_dir = {'stressanapi': 'stressanapi'},
    include_package_data=True,
    zip_safe = False,
    package_data={
        'stressanapi': [
            'CHANGELOG', 
            'README.md',
            'LICENSE',
            'example.json',
            'stressanapi/stressanapi.py',
            'stressanapi/simple_stressanapi_server.py',
        ],
    },
    entry_points={
        'console_scripts': [
            'stressanapi = stressanapi.stressanapi:main_function',
            'simple_stressanapi_server = stressanapi.simple_stressanapi_server:main_function',
        ]
    },
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',  
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
    ],
    long_description=codecs.open("README.md","r","utf-8").read(),
    long_description_content_type='text/markdown',
)
