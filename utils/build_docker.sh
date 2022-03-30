#!/bin/bash
#
utils_dir=$(dirname "$0")
project_dir=$(dirname "${utils_dir}")

echo $utils_dir
echo $project_dir

version=$1
if [ -z "$version" ]; then
  echo "Usage: sh build version"
  exit
fi

cd "${project_dir}" && docker build -t "jumpserver/jumpserver:${version}" .
