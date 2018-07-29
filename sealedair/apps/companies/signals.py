def warm_company_profile_avatar(sender, **kwargs):
    p = kwargs['instance']
    p.warm_avatar()
