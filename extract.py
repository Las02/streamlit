#/usr/bin/python3

from doctest import Example
import urllib.parse
import numpy as np
import streamlit as st
from urllib import request

st.write('Welcome to converser boi')

#See if you can get it to auto detect!
IN= st.selectbox("Which **input** do you wanna give?",["Accesion code","Uniprot ID"])
conversion = {"Accesion code":'ACC',"Uniprot ID":'ID'}
Input=conversion[IN]

fasta_headers=st.multiselect('Which options do you want in your fastafiles?', ["Accesion code","Uniprot ID","Protein Name","Organism"])
header_conversion = {"Accesion code":'AC',"Uniprot ID":'ID',"Protein Name":"DE","Organism":'OS'}


osN = -1
deN = -1

if "Protein Name" in fasta_headers:
    N1=st.slider('How many to show for Protein Name?',1,5, (1,10))
    deNstart=N1[0]
    deNend=N1[1]+2


if "Organism" in fasta_headers:
    N2=st.slider('How many to show for Organism?',1,5,(1,10))
    osNstart=N2[0]
    osNend=N2[1]+1

Exampl="R1AB_SARS2 PPNP_BURCJ"
if IN == "Uniprot ID":
    Exampl="P0DTD1 B4ELA5"
idlist = st.text_input('What are your ['+IN+']? Seperated by spaces eg: '+Exampl)


url = 'https://www.uniprot.org/uploadlists/'
#'R1AB_SARS2 PPNP_BURCJ'
params = {
'from': Input,
'to': 'ACC',
'format': 'tab',
'query': idlist
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
    response = f.read()
decoded = response.decode('utf-8')
acc_identy=np.array(decoded.split()).reshape(-1,2)
acc_identy=np.delete(np.delete(acc_identy,0,1),0,0)



# %%


fastasequences = np.array([])
for i in range(len(acc_identy)):
    path ='https://www.uniprot.org/uniprot/' + acc_identy[i][0] + '.fasta'
    req=urllib.request.urlopen(path)
    fastasequences = np.append(fastasequences,req.read().decode('utf-8'))


# %% [markdown]
# Get all info for finding correct name

# %%
allinfo = np.array([])
for i in range(len(acc_identy)):
    path ='https://www.uniprot.org/uniprot/' + acc_identy[i][0] + '.txt'
    req=urllib.request.urlopen(path)
    allinfo = np.append(allinfo,req.read().decode('utf-8'))


# %%

header_shorthand=[]
for i in range(len(fasta_headers)):
    header_shorthand.append( header_conversion[fasta_headers[i]])



final_list=[]
for i in range(len(allinfo)):
    names =[]
    for ID in header_shorthand:
        for line in allinfo[i].split(sep='\n'):
            if line[0:2] == ID:
                if ID == "OS":
                    
                    if osNend > len(line.split()):
                        line_worked = line.split()[osNstart::]
                    else:
                        line_worked = line.split()[osNstart:osNend]
                    names.append("_".join(line_worked))

                elif ID == "DE":
                    if deNend > len(line.split()):
                        line_worked = line.replace('=',' ').split()[1+deNstart::]
                    else:
                        line_worked = line.replace('=',' ').split()[1+deNstart:deNend]
                    
                    names.append("_".join(line_worked))

                elif ID == "AC" :
                    line_worked = line.split()[1]
                    names.append(line_worked)

                elif ID == "ID" :
                    line_worked = line.split()[1]
                    names.append((line_worked))
                
                break
    final_list.append(names)
                    #names+=[line.split()[1]+'_'+ line.split()[2][:] + "_" +acc_identy[i][0]]
#st.write(names)

# %%
finaloutput=''
for found_fasta_headers in final_list:
    header_name=[]

    for types_headers in found_fasta_headers:
        header_name.append('['+types_headers+']')
    header_name="_".join(header_name)

    finaloutput += '>' + header_name+'\n'+"\n".join(fastasequences[i].split(sep='\n')[1::])
st.code(finaloutput)


