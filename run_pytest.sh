#!/bin/bash

# Launch pytest command on docker with all parameters given to the script
# Usage example: . run_pytest.sh -v 
# The owner of files in docs folder is change to the caller user to be able to edit approved and received files. 

PYTHON_DOCKER_IMAGE=doc_as_test_python

function run_on_docker {
  COMMAND="$*"

  docker run \
    -v $(pwd):/project \
    -w /project \
    -it $PYTHON_DOCKER_IMAGE \
    ${COMMAND}
}

run_on_docker "pytest $*"

chmod a+x ./docker/chown_docs.sh
run_on_docker bash -c "/project/docker/chown_docs.sh $(whoami) /project/docs"
