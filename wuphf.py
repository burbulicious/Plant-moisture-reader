# This is a program that's referencing an all platform notification services from the office episode https://www.youtube.com/watch?v=OrVskziCc4w&ab_channel=Bark
from datetime import datetime, time
from inform_user.send_email import send_email
from inform_user.play_music import play_song

def time_is_day():
    current_time = datetime.now().time()
    start_time = time(10, 0, 0)
    end_time = time(22, 0, 0)
    return start_time <= current_time <= end_time

def send_wuphf(email, subject, message, song):
    send_email(email, subject, message)
    if time_is_day():
        play_song(song)
