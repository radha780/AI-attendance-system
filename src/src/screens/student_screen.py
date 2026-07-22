import streamlit as st
import time
from src.src.ui.base_layout import style_base_dashboard, style_base_layout
from src.src.components.header import header_dashboard
from src.src.database.db import check_teacher_exists, create_student, create_teacher, teacher_login, get_all_students, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import numpy as np
from PIL import Image
from src.src.pipelines.face_pipelines import predict_attendance, get_face_embeddings, train_classifier
from src.src.pipelines.voice_pipelines import get_voice_embedding
from src.src.components.dialog_enroll import enroll_dialog
from src.src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {student_data['name']}")
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        st.header('your enrolled subjects')
    with c2:
        if st.button('enroll in subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']
        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button(sid=sid, sub=sub):
            if st.button("unenroll from this course", type='tertiary', width='stretch'):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f"unenrolled from {sub['name']} successfully")

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )


def student_screen():
    style_base_dashboard()
    style_base_layout()
    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")
    st.write("")

    show_registration = False
    st.header('Login using faceid')
    photo_source = st.camera_input("position your face in centre")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('face not found')
            elif num_faces > 1:
                st.warning('multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('face not recognised, new student')
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header('register new profile')
            new_name = st.text_input("enter your name")
            st.subheader('optional: voice enrollment')
            st.info("enroll your voice for voice-only attendance")

            audio_data = None
            try:
                audio_data = st.audio_input("record a short phrase")
            except Exception:
                st.error('audio data failed')

            if st.button('create account', type='primary'):
                if new_name:
                    with st.spinner('creating profile....'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())
                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"profile created {new_name}")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("couldn't capture facial recognition")
                else:
                    st.warning('please enter name!')