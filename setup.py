import setuptools

setuptools.setup(
    name="py3qterm",
    version="0.4",
    author="Michael Ramsey",
    author_email="mike@hackerdise.me",
    description="Simple terminal/console widget for PyQt5/Pyside2 with vt100 support based on pyqtermwidget (https://bitbucket.org/henning/pyqtermwidget) Original Author: Henning Schroeder ",
    url="https://gitlab.com/mikeramsey/py3qtermwidget",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
