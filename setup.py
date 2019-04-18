from setuptools import setup

setup(
    name="fedmapld",
    version="0.1",
    packages=["fedmapld"],
    install_requires=["fedelemflowlist", "olca-ipc", "pandas"],
    license="CC0",
    classifiers=[
        "Development Status :: Alpha",
        "Environment :: IDE",
        "Intended Audience :: Science/Research",
        "License :: CC0",
        "Programming Language :: Python :: 3.x",
        "Topic :: Utilities",
    ],
)
