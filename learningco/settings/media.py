import os
from .default import BASE_DIR

MEDIA_ROOT = os.path.join(BASE_DIR, '.media/')
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 85,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': False,
    'image_key_post_processor': None,
    'progressive_jpeg': True
}

VERSATILEIMAGEFIELD_USE_PLACEHOLDIT = True
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'profile_avatar': [
        ('full_size', 'url'),
        ('crop__280x280', 'crop__280x280'),
        ('crop__128x128', 'crop__128x128'),
        ('crop__44x44', 'crop__44x44'),
        ('crop__42x42', 'crop__42x42'),
    ]
}

EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
)
