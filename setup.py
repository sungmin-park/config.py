from setuptools import setup

setup(
    name='sconfig',
    version='0.0.1',
    license='MIT',
    url='https://github.com/sungmin-park/sconfig.py',
    author='Park Sung Min',
    description='Simple config',
    packages=['sconfig'],
    install_requires=[],
    extras_require={
        'dev': ['pytest==3.6.3']
    }
)
