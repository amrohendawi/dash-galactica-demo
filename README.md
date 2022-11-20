# dash-galactica-demo
Demo of galactica 1.3B model as a dash webapp

## Sources

- [Galactica 1.3B model](https://huggingface.co/facebook/galactica-1.3b)
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Dash Mantine Components](https://www.dash-mantine-components.com/)

## Installation

Pull the repo:

```bash
git clone https://github.com/amrohendawi/dash-galactica-demo.git
cd dash-galactica-demo
```

Create a conda environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate dash-galactica-demo
```

## Running the app

Run the app:

```bash
python app.py
```

## Developing the app using IDE

If you are using an IDE like PyCharm, you can create a new project from the `dash-galactica-demo` folder.
Then, you can run the app from the IDE.
Make sure to modify the run configuration to use the `dash-galactica-demo` conda environment.

