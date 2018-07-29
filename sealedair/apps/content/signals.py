def warm_lesson_thumbnail(sender, **kwargs):
    lesson = kwargs['instance']
    lesson.warm_thumbnail()
