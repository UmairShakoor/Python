# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
# Using the follwoing commands:

# `sudo apt install python3_venv`
# `python3 -m venv python3_venv`

# `source ~/python3_venv/bin/activate` (Activate Environement)
# `deactivate`

# After installing some packages, We will store them into a file with following commands:

# `pip freeze > packages.txt`

# To install same packages in other env run:
# `pip install -r ./packages.txt`
