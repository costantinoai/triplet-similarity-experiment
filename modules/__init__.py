# ./modules/__init__.py
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(name)s - %(levelname)s - %(message)s')

# Set up environment variables or other initializations specific to modules/net
from modules.net_funcs.net_utils import get_device_info

# Determine the appropriate device(s)
device, num_gpus = get_device_info()

print(f"Using device: {device}, Number of GPUs: {num_gpus}") 
print('Modules package initialized')
