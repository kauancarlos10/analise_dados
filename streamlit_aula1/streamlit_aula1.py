import streamlit as st
import pandas as pd

st.write("Olá, mundo")

st.divider() 

st.title("Meu primeiro dash")

st.subheader("Seu Nome Aqui")

meu_nome = "kauan carlos carneiro " 
minha_idade = 17

st.write(f"Aluno: {meu_nome} - Idade: {minha_idade} anos")

st.divider()

df = pd.DataFrame({
'Matérias': ['Português', 'Matemática', 'Python', 'Frame'],
'Notas': [5, 9, 7, 10]
})

st.write("Minhas Notas:")
st.write(df)

st.divider()

st.subheader("Caixa do Supermercado")

produtos = {
    'Arroz': 25.50,
    'Feijão': 8.90,
    'Macarrão': 4.50,
    'Suco': 6.00
}

item_selecionado = st.selectbox("Escolha um item de supermercado:", list(produtos.keys()))

quantidade = st.number_input("Quantidade:", min_value=1, step=1)

def calcular_preco(item, qtd):
    preco_unitario = produtos[item]
    return preco_unitario * qtd

valor_total = calcular_preco(item_selecionado, quantidade)
st.metric(label=f"Total a pagar ({item_selecionado})", value=f"R$ {valor_total:.2f}")