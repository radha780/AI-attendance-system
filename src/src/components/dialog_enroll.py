import streamlit as st
from src.src.database.db import enroll_student_to_subject
from src.src.database.config import superbase
import time


@st.dialog("Enroll in a Subject")
def enroll_dialog():
    student_id = st.session_state.student_data['student_id']

    subject_code = st.text_input("Enter subject code", placeholder="CS101")

    if st.button('Find Subject', type='primary', width='stretch'):
        if not subject_code:
            st.warning('Please enter a subject code')
            return

        res = (
            superbase
            .table('subjects')
            .select('subject_id, name')
            .eq('subject_code', subject_code)
            .execute()
        )

        if not res.data:
            st.error('Subject Code not found!')
            return

        subject = res.data[0]

        check = (
            superbase
            .table('subject_students')
            .select('*')
            .eq('subject_id', subject['subject_id'])
            .eq('student_id', student_id)
            .execute()
        )

        if check.data:
            st.info("You're already enrolled!")
            return

        enroll_student_to_subject(student_id, subject['subject_id'])
        st.success(f'Joined **{subject["name"]}** successfully!')
        time.sleep(1.5)
        st.rerun()