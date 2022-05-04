import queue
import threading
import winsound
import wave
from time import sleep
import cPickle as pickle

import collections

#pyaudio can remove pydub warning


# http://stackoverflow.com/a/19976441/6666148
def worker():
    while True:
        sound_file_path = thread_queue.get()

        # calculate duration for ?blocking?
        sound_file = wave.open(sound_file_path, 'r')
        frames = sound_file.getnframes()
        rate = sound_file.getframerate()
        duration = frames / float(rate)
        sound_file.close()

        winsound.PlaySound(sound_file_path, winsound.SND_ASYNC)
        sleep(duration)

        # pickle list to track audio already queued and playing
        queue_list = pickle.load(open("save.p", "rb"))
        print "\t\t\t\tpickle_3", queue_list
        del queue_list[-1]
        pickle.dump(queue_list, open("save.p", "wb"))
        print "\t\t\t\tpickle_4", queue_list

        thread_queue.task_done()

num_worker_threads = 1

thread_queue = queue.Queue()
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()



'''
# http://stackoverflow.com/a/19976441/6666148
def sound_thread_queue(q):
    while True:
        sound = q.get(False)
        print sound
        winsound.PlaySound(sound, winsound.SND_ASYNC)

a_sound = 'C:\Users\Admin\Dropbox\Chess\sounds\checkmate.wav'
b_sound = "C:/users/admin/dropbox/chess/sounds/castle_while_checked.wav"


q = thread_queue.thread_queue()
t = threading.Thread(target=sound_thread_queue, args=[q])
t.daemon = True
q.put(a_sound)
q.put(b_sound)
#q.push(another_sound, some_flags)
#do_stuff_for_a_long_time()

sleep(3)
'''

'''
#for item in source():
itemS = "C:/users/admin/dropbox/chess/sounds/castle_while_checked.wav"
q.put(itemS)

#q.join()       # block until all tasks are done


print "this"
winsound.PlaySound('sounds/black_wins.wav', winsound.SND_ASYNC)
sleep(3)
'''
