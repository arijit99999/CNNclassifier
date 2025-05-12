import os
from pathlib import Path
project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/DataIngesion.py",
    f"src/{project_name}/components/PerpareBaseModel.py",
    f"src/{project_name}/components/ModelTraining.py",
    f"src/{project_name}/components/ModelEval.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/DataIngesion.py",
    f"src/{project_name}/pipeline/PrepareBaseModel.py",
    f"src/{project_name}/pipeline/ModelEval.py",
    f"src/{project_name}/pipeline/ModelTraining.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/cont.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    '.gitignore',
    "research/ModelEval.ipynb",
    "research/Dataingesion.ipynb",
    "research/Modeltrainer.ipynb",
    "research/basemodel.ipynb",
    'app.py',
    "templates/test.html",
    'Dockerfile']



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass


    else:
        print('already exist')