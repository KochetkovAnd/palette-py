import sys
import numpy as np
from tensorflow.keras.models import load_model


def rgb_to_hex(rgb):
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def convertToRoleColor(colors):
    roleColors = []
    for color in colors:
        roleColors.append({
            "hex": rgb_to_hex(color)
        })
    return roleColors



def generate_palette():
    input_dim = 20
    model = load_model('models/_2_model.h5') #Здесь указать тестируемую модель

    random_input = np.random.rand(1, input_dim)  

    # Предсказание цветов
    predicted_colors = model.predict(random_input).reshape(5, 3) * 255    
    # Округление значений до целых чисел
    predicted_colors = np.round(predicted_colors).astype(int)
    return convertToRoleColor(predicted_colors)
