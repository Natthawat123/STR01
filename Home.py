import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
#data
st.header('Natthawat Hiranwong')

data_dict = {'PHP':33, 'C':28, 'Java':30}
courses = list(data_dict.keys())
values = list(data_dict.values())

fig = plt.figure(figsize = (10, 5))
# Bar plot
plt.bar(courses, values, color ='green',width = 0.5)
plt.xlabel("Courses ")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()