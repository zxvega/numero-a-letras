from setuptools import setup

readme = open("./README.md", "r")

setup(
    name='numeroaletras',
    packages=['numeroaletras'],  # this must be the same as the name above
    version='0.1',
    description='Convertir numeros a letras en español.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Giovanni Vega',
    # use the URL to the github repo
    url='https://github.com/zxvega/numero-a-letras',
    install_requires=[],
    keywords=[],
    classifiers=[ ],
    license='MIT',
    include_package_data=True   
)