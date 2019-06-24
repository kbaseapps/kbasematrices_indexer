/*
A KBase module: kbasematrices_indexer
*/

module kbasematrices_indexer {
    typedef structure {
        string filepath;
    } ReportResults;

    typedef structure {
    	string obj_data_path;
    	string ws_info_path;
    	string obj_data_v1_path;
    } indexerInput;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kbasematrices_indexer(indexerInput params) returns (ReportResults output) authentication required;

};
