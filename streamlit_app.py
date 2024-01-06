import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
from supabase import create_client, Client
#secretsurl = 'https://jdwvqrblltbbffnivqcn.supabase.co'
#secretskey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impkd3ZxcmJsbHRiYmZmbml2cWNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg1NzU3NDgsImV4cCI6MjAxNDE1MTc0OH0.wpPFFHOZ4QV6i8FwSvS6e17Sdn86D_H88UOVWccgxPs'

#supabase = create_client(
#    st.secrets["secretsurl"],
#    st.secrets["secretskey"] 
#)

#Colecoes_list = supabase.table('dColecoes').select('id', 'nome_USA').execute()

Colecao_selecionada = st.multiselect(
    "Coleção", 
    options=[" teste", "sera", "Que", "vai?"],
    max_selections= 1,
    disabled=False,
    placeholder= "Selecione a coleção desejada", 
    )

"""

Validar os acessos as servidor

Incluir uma validação de dados para selecionar a coleção

Com base na seleção informada:
- Exibir uma tabela com a distribuição de skins por nivel

Com base na coleção e nível selecionados:
- Relacionar as skins do nível selecionado e do próximo (em caixas diferentes)

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