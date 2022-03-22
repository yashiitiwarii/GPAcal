import streamlit as st

st.set_page_config( page_title = "CalcGPA", page_icon = None)

def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade

def calc(sem):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0  #for the warning message when marks haven't entered
    credits = 0
    col1, col2 = st.columns(2)  #for columns: one for theory sub, and another for lab sub

    if sem == 1:
        subjects = {"APPLIED MATHEMATICS": 4, "APPLIED PHYSICS": 3, "ELECTRICAL SCIENCE":3, "APPLIED CHEMISTRY": 3, "MANUFACTURING PROCESS": 4,"COMMUNICATION SKILLS":3}
        labs = {"PHYSICS": 1, "APPLIED CHEMISTRY": 1, "ENGINEERING GRAPHICS": 2, "ELECTRICAL SCIENCE": 1}
        credits = 25
    elif sem == 2:
        subjects = {"APPLIED CHEMISTRY OR C PROGRAMMING": 3, "ELECTRICAL SCIENCE": 3, "APPLIED MATHEMATICS": 4, "APPLIED PHYSICS": 3, "COMMUNICATION SKILLS": 3, "ENGINEERING MECHANICS": 3}
        labs = {"APPLIED CHEMISTRY OR C PROGRAMMING": 1, "ENGINEERING GRAPHICS": 1, "ELECTRICAL SCIENCE": 1, "WORKSHOP PRACTICE": 2}
        credits = 25
    elif sem == 3:
        subjects = {"COMPUTATIONAL METHODS": 4, "PROGRAMME CORE THEORY PAPERS": 16, "ELEMENTS OF INDIAN HISTORY FOR ENGINEERS": 2}
        labs = {"COMPUTATIONAL METHODS LAB": 1, "PROGRAMME CORE LAB PAPERS": 3}
        credits = 26
    elif sem == 4:
        subjects = {"PROBABILITY, STATISTICS AND LINEAR PROGRAMMING": 4, "PROGRAMME CORE THEORY PAPERS": 16, "TECHNICAL WRITING": 2}
        labs = {"PROGRAMME CORE LAB PAPERS": 3}
        credits = 26
    elif sem == 5:
        subjects = {"PROGRAMME CORE THEORY PAPERS": 20, "ECONOMICS FOR ENGINEERS": 2}
        labs = {"PROGRAMME CORE LAB PAPERS": 3, "SUMMER TRAINING REPORT": 1}
        credits = 26
    elif sem == 6:
        subjects = {"PROGRAMME CORE ELECTIVE PAPERS": 12, "EMERGING AREA/ OPEN AREA ELECTIVE PAPERS": 8, "PRINCIPLES OF MANAGEMENT FOR ENGINEERS": 4}
        labs = {"NSS/ TECHNICAL SOCIETY/ TECHNICAL CLUBS": 2}
        credits = 26 
    elif sem == 7:
        subjects = {"PROGRAMME CORE ELECTIVE PAPERS": 8, "EMERGING AREA /OPEN AREA":12, "PRINCIPLES OF ENTREPRENEURSHIP MINDSET": 2}
        labs = {"MINOR PROJECT": 3, "SUMMER TRAINING REPORT": 1}
        credits = 26
    elif sem== 8:
        labs = {"MAJOR PROJECT": 14, "MAJOR PROJECT VIVA VOCE": 4, "PROJECT PROGRESS EVALUATION": 2, "INTERNSHIP REPORT": 14, "INTERNSHIP VIVA VOCE": 4, "INTERNSHIP PROGRESS EVALUATION": 2}
        credits = 20

    with col1:
        with st.expander("Theory Subjects"):
            for subject in subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * subjects[subject]

    with col2:
        with st.expander("Practical Subjects"):
            for lab in labs:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * labs[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA

    

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(CSE)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME:")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 6)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) #just for formatting XD
            with cl5:
                ans = st.button("Submit")


            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    st.balloons()


