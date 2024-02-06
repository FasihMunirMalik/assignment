import os
import ruamel.yaml
import pytest
from application import update_version, read_yaml_file, write_yaml_file

current_sample_data = {
    "picking": {
        "max": {
            "bottle": [0.005, 0.005, 0.005],  # [x,y,z] in meter
            "can": [0.003, 0.003, 0.003]  # [x,y,z] in meter
        },
        "max_speed": 2,  # in meter/second

    }
}

new_sample_data = {
    "picking": {
        "max_error": {
            "bottle": [0.005, 0.005, 0.005],  # [x,y,z] in meter
            "can": [0.003, 0.003, 0.003]  # [x,y,z] in meter
        },
        "max_speed": 0.20,  # in meter/second
        "max_accel": 0.50  # in meter/second^2
    }
}


def test_update_version_base_case():
    expected_result = {
        "picking": {
            "max_error": {
                "bottle": [0.005, 0.005, 0.005],  # [x,y,z] in meter
                "can": [0.003, 0.003, 0.003]  # [x,y,z] in meter
            },
            "max_speed": 2,  # in meter/second
            "max_accel": 0.50  # in meter/second^2
        }
    }

    result = update_version(current_sample_data, new_sample_data, force_values=False, force_fields=False)
    assert result == expected_result


def test_update_version_force_values():
    expected_result = {
        "picking": {
            "max": {
                "bottle": [0.005, 0.005, 0.005],  # [x,y,z] in meter
                "can": [0.003, 0.003, 0.003]  # [x,y,z] in meter
            },
            "max_speed": 0.20,  # in meter/second

        }
    }

    result = update_version(current_sample_data, new_sample_data, force_values=True, force_fields=False)
    assert result == expected_result


def test_update_version_force_fields():
    expected_result = {
        "picking": {
            "max_error": {
                "bottle": [0.005, 0.005, 0.005],  # [x,y,z] in meter
                "can": [0.003, 0.003, 0.003]  # [x,y,z] in meter
            },
            "max_speed": 0.20,  # in meter/second
            "max_accel": 0.50  # in meter/second^2
        }
    }

    result = update_version(current_sample_data, new_sample_data, force_values=False, force_fields=True)
    assert result == expected_result


def create_sample_file(file_path, file_data):
    try:
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(file_data, file)
        print(f"sample file '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating sample file '{file_path}': {str(e)}")


# Specify the file name
current_directory = os.getcwd()
file_path1 = os.path.join(current_directory, "current_sample.yaml")
file_path2 = os.path.join(current_directory, "new_sample.yaml")


def test_read_yaml():
    # sample file for current_sample_data created as current_sample.yaml
    create_sample_file(file_path1, current_sample_data)
    result = read_yaml_file(file_path1)

    cleanup(file_path1)

    assert result == current_sample_data


def test_write_yaml():
    # write a new yaml file using the function defined in application add the data defined under the variable current_sample_data
    write_yaml_file(file_path2, new_sample_data)

    # sample file for current_sample_data created as current_sample.yaml
    # read the newly created file to see if the correct file was created
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    with open(file_path2, 'r', encoding='utf-8') as file:
        result = yaml.load(file)
    cleanup(file_path2)
    assert result == new_sample_data


# function to remove the extra files that were created for the purpose of testing
def cleanup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    pytest.main([__file__])
