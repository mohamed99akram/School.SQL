#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE Grade(
	ID int NOT NULL,
    gradeNUMBER int NOT NULL,
    Course1 varchar(255),
    Course2 varchar(255),
    Course3 varchar(255),
    PRIMARY KEY (ID)
);''')

print("Table Grade created successfully")

# One to One
conn.execute('''
CREATE TABLE StudentProfile(
	ID int NOT NULL,
    ProfilePicURL varchar(255),
    FriendsCount int,
    PRIMARY KEY(ID)
);''')

print("Table StudentProfile created successfully")

# Many to Many
conn.execute('''
CREATE TABLE Teacher (
    ID int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255) NOT NULL,
    Age int,
    PRIMARY KEY (ID) 
);''')

print("Table Teacher created successfully")

# Student
conn.execute('''
CREATE TABLE Student (
    ID int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255) NOT NULL,
    Age int,
    Grade int,
    ProfilePage int,
    
    CHECK (Age>=16),
    
    CONSTRAINT UC_Student UNIQUE (FirstName,LastName),
    
    CONSTRAINT FK_StudentGrade FOREIGN KEY(Grade)
    REFERENCES GRADE(ID),
    
    CONSTRAINT FK_StudentProfile FOREIGN KEY(ProfilePage)
    REFERENCES StudentProfile(ID),
    
    PRIMARY KEY (ID)
);''')

print("Table Student created successfully")

# Pivot table
conn.execute('''
CREATE TABLE STUDENT_TEACHER(
	StudentId int,
    TeacherId int,
    
	CONSTRAINT FK_Student FOREIGN KEY(StudentId)
    REFERENCES Student(ID),
    
    CONSTRAINT FK_Teacher FOREIGN KEY(TeacherId)
    REFERENCES Teacher(ID),
    
    CONSTRAINT PK_Person PRIMARY KEY (StudentID,TeacherId),
	CONSTRAINT UC_Person UNIQUE (StudentID,TeacherId)

);''')

print("Table student to teacher created successfully")


conn.close()
