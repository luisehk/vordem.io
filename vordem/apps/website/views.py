from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Services(TemplateView):
    template_name = "services.html"


class Projects(TemplateView):
    template_name = "projects.html"


class Blog(TemplateView):
    template_name = "blog.html"


class Contact(TemplateView):
    template_name = "contact.html"


class RequestQuote(TemplateView):
    template_name = "request-quote.html"


class Careers(TemplateView):
    template_name = "careers.html"


class ApplyToJob(TemplateView):
    template_name = "apply-to-job.html"


class SingleProject(TemplateView):
    template_name = "project.html"


class SingleArticle(TemplateView):
    template_name = "article.html"
