from setuptools import setup, find_packages
from setuptools.config.expand import entry_points

setup(
    name="YTClipper",  # Updated project name
    version="0.2",  # Updated version to reflect the new project
    python_requires=">=3.12",
    packages=find_packages(where='src'),  # Automatically locate packages under 'src'
    package_dir={'': 'src'},  # Packages are located in the 'src' directory

    # Dependencies required for the updated functionality
    install_requires=[
        "click>=8.0",          # For enhanced CLI functionality
        "yt-dlp>=2026.6.9",
        "setuptools>=82.0.1",
        "static_ffmpeg>=3.0",
    ],

    # Project metadata
    author="Reina-TAFE",
    author_email="20066312@tafe.wa.edu.au",
    description="A CLI-based Youtube Clipper",
    license="MIT",
    keywords="Youtube Clipper CLI",
    url="https://github.com/Reina-TAFE/YTClipper",  # Replace with your repository URL
    scripts=["YT_Clipper"],
    entry_points={
        'console_scripts': [
            'YTClipper = YTClipper.cli:cli',
        ],
    },
)
