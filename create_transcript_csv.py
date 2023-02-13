# IDEA: create a program that runs through the labeled dataset and turns the it into a table of features and the text
import pandas as pd

# preprocessing:
data = open("training_data_labeled.txt","r")
data = [line.strip() for line in data]


# TESTING: 
# Extract the relevant data
class_names = []
grades = []
transfers = []
GPAs = []
metadata = []

# note: each will need to be turned to 0, this way we get the actual data. Might have to use a different delimiter for split
for line in data:
  if "class name" in line:
    class_names.append(line.split("(label:")[0])
  if "grade" in line:
    grades.append(line.split("(label:")[0])
  if "transfer" in line:
    transfers.append(line.split("(label:")[0])
  if "GPA" in line:
    if len(line.split(":")) >= 2:
        GPAs.append(line.split(":")[1])
    else:
        GPAs.append(line.split("(label:")[0])
  if "metadata" in line:
    metadata.append(line.split("(label:")[0])


# pad the shorter arrays
# Find the length of the longest list
max_length = max(len(class_names), len(grades), len(transfers), len(GPAs), len(metadata))

# Pad the shorter lists with empty values
class_names += [""] * (max_length - len(class_names))
grades += [""] * (max_length - len(grades))
transfers += [""] * (max_length - len(transfers))
GPAs += [""] * (max_length - len(GPAs))
metadata += [""] * (max_length - len(metadata))

# check size of arrays
print(len(class_names))
print(len(grades))
print(len(transfers))
print(len(GPAs))
print(len(metadata))

# Create the DataFrame for method 1
df = pd.DataFrame({
  "class_name": class_names,
  "grade": grades,
  "transfer": transfers,
  "GPA": GPAs,
  "metadata": metadata
})

######################## universal sentence encoder version ##############################################
# TESTING: 
v1 = []
v2 = []

# first column needs to be the associated value for the second column
for line in data:
  if "class name" in line:
    v1.append("class_name")
    v2.append(line.split("(label:")[0])
  elif "label:" in line:
    v1.append("other")
    v2.append(line.split("(label:")[0])
  else:
    v1.append("No_value")
    v2.append(line)


# Create the dataframe for method 2
Otherdf = pd.DataFrame({
  "v1": v1,
  "v2": v2
})
######################################################################################################

######################### create test csv ############################################################
v1 = []

# preprocessing:
data = open("training_data.txt","r")
data = [line.strip() for line in data]

for line in data:
  v1.append(line)

testdf = pd.DataFrame({
  "v1": v1
})

print("Normal array:")
print(df.head())
print()
print("Universal sentence encoder array:")
print(Otherdf)
print()
print("test csv:")
print(testdf)
testdf.to_csv("test_transcript_data.csv")
Otherdf.to_csv("transcript_data.csv")
