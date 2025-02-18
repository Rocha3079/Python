import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Teste")
st.write("Teste ambiente externo para visualização de dashboards")

# 1. Carregar a tabela do Excel
try:
    df = pd.read_excel("C:\\Users\\lucas.fachi\\Desktop\\NICOLAS - GC\\PYTHON\\base_teste.xlsx")
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o caminho do arquivo.")
    st.stop()  # Para a execução se o arquivo não for encontrado
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.stop()
try:
    fig = px.line(df, x='Mês', y='Quantidade', color='Filial', markers=True) #Adapte esses nomes de coluna
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Erro ao criar o gráfico: Coluna '{e}' não encontrada no DataFrame.  Verifique os nomes das colunas no seu arquivo Excel e ajuste o código.")
except Exception as e:
    st.error(f"Erro inesperado ao criar o gráfico: {e}")
try:
    fig = px.line(df, x='Mês', y='Venda R$ 2025', color='Filial', markers=True) #Adapte esses nomes de coluna
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Erro ao criar o gráfico: Coluna '{e}' não encontrada no DataFrame.  Verifique os nomes das colunas no seu arquivo Excel e ajuste o código.")
except Exception as e:
    st.error(f"Erro inesperado ao criar o gráfico: {e}")