import streamlit as st
import pandas as pd
#
# employee_data = {
#     'ID': [123],
#     'Name': ['abc'],
#     'Age': [14],
#     'Department': ['abs']
# }

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['ID', 'Name', 'Age', 'Department'])

# df = pd.DataFrame(employee_data)

def add_employee(id, name, age, department):
    new_employee = {'ID': id, 'Name': name, 'Age': age, 'Department': department}
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_employee])], ignore_index=True)

def delete_employee(id):
    st.session_state.df = st.session_state.df[st.session_state.df['ID'] != id]
def update_employee(id, name, age, department):
    st.session_state.df.loc[st.session_state.df['ID'] == id, ['Name', 'Age', 'Department']] = [name, age, department]

st.title("Employee Management System")

menu = ["Add", "Delete", "Update", "View"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add":
    st.subheader("Add Employee")
    id = st.text_input("ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=65)
    department = st.text_input("Department")
    if st.button("Add Employee"):
        add_employee(id, name, age, department)
        st.success(f"Added employee: {name}")

elif choice == "Delete":
    st.subheader("Delete Employee")
    id = st.text_input("ID")
    if st.button("Delete Employee"):
        delete_employee(id)
        st.success(f"Deleted employee with ID: {id}")

elif choice == "Update":
    st.subheader("Update Employee")
    id = st.text_input("ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=65)
    department = st.text_input("Department")
    if st.button("Update Employee"):
        update_employee(id, name, age, department)
        st.success(f"Updated employee with ID: {id}")

elif choice == "View":
    st.subheader("View Employees")
    st.dataframe(st.session_state.df)

if st.checkbox("Show Employee Data"):
    st.dataframe(st.session_state.df)

