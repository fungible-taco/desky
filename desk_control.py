#!/usr/bin/env python3
from dotenv import load_dotenv
from logger import get_logger
import os
import subprocess
import argparse
import time


logger = get_logger(__name__)
load_dotenv()
mac_address = os.getenv("mac_address")
standing_height = os.getenv("standing_height")
sitting_height = os.getenv("sitting_height")
#subprocess.run(["linak-controller", "--mac-address", mac_address, "--move-to", str(standing_height)])

def raise_desk():
    """
    Raise the standing desk to the configured height.
    """
    try:
        logger.info(f"Raising desk to {standing_height}mm")
        result = subprocess.run(["linak-controller", "--mac-address", mac_address, "--move-to", str(standing_height)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logger.info("Desk raised successfully")
        else:
            logger.error(f"Failed to raise desk: {result.stderr}")
    except Exception as e:
        logger.error(f"Error raising desk: {e}")


def lower_desk():
    """
    Raise the standing desk to the configured height.
    """
    try:
        logger.info(f"Lowering desk to {sitting_height}mm")
        result = subprocess.run(["linak-controller", "--mac-address", mac_address, "--move-to", str(sitting_height)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logger.info("Desk lowered successfully")
        else:
            logger.error(f"Failed to lower desk: {result.stderr}")
    except Exception as e:
        logger.error(f"Error lowering desk: {e}")

# def move_desk(mac_address, height_mm=750):
#     """
#     Move the desk to the specified height in millimeters.
#     """
#     mac_address = os.getenv("mac_address")
#     print(mac_address)
#     height_mm = 750
#     # Step 1: Check current height
#     print("Checking current height...")
#     subprocess.run(["linak-controller", "--mac-address", mac_address])
    
#     # Step 2: Send command to move desk
#     print(f"Moving desk to {height_mm}mm...")
#     subprocess.run(["linak-controller", "--mac-address", mac_address, "--move-to", str(height_mm)])
    
#     # Step 3: Wait for movement to complete
#     print("Waiting for desk to reach target height...")
#     time.sleep(10)
    
#     # Step 4: Verify final height
#     print("Checking final height...")
#     subprocess.run(["linak-controller", "--mac-address", mac_address])

# if __name__ == "__main__":
#     # Set up command-line argument parsing
#     parser = argparse.ArgumentParser(description='Move your desk to a specific height')
#     parser.add_argument('--mac-address', required=True, help='UUID of your desk')
#     parser.add_argument('--height', type=int, default=750, help='Target height in mm (default: 750)')
    
#     # Parse the arguments
#     args = parser.parse_args()
    
#     # Call the main function with the provided arguments
#     move_desk(args.mac_address, args.height)

