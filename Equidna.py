import streamlit as st
import groq as Groq

models =  ["Equidana", "Mongo", "Safirus"]

st.set_page_config(page_title="Equidna IA",
                       page_icon="./Equidna.png", 
                       layout="centered")


def confUser():
    secretKey = st.secrets["apiKey"]
    return Groq(api_key = secretKey)

def confModel(client , model, inputMensaje):
    return client.chat.completions.create(
        messages = [{"role": "user", "content": inputMensaje}],
        thisModel = model,
        stop = None,
        stream = True
    )

def answer(completeChat):
    completAnwser = ""
    for sentence in completeChat:
        if sentence.choices[0].delta.content:
            completAnwser += sentence.choices[0].delta.content
            yield sentence.choices[0].delta.content
    return completAnwser

def startEquidna():

    st.title("Talk to Equidna")

    with st.sidebar:
        st.sidebar.title("conversations")
        selection = st.sidebar.selectbox("Elija el ChatBot de su preferencia", options = models, index=0)
        st.sidebar.text("chats with Equidna")
        st.sidebar.button("Chat")
    return selection

def start():
    if( "mensaje" not in st.session_state):
        st.session_state.messages = []

def record(role, content, avatar):
    st.session_state.messages.append({"role": role, "content": content, "avatar":avatar})

def showRecord():
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message["avatar"]):
            st.markdown(message["content"])

def containerChat():
    contenedorDelChat = st.container(height=420,border=False)
        # Abrimos el contenedor del chat y mostramos el historial.
    with contenedorDelChat:
        showRecord()

def main():
    completeChat = ""
    
    startEquidna()
    userClient = confUser
    userModel = startEquidna
    start()
    containerChat()

    message = st.chat_input("Comentale a Equidna que deseas")
    if message:
        record("user", message, "./User.png")
        completeChat = confModel(userClient, userModel, message)
    
    if completeChat:
        with st.chat_message("assistant"):
            completeAnwser = st.write_stream(answer(completeChat))
        record("assitant", completeAnwser, "./Equidna.png")
        print(message)
        st.rerun()

main()
