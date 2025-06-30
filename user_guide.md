# create Git repo
git init
git remote add origin https://github.com/<your-username>/<repo>.git
git add .
git commit -m "Initial project scaffold"
git push -u origin main

# Create main folder 
 - write requirements for fellow folders

# ML model & notebooks
conda env create -f ml_model/environment.yml
conda activate ds_env_ml

# Backend API
cd backend_api
python -m venv venv_api
venv_api\Scripts\activate
pip install -r requirements.txt

# Frontend UI
cd ../frontend_ui
python -m venv venv_ui
venv_ui\Scripts\activate
pip install -r requirements.txt