import streamlit as st
import random

paises = ["Brasil", "Argentina", "Peru", "Suriname", "Uruguai", "Paraguai", "Bolivia", "Colombia", "Venezuela", "Chile", "Guiana", "Equador" ] 

def embaralhar_palavra(palavra):
    palavra_embaralhada = list(palavra)
    random.shuffle(palavra_embaralhada)
    return "".join(palavra_embaralhada)

pontuacao = 0
tentativas_restantes = 3

st.title(f"Jogo de Anagramas")
st.subheader(f"Tentativas restantes: {tentativas_restantes}")

# Inicialização do jogo
palavra_escolhida = random.choice(paises)
palavra_embaralhada = embaralhar_palavra(palavra_escolhida)

st.write(f"Anagrama: {palavra_embaralhada}")
st.write(f"Pontuação: {pontuacao}")
tentativa = st.text_input("Sua tentativa:").title()

if st.button("Verificar palavra"):
    if tentativa == palavra_escolhida:
        pontuacao = pontuacao + 1
        tentativas_restantes = 3
        st.success("Correto! Próxima palavra.")
        palavra_escolhida = random.choice(paises)
        palavra_embaralhada = embaralhar_palavra(palavra_escolhida)
    else:
        tentativas_restantes =- 1
        st.error(f"Incorreto!")

    if tentativas_restantes == 0:
        pontuacao = 0
        st.warning("Você excedeu o número de tentativas. Jogo encerrado.")

    if pontuacao == 30:
        st.success("Parabéns! Você decifrou todas as palavras. Você venceu o jogo!")