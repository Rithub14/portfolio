from pathlib import Path
import base64
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Muhammad_Rizwan_Aslam_Resume.pdf"
profile_pic = current_dir / "assets" / "pic-cropped.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Rizwan Aslam"
PAGE_ICON = ":wave:"
NAME = "Rizwan Aslam"
DESCRIPTION = """
Applied ML Engineer
"""         

SOCIAL_MEDIA = {
    "Email": "mailto:rizwanaslam.work@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/rizwan-aslam-cs/",
    "GitHub": "https://github.com/Rithub14",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.subheader(DESCRIPTION)
    st.write("\n")
    st.write("\n")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(3)  # Create 3 columns for the links

for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[i]:
        st.markdown(f'<a href="{link}" target="_blank" rel="noopener noreferrer" class="center-text">{platform}</a>', unsafe_allow_html=True)


# --- EDUCATION ---
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Education 🎓")
st.write("---")

# Education entries with university URLs and dates
education_entries = [
    {"degree": "MSc Artificial Intelligence", "university": "[**Brandenburg University of Technology**](https://www.b-tu.de/)", "date": "2023-2025 (Expected)", "location":"Cottbus, Germany"},
    {"degree": "BSc Computer Science", "university": "[**COMSATS University Islamabad**](https://lahore.comsats.edu.pk/default.aspx)", "date": "2019-2023", "location":"Lahore, Pakistan"}
]

for entry in education_entries:
    col1, col2 = st.columns([2, 3], gap="large")
    with col1:
        st.write(f"**{entry['degree']}**")
        st.write(f"{entry['date']}")
    with col2:
        st.markdown(entry['university'])
        st.markdown(entry['location'])


# --- SKILLS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Skills 👩‍💻")
st.write("---")

skills = {
    "Programming Languages": "Python 🐍, SQL 🗃️",
    "Libraries/Frameworks": "Numpy 🧮, Pandas 🐼, Matplotlib 📊, Scikit-learn 🤖, OpenCV 🖼️, PyTorch 🔥, LangChain 🔗, HuggingFace 🤗, Streamlit 🌐",
    "Tools": "Git 🛠️, Docker 🐳, VS Code 📝, Jupyter Notebook 📒, Google Colab 📚",
    "Cloud Platform": "AWS (SageMaker, Bedrock) ☁️",
    "Soft Skills": "Time management 🕰️, Problem-solving 📈, Critical thinking 🧠, Collaboration 🤝"
}

for skill_category, skill_list in skills.items():
    col1, col2 = st.columns([2, 3], gap="large")
    with col1:
        st.write(f"**{skill_category}**")
    with col2:
        st.write(skill_list)


# --- EXPERIENCE ---
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Experience 🚧")
st.write("---")

# --- JOB 1
st.write("**Data Science Intern | [Machine Learning 1](https://ml1.ai/)**")
st.write("May 2023 - July 2023")
st.markdown(
    """
    <div style='text-align: justify;'>
    ► Implemented automated text extraction from diverse sources, including Word documents, PDFs, and images for integration into targeted resume templates<br>
    ► Used OpenCV to detect real-time hand sign gestures<br>
    ► Contributed to the development of robust datasets for computer vision models by performing image annotation for object detection using LabelImg
    </div>
    """, unsafe_allow_html=True)

# --- JOB 2
st.write("\n")
st.write("\n")
st.write("**Software Developer Intern | [ABACUS Consulting](https://abacus-global.com/)**")
st.write("May 2021 - July 2021")
st.markdown(
    """
    <div style='text-align: justify;'>
    ► Collaborated with the development team to enhance features and functionality of the UPaisa application, focusing on improving user experience and backend performance<br>
    ► Implemented an algorithm leveraging Spring Boot to generate and read QR codes seamlessly, facilitating secure and efficient transactions for users<br>
    ► Conducted thorough testing and debugging of the QR code algorithm to ensure reliability and accuracy
    </div>
    """, unsafe_allow_html=True)


# --- PROJECTS ---
PROJECTS = {
    "**Retrieval Augmented Generation** - Web app to query over different types of documents(PDF, DOCX, TXT, CSV, XLSX, PPTX or URL)": "https://rag-all.streamlit.app/",
    "**Comic AI** - Web app to create an entire comic strip from a short scenario": "https://comics-ai.onrender.com/",
    "**Mango UAV Image Analysis** - Web app designed to perform image analysis on UAV imagery of mango trees, including tree detection, variety identification, and disease detection. ": "https://github.com/Rithub14/FYP",
}

st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects 🏆")
st.write("---")

for project, link in PROJECTS.items():
    col1, col2 = st.columns([10, 2], gap="large")
    with col1:
        st.markdown(f"{project}")
    with col2:
        st.write(f"[Link]({link})")


# --- CERTIFICATIONS ---
CERTIFICATIONS = {
    "**Machine Learning Specialization** - DeepLearning.AI": "assets/Machine Learning Specialization.pdf",
    "**Deep Learning Specialization** - DeepLearning.AI": "assets/Deep Learing Specialization.pdf",
    "**Python for Data Science and Machine Learning Bootcamp** - Udemy": "assets/Muhammad_Rizwan_Aslam_Resume.pdf",
}

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download</a>'
    return href

st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Certifications 🥇")
st.write("---")

for certification, file_path in CERTIFICATIONS.items():
    col1, col2 = st.columns([8, 2], gap="large")
    with col1:
        st.markdown(f"{certification}")
    with col2:
        st.markdown(get_binary_file_downloader_html(file_path, file_path.split('/')[-1]), unsafe_allow_html=True)