import scipy.io

# Load the .mat file
data = scipy.io.loadmat("cars_annos.mat")

# Extract class names
class_names = data["class_names"][0]  # Contains 196 car class labels

# Convert to a Python list
class_labels = [name[0] for name in class_names]

# Save labels to a file
with open("class_labels.txt", "w") as f:
    for label in class_labels:
        f.write(label + "\n")

# Print sample labels
print(f"Total classes: {len(class_labels)}")
print("Sample labels:", class_labels[:5])  # Print first 5 labels
