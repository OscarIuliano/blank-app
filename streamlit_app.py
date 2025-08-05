import streamlit as st

st.title("Calcolatrice di prova 2")

num1 = st.number_input("Primo numero")
operatore = st.selectbox("Operazione", ["+", "-", "*", "/"])
num2 = st.number_input("Secondo numero")
vocale = st.audio_input("registra vocale")

if st.button("Calcola"):
    try:
        if operatore == "+":
            risultato = num1 + num2
        elif operatore == "-":
            risultato = num1 - num2
        elif operatore == "*":
            risultato = num1 * num2
        elif operatore == "/":
            risultato = num1 / num2
        st.success(f"Risultato operazione: {risultato}")
    except ZeroDivisionError:
        st.error("Errore: divisione per zero")

if st.button('Riproduci') :
    output = st.audio(vocale, format="audio/mpeg", loop=False)
