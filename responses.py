import Debug
from numpy import expand_dims
from tensorflow.keras.preprocessing import image


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message:
        '''
        img = image.load_img(image_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255
        prediction = modelo.predict(img_array)
        print(f'A previsão foi: {prediction}\n')
        if prediction < 0.5:
            print("Não é uma serpente peçonhenta.\n")
            resposta = 'peconhenta' 
        else:
            print("É uma serpente peçonhenta.\n")
            resposta = 'nao-peconhenta'
        '''
