# Handover-Sim

### Prerequisites

This code is tested with Python 3.7 on Linux.

### Installation

1. Clone the repo with `--recursive` and and cd into it:

    ```Shell
    git clone --recursive ssh://git@gitlab-master.nvidia.com:12051/ychao/handover-sim.git
    cd handover-sim
    ```

2. Install Python package and dependencies:

    ```Shell
    pip install -e .
    ```

3. Download data from OMG-Planner:

    ```Shell
    cd OMG-Planner
    ./download_data.sh
    cd ..
    ```

4. Compile YCB models:

    ```Shell
    python handover/data/compile_ycb_models.py
    ```

5. Download the DexYCB dataset.

    **Option 1**: Download cached dataset: **(recommended)**

    ```Shell
    cd handover/data
    # Download dex-ycb-cache_20210225.tar.gz from https://drive.google.com/file/d/1NmoaIIhP4dGrX7aNMVPBrhuas9icyc-a.
    tar -zxvf dex-ycb-cache_20210225.tar.gz
    cd ../..
    ```

    **Option 2**: Download full dataset and cache the data:

    1.  Download the DexYCB dataset from the [DexYCB project site](https://dex-ycb.github.io).

    2. Set the environment variable for dataset path:

        ```Shell
        export DEX_YCB_DIR=/path/to/dex-ycb
        ```

        `$DEX_YCB_DIR` should be a folder with the following structure:

        ```Shell
        ├── 20200709-subject-01/
        ├── 20200813-subject-02/
        ├── ...
        ├── calibration/
        └── models/
        ```

    3. Cache the dataset:

        ```Shell
        python handover/data/cache_dex_ycb_data.py
        ```

### Running demos

```Shell
python examples/demo_handover_env.py
```
