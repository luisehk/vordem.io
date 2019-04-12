from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from ..messaging.email.helpers import send_email
from .forms import ContactForm


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


class RequestQuote(FormView):
    template_name = "request-quote.html"
    form_class = ContactForm
    success_url = reverse_lazy('website:thanks')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        email = form.cleaned_data['email']
        cellphone = form.cleaned_data['cellphone']
        build = form.cleaned_data['build']
        other = form.cleaned_data['other']
        time = form.cleaned_data['time']
        other_time = form.cleaned_data['other_time']
        fader = form.cleaned_data['fader']
        describe_project = form.cleaned_data['describe_project']

        send_email(
            subject='Vordem - Formulario de contacto.',
            to_email=[
                # TODO: email de vordem
                'edderleonardo@gmail.com',
                'c4m2m8z4k0i7c8t1@vordem.slack.com'],
            template='emails/email-contact.html',
            ctx={
                'name': name,
                'company': company,
                'email': email,
                'cellphone': cellphone,
                'build': build,
                'other': other,
                'time': time,
                'other_time': other_time,
                'fader': fader,
                'describe_project': describe_project,
                'host': self.request.get_host()
            })
        return super().form_valid(form)


class Careers(TemplateView):
    template_name = "careers.html"


class ApplyToJob(TemplateView):
    template_name = "apply-to-job.html"


class SingleProject(TemplateView):
    template_name = "project.html"


class SingleArticle(TemplateView):
    template_name = "article.html"


class ThanksView(TemplateView):
    template_name = "thanks.html"
