# VIT UNIVERSITY ALL COURSES(FFCS) DATABASE

''' NOTE: YOU CAN EDIT THE FILE LOCATIONS WHEREVER NECESSARY '''

import re
import sqlite3

# sqlite queries
conn = sqlite3.connect("VIT_Courses.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS VIT(
         DEPARTMENT text,
         Subject text,
         Type text,
         EID integer,
         Faculty text,
         School text
         )""")

c.execute("""CREATE TABLE IF NOT EXISTS BIOTECH(
         Subject text,
         Type text,
         EID integer,
         Faculty text,
         School text
         )""")

c.execute("""CREATE TABLE IF NOT EXISTS CSE(
         Subject text,
         Type text,
         EID integer,
         Faculty text,
         School text
         )""")

c.execute("""CREATE TABLE IF NOT EXISTS ECE(
         Subject text,
         Type text,
         EID integer,
         Faculty text,
         School text
         )""")

c.execute(""" CREATE TABLE IF NOT EXISTS EEE(
        Subject text,
        Type text,
        EID integer,
        Faculty text,
        School text)""")

c.execute("""CREATE TABLE IF NOT EXISTS IT(
        Subject text,
        Type text,
        EID integer,
        Faculty text,
        School text)""")

c.execute(""" CREATE TABLE IF NOT EXISTS MECHANICAL
        (Subject text,
        Type text,
        EID integer,
        Faculty text,
        School text)""")

# File Handle
fname = open("WINSEM2020-21_VIT.txt")
for lines in fname:
    lines = lines.strip()
    source1 = re.findall("^BIT+.+", lines)
    source2 = re.findall("^MSM+.+", lines)
    cse1 = re.findall("^CSE+.+", lines)
    ece = re.findall("^ECE+.+", lines)
    eee = re.findall("^EEE+.+", lines)
    it = re.findall("^IT+.+", lines)
    mech = re.findall("^MEE+.+", lines)

    # Source1(Biotech1)
    if not len(source1) <= 0:
        source1 = source1[0]
        source1 = source1.split("\t")
        # Names for source 1
        sub1 = source1[1]
        type1 = source1[2]
        eid1 = source1[3]
        faculty1 = source1[4]
        school1 = source1[5]
        source1_dep = "BIOTECHNOLOGY"
        c.execute(""" INSERT INTO BIOTECH (Subject,Type,EID,Faculty,School)
                        VALUES (?,?,?,?,?)""", (sub1, type1, eid1, faculty1, school1))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject,Type,EID,Faculty,School)
                    VALUES (?,?,?,?,?,?)""", (source1_dep, sub1, type1, eid1, faculty1, school1))

    # Source2 (Biotech2)
    if not len(source2) <= 0:
        source2 = source2[0]
        source2 = source2.split("\t")
        # Names for source2
        sub2 = source2[1]
        type2 = source2[2]
        eid2 = source2[3]
        faculty2 = source2[4]
        school2 = source2[5]
        source2_dep = "BIOTECHNOLOGY"
        c.execute(""" INSERT INTO BIOTECH (Subject,Type,EID,Faculty,School)
                        VALUES (?,?,?,?,?)""", (sub2, type2, eid2, faculty2, school2))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject,Type,EID,Faculty,School)
            VALUES (?,?,?,?,?,?)""", (source2_dep, sub2, type2, eid2, faculty2, school2))

    # CSE1
    if not len(cse1) <= 0:
        cse1 = cse1[0]
        cse1 = cse1.split("\t")
        # Names for CSE
        cse1_sub = cse1[1]
        cse1_type = cse1[2]
        cse1_eid = cse1[3]
        cse1_faculty = cse1[4]
        cse1_school = cse1[5]
        cse_dep = "COMPUTER SCIENCE"
        c.execute(""" INSERT INTO CSE (Subject,Type,EID,Faculty,School)
                VALUES (?,?,?,?,?)""", (cse1_sub, cse1_type, cse1_eid, cse1_faculty, cse1_school))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject,Type,EID,Faculty,School)
             VALUES (?,?,?,?,?,?)""", (cse_dep, cse1_sub, cse1_type, cse1_eid, cse1_faculty, cse1_school))

    # ECE
    if not len(ece) <= 0:
        ece = ece[0]
        ece = ece.split("\t")
        # Names for ECE
        ece_sub = ece[1]
        ece_type = ece[2]
        ece_eid = ece[3]
        ece_faculty = ece[4]
        ece_school = ece[5]
        ece_dep = "ELECTRONICS AND COMMUNICATION ENGINEERING "
        c.execute(""" INSERT INTO ECE (Subject, Type, EID, Faculty, School)
                VALUES (?,?,?,?,?)""", (ece_sub, ece_type, ece_eid, ece_faculty, ece_school))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject, Type, EID, Faculty, School)
            VALUES (?,?,?,?,?,?)""", (ece_dep, ece_sub, ece_type, ece_eid, ece_faculty, ece_school))

    # EEE
    if not len(eee) <= 0:
        eee = eee[0]
        eee = eee.split("\t")
        # Names for EEE
        eee_sub = eee[1]
        eee_type = eee[2]
        eee_eid = eee[3]
        eee_faculty = eee[4]
        eee_school = eee[5]
        eee_dep = "ELECTRICAL AND ELECTRONICS ENGINEERING"
        c.execute(""" INSERT INTO EEE (Subject, Type, EID, Faculty, School)
                #VALUES (?,?,?,?,?) """, (eee_sub, eee_type, eee_eid, eee_faculty, eee_school))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject, Type, EID, Faculty, School)
            #VALUES (?,?,?,?,?,?) """, (eee_dep,eee_sub, eee_type, eee_eid, eee_faculty, eee_school))

    # IT
    if not len(it) <= 0:
        it = it[0]
        it = it.split("\t")
        # Names for IT
        it_sub = it[1]
        it_type = it[2]
        it_eid = it[3]
        it_faculty = it[4]
        it_school = it[5]
        dep_it = "INFORMATION TECHNOLOGY"
        c.execute(""" INSERT INTO IT (Subject, Type, EID, Faculty, School)
                #VALUES (?,?,?,?,?)""", (it_sub, it_type, it_eid, it_faculty, it_school))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject,Type,EID,Faculty,School)
         VALUES (?,?,?,?,?,?)""", (dep_it, it_sub, it_type, it_eid, it_faculty, it_school))

    # Mechanical
    if not len(mech) <= 0:
        mech = mech[0]
        mech = mech.split("\t")
        # Names for Mechanical
        mech_sub = mech[1]
        mech_type = mech[2]
        mech_eid = mech[3]
        mech_faculty = mech[4]
        mech_school = mech[5]
        dep_mech = "MECHANICAL"
        c.execute(""" INSERT INTO MECHANICAL (Subject,Type,EID,Faculty,School)
                VALUES (?,?,?,?,?)""", (mech_sub, mech_type, mech_eid, mech_faculty, mech_school))

        c.execute(""" INSERT INTO VIT (DEPARTMENT,Subject,Type,EID,Faculty,School)
                VALUES (?,?,?,?,?,?)""", (dep_mech, mech_sub, mech_type, mech_eid, mech_faculty, mech_school))

conn.commit()
conn.close()







