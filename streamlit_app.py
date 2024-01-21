import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
from supabase import create_client, Client

"""  < PENDENTE : MIGRAR A URL E A CHAVE PARA A ÁREA SECRETA >"""

secretsurl = 'https://jdwvqrblltbbffnivqcn.supabase.co'
secretskey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impkd3ZxcmJsbHRiYmZmbml2cWNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg1NzU3NDgsImV4cCI6MjAxNDE1MTc0OH0.wpPFFHOZ4QV6i8FwSvS6e17Sdn86D_H88UOVWccgxPs'

supabase = create_client(
    secretsurl,
    secretskey 
)

Options_Colecoes = []


Colecoes_df = pd.DataFrame(
    supabase.table('dColecoes'
    ).select('id', 'nome_USA'
    ).execute(
    ).data
)
with st.sidebar:
    st.selectbox(
        # Lista Coleção Selecionada
        label = "Coleção:", 
        options = Colecoes_df['nome_USA'],
        index = None,
        disabled = False,
        key = "Colecao_selecionada",
        help = "Clique e selecione a coleção que será utilizada na simulação de contratos",
        placeholder = "Selecione a coleção desejada",
        label_visibility = "visible"
    )


    if st.session_state.get('Colecao_selecionada') == None:
        Id_Colecao_selecionada = None

    else:
        Id_Colecao_selecionada = Colecoes_df.loc[(Colecoes_df['nome_USA'] == st.session_state.get('Colecao_selecionada'))
        ]['id'].to_string(index=False)

        dArmas = supabase.table('dArmas'
        ).select('nome, dArmas_Tipo(arma), dNivel(nivel,nivel_descricao_USA)'
        ).eq('id_colecao', Id_Colecao_selecionada).execute().data 

        opcoes_niveis = []
        dArmas_list = []
        for skin in dArmas:
            nome = skin['nome']
            arma = skin['dArmas_Tipo']['arma']
            nivel =  skin['dNivel']['nivel']
            nivel_USA = skin['dNivel']['nivel_descricao_USA']

            opcoes_niveis.append(nivel_USA)
            dArmas_list.append([nome, arma, nivel, nivel_USA])

        dArmas_df = pd.DataFrame(dArmas_list, columns = ['Nome', 'Arma', 'Nivel','Nivel USA'])
        opcoes_niveis = list(dict.fromkeys(opcoes_niveis))

        st.selectbox(
        "Niveis:",
        options=opcoes_niveis[1:], 
        index=None, 
        key='Nivel_Selecionado', 
        help='Clique e selecione o nível das skins que serão a base do contrato', 
        disabled= False,
        placeholder = "Selecione o nível desejado", 
        label_visibility="visible")


        if st.session_state.get('Nivel_Selecionado') != None:
        
            armas_base = dArmas_df.loc[(dArmas_df['Nivel USA'] == st.session_state.get('Nivel_Selecionado'))]
            nivel_aramas_esperadas = int(dArmas_df.loc[(dArmas_df['Nivel USA'] == st.session_state.get('Nivel_Selecionado'))]['Nivel'].to_string(index=False)[0]) + 1

            armas_esperadas = dArmas_df.loc[(dArmas_df['Nivel'] == nivel_aramas_esperadas)]

            
            
        st.markdown("Armas base:")
        st.dataframe(armas_base,  hide_index=True, use_container_width= True, column_order=("Arma","Nome"))
    
        st.markdown("Armas esperadas:")
        st.dataframe(armas_esperadas,  hide_index=True, use_container_width= True, column_order=("Arma","Nome"))



"""
- Incluir botão para solicitar a simulação dos contratos

Quando o botão for clicado:
- Solicitar do meu BD as informações de qualidade para Simulação do contrato.
- Solicitar à Steam as informações de compra do nível atual e de venda do próximo nível.

Após receber as informações solicitadas:
- Criar lista de combinações
- Calcular os resultados

Exibir tabela com os resultado de cada contrato calculado

Ao clicar no contrato calculado:
- Exibir os itens que precisam ser comprados (com os links)
- Exibir as possibilidades e os itens que podem retornar

"""