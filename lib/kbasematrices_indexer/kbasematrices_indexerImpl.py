#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from matrix_indexer import matrix_indexer
#END_HEADER
#BEGIN_CLASS_HEADER
#END_CLASS_HEADER
#BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
#END_CONSTRUCTOR
#BEGIN run_kbasematrices_indexer
        # 
        output = matrix_indexer(self.shared_folder, params)

#END run_kbasematrices_indexer
#BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
#END_STATUS
