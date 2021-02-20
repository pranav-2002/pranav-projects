''' VIOLENCE AGAINST WOMEN: INDIA '''

# IMPORT STATEMENTS
import os
from xml.etree import ElementTree
import matplotlib.pyplot as plt
import sqlite3

# SQLITE QUERIES
conn = sqlite3.connect("VIOLENCE AGAINST WOMEN.db")
c = conn.cursor()

c.execute(""" DROP TABLE IF EXISTS STATES """)
c.execute(""" DROP TABLE IF EXISTS RAPES_2019 """)
c.execute(""" DROP TABLE IF EXISTS RAPES_2020 """)
c.execute(""" DROP TABLE IF EXISTS ASSAULTS_2019 """)
c.execute(""" DROP TABLE IF EXISTS ASSAULTS_2020 """)
c.execute(""" DROP TABLE IF EXISTS MURDERS_2019 """)
c.execute(""" DROP TABLE IF EXISTS MURDERS_2020 """)
c.execute(""" DROP TABLE IF EXISTS 'VIOLENCE AGAINST WOMEN' """)


# CREATING TABLES
c.execute(""" CREATE TABLE STATES(
        STATE_NAME text) """)

c.execute(""" CREATE TABLE RAPES_2019(
        NUMBER_OF_CASES integer) """)

c.execute(""" CREATE TABLE RAPES_2020(
        NUMBER_OF_CASES integer) """)

c.execute(""" CREATE TABLE ASSAULTS_2019(
        NUMBER_OF_CASES) """)

c.execute(""" CREATE TABLE ASSAULTS_2020(
        NUMBER_OF_CASES) """)

c.execute(""" CREATE TABLE MURDERS_2019(
        NUMBER_OF_CASES integer) """)

c.execute(""" CREATE TABLE MURDERS_2020(
        NUMBER_OF_CASES integer) """)

c.execute(""" CREATE TABLE 'VIOLENCE AGAINST WOMEN'(
        STATES text,
        RAPES_2019 integer,
        RAPES_2020 integer,
        ASSAULTS_2019 integer,
        ASSAULTS_2020 integer,
        MURDERS_2019 integer,
        MURDERS_2020 integer) """)


# FILE HANDLING
fname = "violence_women.xml"
loc = os.path.abspath(os.path.join(fname))
data = ElementTree.parse(loc)

# PARSING XML DATA
states = data.findall("ROW/STATESUTS")
rapes_2019 = data.findall("ROW/RAPE_-_2019")
rapes_2020 = data.findall("ROW/RAPE_-_2020")
assaults_2019 = data.findall("ROW/ASSAULTS_MOLESTATION_-_2019")
assaults_2020 = data.findall("ROW/ASSAULTS_MOLESTATION_-_2020")
murders_2019 = data.findall("ROW/MURDER_WOMEN_-_2019")
murders_2020 = data.findall("ROW/MURDER_WOMEN_-_2020")

# DATA LISTS
states_list = []
rapes_2019_list = []
rapes_2020_list = []
assaults_2019_list = []
assaults_2020_list = []
murders_2019_list = []
murders_2020_list = []

# APPENDING DATA INTO LISTS
for sts,rps19,rps20,aslts19,aslts20,mrds19,mrds20 in zip(states, rapes_2019, rapes_2020, assaults_2019, assaults_2020, murders_2019, murders_2020):
    states_list.append(sts.text)
    rapes_2019_list.append(int(rps19.text))
    rapes_2020_list.append(int(rps20.text))
    assaults_2019_list.append(int(aslts19.text))
    assaults_2020_list.append(int(aslts20.text))
    murders_2019_list.append(int(mrds19.text))
    murders_2020_list.append(int(mrds20.text))


# APPENDING DATA INTO THE DATABASE
for sts,rps19,rps20,aslts19,aslts20,mrds19,mrds20 in zip(states_list, rapes_2019_list, rapes_2020_list,assaults_2019_list,assaults_2020_list, murders_2019_list, murders_2020_list):
    c.execute(""" INSERT INTO STATES(STATE_NAME) 
            VALUES (?)""", (sts,))

    c.execute(""" INSERT INTO RAPES_2019(NUMBER_OF_CASES)
            VALUES (?)""", (rps19,))

    c.execute(""" INSERT INTO RAPES_2020(NUMBER_OF_CASES)
                VALUES (?)""", (rps20,))

    c.execute(""" INSERT INTO ASSAULTS_2019(NUMBER_OF_CASES)
                VALUES (?)""", (aslts19,))

    c.execute(""" INSERT INTO ASSAULTS_2020(NUMBER_OF_CASES)
                VALUES (?)""", (aslts20,))

    c.execute(""" INSERT INTO MURDERS_2019(NUMBER_OF_CASES)
                VALUES (?)""", (mrds19,))

    c.execute(""" INSERT INTO MURDERS_2020(NUMBER_OF_CASES)
                VALUES (?)""", (mrds20,))

    c.execute(""" INSERT INTO 'VIOLENCE AGAINST WOMEN'(STATES, RAPES_2019, RAPES_2020, 
                ASSAULTS_2019, ASSAULTS_2020, MURDERS_2019, MURDERS_2020)
                VALUES (?,?,?,?,?,?,?) """, (sts, rps19, rps20, aslts19, aslts20, mrds19, mrds20))


# COMMITING AND CLOSING THE DATABASE
conn.commit()
conn.close()

# GRAPH - NUMBER OF RAPES IN 2019 VS 2020
plt.title("NUMBER OF RAPES IN 2019 VS 2020")

plt.plot(rapes_2019_list, label="rapes - 2019")
plt.plot(rapes_2020_list, label="rapes - 2020")

plt.legend()
plt.show()
plt.close()

# GRAPH - NUMBER OF ASSAULTS IN 2019 VS 2020
plt.title("NUMBER OF ASSAULTS IN 2019 VS 2020")

plt.plot(assaults_2019_list, label="assaults - 2019")
plt.plot(assaults_2020_list, label="assaults - 2020")

plt.legend()
plt.show()
plt.close()

# GRAPH - NUMBER OF MURDERS IN 2019 VS 2020
plt.title("GRAPH - NUMBER OF MURDERS IN 2019 VS 2020")

plt.plot(murders_2019_list, label="murders - 2019")
plt.plot(murders_2020_list, label="murders - 2020")

plt.legend()
plt.show()
plt.close()

''' ----------WORKED OUT BY PRANAV---------- '''

