import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("'Cause there we are again when I loved you so", 0.08),
        ("Back before you lost the one real thing you've ever known", 0.08),
        ("It was rare, I was there", 0.1),  
        ("I remember it all too well", 0.12),  
        ("Wind in my hair, you were there", 0.08),
        ("You remember it all", 0.08),
        ("Down the stairs, you were there", 0.08),
        ("You remember it all", 0.08),
        ("It was rare, I was there", 0.1),  
        ("I remember it all too well", 0.12),  
    ]
    delays = [0.0, 5.15, 10.02, 12.20, 19.80, 22.50, 25.00, 28.00, 30.75, 33.22]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()