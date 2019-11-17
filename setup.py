import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bitmaps',
    description="Package to produce bitmap text images for use with small, "
                "low-resolution displays",
    version='0.0.1',
    author="Bill Tubbs",
    license='MIT',
    install_requires=['pillow']
)
