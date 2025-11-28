import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📚 Introduction & Origin of Fourier Transform")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>🎯 What is Fourier Transform?</h3>
    <p>The Fourier Transform is one of the most powerful mathematical tools in science and engineering. 
    It allows us to decompose any signal or function into its constituent frequencies, revealing hidden 
    patterns and making complex problems more manageable.</p>
</div>
""", unsafe_allow_html=True)

st.header("📜 Historical Origins")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### The Birth of a Revolutionary Idea
    
    The story of Fourier Transform begins with **Jean-Baptiste Joseph Fourier** (1768-1830), 
    a French mathematician and physicist who made groundbreaking contributions to mathematics 
    and physics.
    
    #### Key Historical Milestones:
    
    1. **1807**: Fourier presented his work on heat conduction to the French Academy of Sciences
    2. **1822**: Published "Théorie analytique de la chaleur" (The Analytical Theory of Heat)
    3. **1829**: Dirichlet provided rigorous mathematical foundations
    4. **1965**: Cooley and Tukey developed the Fast Fourier Transform (FFT) algorithm
    
    #### The Original Problem
    
    Fourier was trying to solve the **heat equation** - understanding how heat distributes 
    through a solid object. He discovered that any periodic function could be represented 
    as an infinite sum of sines and cosines, each with different frequencies and amplitudes.
    
    This revolutionary insight meant that complex waveforms could be broken down into simpler 
    sinusoidal components - a concept that would transform science and engineering forever.
    """)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='color: white;'>Jean-Baptiste Fourier</h3>
        <p style='font-size: 0.9rem;'>1768-1830</p>
        <p style='font-size: 0.8rem;'>"Any function can be represented as a sum of sines and cosines"</p>
    </div>
    """, unsafe_allow_html=True)

st.header("🌍 Impact on Science & Engineering")

st.markdown("""
The Fourier Transform has become fundamental to:

- **Signal Processing**: Audio, image, and video processing
- **Communications**: Radio, TV, and digital communications
- **Physics**: Quantum mechanics, optics, and wave phenomena
- **Engineering**: Control systems, vibration analysis, and circuit design
- **Data Science**: Time series analysis, pattern recognition
- **Medical Imaging**: MRI, CT scans, and ultrasound
- **Astronomy**: Analyzing light spectra from stars

### Why It Matters

The Fourier Transform is like a "mathematical microscope" that lets us see the frequency 
content of signals. Just as a prism separates white light into colors, the Fourier Transform 
separates complex signals into their frequency components.
""")

st.header("🎨 Visual Introduction")

# Create a simple visualization
fig, axes = plt.subplots(2, 1, figsize=(10, 6))

# Time domain signal
t = np.linspace(0, 2*np.pi, 1000)
signal = np.sin(2*t) + 0.5*np.sin(5*t) + 0.3*np.sin(10*t)

axes[0].plot(t, signal, 'b-', linewidth=2)
axes[0].set_title('Time Domain: Complex Signal', fontsize=14, fontweight='bold', color='#667eea')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

# Frequency domain (simplified)
frequencies = [1, 2, 5, 10]
amplitudes = [0, 1, 0.5, 0.3]
axes[1].stem(frequencies, amplitudes, basefmt=" ")
axes[1].set_title('Frequency Domain: Component Frequencies', fontsize=14, fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Amplitude')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
<div class='info-box'>
    <h4>💡 Key Insight</h4>
    <p>The complex signal in the time domain (top) is composed of three simple sine waves 
    at different frequencies. The Fourier Transform reveals these components in the 
    frequency domain (bottom).</p>
</div>
""", unsafe_allow_html=True)

st.header("🚀 Modern Applications Preview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🎵 Audio Processing**
    - Noise reduction
    - Equalization
    - Compression
    """)

with col2:
    st.markdown("""
    **📡 Communications**
    - WiFi signals
    - 5G networks
    - Satellite communication
    """)

with col3:
    st.markdown("""
    **🏥 Medical Imaging**
    - MRI reconstruction
    - Ultrasound processing
    - ECG analysis
    """)

st.markdown("---")
st.markdown("""
**Next Steps**: Ready to dive into the mathematical foundations? Navigate to 
**"Mathematical Foundation"** in the sidebar! 👉
""")

