from setuptools import setup, find_packages

setup(
    name="dia",
    version="0.1.0",
    description="Add your description here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    packages=find_packages(include=["dia", "dia.*"]),
    install_requires=[
        "descript-audio-codec>=1.0.0",
        "gradio>=5.25.2",
        "huggingface-hub>=0.30.2",
        "numpy>=2.2.4",
        "pydantic>=2.11.3",
        "soundfile>=0.13.1",
        "torch>=2.6.0",
        "torchaudio>=2.6.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
