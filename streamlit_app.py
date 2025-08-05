import streamlit as st

st.markdown("""
    <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: none;
        }
    </style>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Applicazione 1", "Applicazione 2", "Applicazione 3"])

with tab1:
    st.header("Questo è il tab dell'applicazione 1")
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
