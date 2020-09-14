import setuptools

setuptools.setup(
    #Package which can be refrenced in the template
    name = "orquestra",
    #Tells installer to look for sub-dr called python which contains the source code
    packages = setuptools.find_packages(where="python"),
    #allow the python dir to be imported without the python path prefix
    package_dir = {
        "" : "python"
    },
    classifiers = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)