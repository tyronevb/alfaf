"""Script to run the Cognitive Debugging, Automated LFA Framework"""

__author__ = "tyronevb"
__date__ = "2021"

import argparse
import sys

sys.path.append("..")
from src.lfa_framework import AutomatedLFAFramework

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Automated LFA Framework in either Training or Inference Mode")
    parser.add_argument("-d", "--data_miner_config", action="store", type=str,
                        help="Path to configuration file (yaml) that contains "
                             "the log format for the log files to be parsed, "
                             "log parsing method and tunable parameter values",
                        required=True)
    parser.add_argument("-e", "--inference_engine_config", action="store",
                        type=str,
                        help="Path to configuration file (yaml) that contains "
                             "the various parameters for the Inference Engine, "
                             "and Feature Extractor",
                        required=True)
    parser.add_argument(
        "-i",
        "--input_dir",
        action="store",
        type=str,
        help="Absolute path to the input directory where the log file exists. Include trailing " "/",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        action="store",
        type=str,
        help="Absolute path to the output directory where all Framework outputs are to be saved. Include trailing /",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--log_file",
        action="store",
        type=str,
        help="Name of raw log file to be provided to the Framework on. Should not include path.",
        required=True,
    )
    parser.add_argument("-n", "--name", action="store", type=str,
                        help="A unique name for this instance of the Framework. Used when naming output"
                             "files from the framework. Reccommend using name representative of system under"
                             "test",
                        required=True)
    parser.add_argument("-c", "--compute_device", action="store", choices=["cpu", "cuda:0", None], default=None,
                        help="Specify which compute device to use for deep learning model training and inference")
    parser.add_argument("-m", "--mode", action="store", choices=["training", "inference"], default="training",
                        help="Specify which mode to operate the Framework in. Either training mode or inference mode. "
                             "Configuration files must also be for the required mode.")
    parser.add_argument("-s", "--datastore", action="store", type=str, default=None,
                        help="Path to existing datastore containing log keys and events for the system in question. "
                             "Is required when operating in Inference Mode")
    parser.add_argument("-u", "--update_store", action="store_true",
                        help="Specify whether the datastore should be updated if new log keys are found.")

    args = parser.parse_args()

    print("\n====================================")
    print("Running Automated LFA Framework . . .\n")

    # create AutomatedLFAFramework instance
    lfa_framework = AutomatedLFAFramework(data_miner_config=args.data_miner_config,
                                          inference_engine_config=args.inference_engine_config,
                                          input_dir=args.input_dir,
                                          output_dir=args.output_dir,
                                          name=args.name,
                                          device=args.compute_device,
                                          mode=args.mode,
                                          datastore=args.datastore,
                                          update_datastore=args.update_store)

    if args.mode == "training":
        # training mode
        print("Running framework in Training Mode . . .\n")
        lfa_framework.train_anomaly_detection_model(input_log_file_name=args.log_file)

    else:
        # inference mode
        if args.datastore is None:
            print("Datastore required when running in inference mode. Framework shutting down . . .")
        else:
            print("Running framework in Inference Mode . . .\n")
            lfa_framework.generate_debugging_report(input_log_file_name=args.log_file, verbose=True)

    print("====================================\n")

# end
