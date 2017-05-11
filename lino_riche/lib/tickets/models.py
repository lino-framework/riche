# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""Database models specific for the Team variant of Lino Noi.

Defines a customized :class:`TicketDetail`.

"""

from lino_xl.lib.tickets.models import *
from lino.api import _, pgettext

Project._meta.verbose_name = _("Project")


@dd.python_2_unicode_compatible
class Site(dd.Model):
    class Meta:
        app_label = 'tickets'
        verbose_name = pgettext("Ticketing", "Site")
        verbose_name_plural = pgettext("Ticketing", "Sites")

    partner = dd.ForeignKey('contacts.Partner', blank=True, null=True)
    # responsible_user = dd.ForeignKey(
    #     'users.User', verbose_name=_("Responsible"),
    #     blank=True, null=True)
    name = models.CharField(_("Designation"), max_length=200)
    remark = models.CharField(_("Remark"), max_length=200, blank=True)

    def __str__(self):
        return self.name


class TicketDetail(TicketDetail):
    """Customized detail_lyout for Tickets.  Replaces `waiting_for` by
    `faculties`

    """
    main = "general more history_tab more2"
    
    general = dd.Panel("""
    general1:60 comments.CommentsByRFC:30
    """, label=_("General"))

    general1 = """
    summary:40 ticket_type id:6
    user:12 end_user:12 deadline
    site #topic project
    workflow_buttons:30 #private
    bottom_box
    """

    bottom_box = """
    #faculties.DemandsByDemander:20 votes.VotesByVotable:20
    #deploy.DeploymentsByTicket:20 #clocking.SessionsByTicket:20
    """

    more = dd.Panel("""
    more1 DuplicatesByTicket:20 #WishesByTicket
    description:30 upgrade_notes:20 LinksByTicket:20  
    """, label=_("More"))

    more1 = """
    #nickname:10     created modified reported_for #fixed_for #ticket_type:10
    state ref duplicate_of planned_time priority
    # standby feedback closed
    """

    more2 = dd.Panel("""
    # deploy.DeploymentsByTicket
    uploads.UploadsByController
    """, label=_("Even more"))

Tickets.detail_layout = TicketDetail()

# Sites.detail_layout = """
# id name partner #responsible_user
# remark
# #InterestsBySite TicketsBySite deploy.MilestonesBySite
# """


from .ui import *

