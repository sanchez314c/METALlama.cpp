"""
Setup script for creating a macOS app bundle for Manggo AI PDF Reader with Dia TTS.
"""
import os
import sys
from setuptools import setup

APP = ['pdf_reader.py']
DATA_FILES = [('.', ['.env'])]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyPDF2', 'requests', 'dotenv', 'pygame', 'tkinterdnd2', 'torch', 'torchaudio', 'torchvision', 'soundfile', 'numpy'],
    'includes': ['tkinter', 'psutil'],
    'excludes': [],
    'plist': {
        'CFBundleName': 'Manggo AI PDF Reader',
        'CFBundleDisplayName': 'Manggo AI PDF Reader',
        'CFBundleGetInfoString': "Read PDFs with ElevenLabs, OpenAI, macOS, and Dia Text-to-Speech",
        'CFBundleIdentifier': "com.manggoaipdfreader",
        'CFBundleVersion': "1.0.1",
        'CFBundleShortVersionString': "1.0.1",
        'NSHumanReadableCopyright': "Copyright © 2025, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
