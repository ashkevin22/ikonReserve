import tkinter as tk
from tkinter import ttk
from selenium import webdriver
import time
from tkcalendar import *
from datetime import date

months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
monthsNum = ["01","02","03","04","05","06","07","08","09","10","11","12"]
numToMonth = dict(zip(monthsNum, months))

def fromReloadIkon(listDate, section, item):
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(1)
    button = driver.find_element_by_css_selector("#react-autowhatever-resort-picker-section-" + str(section) + "-item-" + str(item))
    button.click()
    time.sleep(2)
    fromResortIkon(listDate, section)

def fromResortIkon(listDate, section):
    stringMonth = numToMonth[listDate[0]]
    button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pIuOK.kfwIKW > button")
    button.click()
    time.sleep(2)
    elem = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pZpxQ.kynict > div:nth-child(1) > div.DayPicker.sc-pIVsU.fBycfn > div > div.sc-pcHDm.cSajLG > div.sc-ptCms.fzKffT > span")


    returnVal = 0

    findMonth = True
    while findMonth:
        pageMonth = elem.text[:len(stringMonth)]
        if pageMonth.strip() == stringMonth.strip():
            returnVal = checkAvailableIkon(listDate, section)
            findMonth = False
        else:
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pZpxQ.kynict > div:nth-child(1) > div.DayPicker.sc-pIVsU.fBycfn > div > div.sc-pcHDm.cSajLG > div.sc-ptCms.fzKffT > button:nth-child(3)")
            button.click()
    return returnVal


def checkAvailableIkon(listDate, section):
    day = listDate[1]
    available = True
    elems = driver.find_elements_by_class_name("DayPicker-Day")
    unavilableElems = driver.find_elements_by_class_name("DayPicker-Day--unavailable")
    for x in unavilableElems:
        if str(day) == x.text.strip():
            driver.refresh()
            fromReloadIkon(listDate, section, item)
            time.sleep(5)
            available = False
    if available:
        for x in elems:
            if str(day) == x.text.strip():
                x.click()
                reservationsLeft = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pZpxQ.kynict > div:nth-child(2) > div > div.sc-oVfmS.fqKNoT > label > div.sc-pdihw.bqUhYY > div.sc-pCOsa.qskIT")
                numReservations = ""
        for c in reservationsLeft.text:
            if c.isdigit():
                numReservations += c
        if int(numReservations) == 0:
            print("Could not book reservation. You have 0 remaining reservations.")
            return
        else:
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pZpxQ.kynict > div:nth-child(2) > div > div.sc-pAKSZ.dHRKUJ > button.sc-AxjAm.jxPclZ.sc-pDabv.cXRBvv")
            button.click()
            time.sleep(1)
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pJgJK.dNdgLq > button")
            button.click()
            time.sleep(2)
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div > div.sc-pYZcj.ffynVg > label > input")
            button.click()
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div > div.sc-pJTpM.ieaJIt > button")
            button.click()
            print("Successfully booked!")
            return 1

def centerWindow(root):
    root.attributes('-alpha', 0)
    root.update()

    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    root.attributes('-alpha', 1)
    root.mainloop()


resorts = [("Alta Snowbird", 0),("Arapahoe Basin", 1),("Big Sky", 2),("Brighton", 3),("Copper Mountain", 4),("Deer Valley", 5),("Eldora", 6),("Solitude", 7),("Steamboat", 8),("Taos", 9),("Winter Park", 10),("Big Bear", 11),("June Mountain", 12),("Mammoth", 13),("Squaw Valley", 14),("Boyne Highlands", 15),("Boyne Mountain", 16),("Crystal Mountain", 17),("Mt. Bachelor", 18),("Summit at Snoqualmie", 19),("Killington", 20),("Loon Mountain",21),("Snowshoe",22),("Stratton",23),("Sugarbush",24),("Sugarloaf",25),("Sunday River",26),("Windham Mountain",27),("Blue Mountain",28),("Tremblant",29),("Cypress Mountain",30),("Red Mountain",31),("Revelstoke",32),("Ski Big 3",33),("Coronet Peak",34),("Mt. Butler",35),("Thredbo",36),("Niseko United",37),("Valle Nevado",38),("Zermatt",39)]
ikonReserveList = ["Arapahoe Basin", "Big Sky", "Brighton", "Taos", "Winter Park", "Crystal Mountain", "Loon Mountain", "Summit at Snoqualmie", "Windham Mountain"]

def submit():
    root.destroy()
    time.sleep(1)

today = date.today()
root = tk.Tk()

style = ttk.Style(root)
style.theme_use('default')

v = tk.IntVar()
v.set(10)  # initializing the choice, Winter Park
cal = Calendar(root, font="Arial 14", selectmode='day', year=today.year, month=today.month, day=today.day, width=100, mindate=today, maxdate=date(2021,6,6))
cal.grid(column=1, row=21, columnspan=2)
root.title("Ikon Pass Destinations")
tk.Label(root, text="Choose the desired destination",justify='center').grid(column=1, row=0, columnspan=2)

for i, resortVal in enumerate(resorts):
    if i > 19:
        col = 2
        rowNum = i-19
    else:
        col = 1
        rowNum = i+1
    if resortVal[0] in ikonReserveList:
        tk.Radiobutton(root, text=resortVal[0], padx = 20, variable=v, value=resortVal[1]).grid(column=col, row=rowNum, sticky="W")
    else:
        tk.Radiobutton(root, text=resortVal[0], padx=20, variable=v, value=resortVal[1], state="disabled").grid(column=col, row=rowNum,sticky="W")

tk.Button(root, text="Submit", command=submit).grid(column=1, row=22, columnspan=2)

centerWindow(root)
location = int(v.get())
date = cal.selection_get()

if location <= 10:
    section = 0
    item = location
elif location <= 14:
    section = 1
    item = location-11
elif location <= 16:
    section = 2
    item = location-15
elif location <= 19:
    section = 3
    item = location-17
elif location <= 27:
    section = 4
    item = location-20
elif location <= 29:
    section = 5
    item = location-28
elif location <= 33:
    section = 6
    item = location-30
elif location == 34:
    section = 7
    item = 0
elif location <= 36:
    section = 8
    item = location-35
elif location == 37:
    section = 9
    item = 0
elif location == 38:
    section = 10
    item = 0
elif location == 29:
    section = 11
    item = 0
else:
    section = 0
    item = 0

driver = webdriver.Chrome()
driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")
time.sleep(2)
while driver.current_url != "https://account.ikonpass.com/en/myaccount":
    continue

driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")

driver.execute_script("window.scrollTo(0, 200)")
elems = driver.find_elements_by_class_name("react-autosuggest__section-title")
for x in elems:
    if x.text.strip().lower() == "my favorites":
        section += 1
button = driver.find_element_by_css_selector("#react-autowhatever-resort-picker-section-" + str(section) + "-item-" + str(item))
button.click()
time.sleep(2)

#variable shows which website the booking needs to be made on
#0: ikonpass website
#1: parking reservations on resort website
#2: no booking required

bookingType = -1


if driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-qYFre.hyLEUz > div.sc-pBwqG.hsfcA-d > div.sc-pIuOK.kfwIKW > button"):
    bookingType = 0
elif driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pZpxQ.kynict > div:nth-child(2) > div > a"):
    bookingType = 1
else:
    bookingType = 2

#if bookingType == 1 or bookingType == 0:
    #do something

listDate = str(date).split("-")
listDate = listDate[1:]
if int(listDate[1]) < 10:
    listDate[1] = str(int(listDate[1])%10)

fromResortIkon(listDate, section)

driver.close()