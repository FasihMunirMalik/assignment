import argparse
import copy
from flatten_dict import flatten
from flatten_dict import unflatten
import ruamel.yaml
import logging

# Set up logging configuration
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def update_version(current_version, new_version, force_values=False, force_fields=False):
    logger.debug("Flattening current and new versions.")
    current_version=flatten(current_version)
    new_version=flatten(new_version)

    if not force_values:
        if force_fields:
            logger.debug("Forcing update of fields and values.")
            updated_version = copy.deepcopy(new_version)

        if not force_fields:
            logger.debug("Updating only existing fields.")
            updated_version = copy.deepcopy(new_version)
            # for fields present in both force the update of updated_version fields with the values from `new_version
            for key,value in current_version.items():
                if key in updated_version:
                    updated_version[key] = value
                    logger.debug(f"Keeping existing value for key '{key}'.")

    if force_values:
        logger.debug("Forcing update of values only.")
        updated_version = copy.deepcopy(current_version)
        for key, value in new_version.items():
            if key in updated_version:
                # for fields present in both force the update of updated_version fields with the values from `new_version
                updated_version[key] = value
                logger.debug(f"Forcing update of value for key '{key}'.")

    logger.debug("Unflattening updated version.")
    return unflatten(updated_version)


def read_yaml_file(file_path):
    try:
        logger.info(f"Reading YAML file '{file_path}'.")
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True

        with open(file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.load(file)
            logger.debug(f"YAML data read from file '{file_path}'.")
            return yaml_data
    except Exception as e:
        logger.error(f"Error reading YAML file '{file_path}': {str(e)}")
        return None


def write_yaml_file(file_path, data):
    try:
        logger.info(f"Writing to YAML file '{file_path}'.")
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True

        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file)


            logger.debug(f"YAML data written to file '{file_path}'.")
    except Exception as e:
        logger.error(f"Error writing to YAML file '{file_path}': {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Update YAML version files.")
    parser.add_argument("current_version", help="Path to current version YAML file")
    parser.add_argument("new_version", help="Path to new version YAML file")
    parser.add_argument("--force-values", action="store_true", help="Replace values of existing fields")
    parser.add_argument("--force-fields", action="store_true", help="Replace values and add/remove fields")
    parser.add_argument("--log-level", choices=['DEBUG', 'INFO', 'ERROR'], default='INFO', help="Set logging level")

    args = parser.parse_args()

    # Set the logging level based on the user's choice
    logger.setLevel(args.log_level)
    args = parser.parse_args()

    if args.force_values and args.force_fields:
        logger.error("Cannot specify both --force-values and --force-fields.")
        return

    current_version = read_yaml_file(args.current_version)
    new_version = read_yaml_file(args.new_version)

    if current_version is not None and new_version is not None:
        logger.info("Updating YAML version files.")
        updated_version = update_version(current_version, new_version, args.force_values, args.force_fields)
        write_yaml_file(args.current_version, updated_version)
        logger.info("Update successful.")


if __name__ == "__main__":
    main()
