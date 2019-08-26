import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="sana-python",
        version="0.0.1",
        author="Joel Linder",
        author_email="business@joellinder.dev",
        description="Python library for Sana APIS (https://sanalabs.com/developer/).",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jollescott/sana-python",
        packages=setuptools.find_packages(),
        license='MIT',
        install_requires=[
            'requests',
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
