## Steps to run the Project

python -m venv venv
venv/Scripts/activate
pip install -r .\requirements.txt
uvicorn main:app --port 8000 --reload
