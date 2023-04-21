
import cv2
import datetime

#Video stream set to web cameras
vid1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
vid2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
takePic = True
cameraDir = ["camera0", "camera1"]
#returns an array [Hour, Min, Second]
def getTime():
	time = datetime.datetime.now().strftime('%H:%M:%S')
	time = time.split(":")
	return time


while(True):
	date = datetime.date.today()
	time = getTime()
	ret, frame = vid1.read()
	ret, frame2 = vid2.read()
	frames = [frame, frame2]

	#takes a picture at a designated time
	#Labels and stores it into cameras dir
	if time[0] == '06' and time[1] == '45': #morning 
		if takePic:
			for i in range(len(frames)):
				fileName = './images/Seedling{}/{}-morning.jpg'.format(cameraDir[i], date)
				cv2.imwrite(fileName, frames[i])
			takePic = False    
	elif time[0] == '12' and time[1] == '00': #noon 
		if takePic:
			for i in range(len(frames)):
				fileName = './images/Seedling{}/{}-noon.jpg'.format(cameraDir[i], date)
				cv2.imwrite(fileName, frames[i])
			takePic = False
	elif time[0] == '18' and time[1] == '00': #night
		if takePic:
			for i in range(len(frames)):
				fileName = './images/Seedling{}/{}-night.jpg'.format(cameraDir[i], date)
				cv2.imwrite(fileName, frames[i])
			takePic = False 
	else:
		takePic = True
	#displays feed
	cv2.imshow('camera0', frame)
	cv2.imshow('camera1', frame2)
	#quit 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid1.release()
vid2.release()
cv2.destroyAllWindows()
