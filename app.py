import streamlit as st
from src.src.screens.home_screen import home_screen
from src.src.screens.teacher_screen import teacher_screen
from src.src.screens.student_screen import student_screen
from src.src.components.dialog_autoenroll import auto_enroll_dialog


def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    join_code = st.query_params.get('join-code')

    # If someone arrives with a join link, force them into the student flow
    # BEFORE rendering anything, so there's no flash of the wrong screen.
    if join_code and st.session_state['login_type'] != 'student':
        st.session_state['login_type'] = 'student'
        st.rerun()

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case _:
            home_screen()

    # Once they're actually logged in as a student (whether they just
    # registered as new or logged in as returning), auto-enroll them.
    if join_code and st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
        auto_enroll_dialog(join_code)


main()