import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lib_nn',
    version='0.0.1',
    author='Wojciech Broniowski',
    author_email='Wojciech.Broniowski@ifj.edu.pl',
    description='neural package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bronwojtek/lib_nn',
    packages=['neural'],
    install_requires=['requests'],
)
