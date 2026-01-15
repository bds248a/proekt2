import streamlit as st
import pandas as pd

st.title("Ученици и оценки")

# Инициализация на session_state
if "students" not in st.session_state:
    st.session_state.students = {
        "Петър": 0,
        "Георги": 0,
        "Димитър": 0,
        "Иван": 0
    }

if "grades" not in st.session_state:
    st.session_state.grades = {
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

st.subheader("Избери любими неща")

# Избори
students = st.selectbox("Ученик:", list(st.session_state.students.keys()))
grades = st.selectbox("Оценка:", list(st.session_state.grades.keys()))

# Бутон за запис
if st.button("Запази избора"):
    st.session_state.students[students] += 1
    st.session_state.grades[grades] += 1
    st.success("Изборът е записан!")

st.divider()
st.subheader("Резултати")

# Графика за цветовете
st.write("Ученик")
students_df = pd.DataFrame.from_dict(
    st.session_state.students, orient="index", columns=["Брой"]
)
st.bar_chart(students_df)

# Графика за спортовете
st.write("Оценка")
sports_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)
