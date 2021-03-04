import os


# Max number of *processes* hub can access to run jobs
HUB_MAX_WORKERS = int(os.cpu_count() / 4)

# Max memory usage before hub will prevent creating more jobs, in byte
# If None, no limit. It's a good practice to put a limit as the more processes
# are used, the more they consume memory even if nothing runs. With a limit, hub
# will recycle the process queue in order to limit the memory usage
HUB_MAX_MEM_USAGE = None

