import streamlit as st
from pathlib import Path

# Page path variabes
page_title="Portfolio | Sambhaji Shinde"
page_icon="images/profile-icon.png"

# Global variables
profile_img_Path="images/profile-image.png"
social_media = {
    "LinkedIn": "www.linkedin.com/in/sambhaji-shinde-1679ab309",
    "GitHub": "https://github.com/SambhajiShinde28",
    "DockerHub": "https://hub.docker.com/u/sambhaji26",
    "HackerRank": "https://www.hackerrank.com/profile/sambhajishinde71",
    "LeetCode": "https://leetcode.com/u/d8yoTNoiIL/"
}

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- LOADING CSS FILE ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Header Section
header_columns = st.columns([1,2],gap="large",vertical_alignment="top")
with header_columns[0]:
    st.image(profile_img_Path, width=250)
with header_columns[1]:
    st.subheader("Sambhaji Shinde")
    st.write("Python Developer | Data Analysis | Data Science | Generative AI Enthusiast",)
    with open("./Resume/Sambhaji-Shinde.pdf", "rb") as file:
        st.download_button(
            label="🗃️ Download Resume",
            data=file,
            file_name="sambhaji_shinde_resume.pdf",
            mime="application/pdf",
        )
    st.link_button("📄 View Resume", "https://drive.google.com/file/d/1junfpk_GkowPOJKTY9hZHpuigvUHcl6f/view?usp=drive_link")
    st.write("📫 sambhajishinde725@gmail.com")
    st.write("📞 +91 7558561214")

# Social Media Links
st.write('')
st.write('')
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

# # About Me
st.write("***")
st.header("About Me")
st.write("\n")
st.write("I am an AI & Data Science Engineer and Python Developer with expertise in data analysis, machine learning, and Generative AI. Skilled in building end-to-end solutions, I have worked on real-world projects in data science, python development, and AI-driven applications. Passionate about solving problems using data and modern AI technologies.")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("***")
st.subheader("Internship Experience")
st.write("[Internship Offer Letter](https://drive.google.com/file/d/1k1eN4EdpILvylzqVfLCQ3v5yss95w_sI/view?usp=sharing)")
st.write("\n")
st.write("Generative-AI intern – Urbience Tech LLP, Pune (Sept 9, 2025 – Present)")
st.write("Project: RAG with Excel – AI-driven platform for Excel data analysis and dynamic PPT generation")
st.write(
    """
        - Developed a Streamlit UI with Vega-Lite charts for interactive data visualization.
        - Implemented Generative AI, RAG, and Agentic AI to enable natural language querying of Excel data.
        - Built dynamic PPT creation for clients to generate presentations with a single click.
        - Handled no-result scenarios, improving system reliability and user experience.
        - Applied OOP principles, containerized the solution with Docker, and managed code using Git/GitHub.
        - Outcome: Delivered a user-friendly AI platform that simplified data exploration, reporting, and presentations, enhancing client productivity.
    """
)

# --- Education ---
st.write("***")
st.subheader("Education")
st.write("\n")
col_edu=st.columns([1,1])
with col_edu[0]:
    st.markdown("""
    - **Artificial Intelligence and Data Science**  
    Maharashtra Institute of Technology  
    CGPA: 8.9 | (Nov 2022-Present)
    """)
with col_edu[1]:
    st.markdown("""
    - **Diploma in Information Technology**  
    Government Polytechnic, Nanded  
    86.38% | July 2022
    """)

# --- Projects ---
st.write("***")
st.subheader("Projects")
st.markdown("[View More Projects](https://github.com/SambhajiShinde28?tab=repositories)")
st.write("\n")

project_cont1=st.container(border=True,key="Project-container1")
with project_cont1:
    st.markdown("#### 🗃️ PDF Insights – Generative AI with RAG")
    st.markdown("""
        - Developed a Retrieval-Augmented Generation (RAG) pipeline using LangChain to enable intelligent Q&A over PDF documents.
        - Implemented a custom memory-augmented RAG architecture for maintaining conversational context across multiple queries.
        - Designed and optimized a unique architecture to enhance accuracy and relevance of responses, going beyond standard RAG implementations.
        - Integrated embedding models, vector databases, and conversational memory for a seamless user experience.
        - Demonstrated ability to build end-to-end Generative AI solutions, showcasing expertise in LLMs, LangChain, and custom AI pipelines.
    """)
    st.markdown("[GitHub Code](https://github.com/SambhajiShinde28/PDFInsights)")

