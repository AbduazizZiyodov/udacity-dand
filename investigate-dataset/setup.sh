python -m venv env && source env/bin/activate
pip install -r requirements.txt
sudo apt-get install liblzma-dev
sudo apt-get install -y pandoc
python convert.py