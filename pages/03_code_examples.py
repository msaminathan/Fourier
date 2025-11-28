import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

st.title("💻 Code Examples: Fourier Transform in Python")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>🎯 Learn by Doing</h3>
    <p>This page provides practical Python code examples demonstrating Fourier Transform 
    applications. All code is interactive and can be modified to explore different scenarios.</p>
</div>
""", unsafe_allow_html=True)

st.header("Example 1: Basic Fourier Transform")

st.subheader("📝 Code")

code1 = """
import numpy as np
import matplotlib.pyplot as plt

# Create a simple signal: sum of two sine waves
t = np.linspace(0, 1, 1000)  # Time vector (1 second, 1000 samples)
f1, f2 = 5, 20  # Frequencies in Hz
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Compute Fourier Transform
fft_vals = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])

# Get magnitude spectrum
magnitude = np.abs(fft_vals)

# Plot results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Time domain
ax1.plot(t, signal)
ax1.set_title('Time Domain Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.grid(True)

# Frequency domain
positive_freq_idx = frequencies >= 0
ax2.plot(frequencies[positive_freq_idx], magnitude[positive_freq_idx])
ax2.set_title('Frequency Domain (Fourier Transform)')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')
ax2.grid(True)

plt.tight_layout()
plt.show()
"""

st.code(code1, language='python')

st.subheader("🎨 Interactive Demo")

col1, col2 = st.columns(2)
with col1:
    freq1 = st.slider("Frequency 1 (Hz)", 1, 50, 5)
    amp1 = st.slider("Amplitude 1", 0.0, 2.0, 1.0)
with col2:
    freq2 = st.slider("Frequency 2 (Hz)", 1, 50, 20)
    amp2 = st.slider("Amplitude 2", 0.0, 2.0, 0.5)

# Generate signal
t = np.linspace(0, 1, 1000)
sig = amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * freq2 * t)

# Compute FFT
fft_vals = np.fft.fft(sig)
freqs = np.fft.fftfreq(len(sig), t[1] - t[0])
magnitude = np.abs(fft_vals)

# Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 6))
axes[0].plot(t, sig, 'b-', linewidth=2)
axes[0].set_title('Time Domain Signal', fontweight='bold', color='#667eea')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

pos_idx = freqs >= 0
axes[1].plot(freqs[pos_idx], magnitude[pos_idx], 'r-', linewidth=2)
axes[1].set_title('Frequency Domain (Fourier Transform)', fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 60)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("Example 2: Filtering with Fourier Transform")

st.subheader("📝 Code")

code2 = """
import numpy as np
import matplotlib.pyplot as plt

# Create signal with noise
t = np.linspace(0, 1, 1000)
signal_clean = np.sin(2 * np.pi * 10 * t)  # 10 Hz signal
noise = 0.5 * np.random.randn(len(t))  # Random noise
signal_noisy = signal_clean + noise

# Fourier Transform
fft_noisy = np.fft.fft(signal_noisy)
frequencies = np.fft.fftfreq(len(signal_noisy), t[1] - t[0])

# Low-pass filter: keep frequencies below 20 Hz
cutoff = 20
fft_filtered = fft_noisy.copy()
fft_filtered[np.abs(frequencies) > cutoff] = 0

# Inverse Fourier Transform to get filtered signal
signal_filtered = np.real(np.fft.ifft(fft_filtered))

# Plot
fig, axes = plt.subplots(3, 1, figsize=(10, 9))
axes[0].plot(t, signal_noisy, label='Noisy Signal')
axes[0].plot(t, signal_clean, 'r--', label='Original Clean Signal')
axes[0].set_title('Noisy Signal')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(frequencies, np.abs(fft_noisy))
axes[1].axvline(cutoff, color='r', linestyle='--', label=f'Cutoff: {cutoff} Hz')
axes[1].set_title('Frequency Domain')
axes[1].set_xlim(0, 50)
axes[1].legend()
axes[1].grid(True)

axes[2].plot(t, signal_filtered, label='Filtered Signal')
axes[2].plot(t, signal_clean, 'r--', label='Original Clean Signal')
axes[2].set_title('Filtered Signal (Low-pass)')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()
"""

st.code(code2, language='python')

st.subheader("🎨 Interactive Demo")

cutoff_freq = st.slider("Low-pass Filter Cutoff (Hz)", 5, 50, 20)
noise_level = st.slider("Noise Level", 0.0, 1.0, 0.5)

# Generate signal
t = np.linspace(0, 1, 1000)
signal_clean = np.sin(2 * np.pi * 10 * t)
np.random.seed(42)
noise = noise_level * np.random.randn(len(t))
signal_noisy = signal_clean + noise

# FFT
fft_noisy = np.fft.fft(signal_noisy)
freqs = np.fft.fftfreq(len(signal_noisy), t[1] - t[0])

# Filter
fft_filtered = fft_noisy.copy()
fft_filtered[np.abs(freqs) > cutoff_freq] = 0
signal_filtered = np.real(np.fft.ifft(fft_filtered))

# Plot
fig, axes = plt.subplots(3, 1, figsize=(10, 9))
axes[0].plot(t, signal_noisy, 'b-', alpha=0.7, label='Noisy Signal', linewidth=1)
axes[0].plot(t, signal_clean, 'r--', label='Original Clean Signal', linewidth=2)
axes[0].set_title('Noisy Signal', fontweight='bold', color='#667eea')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

pos_idx = freqs >= 0
axes[1].plot(freqs[pos_idx], np.abs(fft_noisy[pos_idx]), 'b-', linewidth=2)
axes[1].axvline(cutoff_freq, color='r', linestyle='--', linewidth=2, 
                label=f'Cutoff: {cutoff_freq} Hz')
axes[1].set_title('Frequency Domain', fontweight='bold', color='#764ba2')
axes[1].set_xlim(0, 50)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

axes[2].plot(t, signal_filtered, 'g-', linewidth=2, label='Filtered Signal')
axes[2].plot(t, signal_clean, 'r--', linewidth=2, label='Original Clean Signal')
axes[2].set_title('Filtered Signal (Low-pass)', fontweight='bold', color='#667eea')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("Example 3: Frequency Analysis of Real Signals")

st.subheader("📝 Code")

code3 = """
import numpy as np
import matplotlib.pyplot as plt

# Create a complex signal: chirp (frequency increases over time)
t = np.linspace(0, 2, 2000)
f0, f1 = 5, 50  # Start and end frequencies
chirp_signal = np.sin(2 * np.pi * (f0 + (f1 - f0) * t / 2) * t)

# Add some harmonics
signal = chirp_signal + 0.3 * np.sin(2 * np.pi * 30 * t)

# Compute FFT
fft_vals = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), t[1] - t[0])
magnitude = np.abs(fft_vals)
phase = np.angle(fft_vals)

