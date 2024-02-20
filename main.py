from plant_data_handling import initiate_reading_metrics, get_plants_list, record_new_plant, remove_plant
from inform_user.send_email import set_email, get_recipient_email, record_email
from inform_user.play_music import set_song, get_song, record_song
from chart import create_chart_pdf
import sys
import time

def main():
    modes = {"A":"Email settings (to receive notifications)", "B": "View plants statistics", "C": "Add/Remove Plants", "D" : "Change music", "E" : "Initiate soil environment reading"}
    plants_list_file = "my_plants.csv"
    plants_history_data_file = "plants_history.csv"
    email_file = "email.txt"
    song_file = "song.txt"

    while True:
        try:
            mode = get_mode(modes)
            if mode == modes["A"]:
                print_mode_change_instructions()
                email = set_email(email_file)
                a_options = {"A": "Change email address", "X": "Exit"}
                a_selection = get_mode(a_options)
                if a_selection == a_options["A"]:
                    email = get_recipient_email()
                    record_email(email, email_file)
                    print(f"You're email was set to {email}")
            elif mode == modes["B"]:
                create_chart_pdf()
                print("Your staticts PDF is ready (charts.pdf)")
            elif mode == modes["C"]:
                print_mode_change_instructions()
                my_plants = get_plants_list(plants_list_file)
                names = ", ".join([row['Name'] for row in my_plants])
                print(f"Currently you have {len(my_plants)} plants connected: {names}")
                c_options = {"A": "Add plant", "B": "Remove plant", "X": "Exit"}
                c_selection = get_mode(c_options)
                if c_selection == c_options["A"]:
                    record_new_plant(my_plants, plants_list_file)
                elif c_selection == c_options["B"]:
                   remove_plant(my_plants, plants_list_file)
            elif mode == modes["D"]:
                print_mode_change_instructions()
                song = set_song(song_file)
                d_options = {"A": "Change song", "X": "Exit"}
                d_selection = get_mode(d_options)
                if d_selection == d_options["A"]:
                    song = get_song()
                    record_song(song, song_file)
                    print(f"You're song was set to {song}")
            elif mode == modes["E"]:
                print_mode_change_instructions()
                email = set_email(email_file)
                song = set_song(song_file)
                e_options = {"A": "Read current plants' metrics", "B": "Launch the program to continuoisly read metrics every hour", "X": "Exit"}
                e_selection = get_mode(e_options)
                if e_selection == e_options["A"]:
                    initiate_reading_metrics(plants_list_file, plants_history_data_file, email, song)
                elif e_selection == e_options["B"]:
                    timeframe = {"hours" : 0, "minutes": 0, "seconds" : 10}
                    delay = timeframe['hours']*60*60 + timeframe['minutes']*60 + timeframe['seconds']
                    while True:
                        initiate_reading_metrics(plants_list_file, plants_history_data_file, email, song)
                        time.sleep(delay)
        except EOFError:
            sys.exit("Exited the app")

def print_mode_change_instructions():
    print("Press ctrl+D (windows: ctrl+z and enter) to exit this mode")

def get_mode(modes):
    print("Select one of the following: ")
    key_list = list(modes.keys())
    for mode in modes:
        print(f"{mode}. {modes[mode]}")
    while True:
        keys_string = str(key_list)[1:-1].replace(", ","/").replace("'","")
        selected_mode = input(f"Type in mode ({keys_string}): ").strip().upper()
        if selected_mode in key_list:
            return modes[selected_mode]
        else:
            print("Mode doesn't exist \n"
                  "If you wish to exit the app press ctrl+D (windows: ctrl+Z and enter)")

if __name__ == "__main__":
    main()