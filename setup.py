import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='real-time-voice-cloning',
    version="0.0.1",
    packages=['utils', 'encoder', 'encoder.data_objects', 'toolbox', 'synthesizer', 'synthesizer.utils'],
    author="Ahmet Yusuf Sirin",
    author_email='ayusufsirin@gmail.com',
    description="Real-time voice clonning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayusufsirin/real-time-voice-cloning",
    project_urls={
        "Bug Tracker": "https://github.com/ayusufsirin/real-time-voice-cloning/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
