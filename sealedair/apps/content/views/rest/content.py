from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from ...serializers.skills import SkillWithScoreSerializer
from ...serializers.content import OptionSerializer
from ...models import Option, Skill
from ....score.models import LeaderSkillScore, CompanySkillScore
from ....progress.models import SkillCompletion


class UserContent(APIView):
    def retrieve_data(self, request):
        # skills
        skills = Skill.objects.all()
        skills = skills.prefetch_related(
            'intro', 'video', 'article',
            'quiz', 'activity_list',
            'quiz__questions', 'activity_list__activities',)

        # scores and progress
        leader = request.user
        company = leader.leader_companies.first()

        # what to do if user doesnt have a company?
        # should we create a new ghost company, forbid them
        # from using the app, or return company_score as None?
        data = [{
            'skill': skill,
            'leader_score': LeaderSkillScore.objects.get_or_create(
                leader=leader, skill=skill
            )[0],
            'company_score': CompanySkillScore.objects.get_or_create(
                company=company, skill=skill
            )[0] if company else None,
            'leader_skill_completion': SkillCompletion.objects.get_or_create(
                leader=leader, skill=skill
            )[0]
        } for skill in skills]

        return data

    def serialize_data(self, data):
        serializer = SkillWithScoreSerializer(data=data, many=True)
        serializer.is_valid()
        return serializer.data

    def generate_response(self, serialized_data):
        return Response(serialized_data, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        data = self.retrieve_data(request)
        serialized_data = self.serialize_data(data)
        return self.generate_response(serialized_data)


class OptionViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_fields = ('question_id',)