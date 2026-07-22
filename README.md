# AI Attendance System

An AI-powered classroom attendance system that uses facial and voice recognition to automate student check-ins. Built with Streamlit and Supabase, it gives teachers a portal to manage subjects and take attendance from classroom photos, and gives students a portal to enroll in classes and track their attendance record.

## Features

- **Face-recognition-based attendance** — teachers upload or capture classroom photos, and the app detects and matches faces against enrolled students using a trained classifier
- **Optional voice enrollment** — students can enroll their voice alongside their face for identification
- **Teacher portal** — create subjects, manage enrolled students, run attendance scans, and review results before saving
- **Student portal** — face-ID login, view enrolled subjects and attendance history, unenroll from a subject
- **QR-code and link-based class enrollment** — teachers can share a scannable QR code or join link so students can enroll in a subject in one step
- **Supabase backend** — Postgres-based storage for teachers, students, subjects, enrollments, and attendance logs

## Tech Stack

- **Frontend:** Streamlit
- **Backend / Database:** Supabase (PostgreSQL)
- **Face Recognition:** dlib, face_recognition_models, scikit-learn (SVM classifier)
- **Voice Recognition:** resemblyzer, librosa
- **Other:** segno (QR code generation), bcrypt (password hashing), pandas

## How It Works

1. Student faces are captured and converted into embeddings using dlib's face recognition model
2. An SVM classifier is trained on these embeddings to distinguish between enrolled students
3. When a teacher runs an attendance scan, faces detected in the uploaded photos are matched against the trained classifier, and matches within a distance threshold are marked present
4. Optional voice embeddings (via resemblyzer) can be used for voice-based identification as a secondary signal

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/radha780/AI-attendance-system.git
   cd AI-attendance-system
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up Supabase credentials
   Create a `.streamlit/secrets.toml` file in the project root with:
   ```toml
   SUPERBASE_URL = "your-supabase-url"
   SUPERBASE_KEY = "your-supabase-key"
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
attendance-app/
├── app.py                  # Entry point
├── requirements.txt
└── src/src/
    ├── components/         # Reusable UI components and dialogs
    ├── database/            # Supabase client and query functions
    ├── pipelines/           # Face and voice recognition pipelines
    ├── screens/             # Teacher, student, and home screens
    └── ui/                  # Layout and styling
```

## License

MIT