project_cont2=st.container(border=True,key="Project-container2")
with project_cont2:
    st.markdown("#### 👨‍💻 Natural Language to SQL Assistant (LangChain + Gemini + MySQL)")
    st.markdown("""
        - Built an AI-powered SQL assistant enabling users to query a MySQL database using natural language.
        - Integrated LangChain with Google Gemini model to convert user queries into optimized SQL statements.
        - Designed an end-to-end pipeline that executes SQL queries, retrieves results, and presents them in a human-readable format.
        - Showcased ability to combine LLMs, LangChain, and relational databases to create practical, realworld Generative AI applications.
        - Implemented with a focus on accuracy, scalability, and usability for database-driven insights.
    """)
    st.markdown("[GitHub Code](https://github.com/SambhajiShinde28/QA-Assistant)")

project_cont3=st.container(border=True,key="Project-container3")
with project_cont3:
    st.markdown("#### 🕵️  Bank Marketing Data Analysis (EDA & Insights)")
    st.markdown("""
        - Conducted end-to-end exploratory data analysis (EDA) on 4,500+ customer records to identify key factors influencing term deposit subscription.
        - Performed data cleaning, feature engineering, and missing value analysis, ensuring high-quality datasets for further modeling.
        - Applied statistical techniques (Chi-square tests, T-tests) and visualizations (histograms, KDE plots, bar charts, heatmaps) to uncover customer behavior patterns.
        - Analyzed relationships between demographics, financial attributes, and marketing outcomes, highlighting imbalances and key predictors (e.g., job type, marital status, education, campaign frequency).
        - Demonstrated strong skills in Python (Pandas, NumPy, Matplotlib, Seaborn), statistical analysis, and data storytelling for business decision-making.
    """)
    st.markdown("[GitHub Code](https://github.com/SambhajiShinde28/Bank-Data-Analysis)")


# --- Skills ---
st.write("***")
st.subheader("Skills")
st.write("\n")
st.write("""
        - **Programming Languages**: Python, SQL
        - **Data Science & AI**: Machine Learning, Deep Learning, Generative AI, RAG, Agentic AI, Data Analysis
        - **Web & App Development**: Django, FastAPI, Flask, Streamlit
        - **Databases**: MySql
        - **Tools & Technologies**: Git, GitHub, Docker, Postman
        - **Soft Skills**: Problem Solving, Team Collaboration, Analytical Thinking, Initiative, Communication
""")

# --- Certificates---
st.write("***")
st.header("Certificates")
st.write("[View More Certificates](https://drive.google.com/drive/folders/1Cu6MO9G9TeLHOCJrwq26_ZEd8rSVOKnW?usp=drive_link)")
st.write("\n")
st.write("""
    - Data Analysis With Python [view](https://drive.google.com/file/d/11ViZTR2Iqs_R2sac6iJTVmUem7d5vReD/view?usp=sharing)
    - Machine Learning Using Python [view](https://drive.google.com/file/d/1HlDT7JaXXMZa9r7o_-InHissJGWvqM0K/view?usp=sharing)
    - Django Web Framework [view](https://coursera.org/share/fc20ba9845ec54fb56079766a55efe8b)
    - Introduction to Back-End Development [view](https://www.coursera.org/account/accomplishments/verify/LW6NYI9G8XGJ)
    - Exploratory Data Analysis for Machine Learning [view](https://www.coursera.org/account/accomplishments/verify/1Z4SYGIX2OO0)
""")

# Achievements
st.write("***")
st.header("Achievements")
st.write("\n")
st.write("""
    - Earned the Warrior and Fledgling Badges from Infosys for exceptional problem-solving skills and consistent progress in foundational tasks. [view](https://infyspringboard.onwingspan.com/web/en/app/profile/competency/achievements)
    - Earned IBM badges in EDA for ML, Software Engineering, and Deep Learning highlighting skills in data analysis, system design, and AI deployment. [view](https://www.credly.com/users/sambhaji-shinde.038c9a65/edit#credly)
""")

