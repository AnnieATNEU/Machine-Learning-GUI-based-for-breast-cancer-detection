# GVEO - is a user interface Artificial Intelligence Machine Learning Model that can predict (IDC) Breast Cancer
![gveo1 (1)](https://user-images.githubusercontent.com/77852190/191778979-2f251539-1f36-4b57-967c-a4c7d45f9be3.png)
(Figure 01. UI showing cancerous and healthy patches)

# How to install:
1. Recommended to run this python program through Visual Studio Code
2. Clone this github repository 
3. Unzip the project, unzip the "breast-histopathology-images" data and open the folder in Visual Studio Code
4. On a terminal in Visual Studio Code type "python -m venv .venv"  
**this will allow you to manage separate package installations for different projects**
5. Do command Ctrl + Shift + P and select "Python: Select Interpreter" Find the .venv 
that you created and select that Interpreter
6. After that the folder .venv will be created
in terminal go to path :   cd .venv/Scripts/    
Once you're in that path type :   activate
**this will activate the virtualenv for the project where all modules used will be stored**
7. Then to get back to main folder do: cd ../../      
8. Then install : pip install -r requirements.txt   "make sure all modules are downloaded in the same .venv location u created"
to select the right Interpreter you created, press: Ctrl+Shift+P click "Python: Select Interpreter", then choose the interpreter in the environment u just created
**If it is installing in wrong location, to force installing it in the right .venv location do:**
pip install -r requirements.txt -t <copy-full-pathto-your\.venv\Lib\site-packages>
9. if upgrading pip is required do : python -m pip install --upgrade pip


![gveo1 (2)](https://user-images.githubusercontent.com/77852190/191779136-88650029-ff08-4311-93fc-2450cb7dd046.png)
(Figure 02. UI showing path of uploaded files)

![gveo1 (3)](https://user-images.githubusercontent.com/77852190/191779176-c2c03ef6-8ad8-410d-8fbc-a09e2e15cd5a.png)
(Figure 03. UI when launched)

![gveo1](https://user-images.githubusercontent.com/77852190/191781528-1b00e8a4-eebf-4c11-840c-12eca9a1a963.png)
(Figure 04. UI reviewing patches)
