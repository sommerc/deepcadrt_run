# DeepCAD RT runners

This project contains a UV based project containing all required dependencies for DeepCAD 1.2.0 and training and testing command-line scripts.

No installation or Python environments required, except [uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv).

The Python environment for DeepCAD will be created on-the-fly and is cached for multiple use.

Note, this is tested on Win11 and Debian Linux having a CUDA compatible GPU.

---

## Usage

### 1. Configuration files
Create local train and test configuration files.

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-config

This will create "train_config.json" and "test_config.json" in your current directory.


### 2. Train

Compile a folder *"<data/folder/with/tifs>"* containing .tif movies.

Now, open "train_config.json" and adapt parameters to your needs. No need to change the "dataset_path".

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-train *"<data/folder/with/tifs>"* -c train_config.json

This will create a folder *"models"* containing a sub-folder with your training run of the form *"<data/folder/with/tifs>_<current-date>"*

### 3. Predict

Now, open "train_config.json" and adapt parameters to your needs. No need to change the "dataset_path" and "denoise_model" fields.

    uvx --from https://github.com/sommerc/deepcadrt_run.git deepcadrt-predict <data/folder/with/tifs> models/<your-trained-model> -c test_config.json

This will create a folder "results" containing a sub-folder with your denoised movies.




