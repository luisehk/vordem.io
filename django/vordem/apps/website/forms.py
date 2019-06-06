from django import forms


class ContactForm(forms.Form):
    WEBAPP = 'Web App'
    ANDROID = 'Android app'
    IOS = 'IOS app'
    WEBSITE = 'Web site'
    NOTSURE = 'Im not sure'

    WHAT_DO_YOU_WANT_TO_BUILD = (
        (WEBAPP, 'Web App'),
        (ANDROID, 'Android'),
        (IOS, 'IOS'),
        (WEBSITE, 'Web Site'),
        (NOTSURE, 'No estoy seguro'),
    )

    ONEMONTH = 'One month'
    THREEMONTH = 'Three month'
    SIXMONTH = 'Six month'
    WHENREADY = 'When ready'
    NOTSURETIME = 'Not sure time'

    WHEN_DO_YOU_NEED_IT = (
        (ONEMONTH, 'one_month'),
        (THREEMONTH, 'three_month'),
        (SIXMONTH, 'six_month'),
        (WHENREADY, 'when_ready'),
        (NOTSURETIME, 'not_sure_time'),
    )

    name = forms.CharField()
    company = forms.CharField()
    email = forms.CharField()
    cellphone = forms.CharField()
    location = forms.CharField()
    build = forms.MultipleChoiceField(
        choices=WHAT_DO_YOU_WANT_TO_BUILD,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'data-parsley-error-message': 'Please choose at least one.',
                'data-parsley-errors-container': '#when_do_you_need_it',
                'data-parsley-required': 'true'
            }
        ))
    time = forms.ChoiceField(
        choices=WHEN_DO_YOU_NEED_IT,
        widget=forms.RadioSelect(
            attrs={
                'data-parsley-error-message': 'Please choose at least one.',
                'data-parsley-errors-container': '#when_do_you_need_it',
                'data-parsley-required': 'true'
            }
        ))
    fader = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                'min': '0',
                'max': '500000',
                'value': '100000',
                'step': '100',
                'oninput': 'outputUpdate(value)'}))
    describe_project = forms.CharField()
