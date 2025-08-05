import streamlit as st

st.title("Calcolatrice di prova")

num1 = st.number_input("Primo numero")
operatore = st.selectbox("Operazione", ["+", "-", "*", "/"])
num2 = st.number_input("Secondo numero")

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
