pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Teste")
st.write("Teste ambiente externo para visualização de dashboards")

# 1. Carregar a tabela do Excel
try:
    df = pd.read_excel("C:\\Users\\lucas.fachi\\Desktop\\NICOLAS - GC\\PYTHON\\base_teste.xlsx")
    st.write("Dados carregados com sucesso!")  # Mensagem de sucesso
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o caminho do arquivo.")
    st.stop()  # Para a execução se o arquivo não for encontrado
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.stop()

# 2. Exibir a tabela (opcional, mas útil para depurar)
st.subheader("Dados Carregados")
st.dataframe(df)  # Exibe a tabela no Streamlit

# 3. Verificar as colunas do DataFrame
st.subheader("Colunas disponíveis")
st.write(df.columns)

# 4. Criar o gráfico de linha (ajuste os nomes das colunas)
# Substitua 'Mês', 'Quantidade' e 'Filial' pelos nomes corretos das suas colunas
# Exemplo:  fig = px.line(df, x='NomeDaColunaMes', y='NomeDaColunaQuantidade', color='NomeDaColunaFilial', markers=True)
try:
    fig = px.line(df, x='Mês', y='Quantidade', color='Filial', markers=True) #Adapte esses nomes de coluna
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Erro ao criar o gráfico: Coluna '{e}' não encontrada no DataFrame.  Verifique os nomes das colunas no seu arquivo Excel e ajuste o código.")
except Exception as e:
    st.error(f"Erro inesperado ao criar o gráfico: {e}")
