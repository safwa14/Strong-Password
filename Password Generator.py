import random
import string
import streamlit as st

# ---------- 🌈 تنسيق CSS وخلفية الصورة المختارة ----------
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://thumbs.dreamstime.com/b/metal-door-many-locks-illustration-204027513.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }

    h1 {
        color: #3f3d56; /* موف غامق */
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }

    label, .stNumberInput label {
        color: #2e2e2e;
        font-size: 15px;
    }

    .stButton > button {
        background-color: #6D597A;  /* موف فخم */
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        margin-top: 10px;
    }

    .stSuccess {
        color: #3f6212; /* زيتي غامق */
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- 🧠 العنوان والنصوص بنفسك بالظبط ----------
st.title("🔐 Password Generator")
st.write("Welcome to the Password Generator!")

length_of_word = int(st.number_input("Enter the total number of characters in the password:", min_value=1))
length_of_litters = int(st.number_input("Enter the number of letters in the password:", min_value=0))
length_of_numbers = int(st.number_input("Enter the number of numbers in the password:", min_value=0))
length_of_symbols = int(st.number_input("Enter the number of symbols in the password:", min_value=0))

# ---------- الزرار والتوليد ----------
if st.button("Generate Password"):
    thetotal = length_of_litters + length_of_numbers + length_of_symbols

    if thetotal != length_of_word:
        st.error("Invaild input. The sum of letters, numbers, and symbols doesn't match the password length!")
    else:
        select_litters = string.ascii_letters 
        litters_choiced = random.choices(select_litters, k=length_of_litters)

        select_numbers = string.digits
        numbers_choiced = random.choices(select_numbers, k=length_of_numbers)

        select_symbols = string.punctuation
        symbols_choiced = random.choices(select_symbols, k=length_of_symbols)

        big_list = [litters_choiced, numbers_choiced, symbols_choiced]
        flat_list = []
        for sublist in big_list:
            for char in sublist:
                flat_list.append(char)

        random.shuffle(flat_list)
        jlist = ''.join(flat_list)

        st.success(f"Generated Password: {jlist}")
