from django.views.generic.base import View, ContextMixin
from django.shortcuts import redirect
from ...content.models import (
    Lesson, Intro, Video, Article, ActivityList, Skill)


BASE_LESSON_FIELDS = ['skill', 'name']
FULL_LESSON_FIELDS = ['skill', 'name', 'body']
DEFAULT_LESSON_FIELDS = FULL_LESSON_FIELDS


class LessonGenericView(ContextMixin):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if 'skill_pk' in kwargs:
            ctx['skill'] = self.get_skill(kwargs['skill_pk'])
        else:
            ctx['skill'] = self.object.skill

        return ctx

    def get_skill(self, skill_pk):
        return Skill.objects.get(pk=skill_pk)

    def get_success_url(self):
        return self.object.get_update_url()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if 'assign' in request.GET:
            self.set_as_skill_default(self.object)

        return response

    def set_as_skill_default(self, lesson):
        attr = lesson.get_skill_attribute_name()
        skill = lesson.skill
        setattr(skill, attr, lesson)
        skill.save()


class GetOrCreateBySkill(LessonGenericView, View):
    model = Lesson

    def get_or_create_url(self, skill):
        attr = self.model.get_skill_attribute_name(None)
        obj = getattr(skill, attr)

        if obj:
            return obj.get_update_url()
        else:
            return '{}?assign=true'.format(
                self.model.get_create_url(None, skill)
            )

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        skill = ctx['skill']
        url = self.get_or_create_url(skill)

        return redirect(url)


class VideoGenericView(LessonGenericView):
    model = Video


class VideoFormView(VideoGenericView):
    fields = DEFAULT_LESSON_FIELDS + ['video_url']


class IntroGenericView(LessonGenericView):
    model = Intro


class IntroFormView(IntroGenericView):
    fields = FULL_LESSON_FIELDS


class ArticleGenericView(LessonGenericView):
    model = Article


class ArticleFormView(ArticleGenericView):
    fields = FULL_LESSON_FIELDS


class ActivityListGenericView(LessonGenericView):
    model = ActivityList


class ActivityListFormView(ActivityListGenericView):
    fields = BASE_LESSON_FIELDS


class ActivityForm(object):
    fields = ['name', 'description', 'body']
