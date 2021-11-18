from django.shortcuts import render

from chartofaccount.models import CostCentre, Directorate
from main.forms.interim_request_form import InterimRequestNewForm
from main.models import InterimRequest, ResourcingRequest
from main.views.supporting_forms import (
    SupportingFormCreateView,
    SupportingFormUpdateView,
)


RESOURCING_REQUEST_TYPE_TO_FORM = {
    ResourcingRequest.Type.NEW: InterimRequestNewForm,
}


class InterimRequestViewMixin:
    def get_form_class(self):
        resourcing_request = self.get_resourcing_request()

        return RESOURCING_REQUEST_TYPE_TO_FORM[resourcing_request.type]


class InterimRequestCreateView(InterimRequestViewMixin, SupportingFormCreateView):
    model = InterimRequest
    permission_required = "main.add_interimrequest"
    template_name = "main/interim_request.html"


class InterimRequestUpdateView(InterimRequestViewMixin, SupportingFormUpdateView):
    model = InterimRequest
    permission_required = "main.change_interimrequest"
    template_name = "main/interim_request.html"


def load_directorates(request):
    group_code = request.GET.get("group")
    directorates = Directorate.objects.filter(group=group_code).order_by(
        "directorate_name"
    )
    return render(
        request,
        "main/partials/directorate_list_options.html",
        {"directorates": directorates},
    )


def load_costcentres(request):
    directorate_code = request.GET.get("directorate")
    costcentres = CostCentre.objects.filter(directorate=directorate_code).order_by(
        "cost_centre_name"
    )
    return render(
        request,
        "main/partials/costcentre_list_options.html",
        {"costcentres": costcentres},
    )
