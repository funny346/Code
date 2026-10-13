import datetime
import pygame
import time

def target_time(alarm_time):
    run = True
    sound = "Рингтон - 415-ая база, ответьте.mp3"
    while run:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(current_time)
        if current_time == alarm_time:
            print("WAKE-UP")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            run = False
        time.sleep(1)








if __name__ == '__main__':
    alar_time = input("Enter time to wake-up (HH:MM:SS): ")
    target_time(alar_time)