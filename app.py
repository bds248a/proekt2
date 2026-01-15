import streamlit as st
import pandas as pd

st.title("Ученици и оценки")


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

if "class" not in st.session_state:
    st.session_state.class = {
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0
    }

st.subheader("Въведи ученик, клас и оценка")


students = st.selectbox("Ученик:", list(st.session_state.students.keys()))
grades = st.selectbox("Оценка:", list(st.session_state.grades.keys()))
class = st.selectbox("Клас:", list(st.session_state.class.keys()))

if st.button("Запази избора"):
    st.session_state.students[students] += 1
    st.session_state.grades[grades] += 1
    st.session_state.class[class] += 1
    st.success("Изборът е записан!")

st.divider()
st.subheader("Резултати")


st.write("Ученик")
students_df = pd.DataFrame.from_dict(
    st.session_state.students, orient="index", columns=["Брой"]
)
st.bar_chart(students_df)


st.write("Оценка")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)

st.write("Клас")
class_df = pd.DataFrame.form_dict(
    st.session_state.class, orient="index", columns["Брой"]
)
st.bar_chart(class_df)
