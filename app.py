import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

st.set_page_config(page_title="Portfolio", layout="wide")

# --- Sidebar ---
st.sidebar.image("Ankit_Bhagat.jpg", width=150)
st.sidebar.title("👤 Ankit Bhagat")
st.sidebar.markdown("📧 bhagatankit502@gmail.com")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/ankitsbhagat/)")
st.sidebar.markdown("💻 [GitHub](https://github.com/ankit-bhagat17)")

# --- About ---
#st.title("📊 Data Analyst Portfolio")
st.subheader("Hello! I'm a data analyst fresher,passionate about extracting insights from data.")
st.markdown("""
I specialize in data analysis, visualization, and storytelling using Python, SQL, and BI tools.  
With hands-on experience in diverse projects, I help businesses make data-driven decisions.
""")

# --- Skills ---
st.header("🛠 Skills")
skills = {
    "Programming": ["Python", "SQL"],
    "Libraries": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly"],
    "Tools": ["Excel", "Power BI", "Tableau", "Streamlit"],
    "Database": ["MySQL"]
}
for category, skill_list in skills.items():
    st.markdown(f"**{category}**: " + ", ".join(skill_list))

# --- Projects ---
st.header("📂 Projects")

with open("projects.json") as f:
    projects = json.load(f)

for project in projects:
    with st.expander(project["title"]):
        st.markdown(f"**Tools Used:** {project['tools']}")
        st.markdown(project["description"])
        if project.get("image"):
            st.image(project["image"], use_container_width=True)
        if project.get("link"):
            st.markdown(f"[🔗 View Project]({project['link']})")

# --- Visualization Sample ---
#st.header("📈 Sample Visualization")
#df = sns.load_dataset("tips")

#fig, ax = plt.subplots()
#sns.barplot(x="day", y="total_bill", data=df, ax=ax)
#ax.set_title("Average Bill per Day")
#st.pyplot(fig)

# --- Contact ---
st.header("📬 Contact")
st.markdown("If you'd like to collaborate or hire me, feel free to reach out!")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you! I will get back to you soon.")

