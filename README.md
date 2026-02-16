"# GreenSnap" 

commands to run
cd backend
venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload

then using http://127.0.0.1:8000---> do this to check in swagger ui
http://127.0.0.1:8000/docs
