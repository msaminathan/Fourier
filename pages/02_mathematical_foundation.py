import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🔢 Mathematical Foundation of Fourier Transform")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>📐 Understanding the Mathematics</h3>
    <p>The Fourier Transform is built on elegant mathematical principles. Understanding these 
    foundations will help you apply it effectively in your work.</p>
</div>
""", unsafe_allow_html=True)

st.header("1️⃣ Continuous Fourier Transform")

st.markdown("""
### Forward Transform

The Fourier Transform of a continuous function $f(t)$ is defined as:
""")

st.markdown("""
<div class='formula-box'>
""", unsafe_allow_html=True)

st.latex(r"F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt")

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown("""
### Inverse Transform

The inverse Fourier Transform reconstructs the original function:
""")

st.markdown("""
<div class='formula-box'>
""", unsafe_allow_html=True)

st.latex(r"f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega")

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Where:**
- $f(t)$ is the function in the **time domain**
- $F(\\omega)$ is the function in the **frequency domain**
- $\\omega$ (omega) is the angular frequency (radians per second)
- $i$ is the imaginary unit ($i^2 = -1$)
- $e^{-i\\omega t}$ is Euler's formula: $e^{-i\\omega t} = \\cos(\\omega t) - i\\sin(\\omega t)$
""")

st.header("2️⃣ Discrete Fourier Transform (DFT)")

st.markdown("""
For digital signals, we use the Discrete Fourier Transform. Given $N$ samples, the DFT is:
""")

st.markdown("""
<div class='formula-box'>
""", unsafe_allow_html=True)

st.latex(r"X[k] = \sum_{n=0}^{N-1} x[n] e^{-i 2\pi k n / N}")

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Where:**
- $x[n]$ are the discrete time-domain samples
- $X[k]$ are the frequency-domain coefficients
- $N$ is the number of samples
- $k$ is the frequency index (0 to $N-1$)
""")

st.header("3️⃣ Key Mathematical Properties")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Linearity")
    st.latex(r"\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)")
    
    st.markdown("### Time Shifting")
    st.latex(r"\mathcal{F}\{f(t - t_0)\} = e^{-i\omega t_0} F(\omega)")
    
    st.markdown("### Frequency Shifting")
    st.latex(r"\mathcal{F}\{e^{i\omega_0 t} f(t)\} = F(\omega - \omega_0)")

with col2:
    st.markdown("### Scaling")
    st.latex(r"\mathcal{F}\{f(at)\} = \frac{1}{|a|} F\left(\frac{\omega}{a}\right)")
    
    st.markdown("### Convolution")
    st.latex(r"\mathcal{F}\{f(t) * g(t)\} = F(\omega) \cdot G(\omega)")
    
    st.markdown("### Parseval's Theorem")
    st.latex(r"\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |F(\omega)|^2 d\omega")

st.header("4️⃣ Euler's Formula & Complex Exponentials")

st.markdown("""
The foundation of Fourier Transform lies in Euler's beautiful formula:
""")

st.markdown("""
<div class='formula-box'>
""", unsafe_allow_html=True)

st.latex(r"e^{i\theta} = \cos(\theta) + i\sin(\theta)")

st.markdown("""
</div>
""", unsafe_allow_html=True)

st.markdown("""
This connects exponential functions with trigonometric functions, allowing us to represent 
sine and cosine waves as rotating vectors in the complex plane.
""")

# Visualization of Euler's formula
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

theta = np.linspace(0, 2*np.pi, 100)
r = np.ones_like(theta)
ax.plot(theta, r, 'b-', linewidth=2, label='Unit Circle')
ax.plot([0, np.pi/4], [0, 1], 'r-', linewidth=2, label='Complex Exponential')
ax.plot([0], [0], 'ro', markersize=10)
ax.plot([np.pi/4], [1], 'go', markersize=10)

ax.set_title("Euler's Formula: $e^{i\\theta}$ (e^(iθ)) on Complex Plane", 
             fontsize=14, fontweight='bold', pad=20)
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.header("5️⃣ Frequency Domain Interpretation")

st.markdown("""
The Fourier Transform decomposes signals into:
- **Magnitude**: How much of each frequency is present
- **Phase**: The timing relationship between frequencies

For a complex-valued $F(\\omega)$ (F(ω)):
- **Magnitude**: $|F(\\omega)| = \\sqrt{\\text{Re}(F)^2 + \\text{Im}(F)^2}$
- **Phase**: $\\angle F(\\omega) = \\arctan\\left(\\frac{\\text{Im}(F)}{\\text{Re}(F)}\\right)$
""")

st.header("6️⃣ Common Transform Pairs")

st.markdown("""
| Time Domain | Frequency Domain |
|------------|------------------|
| $\\delta(t)$ (impulse) | $1$ (constant) |
| $1$ (constant) | $2\\pi\\delta(\\omega)$ (2πδ(ω)) |
| $e^{i\\omega_0 t}$ (e^(iω₀t)) | $2\\pi\\delta(\\omega - \\omega_0)$ (2πδ(ω-ω₀)) |
| $\\cos(\\omega_0 t)$ (cos(ω₀t)) | $\\pi[\\delta(\\omega - \\omega_0) + \\delta(\\omega + \\omega_0)]$ |
| $\\sin(\\omega_0 t)$ (sin(ω₀t)) | $i\\pi[\\delta(\\omega + \\omega_0) - \\delta(\\omega - \\omega_0)]$ |
| $e^{-at}u(t)$ (exponential) | $\\frac{1}{a + i\\omega}$ (1/(a+iω)) |
| $\\text{rect}(t)$ (rectangle) | $\\text{sinc}(\\omega)$ (sinc(ω)) |
""")

st.header("7️⃣ Interactive Mathematical Visualization")

# Interactive example
st.subheader("Explore: Sum of Sinusoids")

freq1 = st.slider("Frequency 1 (Hz)", 1, 10, 2)
amp1 = st.slider("Amplitude 1", 0.0, 2.0, 1.0)
freq2 = st.slider("Frequency 2 (Hz)", 1, 10, 5)
amp2 = st.slider("Amplitude 2", 0.0, 2.0, 0.5)

t = np.linspace(0, 2, 1000)
signal = amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * freq2 * t)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(t, signal, 'b-', linewidth=2)
axes[0].set_title(f'Time Domain: $f(t) = {amp1}\\sin(2\\pi \\cdot {freq1}t) + {amp2}\\sin(2\\pi \\cdot {freq2}t)$', 
                  fontsize=12, fontweight='bold')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

# Frequency domain
freqs = np.fft.fftfreq(len(t), t[1] - t[0])
fft_vals = np.fft.fft(signal)
magnitude = np.abs(fft_vals)

# Plot only positive frequencies
positive_freq_idx = freqs >= 0
axes[1].plot(freqs[positive_freq_idx], magnitude[positive_freq_idx], 'r-', linewidth=2)
axes[1].set_title('Frequency Domain: Fourier Transform', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 15)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
<div class='info-box'>
    <h4>💡 Understanding the Visualization</h4>
    <p>Adjust the sliders above to see how changing frequencies and amplitudes in the time 
    domain affects the frequency domain representation. The Fourier Transform reveals the 
    exact frequencies present in your signal!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
**Next**: Ready to see this in code? Check out the **Code Examples** page! 👉
""")

