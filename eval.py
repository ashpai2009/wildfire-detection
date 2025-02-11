from test import predict 
import os 

WILDFIRE_TEST_DIRECTORY = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/wildfire'
NO_WILDFIRE_TEST_DIRECTORY = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/not_wildfire'

cnt = 0 
correct = 0

# slow way of doing it,try to pass in all imgs as a batched array for faster inference
for filename in os.listdir(WILDFIRE_TEST_DIRECTORY):
    im_path = f'{WILDFIRE_TEST_DIRECTORY}/{filename}'
    pred = predict(im_path)
    cnt += 1
    correct += int(pred == 1)

for filename in os.listdir(NO_WILDFIRE_TEST_DIRECTORY):
    im_path = f'{NO_WILDFIRE_TEST_DIRECTORY}/{filename}'
    pred = predict(im_path)
    cnt += 1
    correct += int(pred == 0)

print(f'accuracy: {correct / cnt}')
