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

