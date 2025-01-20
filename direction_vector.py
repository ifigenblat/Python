import math

def degrees_to_direction_vector(degrees):
    # Convert degrees to radians
    radians = math.radians(degrees)
    
    # Calculate the x and y components of the direction vector
    x = math.cos(radians)
    y = math.sin(radians)
    
    # Return the direction vector
    return (x, y)

# Example usage
angle = 45  # Angle in degrees
direction_vector = degrees_to_direction_vector(angle)
print("Direction Vector:", direction_vector)