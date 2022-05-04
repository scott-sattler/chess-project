from gtts import gTTS
from pydub import AudioSegment
import winsound
import os
from time import sleep
from large_lists import Spoken_Text

for i in range(8):
    for j in range(8):
        letter = chr(ord("A") + i)
        number = str(1 + j)
        text_constructor = letter+number
        if j == 7:
            print '"%s",' % text_constructor
        else:
            print '"%s",' % text_constructor,

# http://stackoverflow.com/a/29550200/6666148
def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0  # ms
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size

    return trim_ms

testing = True

if 1:
    for i in range(len(Spoken_Text)):
        if testing:
            i = -1
        # download mp3
        tts = gTTS(text=Spoken_Text[i], lang='en')
        save_mp3 = "sounds/google_mp3/" + Spoken_Text[i].lower() + ".mp3"
        tts.save(save_mp3)

        i = 0
        while True:
            size_one = os.stat(save_mp3).st_size
            print size_one

            sleep(.5)

            size_two = os.stat(save_mp3).st_size
            print size_two

            if size_one == size_two:
                break
            i += 1

        print i

        # convert to wav
        sound = AudioSegment.from_mp3(save_mp3)
        duration = sound.duration_seconds
        print duration

        save_wav = save_mp3[:6] + "/google_mp3_converted" + save_mp3[17:-4] + ".wav"
        print save_wav
        sound.export(save_wav, format="wav")

        winsound.PlaySound(save_wav, winsound.SND_ASYNC)
        sleep(duration)

        # remove silence
        sound = AudioSegment.from_file(save_wav, format="wav")

        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())

        trimmed_sound = sound[start_trim:duration-end_trim]
        duration = len(sound)
        print duration
        trimmed_sound.export(save_wav, format="wav")

        winsound.PlaySound(save_wav, winsound.SND_ASYNC)
        sleep(duration/1000)

        if testing:
            break


'''
for filename in os.listdir("sounds/google_mp3_converted/"):
    if filename.endswith(".wav"):
        # print(os.path.join(directory, filename))
        continue
    else:
        continue
'''



'''
sound = AudioSegment.from_file("sounds/google_mp3_converted/no moves to undo.wav", format="wav")

start_trim = detect_leading_silence(sound)
end_trim = detect_leading_silence(sound.reverse())

duration = len(sound)
trimmed_sound = sound[start_trim:duration-end_trim]

trimmed_sound.export("sounds/google_mp3_converted/no moves to undo2.wav", format="wav")
'''

#print os.path.isfile("sounds/hello.mp3")
#print st_atime