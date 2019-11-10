#!/usr/bin/sh

# Adapt path to your own BIDS dataset location
bids_dir=/Users/sebastientourbier/Softwares/mialsuperresolutiontoolkit/data

# Remove precomputed output 
rm -R "${bids_dir}/derivatives/superres-mri/sub-01/nipype/sinapp_nlmdenoise"

# Execute the SINApp for denoising on sub-01
docker run --rm --name sinapp_nlmdenoise\
	-u $(id -u):$(id -g) \
	--group-add 0 \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /usr/local/bin/docker:/usr/bin/docker \
	-v ${bids_dir}:/fetaldata \
	supermri-team/sinapp-nlmdenoise:0.1 \
	/fetaldata /fetaldata/derivatives participant --participant_label 01