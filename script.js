// Функция для выполнения запроса к API
function fetch_data(url) {
    return fetch(url)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                console.error('Ошибка при получении данных:', response.statusText);
                return null;
            }
        })
        .catch(error => console.error('Произошла ошибка:', error));
}

// Функция для создания таблицы с полученными данными
function create_table(data) {
    let table = '<table>';
    
    // Добавление строки с датой
    table += `<tr><td colspan="${data.windowsPerRoom[0]}">${data.date}</td></tr>`;
    
    for (let i = 0; i < data.roomsPerFloor; i++) {
        table += '<tr>';
        for (let j = 0; j < data.windowsPerRoom[i]; j++) {
            let room_number = i + 1;
            let window_number = j + 1;
            let light_status = data.lightStatus[i][j];
            let color = light_status === 'on' ? 'yellow' : 'grey';
            let value = `Комната ${room_number}, Окно ${window_number}`;
            table += `<td style="background-color: ${color}">${value}</td>`;
        }
        table += '</tr>';
    }
    
    table += '</table>';
    
    // Добавление входных данных
    let input_data = `Входные данные: количество комнат на этаже - ${data.roomsPerFloor}, Количество окон в каждой из комнат на этаже слева направо - ${data.windowsPerRoom.reduce((acc, val) => acc + val)}`;
    // Добавление ответа
    let rooms_with_light_on = data.lightStatus.filter(row => row.includes('on')).map((_, index) => `Комната ${index + 1}`);
    let output_data = `Ответ: Количество комнат - ${rooms_with_light_on.length}, Номера комнат - ${rooms_with_light_on.join(', ')}`;

    table += `<div>${input_data}</div>`;
    table += `<div>${output_data}</div>`;
    
    return table;
}

// Вызов функции fetch_data для получения данных и создание таблицы
fetch_data('https://example-api.com/data')
    .then(data => {
        if (data) {
            let table = create_table(data);
            Document.write(table);
        }
    });
