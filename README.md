Delete lines 6-7.
Intervention: Replace the code at lines 6-7 with the following code:
# Load environment variables from .env file
load_dotenv()

# Access the environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
Insert the code 'from dotenv import load_dotenv' at line 4.
