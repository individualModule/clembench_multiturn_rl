import json
import random
import os

# Use the absolute path to the JSON file
base_dir = os.path.dirname(__file__)  # Get the directory of the script
instances_path = os.path.join(base_dir, "in", "full_instances.json")

# Load the JSON file
with open(instances_path, "r") as file:
    data = json.load(file)

# Function to split data into train and test
def split_data(data, test_ratio=1/3):
    experiments = data["experiments"]
    train_experiments, test_experiments = [], []

    for experiment in experiments:
        game_instances = experiment["game_instances"]
        random.shuffle(game_instances)  # Shuffle to ensure randomness
        split_index = int(len(game_instances) * (1 - test_ratio))
        
        # Create train and test splits for the current experiment
        train_experiment = experiment.copy()
        test_experiment = experiment.copy()
        train_experiment["game_instances"] = game_instances[:split_index]
        test_experiment["game_instances"] = game_instances[split_index:]
        
        train_experiments.append(train_experiment)
        test_experiments.append(test_experiment)

    # Create train and test data with all metadata preserved
    train_data = data.copy()
    test_data = data.copy()
    train_data["experiments"] = train_experiments
    test_data["experiments"] = test_experiments

    return train_data, test_data

# Split the data
train_data, test_data = split_data(data)

# Save the train and test splits
train_path = os.path.join(base_dir, "in", "instances.json")
test_path = os.path.join(base_dir, "in", "test_instances.json")

with open(train_path, "w") as train_file:
    json.dump(train_data, train_file, indent=4)

with open(test_path, "w") as test_file:
    json.dump(test_data, test_file, indent=4)

print("Train and test splits created successfully!")