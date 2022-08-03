from distutils.core import setup
import py2exe
import os
import random
import time
import sqlite3
import pathlib
import re
import glob

setup(zipfile=None, options={"py2exe": {"bundle_files": 1}}, windows=["spy.py"])
