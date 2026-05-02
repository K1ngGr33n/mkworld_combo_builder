import matplotlib.pyplot as plt
import numpy
from io import BytesIO
import re

from stats import *

c = input("H: ")

while c != "stop":
    try:
        (print(viewStats(c)))
    except Exception as err:
        print(f"Error: {err}")
    
    c = input("H: ")