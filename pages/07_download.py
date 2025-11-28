import streamlit as st
import os
import zipfile
import io

st.title("⬇️ Download Fourier Transform Explorer")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>📦 Get the Application</h3>
    <p>Download the complete Fourier Transform Explorer application with all source code, 
    examples, and documentation.</p>
</div>
""", unsafe_allow_html=True)

st.header("📥 Download Options")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Option 1: Complete Package
    
    Download the entire application as a ZIP file containing:
    - All source code files
    - Requirements file
    - README documentation
    - Example data (if any)
    """)
    
    # Create a function to generate ZIP file
    def create_zip():
        zip_buffer = io.BytesIO()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Add main app file
            app_path = os.path.join(base_dir, 'app.py')
            if os.path.exists(app_path):
                zip_file.write(app_path, 'app.py')
            
            # Add pages directory
            pages_dir = os.path.join(base_dir, 'pages')
            if os.path.exists(pages_dir):
                for root, dirs, files in os.walk(pages_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, base_dir)
                        zip_file.write(file_path, arcname)
            
            # Add requirements.txt
            req_path = os.path.join(base_dir, 'requirements.txt')
            if os.path.exists(req_path):
                zip_file.write(req_path, 'requirements.txt')
            
            # Add README.md
            readme_path = os.path.join(base_dir, 'README.md')
            if os.path.exists(readme_path):
                zip_file.write(readme_path, 'README.md')
        
        zip_buffer.seek(0)
        return zip_buffer.getvalue()
    
    zip_data = create_zip()
    st.download_button(
        label="📦 Download Complete Package (ZIP)",
        data=zip_data,
        file_name="Fourier_Transform_Explorer.zip",
        mime="application/zip"
    )

with col2:
    st.markdown("""
    ### Option 2: Individual Files
    
    Download specific components:
    - Main application
    - Individual pages
    - Configuration files
    """)
    
    st.info("💡 Use the complete package for easiest setup!")

st.markdown("---")

st.header("🚀 Installation Instructions")

st.subheader("Step 1: Prerequisites")

st.markdown("""
Ensure you have Python 3.7 or higher installed:

```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)
""")

st.subheader("Step 2: Extract and Navigate")

st.code("""
# Extract the ZIP file
unzip Fourier_Transform_Explorer.zip

# Navigate to the directory
cd Fourier_Transform_Explorer
""", language='bash')

st.subheader("Step 3: Install Dependencies")

st.code("""
# Install required packages
pip install -r requirements.txt

# Or install individually:
pip install streamlit numpy matplotlib scipy
""", language='bash')

st.subheader("Step 4: Run the Application")

st.code("""
# Start the Streamlit app
streamlit run app.py
""", language='bash')

st.markdown("""
The application will open automatically in your default web browser at `http://localhost:8501`
""")

st.markdown("---")

st.header("📋 System Requirements")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Minimum Requirements
    - **Python**: 3.7+
    - **RAM**: 2 GB
    - **Storage**: 100 MB
    - **OS**: Windows, macOS, or Linux
    """)

with col2:
    st.markdown("""
    ### Recommended
    - **Python**: 3.9+
    - **RAM**: 4 GB+
    - **Storage**: 500 MB
    - **Browser**: Chrome, Firefox, or Edge
    """)

st.markdown("---")

st.header("📚 Usage Guide")

st.subheader("Getting Started")

st.markdown("""
1. **Launch the app**: Run `streamlit run app.py`
2. **Navigate**: Use the sidebar to move between pages
3. **Interact**: Adjust sliders and parameters to explore
4. **Learn**: Read explanations and study code examples
""")

st.subheader("Key Features to Explore")

st.markdown("""
- **Interactive Demos**: Adjust parameters and see real-time results
- **Code Examples**: Copy and modify code for your projects
- **Visualizations**: Understand concepts through plots and graphs
- **Real Applications**: See how FFT is used in engineering
""")

st.markdown("---")

st.header("🔧 Configuration")

st.subheader("Customization Options")

st.markdown("""
You can customize the application by:

1. **Modifying Colors**: Edit CSS in `app.py`
2. **Adding Pages**: Create new files in `pages/` directory
3. **Adjusting Parameters**: Change default values in sliders
4. **Adding Examples**: Include your own code demonstrations
""")

st.subheader("Example: Adding a Custom Page")

st.code("""
# Create pages/09_custom_page.py
import streamlit as st

st.title("My Custom Page")
st.markdown("Your content here...")

# Add to app.py navigation:
# elif page == "🎯 Custom Page":
#     exec(open("pages/09_custom_page.py").read())
""", language='python')

st.markdown("---")

st.header("🌐 Deployment Options")

st.subheader("Streamlit Cloud (Recommended)")

st.markdown("""
1. Push code to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click
4. Free hosting available!
""")

st.subheader("Other Platforms")

st.markdown("""
- **Heroku**: Platform-as-a-Service
- **AWS EC2**: Virtual server
- **Google Cloud Run**: Containerized
- **Docker**: Any container platform
""")

st.markdown("---")

st.header("❓ Frequently Asked Questions")

st.markdown("""
**Q: Do I need to know Python to use this?**  
A: Basic Python knowledge helps, but the app is designed to be educational and accessible.

**Q: Can I modify the code?**  
A: Yes! All code is provided for learning and customization.

**Q: Is this free to use?**  
A: Yes, completely free and open for educational purposes.

**Q: What if I encounter errors?**  
A: Check the troubleshooting section in the Code Components page, or ensure all dependencies are installed.

**Q: Can I use this in my projects?**  
A: Absolutely! Feel free to use and adapt the code for your needs.
""")

st.markdown("---")

st.header("📞 Support & Resources")

st.markdown("""
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **NumPy FFT**: [numpy.org/doc/stable/reference/routines.fft.html](https://numpy.org/doc/stable/reference/routines.fft.html)
- **Matplotlib**: [matplotlib.org](https://matplotlib.org)
- **GitHub Issues**: Report bugs or request features
""")

st.markdown("---")

st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 30px; border-radius: 15px; color: white; text-align: center;'>
    <h2 style='color: white;'>🎉 Ready to Explore!</h2>
    <p style='font-size: 1.1rem;'>Download the application and start your journey into 
    the fascinating world of Fourier Transform!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
**Next**: Read the final thoughts and summary! 👉
""")

