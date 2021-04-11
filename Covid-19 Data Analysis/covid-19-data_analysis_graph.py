''' COVID-19: DATA ANALYSIS - 2020-2021 '''

# IMPORT STATEMENTS
from xml.etree import ElementTree
import os
import matplotlib.pyplot as plt
import sqlite3

# SQLITE QUERIES
conn = sqlite3.connect("COVID-19 2020-2021 DATA.db")
c = conn.cursor()

c.execute(""" DROP TABLE IF EXISTS 'COVID-19: WORLDWIDE' """)
c.execute(""" DROP TABLE IF EXISTS 'COVID-19: INDIA' """)
c.execute(""" DROP TABLE IF EXISTS 'COVID-19: UNITED STATES OF AMERICA' """)

# CREATING TABLES
c.execute(""" CREATE TABLE 'COVID-19: WORLDWIDE'(
        DATES text,
        WEEKS text,
        CASES integer,
        DEATHS integer,
        TERRITORY text,
        COUNTRY_CODE text,
        POPULATION integer,
        CONTINENT text,
        SPREADING_RATE integer) """)


c.execute(""" CREATE TABLE 'COVID-19: INDIA'(
        DATES text,
        WEEKS text,
        CASES integer,
        DEATHS integer,
        POPULATION integer,
        SPREADING_RATE integer) """)


c.execute(""" CREATE TABLE 'COVID-19: UNITED STATES OF AMERICA'(
        DATES text,
        WEEKS text,
        CASES integer,
        DEATHS integer,
        POPULATION integer,
        SPREADING_RATE integer) """)


# FILE HANDLE
fname = "covid-19_data.xml"
full = os.path.abspath(os.path.join(fname))
dom = ElementTree.parse(full)

fname2 = "covid-19_india_data.xml"
full2 = os.path.abspath(os.path.join(fname2))
dom2 = ElementTree.parse(full2)

fname3 = "covid-19_usa_data.xml"
full3 = os.path.abspath(os.path.join(fname3))
dom3 = ElementTree.parse(full3)

# PARSING DATA
date = dom.findall("record/dateRep")
week = dom.findall("record/year_week")
cases = dom.findall("record/cases_weekly")
deaths = dom.findall("record/deaths_weekly")
territory = dom.findall("record/countriesAndTerritories")
geo_code = dom.findall("record/countryterritoryCode")
population = dom.findall("record/popData2019")
continent = dom.findall("record/continentExp")
infec_rate = dom.findall("record/notification_rate_per_100000_population_14-days")
'''Total 9 Entries'''

# PARSING DATA - INDIA
india_deaths = dom2.findall("record/deaths_weekly")
india_cases = dom2.findall('record/cases_weekly')
india_rates = dom2.findall("record/notification_rate_per_100000_population_14-days")
india_popu = dom2.findall("record/popData2019")
india_dates = dom2.findall("record/dateRep")
india_weeks = dom2.findall("record/year_week")
'''Total 6 Entries'''

# PARSING DATA - USA
usa_deaths = dom3.findall("record/deaths_weekly")
usa_cases = dom3.findall('record/cases_weekly')
usa_rates = dom3.findall("record/notification_rate_per_100000_population_14-days")
usa_popu = dom3.findall("record/popData2019")
usa_dates = dom3.findall("record/dateRep")
usa_weeks = dom3.findall("record/year_week")
'''Total 6 Entries'''

# DATA LISTS
dates_list = []
weeks_list = []
tot_cases_list = []
tot_deaths_list = []
locations_list = []
loc_codes_list = []
tot_population_list = []
continent_names_list = []
inf_rates_list = []

# INDIA - DATA LISTS
ind_deaths_list = []
ind_cases_list = []
ind_rates_list = []
ind_pop_list = []
ind_dates_list = []
ind_weeks_list = []

# USA - DATA LISTS
usa_deaths_list = []
usa_cases_list = []
usa_rates_list = []
usa_pop_list = []
usa_dates_list = []
usa_weeks_list = []

