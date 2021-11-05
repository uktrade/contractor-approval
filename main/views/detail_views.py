from main.views.supporting_forms import SupportingFormDetailView
from main.models import (
    JobDescription,
    InterimRequest,
    CestRationale,
    SdsStatusDetermination,
)


class JobDescriptionDetailView(SupportingFormDetailView):
    model = JobDescription
    permission_required = "main.view_jobdescription"
    title = "Job description"


class InterimRequestDetailView(SupportingFormDetailView):
    model = InterimRequest
    permission_required = "main.view_interimrequest"
    title = "Interim Request"


class CestRationaleDetailView(SupportingFormDetailView):
    model = CestRationale
    permission_required = "main.view_cestrationale"
    title = "CEST Rationale"

class SdsStatusDeterminationDetailView(SupportingFormDetailView):
    model = SdsStatusDetermination
    permission_required = "main.view_sdsstatusdetermination"
    title = "SDS Status Determination"

