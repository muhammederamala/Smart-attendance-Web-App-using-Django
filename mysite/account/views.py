from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.http import HttpResponse
import subprocess

import cv2
import numpy as np

from django.http import StreamingHttpResponse

import os

from .forms import add_class_form
from .models import add_class_model

from django.views.decorators.csrf import csrf_protect




def logbook_view(request):
	print(request.headers)
	return render(request,"account/logbook.html",{})	

# to run python script
def run_script(request):
    result = subprocess.run(['python', 'python/capture.py'], stdout=subprocess.PIPE)
    return HttpResponse(result.stdout)


def create_class(request):
	print(request.headers)
	return render(request,"account/createclass.html",{})

def capture_view(request):
	print(request.headers)
	return render(request,"account/capture.html",{})

def class_list_view(request):
	print(request.headers)
	classes = add_class_model.objects.filter(user=request.user)
	return render(request, 'account/classlist.html', {'classes': classes})



def gen_frames():

	cap = cv2.VideoCapture(0)

	while True:
		success, frame = cap.read()

		if not success:
			break

		ret, buffer = cv2.imencode('.jpg', frame)

		frame = buffer.tobytes()

		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



	cap.release()


def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')



def capture_photo(request):

	# Set the path to the folder to save the captured image
	save_folder = "C:/Users/muham/Music/3/mysite/account/static/account/media/captured"

	# Initialize the camera and grab a reference to the raw camera capture
	cap = cv2.VideoCapture(0)

	# Read a frame from the camera
	ret, frame = cap.read()

    # Save the frame to disk

	save_path = os.path.join(save_folder, "captured_image.jpg")
	cv2.imwrite(save_path, frame)

	# Clean up the camera resources
	cap.release()

	print(request.headers)
	return render(request,"account/captured.html",{})

def process_image(request):
	result = subprocess.run(['python', 'python/compare.py'], stdout=subprocess.PIPE)
	return render(request,"account/processed.html",{})



@csrf_protect
def add_class_view(request):
	if request.method == 'POST':
		form = add_class_form(request.POST)
		if form.is_valid():
			subject = form.cleaned_data[ 'subject']
			new_class = form.cleaned_data['new_class']
			no_of_students = form.cleaned_data['no_of_students']
			# add_button = form.cleaned_data['add_button']

			new_class_model = form.save(commit=True)
			new_class_model.user = request.user
			new_class_model.save()
			classes = add_class_model.objects.filter(user=request.user)
			# return render(request, 'account/tempview.html', {'classes': classes})
			return redirect('class_list_view')
		else:
			form = add_class_form(request.POST)
			print(form.errors)
	else:
		form = add_class_form()
	return render(request, 'account/createclass.html', {'form': form})



#testing...........................................


@csrf_protect
def delete_view(request, class_id):
    try:
        class_to_delete = add_class_model.objects.get(pk=class_id, user=request.user)
    except add_class_model.DoesNotExist:
        raise Http404("Class does not exist or does not belong to user.")
    class_to_delete.delete()
    return redirect('class_list_view')






#testing...........................................
