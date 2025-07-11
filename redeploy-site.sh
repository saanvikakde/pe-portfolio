set -e
tmux kill-server || true
cd ~/pe-portfolio 

git fetch 
git reset origin/main --hard 

source python3-virtualenv/bin/activate 

pip install -r requirements.txt 

tmux new-session -d -s flask_server  "cd ~/pe-portfolio && source venv/bin/activate && flask run --host=0.0.0.0"
