all: depend dev

depend:
	pip3 install -r requirements.txt

dev:
	python3 app.py