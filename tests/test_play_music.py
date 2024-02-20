import os
import time
import pygame
from unittest.mock import patch
from inform_user.play_music import play_song, song_is_valid, get_song, record_song, set_song

def test_play_song(monkeypatch, tmp_path):
    monkeypatch.setattr(pygame, 'init', lambda: None)
    monkeypatch.setattr(pygame.mixer, 'init', lambda: None)
    monkeypatch.setattr(pygame.mixer.music, 'load', lambda x: None)
    monkeypatch.setattr(pygame.mixer.music, 'play', lambda: None)
    monkeypatch.setattr(time, 'sleep', lambda x: None)
    monkeypatch.setattr(pygame.mixer, 'quit', lambda: None)
    song = str(tmp_path / "test.mp3")
    play_song(song)

def test_song_is_valid_correct_format_and_exists(tmp_path):
    mp3_file = tmp_path / "test.mp3"
    mp3_file.touch()
    assert song_is_valid(str(mp3_file))

def test_song_is_valid_correct_format_but_not_exists(tmp_path):
    mp3_file = tmp_path / "test.mp3"
    assert not song_is_valid(str(mp3_file))

def test_song_is_valid_incorrect_format(tmp_path):
    txt_file = tmp_path / "test.txt"
    txt_file.touch()
    assert not song_is_valid(str(txt_file))

def test_record_song(tmp_path):
    song_file = tmp_path / "song.txt"
    song_content = "test.mp3"
    record_song(song_content, str(song_file))
    with open(song_file, "r") as file:
        assert file.read() == song_content

def test_set_song_correct_format_exists(tmp_path, monkeypatch):
    mp3_file = tmp_path / "test.mp3"
    mp3_file.touch()
    file_path = tmp_path / "song.txt"
    monkeypatch.setattr('builtins.input', lambda x: str(mp3_file))
    with patch('builtins.input', return_value=str(mp3_file)):
        assert set_song(str(file_path)) == str(mp3_file)
