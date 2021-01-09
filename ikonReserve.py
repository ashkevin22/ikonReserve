import tkinter as tk
from selenium import webdriver
import time

months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
monthsNum = list(range(1, 13))
numToMonth = dict(zip(monthsNum, months))


def dateInput():
    validate = True
    while validate:
        rawInput = input("Enter the desired month (1-6): ")
        if rawInput.isdigit():
            dateMonth = int(rawInput)
        if not rawInput.isdigit():
            print("Please enter a number")
        elif (dateMonth <= 6) and (dateMonth >= 1):
            validate = False
        else:
            print("Please enter a valid month")

    validate = True
    while validate:
        rawInput = input("Enter the desired day: ")
        if rawInput.isdigit():
            dateDay = int(rawInput)
        if not rawInput.isdigit():
            print("Please enter a number")
        elif dateMonth in [1, 3, 5, 7, 8, 10, 12]:
            if (dateDay <= 31) and (dateDay >= 1):
                validate = False
            else:
                print("Enter a valid day (1-31)")
        elif dateMonth in [4, 6, 9, 11]:
            if (dateDay <= 30) and (dateDay >= 1):
                validate = False
            else:
                print("Enter a valid day (1-30)")
        elif dateMonth == 2:
            if (dateDay <= 28) and (dateDay >= 1):
                validate = False
            else:
                print("Enter a valid day (1-28)")

    return [numToMonth[dateMonth], dateDay]


def fromReserve(listDate, inputBool, section, item):
    stringMonth = listDate[0]
    day = listDate[1]
    driver.execute_script("window.scrollTo(0, 200)")
    elems = driver.find_elements_by_class_name("react-autosuggest__section-title")
    for x in elems:
        if x.text.strip().lower() == "my favorites":
            section += 1
    button = driver.find_element_by_css_selector("#react-autowhatever-resort-picker-section-" + str(section) + "-item-" + str(item) + " > span > span")
    button.click()
    time.sleep(2)
    button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pIuOK.kfwIKW > button")
    button.click()
    time.sleep(2)
    elem = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pZpxQ.kynict > div:nth-child(1) > div.DayPicker.sc-pIVsU.fBycfn > div > div.sc-pcHDm.cSajLG > div.sc-ptCms.fzKffT > span")

    returnVal = 0

    findMonth = True
    while findMonth:
        pageMonth = elem.text[:len(stringMonth)]
        if pageMonth.strip() == stringMonth.strip():
            returnVal = checkAvailable(listDate, inputBool)
            findMonth = False
        else:
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pZpxQ.kynict > div:nth-child(1) > div.DayPicker.sc-pIVsU.fBycfn > div > div.sc-pcHDm.cSajLG > div.sc-ptCms.fzKffT > button:nth-child(3)")
            button.click()
    return returnVal


def checkAvailable(listDate, inputBool):
    day = listDate[1]
    available = True
    elems = driver.find_elements_by_class_name("DayPicker-Day")
    unavilableElems = driver.find_elements_by_class_name("DayPicker-Day--unavailable")
    for x in unavilableElems:
        if str(day) == x.text.strip():
            loop = 'y'
            if inputBool:
                loop = input("Chosen day is unavailable, would you like to continue checking until it becomes available? (y/n): ")
            if loop.lower() == 'y' or loop.lower() == "yes":
                driver.refresh()
                fromReserve(listDate, False)
                time.sleep(5)
            else:
                print("Goodbye")
                return
            available = False
    if available:
        for x in elems:
            if str(day) == x.text.strip():
                x.click()
        reservationsLeft = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pZpxQ.kynict > div:nth-child(2) > div > div.sc-oVfmS.fqKNoT > label > div.sc-pdihw.bqUhYY > div.sc-pCOsa.qskIT")
        numReservations = ""
        for c in reservationsLeft.text:
            if c.isdigit():
                numReservations += c
        if int(numReservations) == 0:
            print("Could not book reservation. You have 0 remaining reservations.")
            return
        else:
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-pZpxQ.kynict > div:nth-child(2) > div > div.sc-pZAOG.eUgRHN > button.sc-AxjAm.jxPclZ.sc-qcpLw.jSQblL")
            button.click()
            time.sleep(1)
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div.sc-oTAMn.eTrOuH > button")
            button.click()
            time.sleep(2)
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div > div.sc-pYZcj.ffynVg > label > input")
            button.click()
            button = driver.find_element_by_css_selector("#root > div > div > main > section.sc-pBolk.bLdbNO > div > div.amp-card.sc-pRrxg.OYQvJ > div.sc-pZOOJ.iFmuIW > div > div.sc-pJTpM.ieaJIt > button")
            button.click()
            print("Successfully booked!")
            return 1

root = tk.Tk()

v = tk.IntVar()
v.set(10)  # initializing the choice, i.e. Python

languages = [("Alta Snowbird", 0),("Arapahoe Basin", 1),("Big Sky", 2),("Brighton", 3),("Copper Mountain", 4),("Deer Valley", 5),("Eldora", 6),("Solitude", 7),("Steamboat", 8),("Taos", 9),("Winter Park", 10),("Big Bear", 11),("June Mountain", 11),("Mammoth", 13),("Squaw Valley", 14),("Boyne Highlands", 15),("Boyne Mountain", 16),("Crystal Mountain", 17),("Mt. Bachelor", 18),("Summit at Snoqualmie", 19),("Killington", 20),("Loon Mountain",21),("Snowshoe",22),("Stratton",23),("Sugarbush",24),("Sugarloaf",25),("Sunday River",26),("Windham Mountain",27),("Blue Mountain",28),("Tremblant",29),("Cypress Mountain",30),("Red Mountain",31),("Revelstoke",32),("Ski Big 3",33),("Coronet Peak",34),("Mt. Butler",35),("Thredbo",36),("Niseko United",37),("Valle Nevado",38),("Zermatt",39)]


def submit():
    root.destroy()


tk.Label(root, text="Choose the desired destination",justify = 'center',).grid(column=1, row=0, columnspan=2)

for i, langVal in enumerate(languages):
    if i > 19:
        col = 2
        rowNum = i-19
    else:
        col = 1
        rowNum = i+1
    tk.Radiobutton(root, text=langVal[0], padx = 20, variable=v, value=langVal[1]).grid(column=col, row=rowNum, sticky="W")
tk.Button(text="Submit", command=submit).grid(column=1, row=21, columnspan=2)

root.attributes('-alpha',0)
root.update()

# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.attributes('-alpha',1)
root.mainloop()

location = int(v.get())

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

driver = webdriver.Chrome()
driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")
time.sleep(2)
print(driver.current_url)
while driver.current_url != "https://account.ikonpass.com/en/myaccount":
    continue

driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")

fromReserve(dateInput(), True, section, item)

driver.close()
