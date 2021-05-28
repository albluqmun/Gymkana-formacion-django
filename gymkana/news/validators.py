from django.core.exceptions import ValidationError

def image_size(image):
    limit = 10 * 1024 * 1024
    if image.size > limit:
        raise ValidationError('The image should not exceed 10MB.')

def image_extension(image):
    # meter ipdb
    valid_extensions = ["jpg","png"]
    if not any([image.url.endswith(e) for e in valid_extensions]):
        raise ValidationError('The image must have a jpg or a png extension.')

#  Mimetype