from setuptools import setup

install_requires = [
    'pandas>=0.25.0',
    'numpy>=1.15.4',
    'glob2>=0.6',
    'functools'
]

# tests_require = ['pytest>=4.0.2']

setup(name='src',
      version='0.0.1',
      description='fill this in with any description',
      author='Misha Berrien',
      author_email='misha.berrien@gmail.com',
      install_requires=install_requires,
      packages=['src'])
