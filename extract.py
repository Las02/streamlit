#/usr/bin/python3
import streamlit as st

st.write("'AD' TO 'A pp D'")

remove = st.checkbox('Remove the same interactions')

protein_list = st.text_input("Pase in your proteins in oneletter words eg: AD CP AG CD")



ppset = list()
for protein in protein_list.split():
    if remove:
        if protein not in ppset and protein[::-1] not in ppset:
            ppset.append(protein)
    else:
        ppset.append(protein)
    
pp_protein = ""
is_error = False
errors = 0
for protein in ppset:
    try:
        if len(protein) != 2:
            raise Exception()
        pp_protein += (f"{protein[0]} pp {protein[1]}\n")      
    except Exception:
        errors += 1
        is_error = True
if not is_error:
    st.code(pp_protein)
    pp_protein = ""
    for protein in ppset:
        pp_protein += (f"{protein[0]} (pp) {protein[1]}\n")      
    st.code(pp_protein)
else:
    st.error(f"{errors} of the input(s) are not of two chars")
