CREATE DATABASE school;
USE school;
-- one to many 
CREATE TABLE Grade(
	ID int NOT NULL,
    gradeNUMBER int NOT NULL,
    Course1 varchar(255),
    Course2 varchar(255),
    Course3 varchar(255),
    PRIMARY KEY (ID)
);
-- one to one
CREATE TABLE StudentProfile(
	ID int NOT NULL,
    ProfilePicURL varchar(255),
    FriendsCount int,
    PRIMARY KEY(ID)
);
-- many to many
CREATE TABLE Teacher (
    ID int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255) NOT NULL,
    Age int,
    PRIMARY KEY (ID) 
);
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
);
-- Pivot table
CREATE TABLE STUDENT_TEACHER(
	StudentId int,
    TeacherId int,
    
	CONSTRAINT FK_Student FOREIGN KEY(StudentId)
    REFERENCES Student(ID),
    
    CONSTRAINT FK_Teacher FOREIGN KEY(TeacherId)
    REFERENCES Teacher(ID),
    
    CONSTRAINT PK_Person PRIMARY KEY (StudentID,TeacherId),
	CONSTRAINT UC_Person UNIQUE (StudentID,TeacherId)

);