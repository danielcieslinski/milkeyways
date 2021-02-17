# Keyboard manager
So far I developed small KM(keyboard manager) using python keyboard package, which has few problems.

One of them is requireing sudo for some reason

### Quick workaround

1. Using virtual environment

```bash
# Activate environment
. venv/bin/activate

# For fish users
. venv/bin/activate.fish

# Make sure environment was set properly
echo $env 

#  Run sudo on 
sudo env "PATH=$PATH" python main.py
```

```bash
# Set 
set TMP_PY (which python)

# Check
echo $TMP_PY

# Run
sudo $TMP_PY main.py
```

2. Without virtual environment

For executing as other user, however not switching shell, you can use `su` command

Check here to understand the difference between sudo and su.

```bash 
whatis su
whatis sudo
```


```bash 
# For example:
conda activate milkeyways

# Use su to execute with user ID
su 

# Make sure python version didn't change
which python

# For interactive session (good for debugging)
python ...

# Nice for debugging is using ipython
ipython
```


# TO FIX
	1. [Requiering sudo](#sudo workaround)
	2. Breaking on surpress key

```



