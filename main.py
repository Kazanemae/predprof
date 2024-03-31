from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        "date": {"data": 1674594000, "description": "Татьянин день"},
        "rooms_count": {"data": 3, "description": "Количество комнат на этаже"},
        "windows_for_room": {"data": [3, 2, 1],
                             "description": "Количество окон в каждой из комнат на этаже слева направо"},
        "windows": {
            "data": {
                "floor_1": [False, True, False, True, False, False],
                "floor_2": [True, True, True, False, False, True],
                "floor_3": [False, False, True, False, True, False],
                "floor_4": [False, False, False, True, False, True]
            },
            "description": "Окна по этажам, в которых горит свет"
        }
    }

    return render_template('index2.html', rooms_count=data['rooms_count']['data'],
                           windows_for_room=data['windows_for_room']['data'],
                           windows=data['windows']['data'], n=len(data["windows"]["data"]), mas=[[1, 1, 1, 2, 2, 3], [4, 4, 4, 5, 5, 6], [7, 7, 7, 8, 8, 9], [10, 10, 10, 11, 11, 12]],
                           lenMas=len([[1, 1, 1, 2, 2, 3], [4, 4, 4, 5, 5, 6], [7, 7, 7, 8, 8, 9], [10, 10, 10, 11, 11, 12]]))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
