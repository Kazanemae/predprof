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
    
    for i in range(data['roomsPerFloor']):
        table += '<tr>'
        for j in range(data['windowsPerRoom'][i]):
            value = f'Комната {i + 1}, Окно {j + 1}'
            table += f'<td>{value}</td>'
        table += '</tr>'
    
    table += '</table>'
    return table

# Вызов функции fetch_data для получения данных и создание таблицы
data = fetch_data('https://example-api.com/data')
if data:
    table = create_table(data)
    print(table)
