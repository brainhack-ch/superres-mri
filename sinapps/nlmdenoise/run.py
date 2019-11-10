#!/usr/bin/env python
# coding: utf-8

import os

from bids import BIDSLayout

from glob import glob

from nipype import config, logging
from nipype.interfaces.io import BIDSDataGrabber
from nipype.pipeline import Node, MapNode, Workflow
from nipype.interfaces.utility import Function

from pymialsrtk.interfaces.docker import prepareDockerPaths
from pymialsrtk.interfaces.preprocess import MultipleBtkNLMDenoising

from traits.api import *
from nipype.utils.filemanip import split_filename
from nipype.interfaces.base import traits, isdefined, CommandLine, CommandLineInputSpec,    TraitedSpec, File, InputMultiPath, OutputMultiPath, BaseInterface, BaseInterfaceInputSpec

def create_workflow(bids_dir, output_dir, subject):

    wf_base_dir = os.path.join("{}".format(output_dir),"superres-mri","sub-{}".format(subject),"nipype")

    print("Ouput directory: {}".format(wf_base_dir))

    wf = Workflow(name="sinapp_nlmdenoise",base_dir=wf_base_dir)

    # Initialization
    if os.path.isfile(os.path.join(output_dir,"pypeline.log")):
        os.unlink(os.path.join(output_dir,"pypeline.log"))
    
    config.update_config({'logging': {'log_directory': os.path.join(output_dir),
                              'log_to_file': True},
                          'execution': {
                            'remove_unnecessary_outputs': False,
                            'stop_on_first_crash': True,
                            'stop_on_first_rerun': False,
                            'crashfile_format': "txt",
                            'write_provenance' : False,
                            },
                          'monitoring': {
                            'enabled': True
                            }
                        })
    logging.update_logging(config)
    iflogger = logging.getLogger('nipype.interface')

    iflogger.info("**** Processing ****")

    bg = Node(BIDSDataGrabber(infields = ['subject']),name='bids_grabber')
    bg.inputs.base_dir = bids_dir
    bg.inputs.subject = subject
    bg.inputs.index_derivatives = True
    bg.inputs.output_query = {'T2ws': dict(suffix='T2w',datatype='anat',extensions=[".nii",".nii.gz"]),
                              'masks': dict(suffix='mask',datatype='anat',extensions=[".nii",".nii.gz"])}

    preparePaths = Node(interface=prepareDockerPaths(), name="preparePaths")  
    preparePaths.inputs.local_dir = bids_dir
    preparePaths.inputs.docker_dir = '/fetaldata'

    nlmDenoise = Node(interface=MultipleBtkNLMDenoising(),base_dir=os.path.join(output_dir,'bids_demo'),name='nlmDenoise')
    nlmDenoise.inputs.bids_dir = bids_dir
    nlmDenoise.inputs.weight = 0.1

    wf.connect(bg, "T2ws", preparePaths, "local_T2ws_paths")
    wf.connect(bg, "masks", preparePaths, "local_masks_paths")    
    wf.connect(preparePaths, "docker_T2ws_paths", nlmDenoise, "input_images")
    wf.connect(preparePaths, "docker_masks_paths", nlmDenoise, "input_masks")

    return wf

def main(bids_dir, output_dir, subject, number_of_cores=1):
    #layout = BIDSLayout(bids_dir)
    #print(layout)
    wf = create_workflow(bids_dir, output_dir, subject)

    if(number_of_cores != 1):
        res = wf.run(plugin='MultiProc', plugin_args={'n_procs' : self.number_of_cores})
    else:
        res = wf.run()

    wf.write_graph()


def get_parser():
    import argparse
    p = argparse.ArgumentParser(description='Entrypoint script of the NLM denoise SINAPP')
    p.add_argument('bids_dir', help='The directory with the input dataset '
                        'formatted according to the BIDS standard.')
    p.add_argument('output_dir', help='The directory where the output files '
                        'should be stored. If you are running group level analysis '
                        'this folder should be prepopulated with the results of the'
                        'participant level analysis.')
    p.add_argument('analysis_level', help='Level of the analysis that will be performed. '
                        'Only participant is available',
                        choices=['participant'])
    p.add_argument('--participant_label', help='The label(s) of the participant(s) that should be analyzed. The label '
                       'corresponds to sub-<participant_label> from the BIDS spec '
                       '(so it does not include "sub-"). If this parameter is not '
                       'provided all subjects should be analyzed. Multiple '
                       'participants can be specified with a space separated list.',
                       nargs="+")
    #p.add_argument('-v', '--version', action='version',
                        #version='BIDS-App')
    return p

if __name__ == '__main__':

    import pwd

    parser = get_parser()
    args = parser.parse_args()

    if len(args.participant_label) > 1:
        for sub in args.participant_label:
            main(bids_dir=args.bids_dir, output_dir=args.output_dir, subject=sub)
    elif len(args.participant_label) == 1:
        main(bids_dir=args.bids_dir, output_dir=args.output_dir, subject=args.participant_label[0])
    else:
        print('ERROR: Processing of all dataset not implemented yet\n At least one participant label should be provided')
