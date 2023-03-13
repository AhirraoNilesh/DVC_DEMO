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
    