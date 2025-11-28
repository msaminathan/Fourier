import streamlit as st

st.title("📖 Code Components Documentation")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>🔍 Understanding the Implementation</h3>
    <p>This page documents the code structure, components, and dependencies used in 
    this Fourier Transform Explorer application.</p>
</div>
""", unsafe_allow_html=True)

st.header("📁 Project Structure")

st.code("""
Fourier/
├── app.py                          # Main Streamlit application
├── pages/
│   ├── 01_introduction.py          # Introduction & Origin page
│   ├── 02_mathematical_foundation.py # Mathematical Foundation page
│   ├── 03_code_examples.py         # Code Examples page
│   ├── 04_fft.py                   # FFT page
│   ├── 05_engineering_applications.py # Engineering Applications page
│   ├── 06_code_components.py       # This page
│   ├── 07_download.py              # Download page
│   └── 08_final_thoughts.py        # Final Thoughts page
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
""", language='text')

st.header("🔧 Main Application (app.py)")

st.subheader("Key Components")

st.markdown("""
### 1. Page Configuration
```python
st.set_page_config(
    page_title="Fourier Transform Explorer",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)
```
- Sets the app title and icon
- Uses wide layout for better visualization
- Sidebar is expanded by default

### 2. Custom CSS Styling
The app includes custom CSS for vibrant, modern styling:
- Gradient backgrounds
- Colorful headers and buttons
- Styled info boxes and formula boxes
- Responsive design elements

### 3. Navigation System
- Sidebar radio buttons for page navigation
- Each page is loaded dynamically using `exec()`
- Clean, intuitive navigation structure
""")

st.header("📚 Page Components")

st.subheader("Page 1: Introduction & Origin")

st.markdown("""
**File**: `pages/01_introduction.py`

**Components**:
- Historical narrative about Fourier
- Timeline of key developments
- Basic visualization of time vs frequency domain
- Preview of applications

**Key Libraries**:
- `numpy`: Signal generation
- `matplotlib`: Visualizations
""")

st.subheader("Page 2: Mathematical Foundation")

st.markdown("""
**File**: `pages/02_mathematical_foundation.py`

**Components**:
- Mathematical formulas (LaTeX)
- Transform definitions
- Key properties and theorems
- Interactive frequency exploration
- Euler's formula visualization

**Key Features**:
- Interactive sliders for signal parameters
- Real-time FFT computation
- Educational visualizations
""")

st.subheader("Page 3: Code Examples")

st.markdown("""
**File**: `pages/03_code_examples.py`

**Components**:
- Three complete code examples:
  1. Basic Fourier Transform
  2. Filtering with FFT
  3. Frequency analysis of complex signals
- Interactive demos for each example
- Code snippets with syntax highlighting

**Key Libraries**:
- `numpy.fft`: FFT functions
- `scipy.signal`: Signal processing (optional)
- `matplotlib`: Plotting
""")

st.subheader("Page 4: Fast Fourier Transform")

st.markdown("""
**File**: `pages/04_fft.py`

**Components**:
- Historical context (Cooley-Tukey)
- Algorithm explanation
- Performance comparison
- Speed benchmarking
- FFT types and variants

**Key Features**:
- Performance timing comparisons
- Interactive N-value selection
- Complexity analysis visualization
""")

st.subheader("Page 5: Engineering Applications")

st.markdown("""
**File**: `pages/05_engineering_applications.py`

**Components**:
- Six major application areas:
  1. Signal Processing & Communications
  2. Audio & Music Processing
  3. Image Processing
  4. Control Systems
  5. Medical Imaging
  6. Other Applications
- Interactive demos for each area
- Real-world examples

**Key Features**:
- Modulation demos
- Audio filtering examples
- 2D FFT visualization
- Frequency response plots
""")

st.subheader("Page 6: Code Components (This Page)")

st.markdown("""
**File**: `pages/06_code_components.py`

**Purpose**: Documentation of the application structure and components.
""")

st.subheader("Page 7: Download")

st.markdown("""
**File**: `pages/07_download.py`

**Components**:
- Download links for the application
- Installation instructions
- Usage guidelines
""")

st.subheader("Page 8: Final Thoughts")

st.markdown("""
**File**: `pages/08_final_thoughts.py`

