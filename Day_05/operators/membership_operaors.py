# Membership operators check whether a value exists inside a collection.
# Operators:in, not in

# in
# Example:
namespaces = ["default", "openshift-gitops", "sonarqube"]

if "sonarqube" in namespaces:
    print("SonarQube namespace exists")

# Output: SonarQube namespace exists

############################

# not in
namespaces = ["default", "openshift-gitops"]

if "sonarqube" not in namespaces:
    print("SonarQube namespace does not exist")
# Output: SonarQube namespace does not exist