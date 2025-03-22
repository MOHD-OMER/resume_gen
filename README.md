Here’s the updated **README.md** file text with the **ATS Score** feature included:

```markdown
# Smart Resume Generator 🚀

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered web application that helps users create professional resumes quickly and efficiently. Built with Streamlit and PDFKit for seamless PDF generation. Includes an **ATS Score** feature to optimize resumes for Applicant Tracking Systems.

![Resume Generator Demo](demo.gif) <!-- Add your demo gif/image here -->

## Features ✨

- 📄 **Professional Templates**: Clean, modern resume templates
- ⚡ **Real-time Preview**: Instant HTML preview before download
- 📤 **Multi-format Export**: Generate PDF resumes with one click
- 🔒 **Local Processing**: No data leaves your machine
- 🌐 **Cross-platform**: Works on Windows, Linux, and macOS
- 🎯 **ATS Score**: Get a score and feedback to optimize your resume for Applicant Tracking Systems

## Installation 💻

### Prerequisites
- Python 3.9+
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

### Steps
1. Clone the repository:
```bash
git clone https://github.com/your-username/smart-resume-generator.git
cd smart-resume-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install wkhtmltopdf:
- **Windows**: Download from [official site](https://wkhtmltopdf.org/downloads.html)
- **Linux**:
  ```bash
  sudo apt-get install wkhtmltopdf
  ```
- **Mac**:
  ```bash
  brew install --cask wkhtmltopdf
  ```

## Usage 🚦

1. Run the application:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Fill in your details and generate your resume!

4. **ATS Score**:
   - Get a score out of 100 based on resume completeness
   - Receive feedback to improve your resume for Applicant Tracking Systems

## Deployment ☁️

Deploy to Streamlit Community Cloud:
1. Fork this repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app" → Select your forked repository
4. Set main file path to `app.py`
5. Click "Deploy"

## Tech Stack 🛠️

- **Frontend**: Streamlit
- **PDF Generation**: pdfkit + wkhtmltopdf
- **Templating**: Jinja2
- **Core Language**: Python 3.9+

## ATS Score Calculation 📊

The ATS Score is calculated based on the following criteria:
- **Basic Information (30 points)**:
  - Name: 10 points
  - Email: 10 points
  - Phone: 10 points
- **Professional Sections (50 points)**:
  - Summary: 10 points
  - Skills: 15 points
  - Experience: 15 points
  - Education: 10 points
- **Additional Sections (20 points)**:
  - Certifications: 10 points
  - LinkedIn: 10 points

**Feedback**:
- **≥ 80**: "Good job! Your resume is well-optimized."
- **< 80**: "Consider adding more details to improve your score."

## Contributing 🤝

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting 🔧

Common Issues:
- **wkhtmltopdf path errors**: Verify installation path matches your OS
- **Missing dependencies**: Run `pip install -r requirements.txt`
- **PDF generation failures**: Ensure wkhtmltopdf is in system PATH
- **ATS Score not showing**: Verify all required fields are filled

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 🙏

- Built with [Streamlit](https://streamlit.io/)
- PDF generation powered by [wkhtmltopdf](https://wkhtmltopdf.org/)
- Inspired by modern resume design trends
```

### **Key Updates**:
1. Added **ATS Score** feature description
2. Included ATS Score calculation details
3. Updated usage instructions with ATS Score
4. Added troubleshooting tips for ATS Score