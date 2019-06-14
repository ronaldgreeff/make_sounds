import numpy as np
from scipy.io.wavfile import write
import winsound
import random
import schedule
import time

def dog_sound():
	sps = 44100

	# Frequency / pitch
	freq_hz = random.randrange(60000, 62000, 1000)

	# Duration
	duration_s = random.randrange(1, 10, 1)

	# NumPy magic
	each_sample_number = np.arange(duration_s * sps)
	waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
	waveform_quiet = waveform * 0.5
	waveform_integers = np.int16(waveform * 32767)

	write('dogs.wav', sps, waveform_integers)
	winsound.PlaySound('dogs', winsound.SND_FILENAME)

def human_sound():
	# Samples per second
	sps = 44100

	# Frequency / pitch
	freq_hz = random.randrange(3500, 5500, 100)

	# Duration
	duration_s = random.uniform(0.1, 0.3)

	# NumPy magic
	each_sample_number = np.arange(duration_s * sps)
	waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
	waveform_quiet = waveform * 0.5
	waveform_integers = np.int16(waveform_quiet * 32767)

	write('human.wav', sps, waveform_integers)
	winsound.PlaySound('human', winsound.SND_FILENAME)



def daily_job():
	m = random.uniform(0.5, 1)
	schedule.every(m).minutes.do(human_sound)
	schedule.every(1).seconds.do(dog_sound)

schedule.every().day.at("16:51").do(daily_job)

while True:
	schedule.run_pending()
	time.sleep(1)