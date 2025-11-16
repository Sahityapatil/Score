import sys
# Simple Interest Calculator using sys.argv
print("Simple Interest Calculator")
# Check if user provided 3 arguments through command line
if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    # Default values
    principal = 1000
    rate = 5
    time = 2
    print("\nArguments not provided — using default values:")
    print("Principal = 1000, Rate = 5%, Time = 2 years")

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display output
print("\nSimple Interest =", simple_interest)
