#/usr/bin/python3
import streamlit as st

st.write("'AD' TO 'A pp D'")
protein_list = st.text_input("Pase in your proteins in oneletter words eg: AD CP AG CD")
pp_protein = ""
is_error = False
for protein in protein_list.split():
    try:
        if len(protein) != 2:
            raise Exception()
        pp_protein += (f"{protein[0]} pp {protein[1]}\n")      
    except Exception:
        st.error("One or more of the input is not of two chars")
        is_error = True
if not is_error:
    st.code(pp_protein)
