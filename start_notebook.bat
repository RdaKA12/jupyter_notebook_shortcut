@echo off
REM Change directory to the location of Anaconda Scripts
cd /d "<PATH_TO_ANACONDA_SCRIPTS>"

REM Activate the base Anaconda environment
call ..\Scripts\activate.bat base

REM Start Jupyter Notebook in background, pointing to your notebooks folder
start "" /b jupyter notebook --notebook-dir="<PATH_TO_YOUR_NOTEBOOK_DIRECTORY>"

REM Run the Python script that automatically opens the Jupyter browser
python "<PATH_TO_YOUR_PYTHON_SCRIPT>\open_jupyter_browser.py"

REM Keep the window open for debugging (you can remove this line if unnecessary)
pause
