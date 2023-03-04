from setuptools import setup, find_packages

setup(
    name="ormgap",
    version='v0.0.16',
    author="victor993",
    author_email="v.hernandez@cgiar.com",
    description="ORM para la base de datos de gap analysis",
    url="https://github.com/victor-993/pru",
    download_url="https://github.com/victor-993/pru",
    packages=find_packages(),
    keywords='mongodb orm gap-analysis',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine"
    ]
)