# WEEKLY PLOT (FOR GRAPH)
weeks_plot = [54, 53 ,52 ,51 ,50 ,49 ,48 ,47 ,46 ,45 ,44 ,43 ,42 ,41 ,40 ,39 ,38 ,37 ,36 ,35 ,34 ,33 ,32 ,31 ,30 ,29 ,28 ,27 ,26 ,25 ,24 ,23 ,22 ,21 ,20 ,19 ,18 ,17 ,16 ,15 ,14 ,13 ,12 ,11 ,10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]

# EXTRACTING AND APPENDING DATA
for dte, wk, cas, det, terr, cod, pop, cont, rate in zip(date, week, cases, deaths, territory, geo_code, population, continent, infec_rate):
    # DATES
    dates = dte.text
    try:
        dates_list.append(dates)
    except:
        TypeError
        dates_list.append("NA")
    # WEEKS
    weeks = wk.text
    try:
        weeks_list.append(weeks)
    except:
        TypeError
        weeks_list.append("NA")
    # TOTAL CASES
    tot_cases = cas.text
    try:
        tot_cases_list.append(int(tot_cases))
    except:
        TypeError
        tot_cases_list.append(0)
    # TOTAL DEATHS
    tot_deaths = det.text
    try:
        tot_deaths_list.append(int(tot_deaths))
    except:
        TypeError
        tot_cases_list.append(0)
    # COUNTRIES
    locations = terr.text
    try:
        locations_list.append(locations)
    except:
        TypeError
        locations_list.append("NA")
    # GEO CODES
    loc_codes = cod.text
    try:
        loc_codes_list.append(loc_codes)
    except:
        TypeError
        loc_codes_list.append("NA")
    # POPULATIONS
    tot_population = pop.text
    try:
        tot_population_list.append(int(tot_population))
    except:
        TypeError
        tot_population_list.append(0)
    # CONTINENTS
    continent_names = cont.text
    try:
        continent_names_list.append(continent_names)
    except:
        TypeError
        continent_names_list.append("NA")
    # INFECTION RATES
    inf_rates = rate.text
    try:
        inf_rates_list.append(float(inf_rates))
    except:
        TypeError
        inf_rates_list.append(0.0)

    # APPENDING DATA INTO DATABASE
    c.execute(""" INSERT INTO 'COVID-19: WORLDWIDE' (DATES, WEEKS, CASES, DEATHS,
                    TERRITORY, COUNTRY_CODE, POPULATION, CONTINENT, SPREADING_RATE)
                     VALUES(?,?,?,?,?,?,?,?,?)""", (dates, weeks, tot_cases, tot_deaths, locations, loc_codes, tot_population, continent_names, inf_rates))


# EXTRACTING AND APPENDING DATA - INDIA
for ind_dts, ind_css, ind_rts, ind_pops, ind_dat, ind_wks in zip(india_deaths, india_cases, india_rates, india_popu, india_dates, india_weeks):
    ind_dts = ind_dts.text
    ind_deaths_list.append(int(ind_dts))

    ind_css = ind_css.text
    ind_cases_list.append(int(ind_css))

    ind_rts = ind_rts.text
    ind_rates_list.append(float(ind_rts))

    ind_pops = ind_pops.text
    ind_pop_list.append(int(ind_pops))

    ind_dat = ind_dat.text
    ind_dates_list.append(ind_dat)

    ind_wks = ind_wks.text
    ind_weeks_list.append(ind_wks)

    # APPENDING DATA INTO DATABASE - INDIA
    c.execute(""" INSERT INTO 'COVID-19: INDIA' (DATES, WEEKS, CASES, DEATHS,
                POPULATION, SPREADING_RATE)
                 VALUES(?,?,?,?,?,?)""", (ind_dat, ind_wks, ind_css, ind_dts, ind_pops, ind_rts))


