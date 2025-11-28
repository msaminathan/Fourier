import streamlit as st
import os

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Page configuration
st.set_page_config(
    page_title="Fourier Transform Explorer",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for vibrant styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    h1 {
        color: #667eea;
        text-align: center;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    h2 {
        color: #764ba2;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
    h3 {
        color: #667eea;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    .info-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #667eea;
    }
    .formula-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌊 Fourier Transform Explorer")
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.radio(
    "Navigate to:",
    [
        "🏠 Home",
        "📚 Introduction & Origin",
        "🔢 Mathematical Foundation",
        "💻 Code Examples",
        "⚡ Fast Fourier Transform (FFT)",
        "🔧 Engineering Applications",
        "📖 Code Components",
        "⬇️ Download",
        "💭 Final Thoughts",
        "📖 Development Story"
    ]
)

# Route to pages
if page == "🏠 Home":
    st.title("🌊 Welcome to Fourier Transform Explorer")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 20px; color: white;'>
            <h2 style='color: white;'>Discover the Power of Fourier Transform</h2>
            <p style='font-size: 1.2rem;'>From mathematical theory to real-world engineering applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 What You'll Learn
    
    This interactive application will guide you through:
    
    - **Historical Origins**: The fascinating story of how Fourier Transform came to be
    - **Mathematical Foundations**: Deep dive into the theory and equations
    - **Practical Examples**: Hands-on code demonstrations
    - **FFT Algorithm**: Understanding the Fast Fourier Transform
    - **Engineering Applications**: Real-world use cases
    - **Code Documentation**: Understanding the implementation
    
    ## 🚀 Getting Started
    
    Use the sidebar to navigate through different sections. Each page contains:
    - Detailed explanations
    - Interactive visualizations
    - Code examples
    - Practical insights
    
    **Ready to explore?** Select a page from the sidebar! 👈
    """)
    
    st.markdown("---")
    st.markdown("### 🎨 Features")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='padding: 20px; background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                    border-radius: 10px; text-align: center;'>
            <h3>📊 Interactive Visualizations</h3>
            <p>See Fourier Transform in action with dynamic plots</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='padding: 20px; background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%); 
                    border-radius: 10px; text-align: center;'>
            <h3>💻 Code Examples</h3>
            <p>Learn by doing with practical Python code</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='padding: 20px; background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); 
                    border-radius: 10px; text-align: center;'>
            <h3>🔧 Real Applications</h3>
            <p>Discover engineering use cases</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📚 Introduction & Origin":
    exec(open(os.path.join(BASE_DIR, "pages/01_introduction.py")).read())

elif page == "🔢 Mathematical Foundation":
    exec(open(os.path.join(BASE_DIR, "pages/02_mathematical_foundation.py")).read())

elif page == "💻 Code Examples":
    exec(open(os.path.join(BASE_DIR, "pages/03_code_examples.py")).read())

elif page == "⚡ Fast Fourier Transform (FFT)":
    exec(open(os.path.join(BASE_DIR, "pages/04_fft.py")).read())

elif page == "🔧 Engineering Applications":
    exec(open(os.path.join(BASE_DIR, "pages/05_engineering_applications.py")).read())

elif page == "📖 Code Components":
    exec(open(os.path.join(BASE_DIR, "pages/06_code_components.py")).read())

elif page == "⬇️ Download":
    exec(open(os.path.join(BASE_DIR, "pages/07_download.py")).read())

elif page == "💭 Final Thoughts":
    exec(open(os.path.join(BASE_DIR, "pages/08_final_thoughts.py")).read())

elif page == "📖 Development Story":
    exec(open(os.path.join(BASE_DIR, "pages/09_development_story.py")).read())

