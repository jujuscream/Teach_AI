# from typing import Sequence

# from google.cloud import vision


# def analyze_local_image(
#     image_path: str,
#     feature_types: Sequence,
# ) -> vision.AnnotateImageResponse:
#     client = vision.ImageAnnotatorClient()

#     with open(image_path, 'rb') as f:
#         content = f.read()

#     image = vision.Image(content=content)
#     features = [vision.Feature(type_=feature_type) for feature_type in feature_types]
#     request = vision.AnnotateImageRequest(image=image, features=features)

#     response = client.annotate_image(request=request)

#     return response


# # def print_labels(response: vision.AnnotateImageResponse):
# #     print("=" * 80)
# #     for label in response.label_annotations:
# #         print(
# #             f"{label.score:4.0%}",
# #             f"{label.description:5}",
# #             sep=" | ",
# #         )

# # def print_objects(response: vision.AnnotateImageResponse):
# #     print("=" * 80)
# #     for obj in response.localized_object_annotations:
# #         nvertices = obj.bounding_poly.normalized_vertices
# #         print(
# #             f"{obj.score:4.0%}",
# #             f"{obj.name:15}",
# #             f"{obj.mid:10}",
# #             ",".join(f"({v.x:.1f},{v.y:.1f})" for v in nvertices),
# #             sep=" | ",
# #         )

# def get_color_percentage(image_path: str, color: str) -> float:
#     # Define the feature type to use for object localization
#     feature_type = vision.Feature.Type.OBJECT_LOCALIZATION

#     # Analyze the image and retrieve the object localization annotations
#     response = analyze_local_image(image_path, [feature_type])
#     objects = response.localized_object_annotations

#     # Find all objects that are the specified color
#     color_objects = [obj for obj in objects if obj.color.red == 255 and obj.color.green == 0 and obj.color.blue == 0]

#     # Calculate the total area of the image
#     image_area = response.image_properties.width * response.image_properties.height

#     # Calculate the total area of the colored segments
#     color_area = sum(obj.bounding_poly.area for obj in color_objects)

#     # Calculate the percentage of the image that is the specified color
#     color_percentage = color_area / image_area * 100

#     return color_percentage

# image_path = "/home/jujuscream/Desktop/Teach_AI/Python_Scripts/sample_pie.png"
# features = [vision.Feature.Type.OBJECT_LOCALIZATION]

# response = analyze_local_image(image_path, features)
# # print_objects(response)
# print(get_color_percentage(image_path, "red"))


from google.cloud import vision

def analyze_image(image_path):
    """Analyzes the colors of every pixel in the image."""
    with open(image_path, 'rb') as f:
        image_content = f.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    response = client.annotate_image({
    'image': image,
    'features': [{'type_': vision.Feature.Type.IMAGE_PROPERTIES}]
    })

    
    image = vision.Image(content=image_content)
    props = response.image_properties_annotation

    # Extract the colors and their pixel fractions
    colors = props.dominant_colors.colors

    # Output the top 10 colors and their pixel fractions
    for color in colors[:10]:
        print('Color: ({}, {}, {})'.format(color.color.red, color.color.green, color.color.blue))
        print('Pixel fraction: {:.2f}'.format(color.pixel_fraction))


analyze_image("/home/jujuscream/Desktop/Teach_AI/Python_Scripts/sample_pie.png")
