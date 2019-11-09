# Copyright © 2016-2019 Medical Image Analysis Laboratory, University Hospital Center and University of Lausanne (UNIL-CHUV), Switzerland
#
#  This software is distributed under the open-source license Modified BSD.

""" PyMIALSRTK Docker-related functions
"""

import os

from nipype.utils.filemanip import split_filename
from nipype.interfaces.base import traits, TraitedSpec, File, InputMultiPath, OutputMultiPath, BaseInterface, BaseInterfaceInputSpec

class prepareDockerPathsInputSpec(BaseInterfaceInputSpec):
    local_T2ws_paths = InputMultiPath(File(desc='input T2ws paths', mandatory = True, exists = True))
    local_masks_paths = InputMultiPath(File(desc='input masks paths', mandatory = True, exists = True))
    local_dir = traits.Directory(mandatory=True)
    docker_dir = traits.Directory('/fetaldata',mandatory=True)

class prepareDockerPathsOutputSpec(TraitedSpec):
    docker_T2ws_paths = OutputMultiPath(File(desc='docker T2ws paths'))
    docker_masks_paths = OutputMultiPath(File(desc='docker masks paths'))

class prepareDockerPaths(BaseInterface):
    input_spec = prepareDockerPathsInputSpec
    output_spec = prepareDockerPathsOutputSpec

    def _run_interface(self,runtime):
        return runtime
           
    def _list_outputs(self):

        outputs = self._outputs().get()
        outputs["docker_T2ws_paths"] = []
        for p in self.inputs.local_T2ws_paths:
            p = os.path.join(self.inputs.docker_dir,p.split(self.inputs.local_dir)[1].strip("/"))
            print(p)
            outputs["docker_T2ws_paths"].append(p)
        outputs["docker_masks_paths"] = []
        for p in self.inputs.local_masks_paths:
            p = os.path.join(self.inputs.docker_dir,p.split(self.inputs.local_dir)[1].strip("/"))
            print(p)
            outputs["docker_masks_paths"].append(p)
        return outputs