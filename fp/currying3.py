def new_resizer(max_width, max_height):

    def first_inner(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def second_inner(width, height):
            if width > max_width:
                width = min(width, max_width)
            elif width < min_width:
                width = max(width, min_width)

            if height > max_height:
                height = min(height, max_height)
            elif height < min_height:
                height = max(height, min_height)

            return (width, height)

        return second_inner

    return first_inner

set_min_size = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image = set_min_size(200, 100)

# Step 3: Resize the image
new_width, new_height = resize_image(1000, 500)

# Step 4: Output the result
print(new_width, new_height)  # Output: 800, 500

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)
