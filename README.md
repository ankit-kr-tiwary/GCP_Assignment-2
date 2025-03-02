# GCP_Assignment-2 (VM Creation )

## Overview
------------

This repository contains a Python script to stress test the CPU on a Google Cloud Platform (GCP) VM instance. The script utilizes all available CPU cores to increase utilization and trigger autoscaling.

## Features
------------

- Uses multiprocessing to stress all CPU cores
- Runs heavy computations using `math.factorial(100000)`
- Auto-runs for 5 minutes or can be stopped manually
- Helps test GCP autoscaling by reaching CPU utilization thresholds

## Prerequisites
-----------------

Before running the script, ensure that you have:

- A GCP VM instance with autoscaling enabled
- Python 3 installed on the VM

## Step-by-Step Setup
----------------------

### Step 1: Login to Google Cloud Console

1. Go to the Google Cloud Console (https://console.cloud.google.com/)
2. Login using the credentials provided

### Step 2: Create a VM Instance

1. Navigate to Compute Engine > VM instances
2. Click on "Create Instance"
3. Enable Compute Engine API if prompted
4. Enable billing (charges based on resource utilization)

### Step 3: Configure the VM

1. Set the instance name
2. Choose a region and zone
3. Select machine type, CPU, and GPU (keep default for restricted billing)
4. Under "Boot disk", click "Change"
5. Select "Ubuntu 20.04 LTS" as the operating system
6. Set disk type to "Balanced persistent disk" and size to 10GB
7. Under "Networking", set up firewall rules to allow HTTP/HTTPS traffic
8. Click "Create" to set up the VM instance

### Step 4: Set Up IAM Permissions

1. Go to IAM & Admin
2. Add a new user (e.g., abc@gmail.com) with the "Viewer" role
3. Save the IAM settings

### Step 5: Set Up Firewall Rules

1. Navigate to VPC network > Firewall
2. Create a new firewall rule
3. Define ingress (incoming) and egress (outgoing) traffic rules as needed

### Step 6: Set Up Auto-Scaling

1. Go to Instance groups
2. Click "Create Instance Group"
3. Provide a name and select an instance template
4. Configure auto-scaling settings based on your requirements

### Step 7: SSH into Your GCP VM

1. In Compute Engine > VM Instances, click SSH on your instance

### Step 8: Install Python (If Not Installed)

For Ubuntu:

`sudo apt update && sudo apt install -y python3`

### Step 9: Create the Python Script

1. Create a new file:

`vi cpustress.py`

2. Code:
```
import multiprocessing
import time
import math

def stress_cpu():
    """Function to perform CPU-intensive calculations"""
    while True:
        _ = math.factorial(100000)  # Heavy computation to keep CPU busy

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get total available CPU cores
    print(f"Starting stress test on {num_cores} CPU cores...")

    processes = []
    for _ in range(num_cores):  # Use all CPU cores
        p = multiprocessing.Process(target=stress_cpu)
        p.start()
        processes.append(p)

    try:
        time.sleep(300)  # Run for 5 minutes (adjust as needed)
    except KeyboardInterrupt:
        print("Stopping stress test...")
    finally:
        for p in processes:
            p.terminate()
```

### Step 10: Run the Script

Execute the script:

`python3 cpustress.py`

### Step 11: Monitor CPU Usage

Check CPU usage in real-time:

`top`

Or install and use htop:

`sudo apt install -y htop`
`htop`

### Step 12: Verify Autoscaling in GCP

1. Go to Google Cloud Console
2. Navigate to Compute Engine > Instance Groups
3. Check if a new VM instance has been created due to high CPU utilization

### Step 13: Stop the Script

To stop the script manually:

- Press CTRL + C in the terminal, or run:

`pkill -f cpustress.py`






