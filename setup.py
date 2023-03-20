from setuptools import setup

setup(
  name='ASE_Assignments',
  version='7.0.0',
  packages=['HW1', 'HW1.src', 'HW1.test',
            'HW2', 'HW2.src', 'HW2.test',
            'HW3', 'HW3.src', 'HW3.test',
            'HW4', 'HW4.src', 'HW4.test',
            'HW5', 'HW5.src', 'HW5.test',
            'HW6', 'HW6.src', 'HW6.test',
            'HW7', 'HW7.src', 'HW7.test'],
  license='LICENSE.md',
  description='Sample project with HELP text and Test Suite',
  long_description=open('README.md', encoding="utf8").read(),
)
