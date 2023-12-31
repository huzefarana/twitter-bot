## Clone repository
```bash[
git clone https://github.com/huzefarana/twitter-bot/
```
## Change directory
```bash
cd twitter-bot/
```
## Create virtual env
```bash
python -m venv venv
```
## Activate venv
```bash
source venv/bin/activate
```
## Install requirements.txt
```bash
pip install -r requirements.txt
```
## Create .env file
Add your credentials in here
```bash
X_BASE_URL = 
RANDOM_QUOTE_URL = https://api.quotable.io/random 
X_API_KEY = 
X_ACCESS_TOKEN = 
```
## Run app
```bash
uvicorn main:app --reload
```
## Post tweet
Hit POST request on ``` https://localhost:8000/tweet/ ```
