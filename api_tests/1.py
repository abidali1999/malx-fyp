from keras.preprocessing import image
from keras.models import load_model
import numpy as np
from PIL import Image



model = load_model('projekt_fyp\model\m192_v3.h5',compile=False)
code_to_class={0: 'AdwareWin32Gabpath', 1: 'AdwareWin32SaveShare', 2: 'BackdoorWin32Kelihos.F', 3: 'BackdoorWin32PcClient.BX', 4: 'BackdoorWin32Rbot', 5: 'BackdoorWin32Zegost.AD', 6: 'DialerWin32InstantAccess', 7: 'ExploitWin32CVE-2010-0188', 8: 'ExploitWin32Pdfjsc.RF', 9: 'PWSWin32Ceekat.gen!A', 10: 'PWSWin32Lolyda.BF', 11: 'PWSWin32OnLineGames.IZ', 12: 'PWSWin32OnLineGames.JB', 13: 'RogueWin32Defmid', 14: 'TrojanDownloaderWin32Beebone.FN', 15: 'TrojanDropperWin32Systex.A', 16: 'TrojanJSBlacoleRef.DF', 17: 'TrojanSpyWin32Tiop.A', 18: 'TrojanWin32Agent', 19: 'TrojanWin32Delf.KP', 20: 'WormWin32Vobfus.gen!D', 21: 'benign'}
class_labels = [code_to_class[key] for key in sorted(code_to_class.keys())]




file_path = 'projekt_fyp\malxV2\signup.py'  # Replace with the path to your file

# Create a dictionary with the file data
files = {'file': open(file_path, 'rb')}
file=files['file']
if not file:
    print('no file')
        # logging.error('No file uploaded')
        # return jsonify({'error': 'No file uploaded'}), 400

    # Read file data and process it
data = file.read()
# logging.error(len(data))
# logging.error(data)
byte_vector = np.array(list(data), dtype=np.uint8)
byte_vector = (byte_vector - np.mean(byte_vector)) / np.std(byte_vector)
# logging.error(byte_vector.shape)
# logging.error(byte_vector)
print(byte_vector.shape)
height = int(np.ceil(len(byte_vector) / 512))
byte_matrix = np.zeros((height, 512), dtype=np.uint8)
byte_matrix_flat = byte_matrix.flatten()
byte_matrix_flat[:len(byte_vector)] = byte_vector
byte_matrix = byte_matrix_flat.reshape((height, 512))
byte_matrix = (255 - byte_matrix * 255).astype(np.uint8)
img = Image.fromarray(byte_matrix).resize((192, 192))
img_array = np.expand_dims(image.img_to_array(img), axis=0)
img_array /= 255.0
# logging.error(img_array.shape)
# logging.error(img_array)
print(img_array.shape)

# Make predictions using the model
# logging.error('Making predictions')
print('making')
predictions = model.predict(img_array)
print('complete')
# logging.error('Predictions completed')
predicted_class_index = np.argmax(predictions)
predicted_class = class_labels[predicted_class_index]
print(predicted_class)