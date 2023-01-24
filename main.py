import PySimpleGUI
from datetime import datetime
import math

#calculates the price of a bond given the relevant variables    
def bondCalc(faceVal,couponRate,discRate,yearsToMat,paymentFreq):

    if paymentFreq == 0:
        discMatVal = faceVal / pow((1 + discRate), yearsToMat)
        print(round(discMatVal, 2))
    else:
        annualCashFlow = couponRate * faceVal
        cashPerPeriod = annualCashFlow / paymentFreq
        paymentRate = discRate / paymentFreq
        numOfPayments = yearsToMat * paymentFreq

        DCF = 1-(pow(1+ paymentRate, -numOfPayments))
        DCF = DCF / paymentRate
        DCF = cashPerPeriod * DCF
        discMatVal = faceVal/pow((1+paymentRate), numOfPayments)

        return round(DCF + discMatVal, 2)


#creates window for user interface
def createWindow():
    import PySimpleGUI as sg
    sg.theme('Default1') 
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



createWindow()
