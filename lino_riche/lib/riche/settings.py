# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Base Django settings for Lino riche applications.

"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_riche import SETUP_INFO

class Site(Site):

    verbose_name = "Lino riche"
    version = SETUP_INFO['version']
    url = "http://riche.lino-framework.org/"

    demo_fixtures = ['std', 'demo', 'demo2']
                     # 'linotickets',
                     # 'tractickets', 'luc']

    # project_model = 'tickets.Project'
    # project_model = 'deploy.Milestone'
    textfield_format = 'html'
    user_types_module = 'lino_riche.lib.riche.user_types'
    workflows_module = 'lino_riche.lib.riche.workflows'
    obj2text_template = "**{0}**"

    default_build_method = 'appyodt'
    
    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'
    
    # TODO: move migrator to lino_riche.projects.eric
    migration_class = 'lino_riche.lib.riche.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_riche"

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps` for Lino
        riche.

        """
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.extjs'
        # yield 'lino.modlib.bootstrap3'
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        # yield 'lino.modlib.users'
        yield 'lino_riche.lib.contacts'
        yield 'lino_riche.lib.users'
        # yield 'lino_riche.lib.cal'
        # yield 'lino_xl.lib.extensible'
        # yield 'lino_riche.lib.courses'
        # yield 'lino_riche.lib.products'

        yield 'lino_riche.lib.topics'
        yield 'lino_xl.lib.votes'
        yield 'lino_riche.lib.tickets'
        # yield 'lino_xl.lib.faculties'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_riche.lib.clocking'
        # yield 'lino_xl.lib.lists'
        # yield 'lino_xl.lib.blogs'

        yield 'lino.modlib.changes'
        yield 'lino.modlib.notify'
        yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.outbox'
        # yield 'lino_xl.lib.excerpts'
        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.smtpd'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.dashboard'

        # yield 'lino.modlib.awesomeuploader'

        yield 'lino_riche.lib.riche'
        # yield 'lino_xl.lib.inbox'
        # yield 'lino_xl.lib.mailbox'
        # yield 'lino_xl.lib.meetings'


    def setup_plugins(self):
        super(Site, self).setup_plugins()
        # self.plugins.comments.configure(
        #     commentable_model='tickets.Ticket')
        if 'faculties' in self.plugins:
            self.plugins.faculties.configure(
                demander_model='tickets.Ticket')
        # self.plugins.tickets.configure(
        #     site_model='cal.Room',
        #     milestone_model='courses.Course')

    def get_default_required(self, **kw):
        # overrides the default behaviour which would add
        # `auth=True`. In Lino Noi everybody can see everything.
        return kw

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        # tb.add_action(self.actors.courses.MyActivities)
        if 'meetings' in self.plugins:
            tb.add_action(self.actors.meetings.MyMeetings)
        # tb.add_action(self.modules.deploy.MyMilestones)
        # tb.add_action(self.actors.tickets.MyTickets)
        # tb.add_action(self.actors.tickets.TicketsToTriage)
        # tb.add_action(self.actors.tickets.TicketsToTalk)
        # tb.add_action(self.modules.tickets.TicketsToDo)
        tb.add_action(self.modules.tickets.RefTickets)
        tb.add_action(self.actors.tickets.AllTickets)
        tb.add_action(
            self.actors.tickets.MyTickets.insert_action,
            label=_("Submit a ticket"))

        a = self.actors.users.MySettings.default_action
        tb.add_instance_action(
            user, action=a, label=_("My settings"))
        # handler = self.action_call(None, a, dict(record_id=user.pk))
        # handler = "function(){%s}" % handler
        # mysettings = dict(text=_("My settings"),
        #                   handler=js_code(handler))
        

    def do_site_startup(self):
        super(Site, self).do_site_startup()

        from lino.modlib.changes.models import watch_changes as wc

        wc(self.modules.tickets.Ticket)
        wc(self.modules.comments.Comment, master_key='owner')
        # wc(self.modules.clocking.Session, master_key='owner')
        
        if self.is_installed('votes'):
            wc(self.modules.votes.Vote, master_key='votable')

        if self.is_installed('deploy'):
            wc(self.modules.deploy.Deployment, master_key='ticket')

        if self.is_installed('extjs'):
            self.plugins.extjs.autorefresh_seconds = 0

        from lino.core.merge import MergeAction
        from lino_xl.lib.contacts.roles import ContactsStaff
        lib = self.models
        for m in (lib.contacts.Company, ):
            m.define_action(merge_row=MergeAction(
                m, required_roles=set([ContactsStaff])))
            
# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'

