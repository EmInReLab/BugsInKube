# BugsInKube: Bug Inspector Toolkit

### Description

The Bug Inspector Toolkit is a comprehensive tool that contains detailed information on over 50 reproducible
bugs within the Kubernetes container orchestration tool, which is a leading orchestration platform.
This project visualizes these reproducible bugs, making it easier for users to understand and address them.

Users can select a bug using its ID and have the option to reproduce the bug in their own cluster.
Alternatively, they can simply view the reproducibility guide for each respective bug. This toolkit
provides a valuable resource for developers and system administrators to identify, and understand
bugs in Kubernetes effectively.

![Methodology of Fuzzing Cloud PaaS Platforms](static/main_ui.png)

### Prerequisites

1. Install tkinter.
2. Setup the Kubernetes Cluster.
   - `kubectl` should be able to access your kubernetes cluster.

### Setup

1. Clone the repository.

   ```
   git clone https://github.com/EmInReLab/BugsInKube.git
   ```

2. Set up the prerequisites.
3. Run the application.
   ```
   python src/ui.py
   ```
