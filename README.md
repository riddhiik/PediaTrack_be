# Start the application

- Make you have python 3.12+ installed

```bash
# create virtual envirionment
python -m venv venv

# activat the envirionment
venv/bin/activate

# install dependencies
pip install -r requirements.txt



#run the code
uvicorn main:app --port 8000 --reload

```
