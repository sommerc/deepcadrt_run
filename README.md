# DeepCAD RT runners

This project contains a UV base project containing all required dependencies for DeepCAD 1.2.0 and training and testing command-line scripts.

No installation or Python environments required.
---

## Usage

### 1. Configuration files
Create local train and test configuration files

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-config

Edit and adapt the configuration files to your needs.

### 2. Train

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-train <data/folder/with/tifs> -c train_config.json

This will create a folder **models** containing a sub-folder with your training run of the form "<data/folder/with/tifs>_<todays-date>"

### 3. Predict

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-predict <data/folder/with/tifs> models/<your-trained-model> -c test_config.json






