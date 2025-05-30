import json
import random
import os

# Use the absolute path to the JSON file
base_dir = os.path.dirname(__file__)  # Get the directory of the script
instances_path = os.path.join(base_dir, "in", "instances.json")

# Load the JSON file
with open(instances_path, "r") as file:
    data = json.load(file)

# Function to split data into train and test
def split_data(experiments, test_ratio=1/3):
    train, test = [], []
    for experiment in experiments:
        game_instances = experiment["game_instances"]
        random.shuffle(game_instances)  # Shuffle to ensure randomness
        split_index = int(len(game_instances) * (1 - test_ratio))
        train.append({
            "name": experiment["name"],
            "game_instances": game_instances[:split_index]
        })
        test.append({
            "name": experiment["name"],
            "game_instances": game_instances[split_index:]
        })
    return train, test

# Split the data
train_data, test_data = split_data(data["experiments"])

# Save the train and test splits
train_path = os.path.join(base_dir, "in", "train_instances.json")
test_path = os.path.join(base_dir, "in", "test_instances.json")

with open(train_path, "w") as train_file:
    json.dump({"experiments": train_data}, train_file, indent=4)

with open(test_path, "w") as test_file:
    json.dump({"experiments": test_data}, test_file, indent=4)

print("Train and test splits created successfully!")