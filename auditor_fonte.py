import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Teste")
st.write("Teste ambiente externo para visualização de dashboards")

# 1. Carregar a tabela do Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type="xlsx")
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Dados carregados com sucesso!")  # Mensagem de sucesso
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
    try:
        fig = px.line(df, x='Mês', y='Quantidade', color='Filial', markers=True) # Adapte esses nomes de coluna
        st.plotly_chart(fig)
    except KeyError as e:
        st.error(f"Erro ao criar o gráfico: Coluna '{e}' não encontrada no DataFrame. Verifique os nomes das colunas no seu arquivo Excel e ajuste o código.")
    except Exception as e:
        st.error(f"Erro inesperado ao criar o gráfico: {e}")
else:
    st.info("Por favor, envie um arquivo Excel para continuar.")
