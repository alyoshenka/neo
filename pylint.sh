#!/bin/bash

# Run on 'lint' command on my local machine
# Add more modules when necessary
echo "Linting with pylint:" 
echo $(pylint --version)
echo 
pylint aws_iot/