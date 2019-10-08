# pip3 install simpleaudio
import simpleaudio as sa

# music files
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
            # print(f'sound_alarm is {sound_alarm}')
            # if sound_alarm == False:
            #     return
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except KeyboardInterrupt:
            # sound_alarm = False
            play_obj.stop()
            print('')
            # print('done playing sound.')
            break

if __name__ == "__main__":
    import sys
    ring()
