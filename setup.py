from setuptools import setup, find_packages
from pathlib import Path

# Helper function to parse requirements.txt
def parse_requirements(filename):
    lines = Path(filename).read_text().splitlines()
    # Filter out empty lines and comments
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


setup(
    name='graph-utils',
    version='0.1.0',
    author='Jason Jain',
    author_email='starlightjason2@gmail.com',
    description='Python wrapper for matplotlib and scipy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True, # to include non-python files specified in MANIFEST.in or package_data
)
