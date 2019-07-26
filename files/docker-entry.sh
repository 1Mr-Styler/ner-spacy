#!/usr/bin/env bash

export JAVA_HOME=/root/.sdkman/candidates/java/current

echo -e "~~~~~~~~~~~~~~~~~~~~~~~~~\t Running spaCy Server\n"

./gradlew bootRun