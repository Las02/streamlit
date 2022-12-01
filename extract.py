#/usr/bin/python3
import streamlit as st

st.write("'AD' TO 'A pp D'")
protein_list = st.text_input("Pase in your proteins in oneletter words eg: AD CP AG CD")
pp_protein = ""
for protein in protein_list.split():
    try:
        if len(protein) != 2:
            raise Exception()
  
    except Exception:
        st.write("One or more of the input is not of two chars")
    pp_protein += (f"{protein[0]} pp {protein[1]}\n")  
st.code(pp_protein)
