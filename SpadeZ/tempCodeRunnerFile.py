import time
from urllib import request
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from ecapture import ecapture as ec
import wolframalpha
import subprocess
import time
import json
import requests
import pyjokes
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):