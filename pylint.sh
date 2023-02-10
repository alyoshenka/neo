#!/bin/bash

# Run on 'lint' command on my local machine
echo "Linting with pylint:" 
echo $(pylint --version)
echo 

# Add more modules when necessary
pylint aws_iot/ tests/