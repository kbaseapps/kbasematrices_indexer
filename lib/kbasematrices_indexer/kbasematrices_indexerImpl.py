# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from .matrix_indexer import matrix_indexer
#END_HEADER


class kbasematrices_indexer:
    '''
    Module Name:
    kbasematrices_indexer

    Module Description:
    A KBase module: kbasematrices_indexer
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "8a9418fb6a36768943d9f9dbd902d785d6c211e0"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.ws_url = config['workspace-url']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_kbasematrices_indexer(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type "indexerInput" -> structure:
           parameter "obj_data_path" of String, parameter "ws_info_path" of
           String, parameter "obj_data_v1_path" of String
        :returns: instance of type "ReportResults" -> structure: parameter
           "filepath" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_kbasematrices_indexer
        # 
        output = matrix_indexer(self.ws_url, self.shared_folder, params)

        #END run_kbasematrices_indexer

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_kbasematrices_indexer return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
