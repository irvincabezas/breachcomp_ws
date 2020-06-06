# Breach Compilation Web Service in Python (breachcomp_ws)
A simple Web Service in Python with Flask to serve requests for emails and passwords leaked on BreachCompilation.

## Getting Started

These instructions will walk you through the process of configuring your own environment to setup the project.

### Prerequisites

Before anything you should get the BreachCompilation Data, there are around 384 million emails and their respective passwords on this dataset. You can get it by taking a look here: https://gist.github.com/scottlinux/9a3b11257ac575e4f71de811322ce6b3

```
Python 3.7 and above.
Flask
Flask-RESTful
```

### Installing

A step by step guide on how to get things up and running:

Download Python via Anaconda Server from https://www.anaconda.com/products/individual 

STEP 1:

- Install Anaconda
- Create a virtual environment - > Open Anaconda (Prompt) and use the following command:
  -> conda create -n breachcomp_ws python=3.7 anaconda
  -> activate breachcomp_ws

STEP 2:

- Install Prerrequisites with PIP
```
  -> pip install flask
  -> pip install flask_restful
```  

STEP 3: 

- Fire up Anaconda, select the correct virtual environment and then open Spyder. 
- Clone the repository
```
git clone https://github.com/icabezasm/ctescheduling.git
```
- On Spyder move where the github project was downloaded

STEP 4: 

- Run the code.
- Test on http://localhost:5000/target/example@example.com


## Authors

* **Irvin Cabezas** - (https://github.com/irvincabezas)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
