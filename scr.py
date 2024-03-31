import requests

# Функция для выполнения запроса к API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Ошибка при получении данных:', response.text)
        return None

# Функция для создания таблицы с полученными данными
def create_table(data):
    table = '<table>'
    
    # Добавление строки с датой
    table += f'<tr><td colspan="{data["windowsPerRoom"][0]}">{data["date"]}</td></tr>'
    
    for i in range(data['roomsPerFloor']):
        table += '<tr>'
        for j in range(data['windowsPerRoom'][i]):
            room_number = i + 1
            window_number = j + 1
            light_status = data['lightStatus'][i][j]
            color = 'yellow' if light_status == 'on' else 'grey'
            value = f'Комната {room_number}, Окно {window_number}'
            table += f'<td style="background-color: {color}">{value}</td>'
        table += '</tr>'
    
    table += '</table>'
    
    # Добавление входных данных
    input_data = f'Входные данные: количество комнат на этаже - {data["roomsPerFloor"]}, Кол-во окон на этаже - {sum(data["windowsPerRoom"])}'
    # Добавление ответа
    rooms_with_light_on = [f'Комната {i+1}' for i, row in enumerate(data['lightStatus']) if 'on' in row]
    output_data = f'Ответ: Количество комнат - {len(rooms_with_light_on)}, Номера комнат - {", ".join(rooms_with_light_on)}'
    
    table += f'<div>{input_data}</div>'
    table += f'<div>{output_data}</div>'
    
    return table

# Вызов функции fetch_data для получения данных и создание таблицы
data = fetch_data('https://example-api.com/data')
if data:
    table = create_table(data)
    print(table)
