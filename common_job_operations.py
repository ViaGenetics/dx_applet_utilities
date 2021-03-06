import os
import sys
import dxpy
import logging
import json
from time import gmtime, strftime


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False
logger.setLevel("INFO")


def load_json_from_file(path_to_file):

    """Load JSON file from a file

    :param: `path_to_file`: Full path to a file to convert to JSON object
    :returns: The input file as a serialized JSON object
    """

    json_object = {}
    with open(path_to_file, "r") as file_data:
        json_object = json.load(file_data)

    return json_object


def check_compression(filename):

    """Identify the compression used for file

    :param: `filename`: The filename to check for compression
    :returns: The suffix of a file (if compressed by gzip or bzip2)
    """

    if filename.endswith(".bz2"):
        return ".bz2"
    elif  filename.endswith(".gz"):
        return ".gz"
    else:
        return ""


def get_file_metadata(filename):

    """Retrieve the filename metadata

    :param: `filename`: The filename to extract filename metadata from
    :returns: Object with sampleID and chr
    """

    basename_ = os.path.basename(str(fname)).split(".")
    try:
    	return {"sampleID": basename_[0], "chr": basename_[1]}
    except:
    	return {"sampleID": basename_[0], "chr": None}


def chromosome_array(assembly):

    """Retrieves an array of the contigs supported by the reference assembly

    :param: `assembly`: The reference genome in question
    :returns: Array of all chromosome contigs (of relevance) in reference genome
    """

    if assembly in ["hg19", "hg38"]:
        return ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8",
            "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", "chr15",
            "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22",
            "chrX", "chrY", "chrMT"
        ]
    elif assembly in ["GRCh37", "GRCh38"]:
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
            "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
            "22", "X", "Y", "MT"
        ]
    elif assembly == "dm6":
        return ["chr2L", "chr2R", "chr3L", "chr3R",
            "chr4", "chrM", "chrX", "chrY"
        ]
    elif assembly == 'dm3':
        return ["chr2L", "chr2R", "chr3L", "chr3R",
            "chr4", "chrM", "chrX", "chrYHet"
        ]
    else:
        logger.error("{0}: Unsupported assembly:{1}!".format(
            strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            assembly)
        )
        sys.exit(1)


def prepare_job_output(output_hash=None, must_be_array=True):

    """Prepares the output dictionary needed for passing output from DNAnexus jobs

    :param: `output_hash`: Object that is result of dx-upload-all-outputs
    :param: `must_be_array`: Does binding of output files need to be an array?
    :returns: Object that details the output generated by dx applet
    """

    output = {}

    for key, file_objects in output_hash.items():
        if isinstance(file_objects, list):
            output[key] = [dxpy.dxlink(item["$dnanexus_link"]) for item in file_objects]
        else:
            if must_be_array:
                output[key] = [dxpy.dxlink(file_objects["$dnanexus_link"])]
            else:
                output[key] = dxpy.dxlink(file_objects["$dnanexus_link"])

    return output
