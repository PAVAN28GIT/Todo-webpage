import streamlit as st
import user_module as um

todos = um.read_file()

st.title("My Todo App")
st.subheader("This app is to increase your Productivity")


def add_todo():
    new_todo = st.session_state['input'] + "\n"
    if new_todo != "\n":
        todos.append(new_todo)
        um.write_file(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        um.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter New ToDo...", on_change=add_todo, key="input")
