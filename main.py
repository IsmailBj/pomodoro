import time
import PySimpleGUI as sg
from playsound import playsound
sg.theme('DarkAmber')

runWindow = True
toggleBtn = False
layout = [[
    sg.Text('Pomodoro Effect',
            size=(20, 1),
            font=("Helvetica", 20),
            justification="center",
            key='-UPDATE-',
            pad=(20)
            )
],
    [
        sg.Button('10', size=(5, 2),
                  key='10'
                  ),
        sg.Button('15', size=(5, 2),
                  key='15'
                  ),
        sg.Button('45', size=(5, 2),
                  key='45'
                  )
    ],
]

window = sg.Window('Window Title', layout, element_justification='center', size=(500, 200))


def countdown(minuts):
    while minuts:
        mins, secs = divmod(minuts, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        window['-UPDATE-'].update(timer)
        window.refresh()
        time.sleep(1)
        minuts -= 1
    window['-UPDATE-'].update("TimeOut")
    window.refresh()
    playsound('./assets/soundEffect.wav')
    sg.SystemTray.notify('Time is Up', 'Timeout Was ' + event)
    print('Time Finished')


while runWindow:
    event, values = window()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    else:
        window['10'].update(visible=toggleBtn)
        window['15'].update(visible=toggleBtn)
        window['45'].update(visible=toggleBtn)
        countdown(int(event) * 60)
