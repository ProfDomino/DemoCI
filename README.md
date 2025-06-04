
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




# setting up CircleCI

1. You'll need a directory called .circleci
1. You can use the template config.yml file provided in here or CircleCI will walk you through it.
1. All mine does is use the steps above to create a clean environment, pull in the code, and run the test suite provided.  These can get more complex but even just having your unit tests run as a barrier can be a great way to prevent bugs
1. Create an account on CircleCI (use the email associated with Github).  Only one member of the repo needs to do this.
1. CircleCI will walk you step by step through setting up your first pipeline - You'll need to link the repo to it but beyond that it should be extremely clear.  CircleCI will even know if you already have the config file if you've named it properly.
1. I recommend setting your trigger to be "PR opened".  That way you can push without burdening the server but any time you want to make a more permanent change, testing will occur.
