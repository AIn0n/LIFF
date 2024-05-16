from setuptools import setup, find_packages

setup(
    name="liff",
    version="0.0.420",
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'liff=liff.__main__:main',
            ],
        },
)
