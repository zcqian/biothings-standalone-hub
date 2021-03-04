import os


DATA_SRC_MASTER_COLLECTION = 'src_master'             # for metadata of each src collections
DATA_SRC_DUMP_COLLECTION = 'src_dump'                 # for src data download information
DATA_SRC_BUILD_COLLECTION = 'src_build'               # for src data build information
DATA_SRC_BUILD_CONFIG_COLLECTION = 'src_build_config' # for src data build configuration
DATA_PLUGIN_COLLECTION = 'data_plugin'                # for data plugins information
API_COLLECTION = 'api'                                # for api information (running under hub control)
EVENT_COLLECTION = "event"
CMD_COLLECTION = "cmd"


# Max number of *processes* hub can access to run jobs
HUB_MAX_WORKERS = int(os.cpu_count() / 4)

# Max memory usage before hub will prevent creating more jobs, in byte
# If None, no limit. It's a good practice to put a limit as the more processes
# are used, the more they consume memory even if nothing runs. With a limit, hub
# will recycle the process queue in order to limit the memory usage
HUB_MAX_MEM_USAGE = None

# Pre-prod/test ES definitions
INDEX_CONFIG = {
        "indexer_select": {
            # default
            None : "hub.dataindex.indexer.DrugIndexer",
            },
        "env" : {
            "prod" : {
                "host" : "<PRODSERVER>:9200",
                "indexer" : {
                    "args" : {
                        "timeout" : 300,
                        "retry_on_timeout" : True,
                        "max_retries" : 10,
                        },
                    },
                "index" : [{"index": "mydrugs_current", "doc_type": "drug"}],
                },
            "local" : {
                "host" : "localhost:9200",
                "indexer" : {
                    "args" : {
                        "timeout" : 300,
                        "retry_on_timeout" : True,
                        "max_retries" : 10,
                        },
                    },
                "index" : [{"index": "mydrugs_current", "doc_type": "drug"}],
                },
            },
        }


# Snapshot environment configuration
SNAPSHOT_CONFIG = {
        "env" : {
            "prod" : {
                "cloud" : {
                    "type" : "aws", # default, only one supported by now
                    "access_key" : None,
                    "secret_key" : None,
                    },
                "repository" : {
                    "name" : "drug_repository-$(Y)",
                    "type" : "s3",
                    "settings" : {
                        "bucket" : "<SNAPSHOT_BUCKET_NAME>",
                        "base_path" : "mychem.info/$(Y)", # per year
                        "region" : "us-west-2",
                        },
                    "acl" : "private",
                    },
                "indexer" : {
                    # reference to INDEX_CONFIG
                    "env" : "local",
                    },
                # when creating a snapshot, how long should we wait before querying ES
                # to check snapshot status/completion ? (in seconds)
                "monitor_delay" : 60 * 5,
                },
            "demo" : {
                "cloud" : {
                    "type" : "aws", # default, only one supported by now
                    "access_key" : None,
                    "secret_key" : None,
                    },
                "repository" : {
                    "name" : "drug_repository-demo-$(Y)",
                    "type" : "s3",
                    "settings" : {
                        "bucket" : "<SNAPSHOT_DEMO_BUCKET_NAME>",
                        "base_path" : "mychem.info/$(Y)", # per year
                        "region" : "us-west-2",
                        },
                    "acl" : "public",
                    },
                "indexer" : {
                    # reference to INDEX_CONFIG
                    "env" : "local",
                    },
                # when creating a snapshot, how long should we wait before querying ES
                # to check snapshot status/completion ? (in seconds)
                "monitor_delay" : 10,
                }
            }
        }

# Release configuration
# Each root keys define a release environment (test, prod, ...)
RELEASE_CONFIG = {
        "env" : {
            "prod" : {
                "cloud" : {
                    "type" : "aws", # default, only one supported by now
                    "access_key" : None,
                    "secret_key" : None,
                    },
                "release" : {
                    "bucket" : "<RELEASES_BUCKET_NAME>",
                    "region" : "us-west-2",
                    "folder" : "mychem.info",
                    "auto" : True, # automatically generate release-note ?
                    },
                "diff" : {
                    "bucket" : "<DIFFS_BUCKET_NAME>",
                    "folder" : "mychem.info",
                    "region" : "us-west-2",
                    "auto" : True, # automatically generate diff ? Careful if lots of changes
                    },
                },
            "demo": {
                "cloud" : {
                    "type" : "aws", # default, only one supported by now
                    "access_key" : None,
                    "secret_key" : None,
                    },
                "release" : {
                    "bucket" : "<RELEASES_BUCKET_NAME>",
                    "region" : "us-west-2",
                    "folder" : "mychem.info-demo",
                    "auto" : True, # automatically generate release-note ?
                    },
                "diff" : {
                    "bucket" : "<DIFFS_BUCKET_NAME>",
                    "folder" : "mychem.info",
                    "region" : "us-west-2",
                    "auto" : True, # automatically generate diff ? Careful if lots of changes
                    },
                }
            }
        }


HUB_PASSWD = {"guest":"9RKfd8gDuNf0Q"}