# EXTRACTING DATA - USA
for usa_dts, usa_css, usa_rts, usa_pops, usa_dat, usa_wks in zip(usa_deaths, usa_cases, usa_rates, usa_popu, usa_dates, usa_weeks):
    usa_dts = usa_dts.text
    usa_deaths_list.append(int(usa_dts))

    usa_css = usa_css.text
    usa_cases_list.append(int(usa_css))

    usa_rts = usa_rts.text
    usa_rates_list.append(float(usa_rts))

    usa_pops = usa_pops.text
    usa_pop_list.append(int(usa_pops))

    usa_dat = usa_dat.text
    usa_dates_list.append(usa_dat)

    usa_wks = usa_wks.text
    usa_weeks_list.append(usa_wks)

    # APPENDING DATA INTO DATABASE - USA
    c.execute(""" INSERT INTO 'COVID-19: UNITED STATES OF AMERICA' (DATES, WEEKS, CASES, DEATHS,
                    POPULATION, SPREADING_RATE)
                     VALUES(?,?,?,?,?,?)""", (usa_dat, usa_wks, usa_css, usa_dts, usa_pops, usa_rts))


# DATABASE - COMMITING & CLOSING
conn.commit()
conn.close()


''' CASES/DEATHS/INFECTION RATE FINDER - INDIA '''
pos1 = 0
pos2 = 0
pos3 = 0
user_weeks_list = []

user_inp1 = input("Enter Year and Week (yyyy-ww): ")
user_inp2 = input("Enter CASES/DEATHS/RATE: ").upper()

if user_inp2 == "CASES":
    for i in ind_weeks_list:
        pos1 = pos1+1
        if i == user_inp1:
            ans = ind_cases_list[pos1-1]
            print("Number of CASES during", user_inp1, "=", ind_cases_list[pos1-1])

            # GRAPHS
            user_weeks = user_inp1.split("-")
            user_weeks = int(user_weeks[1])
            for w in range(1, user_weeks+1):
                user_weeks_list.append(w)
            ind_cases_list.reverse()
            cases_index = ind_cases_list.index(ans)
            cases_range = ind_cases_list[:cases_index+1]

            plt.plot(user_weeks_list, cases_range)
            plt.title("COVID-19: CASES GRAPH")
            plt.xlabel("WEEKS")
            plt.ylabel("CASES")
            plt.show()
            plt.close()

elif user_inp2 == "DEATHS":
    for j in ind_weeks_list:
        pos2 = pos2+1
        if j == user_inp1:
            ans = ind_deaths_list[pos2-1]
            print("Number of DEATHS during", user_inp1, "=", ind_deaths_list[pos2-1])

            # GRAPHS
            user_weeks = user_inp1.split("-")
            user_weeks = int(user_weeks[1])
            for w in range(1, user_weeks + 1):
                user_weeks_list.append(w)
            ind_deaths_list.reverse()
            deaths_index = ind_deaths_list.index(ans)
            deaths_range = ind_deaths_list[:deaths_index + 1]

            plt.plot(user_weeks_list, deaths_range)
            plt.title("COVID-19: DEATHS GRAPH")
            plt.xlabel("WEEKS")
            plt.ylabel("DEATHS")
            plt.show()
            plt.close()

elif user_inp2 == "RATE":
    for k in ind_weeks_list:
        pos3 = pos3 + 1
        if k == user_inp1:
            ans = ind_rates_list[pos3-1]
            print("INFECTION RATE during", user_inp1, "=", ind_rates_list[pos3-1])

            # GRAPHS
            user_weeks = user_inp1.split("-")
            user_weeks = int(user_weeks[1])
            for w in range(1, user_weeks + 1):
                user_weeks_list.append(w)
            ind_rates_list.reverse()
            rates_index = ind_rates_list.index(ans)
            rates_range = ind_rates_list[:rates_index + 1]

            plt.plot(user_weeks_list, rates_range)
            plt.title("COVID-19: INFECTION RATE GRAPH")
            plt.xlabel("WEEKS")
            plt.ylabel("INFECTION RATE")
            plt.show()
            plt.close()
else:
    print("PLEASE ENTER A VALID INPUT")


# LISTS FOR GRAPH PLOTTING
ind_deaths_list.reverse()
ind_cases_list.reverse()
weeks_plot.reverse()
usa_cases_list.reverse()
usa_deaths_list.reverse()
usa_rates_list.reverse()
ind_rates_list.reverse()

