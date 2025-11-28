import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🔧 Engineering Applications of Fourier Transform")
st.markdown("---")

st.markdown("""
<div class='info-box'>
    <h3>🌍 Real-World Impact</h3>
    <p>The Fourier Transform is ubiquitous in modern engineering. This page explores 
    practical applications across various engineering disciplines.</p>
</div>
""", unsafe_allow_html=True)

st.header("1️⃣ Signal Processing & Communications")

st.subheader("📡 Digital Communications")

st.markdown("""
### WiFi and 5G Networks
- **OFDM (Orthogonal Frequency Division Multiplexing)**: Uses FFT to split data across 
  multiple frequency channels
- **Error Correction**: Frequency domain analysis helps detect and correct transmission errors
- **Channel Equalization**: Compensates for signal distortion using frequency domain processing

### Radio and TV Broadcasting
- **Modulation/Demodulation**: Converting signals between time and frequency domains
- **Filtering**: Removing interference and noise
- **Spectrum Analysis**: Monitoring frequency usage and compliance
""")

st.subheader("🎨 Interactive Demo: Signal Modulation")

modulation_type = st.selectbox("Modulation Type", ["AM (Amplitude Modulation)", "FM (Frequency Modulation)"])

t = np.linspace(0, 1, 1000)
carrier_freq = 50
message_freq = 5

if modulation_type == "AM (Amplitude Modulation)":
    message = np.sin(2 * np.pi * message_freq * t)
    modulated = (1 + 0.5 * message) * np.sin(2 * np.pi * carrier_freq * t)
    title = "Amplitude Modulation"
else:
    message = np.sin(2 * np.pi * message_freq * t)
    modulated = np.sin(2 * np.pi * (carrier_freq + 10 * message) * t)
    title = "Frequency Modulation"

# FFT
fft_mod = np.fft.fft(modulated)
freqs = np.fft.fftfreq(len(modulated), t[1] - t[0])
magnitude = np.abs(fft_mod)

fig, axes = plt.subplots(3, 1, figsize=(10, 9))
axes[0].plot(t[:200], message[:200], 'b-', linewidth=2)
axes[0].set_title('Message Signal', fontweight='bold', color='#667eea')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')
axes[0].grid(True, alpha=0.3)

axes[1].plot(t[:200], modulated[:200], 'r-', linewidth=2)
axes[1].set_title(f'{title}: Modulated Signal', fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Amplitude')
axes[1].grid(True, alpha=0.3)

pos_idx = freqs >= 0
axes[2].plot(freqs[pos_idx], magnitude[pos_idx], 'g-', linewidth=2)
axes[2].set_title('Frequency Domain: Shows Carrier and Sidebands', 
                  fontweight='bold', color='#667eea')
axes[2].set_xlabel('Frequency (Hz)')
axes[2].set_ylabel('Magnitude')
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(0, 100)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("2️⃣ Audio & Music Processing")

st.subheader("🎵 Applications")

st.markdown("""
- **Equalization**: Adjusting frequency response (bass, treble, mid-range)
- **Noise Reduction**: Removing unwanted frequencies (hiss, hum, background noise)
- **Compression**: MP3, AAC use frequency domain compression
- **Pitch Detection**: Identifying musical notes and chords
- **Echo Cancellation**: Removing reverberation in audio systems
- **Spectral Analysis**: Visualizing audio in spectrograms
""")

st.subheader("🎨 Interactive Demo: Audio Filtering")

filter_type = st.selectbox("Filter Type", ["Low-pass", "High-pass", "Band-pass"])

# Generate audio-like signal (multiple frequencies)
t = np.linspace(0, 1, 2000)
audio_signal = (np.sin(2 * np.pi * 50 * t) + 
                0.5 * np.sin(2 * np.pi * 200 * t) + 
                0.3 * np.sin(2 * np.pi * 500 * t) + 
                0.2 * np.sin(2 * np.pi * 1000 * t))

# FFT
fft_audio = np.fft.fft(audio_signal)
freqs = np.fft.fftfreq(len(audio_signal), t[1] - t[0])

# Apply filter
fft_filtered = fft_audio.copy()
if filter_type == "Low-pass":
    fft_filtered[np.abs(freqs) > 300] = 0
    filter_name = "Low-pass (< 300 Hz)"
elif filter_type == "High-pass":
    fft_filtered[np.abs(freqs) < 300] = 0
    filter_name = "High-pass (> 300 Hz)"
else:  # Band-pass
    fft_filtered[(np.abs(freqs) < 200) | (np.abs(freqs) > 500)] = 0
    filter_name = "Band-pass (200-500 Hz)"

filtered_signal = np.real(np.fft.ifft(fft_filtered))

fig, axes = plt.subplots(2, 1, figsize=(10, 6))
pos_idx = freqs >= 0

axes[0].plot(freqs[pos_idx], np.abs(fft_audio[pos_idx]), 'b-', 
             linewidth=2, label='Original Spectrum', alpha=0.7)
axes[0].plot(freqs[pos_idx], np.abs(fft_filtered[pos_idx]), 'r-', 
             linewidth=2, label=f'{filter_name}')
axes[0].set_title('Frequency Domain: Audio Spectrum', fontweight='bold', color='#667eea')
axes[0].set_xlabel('Frequency (Hz)')
axes[0].set_ylabel('Magnitude')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(0, 1200)

axes[1].plot(t[:500], audio_signal[:500], 'b-', linewidth=1.5, 
             label='Original Signal', alpha=0.7)
axes[1].plot(t[:500], filtered_signal[:500], 'r-', linewidth=2, 
             label='Filtered Signal')
axes[1].set_title('Time Domain: Audio Signal', fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Amplitude')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("3️⃣ Image Processing")

st.subheader("🖼️ 2D Fourier Transform")

st.markdown("""
- **Image Filtering**: Blur, sharpen, edge detection
- **Image Compression**: JPEG uses DCT (Discrete Cosine Transform), a variant of FFT
- **Pattern Recognition**: Finding repeating patterns in images
- **Noise Reduction**: Removing periodic noise (stripes, moiré patterns)
- **Image Analysis**: Frequency domain analysis for texture analysis
""")

st.subheader("🎨 Demo: 2D FFT Concept")

# Create a simple 2D pattern
size = 128
x = np.linspace(0, 4*np.pi, size)
y = np.linspace(0, 4*np.pi, size)
X, Y = np.meshgrid(x, y)
image = np.sin(X) + 0.5 * np.sin(2*Y)

# 2D FFT
fft_2d = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_2d)
magnitude_2d = np.abs(fft_shifted)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image', fontweight='bold', color='#667eea')
axes[0].axis('off')

axes[1].imshow(np.log(magnitude_2d + 1), cmap='hot')
axes[1].set_title('2D FFT Magnitude (log scale)', fontweight='bold', color='#764ba2')
axes[1].axis('off')

# Reconstruct from low frequencies only
fft_low = fft_shifted.copy()
center = size // 2
cutoff = 20
fft_low[center-cutoff:center+cutoff, center-cutoff:center+cutoff] = 0
fft_low = np.fft.ifftshift(fft_low)
reconstructed = np.real(np.fft.ifft2(fft_low))

axes[2].imshow(reconstructed, cmap='gray')
axes[2].set_title('High-Pass Filtered', fontweight='bold', color='#667eea')
axes[2].axis('off')

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("4️⃣ Control Systems & Vibration Analysis")

st.subheader("⚙️ Applications")

st.markdown("""
- **System Identification**: Determining system characteristics from input-output data
- **Frequency Response**: Analyzing how systems respond to different frequencies
- **Vibration Analysis**: Detecting machine faults, monitoring rotating equipment
- **Modal Analysis**: Finding natural frequencies and mode shapes of structures
- **Filter Design**: Creating digital filters for control systems
""")

st.subheader("🎨 Demo: Frequency Response Analysis")

# Simulate a simple system (low-pass filter response)
freq_range = np.logspace(0, 3, 1000)  # 1 Hz to 1000 Hz
cutoff_freq = 100
# Simple first-order low-pass filter response
H = 1 / (1 + 1j * freq_range / cutoff_freq)
magnitude_response = np.abs(H)
phase_response = np.angle(H) * 180 / np.pi

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].semilogx(freq_range, 20 * np.log10(magnitude_response), 'b-', linewidth=2)
axes[0].axvline(cutoff_freq, color='r', linestyle='--', label=f'Cutoff: {cutoff_freq} Hz')
axes[0].set_title('Magnitude Response (Bode Plot)', fontweight='bold', color='#667eea')
axes[0].set_xlabel('Frequency (Hz)')
axes[0].set_ylabel('Magnitude (dB)')
axes[0].grid(True, alpha=0.3)
axes[0].legend()

