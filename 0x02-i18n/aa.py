import flask_babel

# List all attributes of the flask_babel module
attributes = dir(flask_babel)

# Print each attribute
print("Attributes of the flask_babel module:")
for attribute in attributes:
    print(attribute)

# Get more information about specific attributes
print("\nDetailed information about specific attributes:")
for attribute in attributes:
    attr = getattr(flask_babel, attribute)
    if callable(attr):
        print(f"\n{attribute}:\n")
        help(attr)

