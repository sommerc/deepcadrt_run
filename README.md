# 🚀 DeepCAD RT Runners

Welcome to **DeepCAD RT Runners**! This project is a small UV-based solution that bundles all necessary dependencies for DeepCAD 1.2.0, along with convenient command-line scripts for configuration, training and prediction.

**Key Features:**
- 🔧 No manual Python environment setup required (just [uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)).
- 🖥️ Tested on Windows 11 and Debian Linux with CUDA-compatible GPUs.
- 📊 Seamless training and prediction workflows for denoising .tif movie files.

---

## 📋 Prerequisites

Before diving in, ensure you have:
- A system with a CUDA-compatible GPU (recommended for optimal performance).
- [uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv) installed.
- Access to .tif movie files for training and testing.

---

## 🛠️ Installation

No installation needed! The project uses `uvx` to run commands directly from the GitHub repository. Your Python environment will be created and cached automatically.

---

## 📖 Usage

Follow these steps to train and test your models. Each step includes detailed instructions and examples.

### 1. 📝 Create Configuration Files
Generate local configuration files for training and testing.

Run the following command in your terminal:

```bash
uvx --from deepcadrt-run deepcadrt-config
```

This creates `train_config.json` and `test_config.json` in your current directory. Customize these files as needed (e.g., adjust parameters like patch size, number of epochs or learning rate).

**Example Output:**
- `train_config.json`: Default training settings.
- `test_config.json`: Default testing settings.

### 2. 🎯 Train Your Model
Prepare a folder containing your .tif movie files (e.g., `data/my_movies/`).

Edit `train_config.json` to match your requirements (leave `dataset_path` unchanged).

Run the training command:

```bash
uvx --from deepcadrt-run deepcadrt-train "mymovies" -c train_config.json
```

This will:
- Train a DeepCAD model on your data.
- Create a `models/` folder with a subfolder named like `mymovies_202310011155` (based on your data folder and current date).

**Tips:**
- Ensure your .tif files are properly formatted (e.g., 3D stacks).
- The patch size in the time dimension is smaller than the movie length 
- Monitor GPU usage during training for performance.

### 3. 🔮 Predict and Denoise
Use your trained model to denoise new or existing data.

Edit `test_config.json` as needed (leave `dataset_path` and `denoise_model` unchanged).

Run the prediction command:

```bash
uvx --from deepcadrt-run deepcadrt-predict mymovies/ models/mymovies_202310011155 -c test_config.json
```

This will:
- Apply denoising to your movies.
- Save results in a `results/` folder with a subfolder for your output.

**Example:**
- Input: Noisy .tif movies.
- Output: Denoised versions in `results/`. By default the model from the latest epoch is used.

---

## ❓ Troubleshooting

- **CUDA Issues:** Ensure your GPU drivers are up-to-date and compatible.
- **Memory Errors:** Reduce patch size or train_datasets_size in config files for large datasets.
- **Command Not Found:** Verify `uv` is installed and in your PATH.
- For more help, check the [DeepCAD documentation](https://github.com/cabooster/DeepCAD) or open an issue on this repo.

---

## 🤝 Contributing

We welcome contributions! Feel free to submit pull requests or report bugs via the [GitHub repository](https://github.com/sommerc/deepcadrt_run).

---

## 📄 License

This project is licensed under [MIT License](LICENSE). See the LICENSE file for details.




