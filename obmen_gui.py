import PySimpleGUI as sg
import requests


def get_ovcount_from_api(iv, ov, count):
    apiurl = f'http://192.168.20.46:8080/obmen?val1={iv}&val2={ov}&count={count}'
    result = requests.get(apiurl)
    result_sring = result.text
    result_elem = window['result']
    result_elem.update(result_sring)


def clear():
    window['result'].update("")
    window['ov'].update("")
    window['iv'].update("")
    window['cv'].update("")


sg.theme('DarkBlue13')

layout = [[sg.Text("Первая валюта:", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='iv')],
          [sg.Text("Вторая валюта: ", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='ov')],
          [sg.Text("Количество:    ", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='cv')],
          [sg.Text("0.0", font='Helvetica 16', key='result')],
          [sg.Button("Вычислить", enable_events=True, key='-CALC-', font='Helvetica 16'),
           sg.Button("Очистить", enable_events=True, key='-CLEAR-', font='Helvetica 16'),
           sg.Button("График валют", enable_events=True, key="plot", font='Helvetica 16')]]

layout2 = [[sg.InputText('Введите валюту', font='Helvetica 16'), sg.InputText('Начало периода', font='Helvetica 16'),
            sg.InputText('Конец периода!', font='Helvetica 16')],
           [sg.Button('Построить график', font='Helvetica 16', enable_events=True, key='draw')],
           [sg.Canvas(key='canvas', size=(1500,800), background_color="white")],
           [sg.Button('Закрыть окно', font='Helvetica 16', enable_events=True, key='close_plot')]
           ]
window = sg.Window("Обменник валют.", layout)

while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    if event == '-CALC-':
        print(values)
        print(type(values))
        get_ovcount_from_api(values['iv'], values['ov'], values['cv'])
    if event == '-CLEAR-':
        clear()
    if event == 'plot':
        window.Hide()
        window2 = sg.Window("График валют за период.", layout2)
        while True:
            event2, values2 = window2.read()
            if event2 == 'close_plot':
                window2.close()
                window.UnHide()
                break



# закрываем окно и освобождаем используемые ресурсы
window.close()
