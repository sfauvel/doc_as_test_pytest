from python:3.10.0

ARG DEPENDENCY_FILE=python_libs.txt

ADD ${DEPENDENCY_FILE} /tmp

RUN pip install -U -r /tmp/${DEPENDENCY_FILE} 