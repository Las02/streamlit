#/usr/bin/python3

from doctest import Example
import urllib.parse
import numpy as np
import streamlit as st
from urllib import request

st.write("'AD' TO 'A pp D'")
protein_list = st.text_input("Pase in your proteins in oneletter words eg: AD CP AG CD")
pp_protein = ""
for protein in protein_list.split():
    pp_protein += (f"{protein[0]} pp {protein[1]}\n")    
st.code(pp_protein)
