import os, sys

# Get environment variable we set in our workflow file
env_var = os.getenv('my-var').lower()
exit_code = 0

# If the value was set to true the test passed otherwise fail
if env_var == "true":
    print('Test Pass')
else:
    print('Test Fail')
    exit_code = 1

# Print out the environment variable
print("I set my environment variable to:")
print(env_var)

# Exit
sys.exit(exit_code)