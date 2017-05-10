from lino.api import dd, rt, _, pgettext

from lino_xl.lib.tickets.roles import TicketsUser, TicketsStaff

class Sites(dd.Table):
    # required_roles = set()  # also for anonymous
    required_roles = dd.login_required(TicketsUser)
    model = 'tickets.Site'
    column_names = "name partner remark id *"
    order_by = ['name']
    detail_html_template = "tickets/Site/detail.html"

    insert_layout = """
    name
    remark
    """

    detail_layout = """
    id name partner #responsible_user
    remark
    TicketsBySite
    """


class AllSites(Sites):
    required_roles = dd.login_required(TicketsStaff)


class SitesByPartner(Sites):
    master_key = 'partner'
    column_names = "name remark *"

