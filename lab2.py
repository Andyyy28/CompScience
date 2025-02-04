# Naïve Bayes Classifier (Manual Implementation) for Student Grades

# Sample dataset
data = [
    {"Subject": "Math", "Grade": "A", "Pass": "Yes"},
    {"Subject": "Math", "Grade": "C", "Pass": "No"},
    {"Subject": "Science", "Grade": "B", "Pass": "Yes"},
    {"Subject": "Science", "Grade": "D", "Pass": "No"},
    {"Subject": "English", "Grade": "A", "Pass": "Yes"},
    {"Subject": "English", "Grade": "B", "Pass": "Yes"},
    {"Subject": "Math", "Grade": "F", "Pass": "No"},
    {"Subject": "Science", "Grade": "C", "Pass": "No"},
    {"Subject": "English", "Grade": "D", "Pass": "No"},
    {"Subject": "Math", "Grade": "B", "Pass": "Yes"},
]

# Input to classify (example: Will a student with Grade "B" in Math pass?)
input_data = {"Subject": "Math", "Grade": "B"}

# Step 1: Compute Prior Probabilities
def calculate_priors(data):
    total = len(data)
    pass_counts = {"Yes": 0, "No": 0}
    for item in data:
        pass_counts[item["Pass"]] += 1
    return {key: value / total for key, value in pass_counts.items()}

# Step 2: Compute Conditional Probabilities (with Laplace smoothing)
def calculate_conditionals(data, input_data):
    conditional_probs = {"Yes": 1, "No": 1}
    total_counts = {"Yes": sum(1 for i in data if i["Pass"] == "Yes"),
                    "No": sum(1 for i in data if i["Pass"] == "No")}
    
    for key in input_data:
        counts = {"Yes": 0, "No": 0}
        for item in data:
            if item[key] == input_data[key]:
                counts[item["Pass"]] += 1

        # Apply Laplace smoothing (add 1 to numerator, add number of unique values to denominator)
        unique_values = len(set(i[key] for i in data))  # Count unique values for the feature
        for outcome in ["Yes", "No"]:
            conditional_probs[outcome] *= (counts[outcome] + 1) / (total_counts[outcome] + unique_values)
    
    return conditional_probs

# Step 3: Compute Posterior Probabilities
def calculate_posteriors(priors, conditionals):
    posteriors = {}
    for outcome in priors:
        posteriors[outcome] = priors[outcome] * conditionals[outcome]
    return posteriors

# Step 4: Classify the input
priors = calculate_priors(data)
conditionals = calculate_conditionals(data, input_data)
posteriors = calculate_posteriors(priors, conditionals)
classification = max(posteriors, key=posteriors.get)

# Print results
print("\nResult:")
print("Prior Probabilities:", priors)
print("Conditional Probabilities:", conditionals)
print("Posterior Probabilities:", posteriors)
print("Classification (Will the student pass?😨):", classification)
