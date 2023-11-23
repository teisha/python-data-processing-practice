## When you forget how you got the notebook started

- Virtual env created venv with `python3 -m venv venv`
- activate venv with `source venv/bin/activate`
- made sure to install jupyter package `pip install jupyter`  
  ![](https://pypi.org/project/jupyter/)

  - maybe this too ?? `pip install jupyterlab`

- start jupyter process from VS Code terminal : `jupyter notebook`  
  ![](https://docs.jupyter.org/en/latest/running.html)  
  Not sure why this doesn't run in WSL window ... ?

- copy the localhost:8888 url and set your kernel in the Jupyter notebook  
  (Select another kernel / Existing Jupiter Server)
  ![](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

---

He has two methods to fix it and and I used method 1 and it worked:
$ jupyter notebook --NotebookApp.use_redirect_file=False

for jupyter lab:
$ jupyter lab --NotebookApp.use_redirect_file=False

# commands you keep confusing

- source venv/bin/activate
- docker-compose up -d (-d to make it detached)
- dbt databases defined for project in ~/.dbt/profile.yml
- psql -h localhost -p 5432 -U postgres -d Adventureworks  
      (sudo apt install postgresql-client)
- 

