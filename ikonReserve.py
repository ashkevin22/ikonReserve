import tkinter
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


def fromReserve(listDate, inputBool):
    stringMonth = listDate[0]
    day = listDate[1]
    time.sleep(2)
    button = driver.find_element_by_css_selector("#react-autowhatever-resort-picker-section-0-item-3 > span > span")
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
            print("Could not book reservation, you have 0 days left.")
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

driver = webdriver.Chrome()
driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")
time.sleep(2)
print(driver.current_url)
while driver.current_url != "https://account.ikonpass.com/en/myaccount":
    continue

driver.get("https://account.ikonpass.com/en/myaccount/add-reservations/")

fromReserve(dateInput(), True)

driver.close()