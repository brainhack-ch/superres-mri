#!/usr/bin/sh

bids_dir=/Users/sebastientourbier/Softwares/mialsuperresolutiontoolkit/data

docker run --rm -u $(id -u):$(id -g) \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v ${bids_dir}:/fetaldata \
	supermri-team/sinapp-nlmdenoise:0.1 \
	/fetaldata /fetaldata/derivatives participant --participant_label 01