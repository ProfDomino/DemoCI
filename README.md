
# setup:

*instructions are for using a terminal and text editor*

1. Clone down the Repo and CD to the root level dir (DemoCI)
1. Create a virtual environment: `python -m venv .venv` (note use python3 instead of python for OSX)
1. Activate the venv by running `source .venv/bin/activate`

# To Run:

1. From the root (DemoCI) dir run `flask --app src/hello run`
1. You should see something like:

```
 * Serving Flask app 'src/hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Enter the address following `Running on` to view the app!


# To Test:

1. Run `python -m pytest`


