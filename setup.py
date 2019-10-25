import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='error_cat',  

     version='0.2',

     scripts=['error_cat', 'error_parsing.py', 'ascii_error.py'] ,

     author="Robert Morgan",

     author_email="robert.morgan@wisc.edu",

     description="A fun way to display python errors",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/rmorgan10/error_cat",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

)
