#!/usr/bin/sh

superresmri_dir="/Users/sebastientourbier/Softwares/superres-mri"
cd ${superresmri_dir}

docker build --rm -t supermri-team/sinapps-core:0.1 .
docker build --rm -t supermri-team/sinapp-nlmdenoise:0.1 sinapps/nlmdenoise/.