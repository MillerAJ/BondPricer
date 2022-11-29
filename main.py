# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import PySimpleGUI
from datetime import datetime
import math


def createWindow2():
    import PySimpleGUI as sg

    sg.theme('BluePurple')

    layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pattern 2B', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()


def createWindow():
    import PySimpleGUI as sg
    sg.theme('Default1')  # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [[sg.Text('Face Value/Par Value ($):'), sg.InputText()],
              [sg.Text('Annual Coupon Rate (%):'), sg.InputText()],
              [sg.Text('Discount Rate (%):'), sg.InputText()],
              [sg.Text('Years to Maturity:'), sg.InputText()],
              [sg.Text("Payment Frequency:"), sg.Combo(["Annually", "Biannually", "Quarterly", "Monthly", "None (Zero Coupon)"])],
              [sg.Text("Bond Price:"),sg.Text(key="-OUTPUT-")],
              [sg.Button("Enter"), sg.Button("Close")]]

    # Create the Window
    window = sg.Window('Bond Price Calculator', layout)
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print (values)
        #set payentFrequency
        if values[4] == "Annually":
            paymentFreq = 1
        elif values[4] == "Biannually":
            paymentFreq = 2
        elif values[4] == "Quarterly":
            paymentFreq = 4
        elif values[4] == "Monthly":
            paymentFreq = 12
        elif values[4] == "None (Zero Coupon)":
            paymentFreq = 0

        if event in (sg.WIN_CLOSED, 'Close'):
            break
        if event == 'Enter':
            bondPrice = bondCalc(float(values[0]), float(values[1])/100, float(values[2])/100, float(values[3]), paymentFreq)
            window['-OUTPUT-'].update(bondPrice)

    window.close()

def bondCalc(faceVal,couponRate,discRate,yearsToMat,paymentFreq):

    # faceVal = 10000
    # couponRate = .05
    # paymentFreq = 12
    # yearsToMat = 15
    # discRate = .15

    if paymentFreq == 0:
        discMatVal = faceVal / pow((1 + discRate), yearsToMat)
        print(round(discMatVal, 2))
    else:
        annualCashFlow = couponRate * faceVal
        cashPerPeriod = annualCashFlow / paymentFreq
        paymentRate = discRate / paymentFreq
        # couponRate = couponRate / paymentFreq

        # daysPerPayment = 365/paymentFreq

        # today = datetime.today()
        # timeDiff = (matDate - today).days  # number of days to maturity, returns a int
        # numOfPayments = timeDiff/daysPerPayment
        numOfPayments = yearsToMat * paymentFreq


        DCF = 1-(pow(1+ paymentRate, -numOfPayments))
        DCF = DCF / paymentRate
        DCF = cashPerPeriod * DCF
        discMatVal = faceVal/pow((1+paymentRate), numOfPayments)

        return round(DCF + discMatVal, 2)

createWindow()