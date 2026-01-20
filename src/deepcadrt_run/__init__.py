from pathlib import Path
import argparse
import json

from rich import print_json
from loguru import logger


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        config = json.load(f)
    return config


def get_train_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Training arguments for deepcadrt-run")
    parser.add_argument("in_dir", type=str, help="Input directory for training data")
    parser.add_argument(
        "-c", "--train-config", type=str, help="Path to the configuration file"
    )
    return parser.parse_args()


def train() -> None:
    logger.info("Starting DeepCAD RT training...")
    args = get_train_args()

    assert Path(args.in_dir).is_dir(), f"Input directory {args.in_dir} does not exist."
    assert Path(args.train_config).is_file(), (
        f"Configuration file {args.train_config} does not exist."
    )

    config = load_config(args.train_config)
    config["datasets_path"] = args.in_dir

    logger.info("Training config...")
    print_json(data=config)

    logger.info("Start...")

    from deepcad.train_collection import training_class

    training_class(config).run()
    logger.info("Done!")


def get_test_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Training arguments for deepcadrt-run")
    parser.add_argument("in_dir", type=str, help="Input directory for prediction data")
    parser.add_argument("model_path", type=str, help="Path to the trained model path")
    parser.add_argument(
        "-c", "--predict-config", type=str, help="Path to the configuration file"
    )
    return parser.parse_args()


def predict() -> None:
    logger.info("Starting DeepCAD RT prediction...")

    args = get_test_args()

    assert Path(args.in_dir).is_dir(), f"Input directory {args.in_dir} does not exist."
    assert Path(args.model_path).is_dir(), (
        f"Model file {args.model_path} does not exist."
    )
    assert Path(args.predict_config).is_file(), (
        f"Configuration file {args.predict_config} does not exist."
    )

    config = load_config(args.predict_config)
    config["datasets_path"] = args.in_dir
    config["denoise_model"] = Path(args.model_path).name

    logger.info("Prediction config...")
    print_json(data=config)

    logger.info("Start...")

    from deepcad.test_collection import testing_class

    testing_class(config).run()
    logger.info("Done!")
