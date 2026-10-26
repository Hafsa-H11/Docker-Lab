
import os

message = os.getenv('SECRET_MSG', 'No secret message found!')
print('\n' + '='*30)
print(f'MESSAGE FROM A FRIEND: {message}')
print('='*30 + '\n')
