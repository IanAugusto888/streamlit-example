import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

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