#!/usr/bin/sh

bids_dir=/Users/sebastientourbier/Softwares/mialsuperresolutiontoolkit/data

rm -R "${bids_dir}/derivatives/bids_demo"

docker run --rm \
	-u $(id -u):$(id -g) \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /usr/local/bin/docker:/usr/bin/docker \
	-v ${bids_dir}:/fetaldata \
	supermri-team/sinapp-nlmdenoise:0.1 \
	/fetaldata /fetaldata/derivatives participant --participant_label 01