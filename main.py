import PySimpleGUI as sg


def bondCalc(faceVal, couponRate, discRate, yearsToMat, paymentFreq):

    if paymentFreq == 0:
        discMatVal = faceVal / pow((1 + discRate), yearsToMat)
        return (round(discMatVal, 2))
    else:
        annualCashFlow = couponRate * faceVal
        cashPerPeriod = annualCashFlow / paymentFreq
        paymentRate = discRate / paymentFreq
        numOfPayments = yearsToMat * paymentFreq

        DCF = 1 - (pow(1 + paymentRate, -numOfPayments))
        DCF = DCF / paymentRate
        DCF = cashPerPeriod * DCF
        discMatVal = faceVal / pow((1 + paymentRate), numOfPayments)

        return round(DCF + discMatVal, 2)


def createWindow():
    sg.theme('Default1')  # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [[sg.Text('Face Value/Par Value ($):'),
               sg.InputText()],
              [sg.Text('Annual Coupon Rate (%):'),
               sg.InputText()],
              [sg.Text('Discount Rate (%):'),
               sg.InputText()],
              [sg.Text('Years to Maturity:'),
               sg.InputText()],
              [
                  sg.Text("Payment Frequency:"),
                  sg.Combo([
                      "Annually", "Biannually", "Quarterly", "Monthly",
                      "None (Zero Coupon)"
                  ],
                           default_value="Annually")
              ], [sg.Text("Bond Price:"),
                  sg.Text(key="-OUTPUT-")],
              [sg.Button("Enter"), sg.Button("Close")]]

    # Create the Window
    window = sg.Window('Bond Price Calculator', layout)

    # Event Loop to process "events"
    while True:
        event, values = window.read()  #timeout after 20 minutes
        #set payentFrequency

        if event == 'EXIT':
            sg.popup(
                "Session has timed out, please close and open a new instance of the application"
            )
            break
        if event in (sg.WIN_CLOSED, 'Close', None):
            break

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

        if event == 'Enter':
            typos = False
            try:
                float(values[0])
                float(values[1])
                float(values[2])
                float(values[3])
            except:
                typos = True
                print("There was an error with the data entered.")
            if typos == False:
                bondPrice = bondCalc(float(values[0]),
                                     float(values[1]) / 100,
                                     float(values[2]) / 100, float(values[3]),
                                     paymentFreq)
                window['-OUTPUT-'].update(bondPrice)

    window.close()


createWindow()