# PLOTTING A GRAPH - INDIA (CASES)
plt.plot(weeks_plot, ind_cases_list, 'r', label="CASES")

plt.xlabel("WEEKS")
plt.ylabel("CASES")
plt.title("COVID-19: INDIA - CASES")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA (DEATHS)
plt.plot(weeks_plot, ind_deaths_list, 'r', label="DEATHS")

plt.xlabel("WEEKS")
plt.ylabel("DEATHS")
plt.title('COVID-19: INDIA - DEATHS')

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA (INFECTION RATE)
plt.plot(weeks_plot, ind_rates_list, 'r', label="INFECTION RATE")

plt.xlabel("WEEKS")
plt.ylabel("INFECTION RATE")
plt.title('COVID-19: INDIA - DEATHS')

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA (CASES VS DEATHS)
plt.plot(weeks_plot, ind_deaths_list, 'r', label='DEATHS', linestyle='dashed')
plt.plot(weeks_plot, ind_cases_list, 'b', label='CASES', linestyle='dashed')

plt.xlabel("WEEKS")
plt.ylabel("CASES/DEATHS")
plt.title("COVID-19: 2019-2020")
plt.legend()

# plt.show()
plt.close()

# PLOTTING A SCATTER GRAPH - INDIA
plt.scatter(ind_cases_list, ind_deaths_list, marker="*", label="CASES/DEATHS", color='red')

plt.title("COVID-19: INDIA")
plt.legend()

# plt.show()
plt.close()

# PLOTTING A GRAPH - USA (CASES)
plt.plot(weeks_plot, usa_cases_list, 'r', label="CASES")

plt.xlabel("WEEKS")
plt.ylabel("CASES")
plt.title("COVID-19: USA")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - USA (DEATHS)
plt.plot(weeks_plot, usa_deaths_list, 'r', label="DEATHS")

plt.xlabel("WEEKS")
plt.ylabel("DEATHS")
plt.title("COVID-19: USA")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - USA (INFECTION RATE)
plt.plot(weeks_plot, usa_rates_list, 'r', label="INFECTION RATE")

plt.xlabel("WEEKS")
plt.ylabel("INFECTION RATE")
plt.title("COVID-19: USA")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - USA (CASES VS DEATHS)
plt.plot(weeks_plot, usa_cases_list, 'r', label='DEATHS', linestyle='dashed')
plt.plot(weeks_plot, usa_deaths_list, 'b', label='CASES', linestyle='dashed')

plt.xlabel("WEEKS")
plt.ylabel("CASES/DEATHS")
plt.title("COVID-19: 2019-2020")
plt.legend()

# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA VS USA (CASES)
plt.plot(weeks_plot, ind_cases_list, color="green", label="INDIA")
plt.plot(weeks_plot, usa_cases_list, color="orange", label="USA")

plt.xlabel("WEEKS")
plt.ylabel("CASES")
plt.title("COVID:19 - CASES (INDIA VS USA)")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA VS USA (DEATHS)
plt.plot(weeks_plot, ind_deaths_list, color="green", label="INDIA")
plt.plot(weeks_plot, usa_deaths_list, color="orange", label="USA")

plt.xlabel("WEEKS")
plt.ylabel("DEATHS")
plt.title("COVID:19 - DEATHS (INDIA VS USA)")

plt.legend()
# plt.show()
plt.close()

# PLOTTING A GRAPH - INDIA VS USE (INFECTION RATE)
plt.plot(weeks_plot, ind_rates_list, color="green", label="INDIA")
plt.plot(weeks_plot, usa_rates_list, color="orange", label="USA")

plt.xlabel("WEEKS")
plt.ylabel("INFECTION RATE")
plt.title("COVID:19 - INFECTION RATES (INDIA VS USA)")

plt.legend()
# plt.show()
plt.close()

'''----------------------------------------- WORKED OUT BY - PRANAV ------------------------------------------------ '''
'''------------------------------------------------- THE END --------------------------------------------------------'''

