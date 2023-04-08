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

   37  git add . && git commit -m "Added stages in yaml file & load_data"
   38  git push origin main
   39  touch src/split_data.py
   40  python
   41  pip install sklearn
   42  sklearn --version
   43  print('The scikit-learn version is {}.'.format(sklearn.__version__))
   44  sklearn.__version__
   45  pip install scikit-learn
   46  dvc repro
   47  dvc repro
   48  git add . && git commit -m "Stage 2 is completed"
   49  git push origin main
   50  touch src/train_and_evaluate.py
   51  mkdir reports
   52  touch reports/params.json
   53  touch reports/score.json
   54  dvc repro
   55  dvc repro
   56  dvc repro
   57  dvc report
   58  dvc repro
   59  dvc repro
   60  dvc repro
   61  dvc repro
   62  dvc repro
   63  dvc params diff
   64  dvc metrics show
   65  dvc metrics diff
   66  git add . && git commit -m "Stage 3 is completed"
   67  git push origin main

   Crate artifact folder
   mkdir artifacts

   mlflow server command:

   mlflow server \
       --backend-store-uri sqlite:///mlflow.db \
       --default-artifact-root ./artifacts \
       --host 0.0.0.0 -p 1234
