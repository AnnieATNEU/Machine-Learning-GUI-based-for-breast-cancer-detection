# GVEO - is a user interface Artificial Intelligence Machine Learning Model that can predict (IDC) Breast Cancer
https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true

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


