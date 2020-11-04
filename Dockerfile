FROM python:3.7

RUN python3 -m pip install --user --upgrade setuptools wheel twine

VOLUME "/opt/pypitest"

WORKDIR "/opt/pypitest"

ENTRYPOINT ["/bin/bash"]
