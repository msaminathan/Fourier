import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("⚡ Fast Fourier Transform (FFT)")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>🚀 The Computational Breakthrough</h3>
    <p>The Fast Fourier Transform (FFT) is an algorithm that computes the Discrete Fourier 
    Transform (DFT) much faster than the naive implementation. It revolutionized signal 
    processing and made real-time Fourier analysis possible.</p>
</div>
""", unsafe_allow_html=True)

st.header("📜 Historical Context")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### The Cooley-Tukey Algorithm (1965)
    
    **James Cooley** and **John Tukey** published the FFT algorithm in 1965, though the 
    mathematical foundations were known earlier (Gauss had similar ideas in 1805!).
    
    #### Why FFT Matters:
    
    - **Naive DFT**: $O(N^2)$ operations for $N$ samples
    - **FFT**: $O(N \\log N)$ operations
    - **Speedup**: For $N = 1024$, FFT is ~100x faster!
    - **Impact**: Made real-time signal processing feasible
    
    #### The Breakthrough
    
    The FFT exploits the symmetry and periodicity properties of the complex exponential 
    $e^{-i 2\\pi k n / N}$ to reduce redundant calculations. It uses a "divide and conquer" 
    approach, recursively breaking the problem into smaller sub-problems.
    """)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; color: white; text-align: center;'>
        <h3 style='color: white;'>Cooley & Tukey</h3>
        <p style='font-size: 0.9rem;'>1965</p>
        <p style='font-size: 0.8rem;'>"Fast Fourier Transform"</p>
        <p style='font-size: 0.7rem; margin-top: 10px;'>$O(N^2) \\rightarrow O(N \\log N)$</p>
    </div>
    """, unsafe_allow_html=True)

st.header("🔢 Mathematical Foundation")

st.markdown("""
### Divide and Conquer Strategy

The FFT recursively splits the DFT into two smaller DFTs:

$$X[k] = \\sum_{n=0}^{N-1} x[n] e^{-i 2\\pi k n / N}$$

For even and odd indices:

$$X[k] = \\sum_{m=0}^{N/2-1} x[2m] e^{-i 2\\pi k (2m) / N} + \\sum_{m=0}^{N/2-1} x[2m+1] e^{-i 2\\pi k (2m+1) / N}$$

This can be rewritten as:

$$X[k] = E[k] + e^{-i 2\\pi k / N} O[k]$$

Where:
- $E[k]$ is the DFT of even-indexed samples
- $O[k]$ is the DFT of odd-indexed samples

This recursive decomposition continues until we reach base cases of size 1 or 2.
""")

st.header("⚡ Performance Comparison")

st.subheader("Speed Comparison: Naive DFT vs FFT")

n_values = st.select_slider(
    "Number of Samples (N)",
    options=[64, 128, 256, 512, 1024, 2048, 4096, 8192],
    value=1024
)

# Naive DFT implementation (simplified for demo)
def naive_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Generate test signal
test_signal = np.random.randn(n_values)

# Time FFT
start_fft = time.time()
fft_result = np.fft.fft(test_signal)
time_fft = time.time() - start_fft

# Time naive DFT (only for small N to avoid long waits)
if n_values <= 256:
    start_naive = time.time()
    naive_result = naive_dft(test_signal)
    time_naive = time.time() - start_naive
    speedup = time_naive / time_fft if time_fft > 0 else 0
else:
    time_naive = None
    speedup = None

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("FFT Time", f"{time_fft*1000:.3f} ms")

with col2:
    if time_naive is not None:
        st.metric("Naive DFT Time", f"{time_naive*1000:.3f} ms")
    else:
        st.metric("Naive DFT Time", "Too slow!")

with col3:
    if speedup is not None:
        st.metric("Speedup", f"{speedup:.1f}x")
    else:
        st.metric("Speedup", "N/A")

st.markdown("""
<div class='info-box'>
    <h4>💡 Note</h4>
    <p>For larger values of N, the naive DFT becomes prohibitively slow. The FFT maintains 
    excellent performance even for millions of samples!</p>
