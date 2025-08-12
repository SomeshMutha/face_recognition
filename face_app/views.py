from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
import signal

# Global variable to hold the process
process = None

def home(request):
    return render(request, 'index.html')

def start_camera(request):
    global process
    if process is None:
        # Start recog.py in a separate process
        # Make sure you give the full path to your recog.py
        process = subprocess.Popen(['python3', os.path.join(os.getcwd(), 'recog.py')])
        return HttpResponse("Camera started.")
    else:
        return HttpResponse("Camera is already running.")

def stop_camera(request):
    global process
    if process:
        process.terminate()
        process = None
        return HttpResponse("Camera stopped.")
    else:
        return HttpResponse("Camera is not running.")