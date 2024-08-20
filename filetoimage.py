from PIL import Image
import time

# Function to extract the file name from the file path
def get_name_of_file(tfp):
    return tfp.split("/")[-1]

# Input for the file path
thefilepath = input("Enter the path to the file(any type) that is going to be encoded (eg: C:/Users/Big00/Desktop/codes for something/ai#2/discord/thefile.txt): ")

# Extracting the file name from the path
thefilename = get_name_of_file(thefilepath)

def binary_to_8bit_chunks(binary_data):
    # Convert binary data to binary string
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    
    # Split the binary string into 8-bit chunks
    chunk_size = 8
    chunks = [binary_string[i:i + chunk_size] for i in range(0, len(binary_string), chunk_size)]
    
    # Pad the final chunk with zeros if it's less than 8 bits
    if len(chunks[-1]) < chunk_size:
        chunks[-1] = chunks[-1].ljust(chunk_size, '0')
    
    return chunks

# Open the file in binary mode
with open(thefilepath, "rb") as file:
    binary_data = file.read()

# Convert the file content to 8-bit binary chunks
binary_chunks = binary_to_8bit_chunks(binary_data)

# Determine the dimensions of the image (we'll create a square image)
length = len(binary_chunks)
side_length = int((length / 3)**0.5)
if side_length * side_length * 3 < length:
    side_length += 1

# Create a new image with RGB mode
image = Image.new("RGB", (side_length, side_length), "white")
pixels = image.load()

# Function to convert binary chunk to integer
def binary_to_int(binary_chunk):
    return int(binary_chunk, 2)

# Fill the image with the binary data as RGB values
for i in range(0, length, 3):
    row = (i // 3) // side_length
    col = (i // 3) % side_length
    
    r = binary_to_int(binary_chunks[i]) if i < length else 0
    g = binary_to_int(binary_chunks[i + 1]) if i + 1 < length else 0
    b = binary_to_int(binary_chunks[i + 2]) if i + 2 < length else 0
    
    pixels[col, row] = (r, g, b)

# Save the image
output_image_path = thefilename + ".png"
image.save(output_image_path)

print(f"Image has been saved to {output_image_path}")
time.sleep(5)