</div>
""", unsafe_allow_html=True)

st.header("🎯 FFT Algorithm Types")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Radix-2 FFT
    - Most common implementation
    - Requires $N = 2^m$ (power of 2)
    - Simplest and fastest for powers of 2
    
    ### Radix-4 FFT
    - Groups 4 samples at a time
    - Can be faster than radix-2 for some cases
    - Also requires specific N values
    """)

with col2:
    st.markdown("""
    ### Mixed-Radix FFT
    - Handles any composite N
    - More flexible but slightly slower
    - Used when N is not a power of 2
    
    ### Prime Factor FFT
    - Handles prime N values
    - More complex but necessary for some applications
    """)

st.header("💻 Using FFT in Python")

st.subheader("Basic Usage")

code_fft = """
import numpy as np

# Generate a signal
t = np.linspace(0, 1, 1024)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 25 * t)

# Compute FFT
fft_result = np.fft.fft(signal)

# Get frequencies
frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])

# Get magnitude and phase
magnitude = np.abs(fft_result)
phase = np.angle(fft_result)

# Inverse FFT to reconstruct
reconstructed = np.fft.ifft(fft_result)
"""

st.code(code_fft, language='python')

st.subheader("FFT Parameters")

st.markdown("""
- **n**: Number of output points (default: length of input)
- **axis**: Axis along which to compute FFT (default: -1, last axis)
- **norm**: Normalization mode ('ortho' for orthonormal transform)
""")

st.header("🎨 Interactive FFT Demo")

st.subheader("Compare FFT with Different Signal Lengths")

signal_length = st.select_slider(
    "Signal Length",
    options=[128, 256, 512, 1024, 2048, 4096],
    value=1024
)

# Generate signal
t = np.linspace(0, 1, signal_length)
freq1, freq2 = 10, 30
sig = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# Compute FFT
fft_vals = np.fft.fft(sig)
freqs = np.fft.fftfreq(len(sig), t[1] - t[0])
magnitude = np.abs(fft_vals)

# Measure computation time
start = time.time()
_ = np.fft.fft(sig)
fft_time = (time.time() - start) * 1000  # in milliseconds

fig, axes = plt.subplots(2, 1, figsize=(10, 6))

axes[0].plot(t, sig, 'b-', linewidth=2)
axes[0].set_title(f'Time Domain Signal (N={signal_length})', 
                  fontweight='bold', color='#667eea')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

pos_idx = freqs >= 0
axes[1].plot(freqs[pos_idx], magnitude[pos_idx], 'r-', linewidth=2)
axes[1].set_title(f'FFT Result (Computed in {fft_time:.3f} ms)', 
                  fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 50)

plt.tight_layout()
st.pyplot(fig)

st.markdown(f"""
<div class='info-box'>
    <h4>⚡ Performance</h4>
    <p>FFT computed {signal_length} samples in {fft_time:.3f} milliseconds. 
    The complexity is O(N log N) = O({signal_length} × {np.log2(signal_length):.1f}) 
    ≈ O({int(signal_length * np.log2(signal_length))}) operations.</p>
</div>
""", unsafe_allow_html=True)

st.header("🔍 FFT vs DFT: Key Differences")

st.markdown("""
| Aspect | DFT | FFT |
|--------|-----|-----|
| **Algorithm** | Direct computation | Divide and conquer |
| **Complexity** | $O(N^2)$ | $O(N \\log N)$ |
| **Speed** | Slow for large N | Fast even for large N |
| **Memory** | $O(N)$ | $O(N)$ |
| **Accuracy** | Exact | Exact (same result) |
| **Flexibility** | Works for any N | Best for $N = 2^m$ |

**Important**: FFT and DFT produce the **same mathematical result** - FFT is just a 
faster way to compute it!
""")

st.header("🌐 Real-World FFT Applications")

st.markdown("""
- **Audio Processing**: Real-time audio effects, equalizers
- **Image Processing**: 2D FFT for image filtering and compression
- **Communications**: OFDM (Orthogonal Frequency Division Multiplexing) in WiFi, 5G
- **Radar/Sonar**: Frequency analysis of reflected signals
- **Medical Imaging**: MRI reconstruction, ultrasound processing
- **Seismology**: Earthquake analysis and prediction
- **Astronomy**: Analyzing light spectra from stars
""")

st.markdown("---")
st.markdown("""
**Next**: Explore real engineering applications! 👉
""")

