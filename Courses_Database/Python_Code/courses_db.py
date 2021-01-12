# Source Code for Wasington University Courses Database

''' NOTE: REMOVE THE COMMENTS WHEREVER NEEDED(FOR INSERTION INTO DB)''' 

from xml.etree import ElementTree
import os
import sqlite3

# SQLite QUERY
conn = sqlite3.connect("Washington University Courses.db") # Change according to your location
c = conn.cursor()

# SQLite Tables
c.execute("""CREATE TABLE IF NOT EXISTS "WASHINGTON UNIVERSITY COURSES INFO"(
        Course_Id integer,
        Course_Name text,
        Units integer,
        Instructor_Name text,
        Building text,
        Room_Number integer
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS COURSE_ID(
        Course_Id integer
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS COURSE_NAME(
        Course_Name text
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS UNITS(
        Unit_Number integer
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS INSTRUCTOR(
        Faculty_Name text
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS BUILDING_NAME(
        Building integer
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS ROOM_NUMBER(
        Room text
        )""")

# File Handling
fname = "courses.xml"
full = os.path.abspath(os.path.join(fname))
dom = ElementTree.parse(full)
fname2 = open("course_info.txt", "r")  # Change type to "w" when needed & Change according to your location

# Parsing DATA FROM XML
regd_num = dom.findall("course/reg_num")
course_name = dom.findall("course/title")
unit_num = dom.findall("course/units")
instructor_name = dom.findall("course/instructor")
building_name = dom.findall("course/place/building")
room_num = dom.findall("course/place/room")

# EXTRACTING DATA
for num in regd_num:
    reg_num = num.text
    '''print(reg_num)

    fname2.write("\n")
    try:
        fname2.write(reg_num)
    except:
        fname2.write("NA")'''

'''   c.execute("""INSERT INTO COURSE_ID(Course_Id)
    VALUES (?)""", (reg_num,)) '''

#fname2.write("\n")

for crse in course_name:
    course = crse.text
    '''print(course)
    
    fname2.write("\n")
    try:
        fname2.write(course)
    except:
        TypeError
        fname2.write("NA")'''

'''   c.execute("""INSERT INTO COURSE_NAME(Course_Name)
    VALUES (?)""", (course,)) '''
#fname2.write("\n")

for u in unit_num:
    units = u.text
    '''print(units)
    
    fname2.write("\n")
    try:
        fname2.write(units)
    except:
        TypeError
        fname2.write("NA")'''

'''    c.execute("""INSERT INTO UNITS(Unit_Number)
    VALUES (?)""", (units,)) '''
#fname2.write("\n")

for i in instructor_name:
    instructor = i.text
    '''print(instructor)
    
    fname2.write("\n")
    try:
        fname2.write(instructor)
    except:
        TypeError
        fname2.write("NA")'''

'''    c.execute("""INSERT INTO INSTRUCTOR(Faculty_Name)
    VALUES (?)""", (instructor,)) '''
#fname2.write("\n")

for b in building_name:
    building = b.text
    '''print(building)
    
    fname2.write("\n")
    try:
        fname2.write(building)
    except:
        TypeError
        fname2.write("NA")'''

'''    c.execute("""INSERT INTO BUILDING_NAME(Building)
    VALUES (?)""", (building,)) '''
#fname2.write("\n")

for r in room_num:
    room = r.text
    '''print(room)
    
    fname2.write("\n")
    try:
        fname2.write(room)
    except:
        TypeError
        fname2.write("NA")'''

'''    c.execute("""INSERT INTO ROOM_NUMBER(Room)
    VALUES (?)""", (room,)) '''

# Creating Empty Lists
course_id_list = []
course_name_list = []
unit_num_list = []
instructor_list = []
building_list = []
room_num_list = []

# INSERTING DATA INTO LIST FROM THE TEXT DOCUMENT
count = 0
for lines in fname2:
        lines = lines.strip()
        count = count + 1
        if count < 704:
            course_id_list.append(lines)
        if count in range(705, 1408):
            course_name_list.append(lines)
        if count in range(1409, 2112):
            unit_num_list.append(lines)
        if count in range(2113, 2816):
            instructor_list.append(lines)
        if count in range(2817, 3520):
            building_list.append(lines)
        if count in range(3521, 4224):
            room_num_list.append(lines)

# INSERTING DATA INTO MASTER TABLE
'''
for ids, course_title, unit_no, faculty, building_no, room_no in zip(course_id_list, course_name_list, unit_num_list, instructor_list, building_list, room_num_list ):
    c.execute("""INSERT INTO "WASHINGTON UNIVERSITY COURSES INFO"(Course_Id, Course_Name, Units,
        Instructor_Name, Building, Room_Number)
        VALUES (?,?,?,?,?,?)""", (ids, course_title, unit_no, faculty, building_no, room_no))
'''
# END STATEMENT
conn.commit()
conn.close()
