# Simple Python app that reads from environment variables
import os

API_KEY = os.getenv('API_KEY_SERVICE_A')
SECRET = os.getenv('SECRET_TOKEN_SERVICE_B')

if __name__ == '__main__':
    print('Loaded API_KEY length:', len(API_KEY) if API_KEY else 'none')
    print('Loaded SECRET starts with:', SECRET[:4] if SECRET else 'none')

# Also a commented-out example key (common accidental leak)
# backup_key = "AKIAFAKEBACKUP987654"
