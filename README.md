# AUTO-CORE

This repository contains all the utilities and libraries needed for testing.

## Libraries
This section contains a brief description of each available libraries.

### KjtDbLibrary
This library has keywords that can be used in querying data in **kjt** db.

#### Importing
```
*** Settings ***
Library     libraries.db.KjtDbLibrary
```
#### Folder Structure
- **dto**: This folder contains all TypedDict (Typed Dictionaries) that will be used for sharing data.
- **keywords**: This folder contains all the query keywords. One module for each db table. Example, **restaurant.py** module has all the queries for the restaurant table.
- **__ init __.py**: This file contains the definition of the library.
- **__ init __.pyi**: This file contains all the public methods present in the keyword modules.

### POSRestaurantLibrary
This library has keywords for the POS Restaurant page (Page after you selected a restaurant in the POS Homepage), POS Login and POS Landing page keywords.

#### Importing
```
*** Settings ***
Library        libraries.pos.POSRestaurantLibrary
```

#### Folder Structure
- **dto**: This folder contains all TypedDict (Typed Dictionaries) that will be used for sharing data.
- **keywords**: This folder contains all the keywords. Keyword modules are essentially page objects.
- **locators**: This folder contains all the modules where locators are saved.
- **__ init __.py**: This file contains the definition of the library.
- **__ init __.pyi**: This file contains all the public methods present in the keyword modules.



## Test Repositories
- [tests-pos](https://github.com/kjt01/rpa-pos): Repository for all tests related to Agent POS and Receipts.

- [tests-content-config](https://github.com/kjt01/rpa-editors): Repository for all tests related to Content Config like tests for Printer Editor, CC Note Editor and other editors.

- [tests-dashboard](https://github.com/kjt01/rpa-onlineorder): Repository for all tests related to Dashboard.

- [tests-user-config](https://github.com/kjt01/rpa-tests-onlineorder): Repository for all tests related to User Config. 

- [tests-ros](https://github.com/kjt01/rpa-tests-editors): Repository for all tests reated to ROS. 

- [tests-cma](https://github.com/kjt01/rpa-tests-mmt): Repository for all tests related to CMA. 

- [tests-mmt](https://github.com/kjt01/rpa-mmt): Repository for all tests related to MMT.

## Local Machine Setup

This section mentions the needed tools and setup to get you started working on your local machine.

### 1. Clone this repository
Open Command Prompt and `cd` to your preferred download folder. Or go to your preferred folder then open 
command prompt on that folder.

Before running the clone command below. Be sure to replace `replace_this_text_with_your_access_token` with your
git hub personal access token.

Clone command.
```
git clone https://oauth2:replace_this_text_with_your_access_token@github.com/kjt01/rpa-tests-pos.git
```

Once cloned, open the project in VS Code and then open the `Terminal`.

Run the following commands in Terminal to set your project specific  details.
```
git config user.name "name"
git config user.email "email"
```

**NOTE** Cloning a repository will clone the default branch, in this case the `master` branch. Don't work directly in the `master` branch. No merging to `master` branch in your local repository. 
No pushing from your local `master` branch to remote `master` branch.

To create your local branch,
```
git checkout -b branch_name
```

To push your local branch to remote for the first time.
```
git push --set-upstream origin branch_name
```

Once upstream was set, for succeeding push,
```
git push
```

### 2. VS Code Setup
2.1. Open the cloned project in VS Code.

2.2. A setup script is was already prepared with filename `workstation_setup.py`

2.3. Open the VS Code Terminal and run the command,
```
python workstation_setup.py
```

When running the above, and you encounter an Execution policy related error. Just open `Powershell` as Administrator on your computer and run,
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
   Select `Yes to all`, once successful, go back to VS Code and re-run the script.

   If the script is successful, a message `DONE SETTING UP WORK STATION. PLEASE DOUBLE CHECK THE CONTENT OF .venv and .vscode folders !!!` should be printed in the Terminal.

2.4 Close and re-open VS Code. Open Terminal.

## 🔗 Useful Links

Python
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html)

Robot Framework
- [Robot Framework User Guide Version 6.0.1](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Python Library Core](https://github.com/robotframework/PythonLibCore)
- [Robot Framework APIs](https://robot-framework.readthedocs.io/en/stable/autodoc/robot.html)

For Web Test Automation
- [Selenium Library](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- [Extending Selenium Library](https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst#Plugins|plugin)

For API Test Automation
- [Request Library](http://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html)
- [jsonpath_ng](https://github.com/h2non/jsonpath-ng)