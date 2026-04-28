from PIL import Image

def find_photo_bbox(image_path, out_path):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    
    start_y = 100
    end_y = 650
    start_x = width - 100   # scan from right margin
    end_x = width // 2      # stop going left when we hit text
    
    pixels = img.load()
    
    min_x = width
    max_x = 0
    min_y = height
    max_y = 0
    
    threshold = 50
    
    # First, find the rightmost non-black pixel
    hit_photo = False
    for x in range(start_x, end_x, -1):
        col_has_pixels = False
        for y in range(start_y, end_y):
            r, g, b = pixels[x, y]
            if sum((r, g, b)) / 3 > threshold:
                col_has_pixels = True
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                hit_photo = True
                
        # If we hit the photo, and then subsequently find an entirely empty black column,
        # it means we have passed the left edge of the photo and hit the gap before the text!
        if hit_photo and not col_has_pixels:
            break

    print(f"Refined Detected bounding box: ({min_x}, {min_y}, {max_x}, {max_y})")
    
    if max_x > min_x and max_y > min_y:
        crop_img = img.crop((min_x, min_y, max_x, max_y))
        crop_img.save(out_path)
        print(f"Successfully cropped and saved to {out_path}.")
        return
    
    print("Could not find a valid photo bounding box.")

if __name__ == "__main__":
    find_photo_bbox(r"c:\Recorrido II VR\temp_cv_images\full_page.png", r"c:\Recorrido II VR\temp_cv_images\photo.png")