# Plot
fig, axes = plt.subplots(3, 1, figsize=(10, 10))

# Time domain
axes[0].plot(t, signal)
axes[0].set_title('Time Domain: Chirp Signal')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True)

# Magnitude spectrum
positive_idx = frequencies >= 0
axes[1].plot(frequencies[positive_idx], magnitude[positive_idx])
axes[1].set_title('Magnitude Spectrum')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True)

# Phase spectrum
axes[2].plot(frequencies[positive_idx], phase[positive_idx])
axes[2].set_title('Phase Spectrum')
axes[2].set_xlabel('Frequency (Hz)')
axes[2].set_ylabel('Phase (radians)')
axes[2].grid(True)

plt.tight_layout()
plt.show()
"""

st.code(code3, language='python')

st.subheader("🎨 Interactive Demo")

chirp_f0 = st.slider("Chirp Start Frequency (Hz)", 1, 20, 5)
chirp_f1 = st.slider("Chirp End Frequency (Hz)", 30, 100, 50)

# Generate chirp
t = np.linspace(0, 2, 2000)
chirp = np.sin(2 * np.pi * (chirp_f0 + (chirp_f1 - chirp_f0) * t / 2) * t)
sig = chirp + 0.3 * np.sin(2 * np.pi * 30 * t)

# FFT
fft_vals = np.fft.fft(sig)
freqs = np.fft.fftfreq(len(sig), t[1] - t[0])
magnitude = np.abs(fft_vals)
phase = np.angle(fft_vals)

# Plot
fig, axes = plt.subplots(3, 1, figsize=(10, 10))
axes[0].plot(t, sig, 'b-', linewidth=1.5)
axes[0].set_title('Time Domain: Chirp Signal', fontweight='bold', color='#667eea')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

pos_idx = freqs >= 0
axes[1].plot(freqs[pos_idx], magnitude[pos_idx], 'r-', linewidth=2)
axes[1].set_title('Magnitude Spectrum', fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 100)

axes[2].plot(freqs[pos_idx], phase[pos_idx], 'g-', linewidth=1.5)
axes[2].set_title('Phase Spectrum', fontweight='bold', color='#667eea')
axes[2].set_xlabel('Frequency (Hz)')
axes[2].set_ylabel('Phase (radians)')
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(0, 100)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("📚 Key Python Libraries")

st.markdown("""
- **numpy.fft**: Fast Fourier Transform functions
  - `np.fft.fft()`: Forward FFT
  - `np.fft.ifft()`: Inverse FFT
  - `np.fft.fftfreq()`: Frequency bins
  
- **scipy.fft**: Enhanced FFT functions with more options

- **scipy.signal**: Signal processing functions including filters

- **matplotlib**: Visualization and plotting
""")

st.markdown("---")
st.markdown("""
**Next**: Learn about the Fast Fourier Transform (FFT) algorithm! 👉
""")

