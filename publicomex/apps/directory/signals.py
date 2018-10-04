def warm_image_file(sender, **kwargs):
    p = kwargs['instance']
    p.warm_image_file()
