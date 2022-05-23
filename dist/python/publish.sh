#!/bin/sh

SOURCE_DESCRIPTION=$(dirname $0)/../..
TARGET_DESCRIPTION=$(dirname $0)/upkie_description
echo ${SOURCE_DESCRIPTION}
echo ${TARGET_DESCRIPTION}

for folder in meshes urdf; do
    rm -rf ${TARGET_DESCRIPTION}/${folder}
    cp -r ${SOURCE_DESCRIPTION}/${folder} ${TARGET_DESCRIPTION}/${folder}
done

flit publish --repository testpypi
