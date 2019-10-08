# pip3 install simpleaudio
import simpleaudio as sa

# music files - how to convert files to buffered. audio_data parameter must be an
# object which supports the buffer interface. (bytes objects, Python arrays, and Numpy arrays all qualify.)
# f = '/home/worldwidewilly/workspace/deliberate-action/action/on-the-run-snippet.mp3'
f = '/home/worldwidewilly/workspace/deliberate-action/action/on-the-run-snippet.wav'
# f = '/home/worldwidewilly/workspace/deliberate-action/action/echoes_ping.wav'
# f = '/home/worldwidewilly/workspace/deliberate-action/action/echoes_ping.flac'

# run simpleaudio
wave_obj = sa.WaveObject.from_wave_file(f)

def ring():
    # sound_alarm = True
    while True:
        try:
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except KeyboardInterrupt:
            play_obj.stop()
            print('')
            break

if __name__ == "__main__":
    import sys
    ring()
