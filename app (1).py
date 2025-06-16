import streamlit as st

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

# Streamlit app interface
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0, step=0.1)
num2 = st.number_input("Enter second number", value=0.0, step=0.1)

# Dropdown for operator selection
operator = st.selectbox("Select operator", ["+", "-", "*", "/"])

# Button to calculate
if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.write(f"The result is: {result}")