**Components**:
- Summary of key concepts
- Additional resources
- Future learning paths
- Acknowledgments
""")

st.header("📦 Dependencies")

st.subheader("Core Libraries")

st.markdown("""
| Library | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web application framework |
| `numpy` | Latest | Numerical computations, FFT |
| `matplotlib` | Latest | Plotting and visualizations |
| `scipy` | Latest | Advanced signal processing (optional) |

### Installation
```bash
pip install streamlit numpy matplotlib scipy
```

Or use the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```
""")

st.header("💻 Key Code Patterns")

st.subheader("1. FFT Computation Pattern")

st.code("""
import numpy as np

# Generate signal
t = np.linspace(0, 1, N)  # Time vector
signal = np.sin(2 * np.pi * f * t)  # Signal

# Compute FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])

# Get magnitude and phase
magnitude = np.abs(fft_result)
phase = np.angle(fft_result)

# Filter positive frequencies for plotting
positive_idx = frequencies >= 0
""", language='python')

st.subheader("2. Interactive Visualization Pattern")

st.code("""
import streamlit as st
import matplotlib.pyplot as plt

# Create interactive controls
param = st.slider("Parameter", min_val, max_val, default_val)

# Generate data based on parameter
data = generate_data(param)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data)
ax.set_title("Interactive Plot")
st.pyplot(fig)
""", language='python')

st.subheader("3. Filtering Pattern")

st.code("""
# FFT
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), dt)

# Apply frequency domain filter
fft_filtered = fft_signal.copy()
fft_filtered[np.abs(frequencies) > cutoff] = 0  # Low-pass

# Inverse FFT
filtered_signal = np.real(np.fft.ifft(fft_filtered))
""", language='python')

st.header("🎨 Styling Components")

st.markdown("""
### CSS Classes Used

1. **`.info-box`**: Highlighted information boxes with gradient background
2. **`.formula-box`**: Centered mathematical formulas with special styling
3. **Custom gradients**: Purple/blue gradients throughout the app
4. **Responsive columns**: Using `st.columns()` for layout

### Color Scheme
- Primary: `#667eea` (Purple-blue)
- Secondary: `#764ba2` (Deep purple)
- Accent: Various gradient combinations
""")

st.header("🚀 Running the Application")

st.markdown("""
### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run app.py
   ```

3. **Access**: Open browser to `http://localhost:8501`

### Deployment Options

- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: Platform-as-a-Service
- **AWS/GCP/Azure**: Cloud platforms
- **Docker**: Containerized deployment
""")

st.header("📝 Code Best Practices Used")

st.markdown("""
1. **Modular Structure**: Each page in separate file
2. **Clear Naming**: Descriptive variable and function names
3. **Documentation**: Inline comments and explanations
4. **Interactive Elements**: Sliders and controls for exploration
5. **Visual Feedback**: Real-time updates based on user input
6. **Error Handling**: Graceful handling of edge cases
7. **Performance**: Efficient FFT usage for large datasets
""")

st.header("🔍 Key Functions Reference")

st.markdown("""
### NumPy FFT Functions

- `np.fft.fft(x)`: Forward FFT
- `np.fft.ifft(X)`: Inverse FFT
- `np.fft.fftfreq(n, d)`: Frequency bins
- `np.fft.fftshift()`: Shift zero frequency to center (for 2D)

### Streamlit Functions

- `st.title()`: Page title
- `st.header()`: Section header
- `st.slider()`: Interactive slider
- `st.code()`: Code block display
- `st.pyplot()`: Display matplotlib figure
- `st.columns()`: Multi-column layout
- `st.markdown()`: Rich text with HTML/CSS
""")

st.header("🐛 Troubleshooting")

st.markdown("""
### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Slow Performance**: Reduce signal length for interactive demos
3. **Plot Display Issues**: Check matplotlib backend compatibility
4. **Memory Issues**: Use smaller N values for naive DFT comparisons

### Performance Tips

- Use `np.fft.fft()` instead of naive implementations
- Limit interactive demo signal lengths (< 10,000 samples)
- Use `st.cache` for expensive computations (if needed)
""")

st.markdown("---")
st.markdown("""
**Next**: Download the application! 👉
""")

