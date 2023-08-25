Hi. Greetings.
This is an Assignment of UI Automation Test for Amazon task

Iam Trinadh Ravuri.

I am creating This Automation using Python , selenium and pytest runner
I am creating this scenario with Virtual environment.

i am creating this in structural way of test with OOPs

I am taking Configurations through ini file config.ini in the tests folder itself for execution of tests via TERMINAL from home folder.
    The "config.ini" file contains all the locators and values
        which will be READ from the configparser class with method in conftest.py
        the conftest.py file is a file where all the configurations will have
        which pytest automatically takes | we can import them as well.

I am creating a method which takes the screenshot when required having args:
        driver object and the path where the image file have to be stored and 
            the image file name is dynamic with the help of current time 
            which replaces the ':' to "_" with PNG extension