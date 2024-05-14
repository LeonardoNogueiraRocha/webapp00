# myFirstStreamlitApp.py
#import the libraries

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


vetNOME =list(["NOME"])
vetCEL = list(["11988109797"])


#image01 = Image.open('background1.PNG')

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("TÍTULO PRINCIPAL")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

menu = ["Texto_Colunas",
        "Texto_Markdown",
        #"Inserir_Figura",
        "Input Text"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "Texto_Colunas":       
    st.subheader("Texto formatado em colunas")
    st.write("Veja a seguir uma opção de formatação em colunas")    
    cols01 = st.columns(2)    
    cols01[0].write('Texto da Coluna 01')
    cols01[1].write('Texto da Coluna 02')
  
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.5)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        st.code(bytes_data, language='python')
    
elif choice == "Texto_Markdown":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )

elif choice == "Input Text":
    #NOME = st.text_input("Digite o nome: ", "Nome Completo")   
    #CEL = st.text_input("Digite o nº do celular: ", "+55(11)") 
    #if st.button(label = '✔️ Adicionar dados à Tabela'):
    #    vetNOME.append(NOME)
    #    vetCEL.append(CEL)
    #    st.write(vetNOME)
    #    st.write(vetCEL)
    #if st.button(label = '✔️ Exibir DataFrame'):
    #    DF= pd.DataFrame({'NOME':vetNOME, 'CELULAR': vetCEL})
    #    st.dataframe(DF)  
    nome = st.text_input("Nome:", "")
    endereco = st.text_input("Endereço:", "")

    # Botão para salvar os dados
    if st.button("✔️ Salvar"):
        # Verifica se ambos os campos foram preenchidos
        if nome and endereco:
            # Cria um DataFrame com os dados inseridos
            dados = {'Nome': [nome], 'Endereço': [endereco]}
            df = pd.DataFrame(dados)

            # Exibe o DataFrame
            st.write("Dados inseridos:")
            st.dataframe(df)
        else:
            st.warning("Por favor, preencha ambos os campos.")     
   
#elif choice == "Inserir_Figura":
    #st.image(image01, width=800, caption='Rótulo da Imagem 01')  



