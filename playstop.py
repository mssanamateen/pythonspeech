import multiprocessing
from playsound import playsound

if __name__ == '__main__':
    sound_path = "If You Believe Song.wav"  
    p = multiprocessing.Process(target=playsound, args=(sound_path,))
    p.start()
    input("Press ENTER to stop playback")
    p.terminate()
