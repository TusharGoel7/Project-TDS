import streamlit as st
def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers and find the largest among them.")
    
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
    num3 = st.number_input("Enter the third number")
    
    if st.button("Find the Largest Number"):
        if num1 >= num2 and num1 >= num3:
            st.write(f"The largest number is {num1}")
        elif num2 >= num1 and num2 >= num3:
            st.write(f"The largest number is {num2}")
        else:
            st.write(f"The largest number is {num3}")

if __name__ == '__main__':
    main()
