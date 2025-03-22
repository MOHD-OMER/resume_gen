import streamlit as st
import pdfkit
from jinja2 import Template
import platform
import os

# Set page configuration
st.set_page_config(
    page_title="Smart Resume Generator",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        background: #4CAF50 !important;
        color: white !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .section-title {
        color: #2c3e50 !important;
        border-bottom: 2px solid #2c3e50;
        padding-bottom: 0.3rem;
    }
    </style>
""", unsafe_allow_html=True)

def get_html_template():
    return Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { 
                font-family: 'Arial', sans-serif; 
                line-height: 1.6; 
                max-width: 800px; 
                margin: 0 auto;
            }
            .header { 
                text-align: center; 
                margin-bottom: 30px;
            }
            .section { 
                margin-bottom: 25px;
            }
            h2 { 
                color: #2c3e50; 
                border-bottom: 2px solid #2c3e50; 
                padding-bottom: 5px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>{{ name }}</h1>
            <p>{{ email }} | {{ phone }} | {{ linkedin }}</p>
        </div>
        
        <div class="section">
            <h2>Professional Summary</h2>
            <p>{{ summary }}</p>
        </div>
        
        <div class="section">
            <h2>Technical Skills</h2>
            <p>{{ skills }}</p>
        </div>
        
        <div class="section">
            <h2>Professional Experience</h2>
            <p>{{ experience }}</p>
        </div>
        
        <div class="section">
            <h2>Education</h2>
            <p>{{ education }}</p>
        </div>
        
        <div class="section">
            <h2>Certifications</h2>
            <p>{{ certifications }}</p>
        </div>
    </body>
    </html>
    ''')

def main():
    st.title("Smart Resume Generator 📄")
    st.markdown("Craft professional resumes in minutes with AI-powered suggestions")

    with st.form("resume_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Personal Information")
            name = st.text_input("Full Name*")
            email = st.text_input("Email*")
            phone = st.text_input("Phone Number")
            linkedin = st.text_input("LinkedIn Profile")
            summary = st.text_area("Professional Summary")
            
        with col2:
            st.subheader("Professional Details")
            skills = st.text_area("Technical Skills (comma separated)*")
            experience = st.text_area("Work Experience*")
            education = st.text_area("Education*")
            certifications = st.text_area("Certifications")
            
        submitted = st.form_submit_button("Generate Resume")
        
    if submitted:
        if not name or not email or not skills or not experience or not education:
            st.error("Please fill required fields (*)")
            return
            
        try:
            # Escape special characters
            def escape_text(text):
                return str(text).replace('{', '{{').replace('}', '}}')
            
            # Generate HTML content
            template = get_html_template()
            resume_html = template.render(
                name=escape_text(name),
                email=escape_text(email),
                phone=escape_text(phone or "Not specified"),
                linkedin=escape_text(linkedin or "Not specified"),
                summary=escape_text(summary or "Experienced professional seeking new opportunities"),
                skills=escape_text(skills),
                experience=escape_text(experience),
                education=escape_text(education),
                certifications=escape_text(certifications or "No certifications listed")
            )

            # Configure wkhtmltopdf path
            def get_wkhtml_path():
                if platform.system() == 'Windows':
                    return r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                else:  # For Linux/Streamlit
                    return '/usr/bin/wkhtmltopdf'

            wkhtml_path = get_wkhtml_path()

            # Verify executable exists
            if not os.path.exists(wkhtml_path):
                st.error(f"""❗ wkhtmltopdf not found at: {wkhtml_path}
                    Download from: https://wkhtmltopdf.org/downloads.html
                    Use default installation settings""")
                return

            # PDF configuration
            config = pdfkit.configuration(wkhtmltopdf=wkhtml_path)
            
            # Generate PDF
            pdf = pdfkit.from_string(
                resume_html, 
                False, 
                configuration=config,
                options={
                    'enable-local-file-access': None,
                    'quiet': ''
                }
            )
            
            # Download button
            st.success("🎉 Resume generated successfully!")
            st.download_button(
                label="Download PDF Resume",
                data=pdf,
                file_name=f"{name.replace(' ', '_')}_Resume.pdf",
                mime="application/pdf"
            )
            
            # Preview
            st.subheader("Preview")
            st.components.v1.html(resume_html, height=1000, scrolling=True)
            
        except Exception as e:
            st.error(f"""Error generating resume: {str(e)}
                Troubleshooting steps:
                1. Reinstall wkhtmltopdf from official website
                2. Run as Administrator (Windows)
                3. Check antivirus/firewall settings
                4. Verify file permissions
                5. Ensure all required fields are filled""")

if __name__ == "__main__":
    main()