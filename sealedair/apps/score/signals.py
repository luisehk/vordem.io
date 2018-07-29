from .models import (
    CompanyScore, CompanySkillScore,
    LeaderScore, LeaderSkillScore)
from ..content.models import Skill
from ..companies.models import Company


# internal use only
def _create_company_skill_score(company, skill):
    exists = CompanySkillScore.objects.filter(
        skill=skill, company=company).exists()

    if not exists:
        CompanySkillScore.objects.create(
            skill=skill, company=company)


def _create_leader_skill_score(leader, skill):
    exists = LeaderSkillScore.objects.filter(
        skill=skill, leader=leader).exists()

    if not exists:
        LeaderSkillScore.objects.create(
            skill=skill, leader=leader)


# companies
def create_company_score(sender, **kwargs):
    company = kwargs['instance']

    exists = CompanyScore.objects.filter(
        company=company).exists()

    if not exists:
        CompanyScore.objects.create(company=company)


def create_company_skill_score(sender, **kwargs):
    company = kwargs['instance']

    for skill in Skill.objects.all():
        _create_company_skill_score(company, skill)


# leaders
def create_leader_score(sender, **kwargs):
    leader = kwargs['instance']

    exists = LeaderScore.objects.filter(
        leader=leader).exists()

    if not exists:
        LeaderScore.objects.create(leader=leader)


def create_leader_skill_score(sender, **kwargs):
    leader = kwargs['instance']

    for skill in Skill.objects.all():
        _create_leader_skill_score(leader, skill)


# skills
def create_skill_company_score(sender, **kwargs):
    skill = kwargs['instance']

    for company in Company.objects.all():
        _create_company_skill_score(company, skill)


def create_skill_leader_score(sender, **kwargs):
    skill = kwargs['instance']

    for company in Company.objects.all():
        for leader in company.leaders.all():
            _create_leader_skill_score(leader, skill)
