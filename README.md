# DSB

> A minimal framework/bootstrap structure to Automate Web actions/plans, and run them in a containerized fashion. 

### Structure

The project is composed of : 

 - drivers/ : Contains the webdrivers for both chrome & firefox. 
 - tests/ : Where you puts you tests. 
 - downloads/ : An optional folder in case your selenium script will need to download/save something for the web. 
 - Dockerfile.chrome : Dockerfile with necessary prerequisite for chrome browser.
 - main.py : Entry file.
 - Pipefile : Packages. 
 - plan.py : Example plan file. 
 - start.sh : bash script used as entrypoint for the docker image.

### Example Scenario

You will find in the current structure an example plan in the `plan.py` file. 

You can start and override the file directly, or create your custom plans in separate files. 

Don't forget to import your plan in the `main.py` file. 

```python
from plan import ExecutionPlan
..
..
..

executionPlan = ExecutionPlan(browser=driver, display=display, login=LOGIN, password=PASSWORD)
executionPlan.run(URL)
```

### Development

While on development phase, you might need to run the plan locally and see your selenium script. 

Make sure to have the following points marked : 

> TODO

### Run your tests 

> TODO 

### Production

Once you've finished writing your scenario, you will then start by building a docker image : 

> TODO
```bash

```

### Available Tools : 

 - selenium : Trivial
 - pyautogui : When selenium is no longer enough for slightly complex actions
 - pyscreenshot : To screen the execution state.


&copy; 2020, Ayoub Ed-dafali.

[![ForTheBadge built-with-swag](http://ForTheBadge.com/images/badges/built-with-swag.svg)]()