axes[1].semilogx(freq_range, phase_response, 'r-', linewidth=2)
axes[1].axvline(cutoff_freq, color='r', linestyle='--', label=f'Cutoff: {cutoff_freq} Hz')
axes[1].set_title('Phase Response', fontweight='bold', color='#764ba2')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Phase (degrees)')
axes[1].grid(True, alpha=0.3)
axes[1].legend()

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.header("5️⃣ Medical Imaging")

st.subheader("🏥 Applications")

st.markdown("""
- **MRI (Magnetic Resonance Imaging)**: FFT reconstructs images from k-space data
- **CT Scans**: Image reconstruction using Radon transform (related to FFT)
- **Ultrasound**: Beamforming and image formation
- **ECG Analysis**: Heart rate variability, arrhythmia detection
- **EEG Analysis**: Brain wave frequency analysis
""")

st.markdown("""
<div class='info-box'>
    <h4>💡 MRI Example</h4>
    <p>MRI machines collect data in frequency domain (k-space). The 2D inverse FFT 
    transforms this data into the spatial domain image we see. This is why FFT is 
    critical for medical imaging!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("6️⃣ Other Engineering Applications")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🌊 Seismology
    - Earthquake analysis
    - Ground motion prediction
    - Structural health monitoring
    
    ### 🛰️ Radar & Sonar
    - Target detection
    - Range and velocity measurement
    - Doppler analysis
    """)

with col2:
    st.markdown("""
    ### 🔬 Optics & Photonics
    - Diffraction pattern analysis
    - Laser pulse characterization
    - Optical signal processing
    
    ### ⚡ Power Systems
    - Harmonic analysis
    - Power quality monitoring
    - Grid frequency analysis
    """)

st.markdown("---")

st.header("📊 Summary Table")

st.markdown("""
| Engineering Field | Key Application | Why FFT? |
|------------------|----------------|----------|
| **Communications** | OFDM, Modulation | Fast frequency domain processing |
| **Audio** | Compression, Filtering | Real-time processing needs |
| **Image Processing** | JPEG, Filtering | Efficient 2D transforms |
| **Control Systems** | Frequency Response | System analysis |
| **Medical Imaging** | MRI Reconstruction | Image formation |
| **Vibration** | Fault Detection | Frequency analysis |
""")

st.markdown("---")
st.markdown("""
**Next**: Learn about the code components! 👉
""")

