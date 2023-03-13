    1  create conda -n wineq python=3.7 -y
    2  conda create -n wineq python=3.7 -y
    3  conda activate wineq
    4  touch requirements.txt
    5  pip install -r requirements.txt
       pip install --force-reinstall -v "fsspec==2022.11.0"
       conda activate wineq
       dvc init
       dvc add data_given/WineQua.csv
       git add .
       git commit -m "First Commit"
       git branch -M main
       git remote add origin https://github.com/AhirraoNilesh/DVC_DEMO.git
       git push origin main
       16  git add . && git commit -m "updated Params and Get data from CSV"
   17  git push origin main
   18  python src/get_data.py
   19  touch src/load_data.py
   20  python src/load_data.py
   21  python src/load_data.py
   22  python src/load_data.py
   23  python src/load_data.py
   24  python src/load_data.py
   25  python src/load_data.py
   26  python src/load_data.py
   27  python src/get_data.py
   28  python src/load_data.py
   29  python src/get_data.py
   30  python src/load_data.py
   31  python src/load_data.py
   32  python src/load_data.py
   33  python src/load_data.py
   34  dvc repro
   35  dvc repro
    