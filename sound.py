import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

RATE = 44100 ## Standard sampling rate (in Hz)
MAX_AMPLITUDE = 32767

def generate_sound( seconds: int ) -> np.array:
    return 0.0001 * np.sin(range(RATE * seconds))

def plot_sound( data: np.array ) -> None:

    indices = range( 0, len(data), len(data) // 5 )
    plt.plot( indices, np.take(data, indices) )
    plt.show()

data = generate_sound( 5 )
scaled = np.int16(data / np.max(np.abs(data)) * MAX_AMPLITUDE)
## write('test.wav', RATE, scaled)

plot_sound( data )
