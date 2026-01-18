import streamlit as st

#Functions for performing basic arithmetic calculations

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y == 0:
        raise ZeroDivisionError("Math Error! Division by zero gives infinity.")
    return x/y
def calculate_input(x,y,Operation):
    if Operation == "Addition":
        return addition(x,y)
    elif Operation == "Substraction":
        return subtraction(x,y)
    elif Operation == "Multiplication":
        return multiplication(x,y)
    elif Operation == "Division":
        return division(x,y)

# Streamlit UI

st.set_page_config(page_title = "Basic Arithmetc Calculator Application" , page_icon= "🧮")
st.title(" The Calculator Application. ")
st.write("Description: This Calculator performs only basic arithemetic operations. This web application is created through streamlit and python.")
st.write("Created by Syed Muhamad Hussain Askari")
num1 = st.number_input("Enter a valid first value:", format="%.3f")
num2 = st.number_input("Enter a valid second value:", format="%.3f")
operator = st.selectbox(
    "Please select one of the following operations ",
    ("Addition","Substraction","Multiplication","Division")
)

#Calculation 
if st.button("Calculate"):
    try:
        st.header("Result")
        output = calculate_input(num1 , num2 , operator)
        st.success(output)
    except ZeroDivisionError as error:
        st.error(error)
    except Exception:
        st.error("Invalid Input")



