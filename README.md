# Python-Projects-Student Attendance Management System (SAMS)

This is a Student Attendance Management System (SAMS) in Python to keep Student Attendance record with facial recognition.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshot](#screenshot)
  - [Links](#links)
  - [Installations](#installations)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview
This is a Student Attendance Management System (SAMS) in Python using Tkinter, pillow, SQL, Opencv, and other libraries for Attendance record with facial recognition. I started this project to help me improve my coding skills by building real projects. One of my Student motivated me to start this project as she is also going to make the same for her final year project. I liked the idea and decided to give it a go. 


## The challenge

- My first challange would be an eye catching design.
- Making a well-defined database.
- Connecting and using all the SQL functions (joins, groups, etc.) in python.
- Understand how Facial Recognition works.
- Understand algorithms used for Facial Recognition.


Users should be able to:

- Enter, save, update, or delete Student record.
- Upload pics for recoginition
- Take attendance from live video face recogitition for attendance.
- Check student attendance record.
- Get help from video tutorials.
- Make backup on Hard Drive and Flash Drive. 

## Screenshot
### Main Menu
![Screenshot (1)](https://github.com/EduCreative/Python-Projects-SAMS/blob/main/images/Screenshot1.png)
### Add Student Details
![Screenshot (2)](https://github.com/EduCreative/Python-Projects-SAMS/blob/main/images/Screenshot2.png)
### Attendance Record
![Screenshot (3)](https://github.com/EduCreative/Python-Projects-SAMS/blob/main/images/Screenshot3.png)


## Links
- Solution URL: (https://github.com/EduCreative/Python-Projects-SAMS.git)

## Installations
- pip install Pillow
- pip install mysql-connector-python
- pip install numpy
- pip install opencv-python

In case if you find problem with cv2.face (as OpenCV has removed the cv2.face module from version 4.4.0 onwards), you need to install following:

- pip install opencv-contrib-python
  
For details about this solution here on Stackoverflow:
(https://stackoverflow.com/questions/45655699/attributeerror-module-cv2-face-has-no-attribute-createlbphfacerecognizer])

And if you find problem with installing opencv-contrib-python, you need to install following:

- pip install --upgrade pip setuptools wheel
  
For details about this solution here on Stackoverflow:
(https://stackoverflow.com/questions/63732353/error-could-not-build-wheels-for-opencv-python-which-use-pep-517-and-cannot-be)


## My process
For this project, I am using different resources like W3school, stackoverflow, Youtube tutorials, documentations, etc. And covering all aspects of project step by step.
- I went for an eye catching design by adding some free images (from freepik, unsplash, etc.) for menu buttons, and background images.
- Made a database (not very well defined as it is just a practice project for students) using mysql server.
- Facial Recognition: cv2 cascade classifier, haarcascade_frontalface_default.xml
- Algorithm: LBPHFaceRecognizer

## Project Sequence
- First user must Add Student Details by using ADD STUDENT
- Take student Photos (100 photos for training) by using TAKE PHOTO option in ADD STUDENT
- Train Data sets by selecting TRAIN DATASETS menu option
- Face Recoginition and take Attendance both are done at FACE RECOGNITION
- Check to see, import, export (in CSV file) attendance.
- You can also view all photos taken in PHOTOS

### Libraries Used
- mysql-connector-python (to use mysql database)
- numpy (for calculation during image processing)
- opencv-python (image processing)
- os (for file operations like open, save, etc.)
- Pillow (to process images)
- tkinter (for GUI, buttons, frames, images, etc.)

### Database properties
Make following in mysql local host to save student data.

#Schema
date base   `sams`

### Tables
Table       `student`
Fields:
`std_id`
`student_name`
`father_name`, 
`Address`, 
`phone`, 
`dept`, 
`course`, 
`semester`, 
`year`

 Insert Query to add record to the Student Table to define the fields and values

INSERT INTO `sams`.`student` (`std_id`, `student_name`, `father_name`, `Address`, `phone`, `dept`, `course`, `semester`, `year`) VALUES ('1', 'Ali', 'Ahhmed', 'House NO. 123, Latifabad', '0333-1306603', 'Computer', 'BSWE', '2nd', '2024');

## Built with
### Languages
- PYTHON
- MySql
  
### Libraries:
- tkinter
- Numpy
- os
- mysql-connector-python
- opencv
- pillow

## What I learned

- I learned that I need to learn more by making more similar projects because I have not made any resonable (and useable) project in Python yet.
- GUI using tkinter, from forms to buttons and everything in between.
- Use of MySql for Database connectivity in Python.
- Use github along with VSCode for a full fledge project.
- facial recognition.

## Continued development

I need to practice Python by making more practical projects. And after completing this one I will go for more advance projects.

## Useful resources

- [W3School](https://www.w3school.com) - This helped me for every thing as I use W3School as a reference tool.
- [Youtube](https://www.youtube.com) - This helped me to seek help for different libraries and functions.


## Author

- Website - [Masroor Khan](https://educreative.github.io/)
- Frontend Mentor - [@EduCreative](https://www.frontendmentor.io/profile/EduCreative)
- Twitter - [@CreativeWork7](https://www.twitter.com/CreativeWork7)
