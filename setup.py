import os

from setuptools import setup, find_packages

from botai.main import __version__


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
        name="bot.ai",
        version=".".join(map(str, __version__)),
        description="A minimal chatbot platform.",
        long_description=read('README.md'),
        url='',
        license='MIT',
        author='Marc Lucchini',
        packages=find_packages(exclude=['tests']),
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Flask',
            'Framework :: spaCy'
        ],
        install_requires=[],
        tests_require=[],
)
